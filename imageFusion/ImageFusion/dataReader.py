from geotiff import GeoTiff
import numpy as np
import imageio.v2 as imageio

class DataReader:

    def __init__(self):
        """
        Initailizing Data Reader
        """
        self.image = None
    
    def add_additional_axis(self):
        """
        For adding additional axis, useful while processing only single band from image
        """
        self.image = self.image[:, :, np.newaxis]

    def read_geotiff_file(self, filename):
        """
        For reading geotiff files

        Args:
            filename (_string_): _Path of the image_

        Returns:
            _numpy_arr_: _numpy array containing each image band_
        """
        image_data = GeoTiff(filename)
        self.image = np.array(image_data.read(), dtype = np.float64)
        print(self.image.shape)
        
        if(len(self.image.shape) == 2):
            self.add_additional_axis()

        return self.image

    def read_numpy_file(self, filename):
        """
        For reading numpy arrays directly from files

        Args:
            filename (_string_): _Path of the file_

        Returns:
            _numpy_arr_: _Numpy array loaded from file_
        """
        self.image = np.load(filename, dtype=np.float64)
        
        if(len(self.image.shape) == 2):
            self.add_additional_axis()
        
        return self.image

    def read_tiff_file(self, filename):
        """
        For reading tiff files
        Args:
            filename (_string_): _Path of the image_

        Returns:
            _numpy_arr_: _numpy array containing each image band_
        """
        self.image = np.array(imageio.imread(filename), dtype=np.float64)

        if(len(self.image.shape) == 2):
            self.add_additional_axis()
        
        return self.image

    

