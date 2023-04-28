import tifffile as tiff
from osgeo import gdal
import numpy as np

class DataWriter:

    def __init__(self, image, filename):
        """
        Initilaizes data writer class
        Args:
            image (_numpy_arr_): _Numpy array containing image file_
            filename (_string_): _Name of the file_
        """
        self.image = image
        self.filename = filename
    
    def add_additional_axis(self):
        """
        For adding additional axis, useful while processing only single band from image
        """
        self.image = self.image[:, :, np.newaxis]


    def store_tiff_file(self):
        """
        For storing files in Tiff format
        """
        image_recreated = []

        for band in range(self.image.shape[2]):
            image_recreated.append(self.image[:, :, band].reshape(self.image.shape[0], self.image.shape[0]))

        image_recreated = np.array(image_recreated)
        tiff.imsave(self.filename, self.image, append=True)

    def store_geotiff_file(self, fine_t0 = None):
        """
        For storing files in GeoTiff format
        """
        driver = gdal.GetDriverByName('GTiff')
        dataset = driver.Create(self.filename,self.image.shape[0], self.image.shape[1], self.image.shape[2],gdal.GDT_Float32)
        print(self.image.shape)
        for band_range in range(self.image.shape[2]):
            dataset.GetRasterBand(band_range+1).WriteArray(self.image[:, :, band_range].reshape(self.image.shape[0], self.image.shape[1]))

        if(fine_t0 is not None):
            data0 = gdal.Open(fine_t0)
            geotrans=data0.GetGeoTransform()
            proj=data0.GetProjection()
            dataset.SetGeoTransform(geotrans)
            dataset.SetProjection(proj)
            
        dataset.FlushCache()
        dataset=None

    def store_numpy_file(self):
        """
        For storing files in Numpy format
        """
        np.save(self.filename, self.image)