import numpy as np
from .optimizationFunction import OptimizationFunction

class ChangesModulation:
    """
    For applying temporal modulation on the final images
    """        

    def multiplicativeModulation(self, coarse_t0_psf, coarse_t1_psf, fine_t0, modified_params, coarse_t0, edge, n):
        """
        Responsible for applying multiplicativeModulation (Applying modulation changes from coarse t0 to t1)

        Args:
            coarse_t0_psf (_numpy_arr_): _Coarse T0 after applying PSF_
            coarse_t1_psf (_numpy_arr_): _Coarse T1 after applying PSF_
            fine_t0 (_numpy_arr_): _Fine T0_
            modified_params (_numpy_arr_): _Modified params used for optimization_
            coarse_t0 (_numpy_arr_): _Coarse T0_ standard image_
            edge (_int_): _Edge to be used for padding_
            n (_int_): _Size of image_

        Returns:
            _numpy_arr_: _Predicted FIne t1 image_
        """

        coarse_t0_psf_mod = OptimizationFunction().FFT(modified_params, coarse_t0, edge, n)
        fine_t0_predicted  = np.multiply(np.divide(coarse_t0_psf_mod, coarse_t0_psf), fine_t0)

        # Modulate the changes by multiplicative term and add the error
        fine_t1_predicted = np.multiply(np.divide(coarse_t1_psf, coarse_t0_psf), fine_t0) + fine_t0 - fine_t0_predicted
        return fine_t1_predicted