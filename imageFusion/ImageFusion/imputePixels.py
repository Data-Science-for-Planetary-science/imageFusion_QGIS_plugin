import numpy as np
from sklearn.neighbors import KDTree
from .dataReader import DataReader

class ImputeMissingPixels:
    """
    Handles all functions realted to imputation of missing pixels
    """

    def __init__(self, image):
        """
        Args:
            image (_numpy_arr_): _description_
        """
        self.image_frame = image

    def using_nn_weighted_average(self, neighbours):
        """
        Imputes the missing pixels using weighted average of neighbouring pixels
        Args:
            neighbours (_int_): _Number of neighbours to consider to impute missing pixels_

        Returns:
            _numpy_arr_: _Image Frame with complete set of pixels_
        """
        # Fix missing pixels bandwise
        for band_num in range(self.image_frame.shape[2]):
            
            replica_frame = np.copy(self.image_frame[:, :, band_num])
            # Finding missing pixels in the band
            missing_pixels = np.argwhere(np.isnan(replica_frame) == True)

            if(len(missing_pixels) == 0):
                print(f"No pixels was missing for band {band_num}")
                continue

            # If any pixel is missing build KD Tree from remaining pixels, and query for nearest neighbours
            available_pixels = np.argwhere(np.isnan(replica_frame) == False)
            kdtree = KDTree(available_pixels, leaf_size = 2)
            distances, indexes = kdtree.query(missing_pixels, k = neighbours)

            # Find the avg of all neighbouring pixels
            for ind in range(len(missing_pixels)):
                nearest_pixels = indexes[ind]
                pixel_val = 0
                
                for pixel_num in range(neighbours):
                    pixel_val += replica_frame[available_pixels[nearest_pixels[pixel_num]][0]][available_pixels[nearest_pixels[pixel_num]][1]]
                
                replica_frame[missing_pixels[ind]] = pixel_val / neighbours

            # Impute the final completed frame to the original frame
            self.image_frame[:, :, band_num] = replica_frame

        return self.image_frame
