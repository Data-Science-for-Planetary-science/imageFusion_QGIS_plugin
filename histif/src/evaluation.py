import numpy as np
from geotiff import GeoTiff
import pandas as pd
# from sklearn.metrics import mean_squared_error
import math

# class DataReader:
#
#     def __init__(self, observed, predicted) -> None:
#         self.observed = pd.read_csv(observed,sep='\t')
#         fine1Points = self.observed.iloc[:, 0]
#         fineSize0 = len(fine1Points.apply(get_x_point).unique())
#         fineSize1 = len(fine1Points.apply(get_y_point).unique())
#         fineSize2 = len(fine1.columns) - 1
#         fine1 = np.reshape(np.array(fine1.iloc[:, 1:]), (fineSize0, fineSize1, fineSize2))
#
#         self.predicted = pd.read_csv(predicted,sep='\t')
#
#
#     def read_images(self):
#         obs = np.array(self.observed).reshape()
#         pred = np.array(self.predicted).reshape()
#         return obs, pred

def find_cc(observed, predicted, file_read = True):

    """Finding Correlation Coefficient"""

    # if(file_read):
    #     input_data = DataReader(observed, predicted)
    #     obs, pred = input_data.read_images()
    #
    # else:
    obs, pred = observed, predicted

    band_wise_data = []

    for band in range(obs.shape[2]):
        x_band = pd.Series(obs[:, :, band].flatten())
        y_band = pd.Series(pred[:, :, band].flatten())
        band_wise_data.append(x_band.corr(y_band))
        
    return band_wise_data

# def find_rmse(observed, predicted, file_read = True):
#     """Finding Root Mean Square Error"""

#     # if(file_read):
#     #     input_data = DataReader(observed, predicted)
#     #     obs, pred = input_data.read_images()
#     #
#     # else:
#     obs, pred = observed, predicted

#     band_wise_error = []

#     for band in range(obs.shape[2]):
#         band_wise_error.append(math.sqrt(mean_squared_error(obs[:, :, band], pred[:, :, band])))
        
#     return band_wise_error

def find_mean_absolute_difference(observed, predicted, file_read = True):
    """Finding Mean Absolute Difference"""

    # if(file_read):
    #     input_data = DataReader(observed, predicted)
    #     obs, pred = input_data.read_images()
    #
    # else:
    obs, pred = observed, predicted

    band_wise_error = []

    for band in range(obs.shape[2]):
        band_wise_error.append(np.mean(abs(obs[:, :, band] - pred[:, :, band])))
        
    return band_wise_error


def get_x_point(point):
    return float(point[6:-1].split()[0])

def get_y_point(point):
    return float(point[6:-1].split()[1])


def save_result(groundTruthFile,predictedFile):
    orgArray = groundTruthFile
    predArray = predictedFile
    result_df = pd.DataFrame()
    result_df['Correlation Coefficient'] = find_cc(orgArray,predArray)
    # result_df["Root Mean Square Error (RMSE)"] = find_rmse(orgArray, predArray)
    result_df["Mean Absolute Error"] = find_mean_absolute_difference(orgArray, predArray)
    band_values = []
    for i in range(result_df.shape[0]):
        band_values.append("B" + str(i))
    result_df.index = band_values
    return result_df


    # for i in range(len(values)):
    #     print("The {} for the {} is {}".format(param_name, f"B{i}", values[i]))
#
# result_df = pd.DataFrame()
# save_result("Correlation Coefficient", find_cc("/home/raashika/Documents/Research/Image Fusion/imageFusionData/fine_t0_clipped.tif", "/home/raashika/Desktop/573cf9e0-f7d7-4c60-aae4-231eb17fc6e5.tif"))
# save_result("Root Mean Square Error (RMSE)", find_rmse("/home/raashika/Documents/Research/Image Fusion/imageFusionData/fine_t0_clipped.tif", "/home/raashika/Desktop/573cf9e0-f7d7-4c60-aae4-231eb17fc6e5.tif"))
# save_result("Mean Absolute Error", find_mean_absolute_difference("/home/raashika/Documents/Research/Image Fusion/imageFusionData/fine_t0_clipped.tif", "/home/raashika/Desktop/573cf9e0-f7d7-4c60-aae4-231eb17fc6e5.tif"))
# band_values = []
# for  i in range(result_df.shape[0]):
#     band_values.append("B"+str(i))
# result_df.index  = band_values
