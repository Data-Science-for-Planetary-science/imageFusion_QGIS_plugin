from .changesModulation import ChangesModulation
from .dataReader import DataReader
from .imputePixels import ImputeMissingPixels
import pyswarms as ps
from .optimizationFunction import OptimizationFunction
import numpy as np
from multiprocessing import Manager, Process, Pool
import time
# np.random.seed(100)
from .dataWriter import DataWriter

class IHISTIF:
    """
    Contains implementation of Improved HISTIF algorithm
    """

    def __init__(self,coarse_image_t0, coarse_image_t1, fine_image_t0, file_type = "geotiff"):
        """
        Initialize with the file reading 
        """
        self.coarse_image_t0 = coarse_image_t0
        self.coarse_image_t1 = coarse_image_t1
        self.fine_image_t0 = fine_image_t0
        self.__parameters = None

        # if(file_type == "geotiff"):
        #     """
        #     File Reading for GeoTIFF files
        #     """
        #     self.coarse_image_t0 = DataReader().read_geotiff_file(coarse_image_t0)
        #     self.coarse_image_t1 = DataReader().read_geotiff_file(coarse_image_t1)
        #     self.fine_image_t0 = DataReader().read_geotiff_file(fine_image_t0)

        # if(file_type == "tiff"):
        #     """
        #     File Reading for TIFF files
        #     """
        #     self.coarse_image_t0 = DataReader().read_tiff_file(coarse_image_t0)
        #     self.coarse_image_t1 = DataReader().read_tiff_file(coarse_image_t1)
        #     self.fine_image_t0 = DataReader().read_tiff_file(fine_image_t0)

        # if(file_type == "numpy"):
        #     """
        #     File Reading for numpy files
        #     """
        #     self.coarse_image_t0 = DataReader().read_numpy_file(coarse_image_t0)
        #     self.coarse_image_t1 = DataReader().read_numpy_file(coarse_image_t1)
        #     self.fine_image_t0 = DataReader().read_numpy_file(fine_image_t0)

        # Missing Pixel Imputation Initializer
        self.coarse_t0_impute = ImputeMissingPixels(self.coarse_image_t0)
        self.fine_t0_impute = ImputeMissingPixels(self.fine_image_t0)
        self.coarse_t1_impute = ImputeMissingPixels(self.coarse_image_t1)

    def set_parameters(self, parameters):
        """
        Set the parameters for the algorithm
        Args:
            parameters (_list_): _List containing all the parameters_
        """
        self.__parameters = parameters

    def get_parameters(self):
        """
        Get the parameters for the algorithm
        Returns:
            _list_: _List containing all the parameters_
        """
        return self.__parameters

    def process_band_fusion(self, band_num, optimizer_params, evaluation):
        """
        Contains all the related operations required for prediction of each band
        Args:
            band_num (_int_): _The band number which is being processed_
            opt_params (_dict_): _Dict which stores all the optimal parameters for each band_
            band_vals (_dict_): _Dict which stores all the pred band values for each band_
            optimizer (_PSO_): _PSO optimizer which is used for optimization_
            kwargs (_dict_): _Dictionary containing all the parameters for optimizer_
            iterations (_int_): _Number of maximum iterations for reaching the optimal condition_
            evaluation (_bool_): _Mode in which the current processing is being done_
        """
        # np.random.seed(100)

        bounds = optimizer_params["bounds"]
        kwargs = optimizer_params["kwargs"]
        iterations = optimizer_params["iterations"]
        variant = optimizer_params["variant"]

        options = {'c1': 2.0, 'c2': 2.0, 'w': 0.6}
        del kwargs['n_components']

    
        optimizer = ps.single.GlobalBestPSO(n_particles=50, dimensions=5, options=options, bounds=bounds)
        cost, optimized_params = optimizer.optimize(OptimizationFunction().optima, iters = iterations, **kwargs)

        # Modulation of changes
        coarse_t0_psf = OptimizationFunction().FFT(optimized_params, self.coarse_image_t0[:, :, band_num], kwargs['edge'], kwargs['N'])

        # For avoiding floating precision errors
        modified_params = np.rint(optimized_params)
        coarse_t1_psf = OptimizationFunction().FFT(modified_params, self.coarse_image_t1[:, :, band_num], kwargs['edge'], kwargs['N'])
    

        pred_fine_t1 =  ChangesModulation().multiplicativeModulation(coarse_t0_psf, coarse_t1_psf, self.fine_image_t0[:, :, band_num].reshape(1, kwargs['N'] * kwargs['N']), modified_params, self.coarse_image_t0[:, :, band_num], kwargs['edge'], kwargs['N'])     
        pred_fine_t1 = pred_fine_t1.reshape(kwargs['N'], kwargs['N'])
        return pred_fine_t1, [cost, optimized_params]

    def fusion(self, iterations, neighbours = 4, evaluation = False, variant = 'new', optimizer = "default", n_components = 10):
        """
        Start fusion process for predicting fine t1 image
        Args:
            iterations (_int_): _Iterations to be used for optimization process_
            neighbours (int, optional): _Neighbours to consider for missing pixels_. Defaults to 4.
            evaluation (bool, optional): _To run simulataneous algos for eval mode_. Defaults to False.
            variant (str, optional): _For specifying varaint of algo to use_. Defaults to 'new'.

        Returns:
            _list_: _cost values and parameters, list of predisted bands_
        """

        # Impute Missing Values
        print("Processing imputation for Coarse t0 image...")
        self.coarse_image_t0 = self.coarse_t0_impute.using_nn_weighted_average(neighbours = neighbours)
        
        print("Processing imputation for Coarse t1 image...")
        self.coarse_image_t1 = self.coarse_t1_impute.using_nn_weighted_average(neighbours = neighbours)

        print("Processing imputation for Fine t0 image...")
        self.fine_image_t0 = self.fine_t0_impute.using_nn_weighted_average(neighbours = neighbours)

        # Particle Swarm Optimization for alignment
        lower_bound = np.array([self.get_parameters()[0][0], self.get_parameters()[1][0], self.get_parameters()[2][0], self.get_parameters()[3][0], self.get_parameters()[4][0]])
        upper_bound = np.array([self.get_parameters()[0][1], self.get_parameters()[1][1], self.get_parameters()[2][1], self.get_parameters()[3][1], self.get_parameters()[4][1]])
        bounds = (lower_bound, upper_bound)
        edge = (self.coarse_image_t0.shape[0] - self.fine_image_t0.shape[0]) / 2
        N = self.fine_image_t0.shape[0]
        
        values = []
        pred_img_bands = []
        old_var_img_bands = []

        args_p = []
        img_bands = []
        opt_params = []

        for band_num in range(min(self.coarse_image_t0.shape[2], self.fine_image_t0.shape[2])):

            kwargs = {  
                "coarse_image" : self.coarse_image_t0[:, :, band_num],
                "fine_image" : self.fine_image_t0[:, :, band_num].reshape(1, N * N),
                "edge" : edge,
                "N" : N,
                "n_components" : n_components
            }

            optimizer_params = {}
            optimizer_params["bounds"] = bounds
            optimizer_params["kwargs"] = kwargs
            optimizer_params["iterations"] = iterations
            optimizer_params["variant"] = variant

            band_obtained, cost_obtained = self.process_band_fusion(band_num, optimizer_params, evaluation)

            pred_img_bands.append(band_obtained)
            values.append(cost_obtained)   

        return values, pred_img_bands


if __name__ == "__main__":

    fusion_test = IHISTIF("Tests/test-1/coarse_t0.tif", "Tests/test-1/coarse_t1.tif", "Tests/test-1/fine_t0.tif", file_type = "tiff")
    parameters = [[2, 15], [2, 15], [-10, 10], [-10, 10], [1, 10]]
    fusion_test.set_parameters(parameters)
    params,image = fusion_test.fusion(2)
    N = image[0].shape[0]
    standard_predicted = image[0].reshape(N, N, 1)
        
    for band in range(1, len(image)):
        standard_predicted = np.dstack((standard_predicted, image[band].reshape(N, N, 1)))

    print(standard_predicted.shape)
    standard_writer = DataWriter(standard_predicted, f"Predictions/IHISTIF_pred.tiff").store_geotiff_file()