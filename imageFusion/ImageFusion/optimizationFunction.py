import numpy as np
from scipy.ndimage import rotate
from scipy.signal import convolve2d
import math
from .dataReader import DataReader
import imutils
from PIL import Image
from math import ceil
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def conv2(x, y, mode='same'):
    """
    Convoles two images similar to MATLAB's convolution'
    Args:
        x (_numpy_arr_): _First arr to convolve_
        y (_numpy_arr_): _Second array to convolve with_
        mode (str, optional): Defaults to 'same'.

    Returns:
        _type_: _description_
    """
    return np.rot90(convolve2d(np.rot90(x, 2), np.rot90(y, 2), mode=mode), 2)

class OptimizationFunction:
    """
    Optimization reated functions to align the coarse image exactly with fine image
    """
    def optima(self, inputs, coarse_image, fine_image, edge, N):
        """
        RMSE cost Function to be used for optimization and obtain parameters
        Args:
            inputs (_list_): _Swarm positions for optimization_
            coarse_image (_numpy_array_): _Band from coarse image_
            fine_image (_numpy array_): _Band from fine image_
            edge (_int_): _Difference between the size of coarse and fine image_
            N (_int_): _Size of fine image_

        Returns:
            _list_: _Cost from each swarm position_
        """
        inputs = np.array(inputs)
        cost = []

        # Process for each particle position
        for i  in range(len(inputs)):

            # Apply FFT on image and use RMSE for optimization
            filtered_CoarseImage = self.FFT(inputs[i], coarse_image, edge, N)
            cost.append(np.sqrt(np.mean(np.power(filtered_CoarseImage - fine_image, 2))))

        cost = np.array(cost).T
        return cost

    def FFT(self, parameters, image, edge, N):
        """
        FFT function which applies PSF and finds appropraites portion from complete coarse image
        Args:
            parameters (_list_): _Parameters for applying PSF and shifting_
            image (_numpy_arr_): _Numpy array of image_
            edge (_int_): _Difference between the coarse and fine image_
            N (_int_): _Size of the fine image_

        Returns:
            _numpy_arr_: _coarse image which aligns to fine image_
        """
        fwhm_x = parameters[0]
        fwhm_y = parameters[1]
        sh_x = parameters[2]
        sh_y = parameters[3]
        angle = parameters[4]

        # Calculate SMF for given parameters
        psf_cal = self.SMF(fwhm_x, fwhm_y, angle)

        # convolve image with PSF
        image_fft = conv2(image, psf_cal, 'same')
        ends = list(image_fft.shape)

        # Cut the coarse image such that it aligns with the fine image exactly
        image_fft = image_fft[int(edge + sh_y): int(ends[0] - edge + sh_y), int(edge + sh_x): int(ends[1]-edge + sh_x)]
        return image_fft.reshape(1, (N * N))

    def SMF(self, fwhm_x, fwhm_y, angle):
        """
        SMF obtains the PSF and creates the appropraite mask and rotates for it to align exactly
        Args:
            fwhm_x (_int_): _accomodates for PSF in X direction_
            fwhm_y (_int_): _accomodates for PSF in Y direction_
            angle (_int_): _rotates the PSF_

        Returns:
            _numpy_arr_: _rotated PSF array_
        """
       
        # Obtain PSF
        psf_gaussian = self.PSF(fwhm_x, fwhm_y)
        psf_mask = np.zeros_like(psf_gaussian)

        # PSF Mask 
        psf_mask[int(ceil(fwhm_y/2)) : int(ceil(2*fwhm_y-(fwhm_y/2))) + 1, int(ceil(fwhm_x/2)) : int(ceil(2 * fwhm_x - (fwhm_x/2))) +1] = 1
        
        # Rotate MASK and the gaussian in counter clockwise direction
        rot_psf_mask = np.array(Image.fromarray(psf_mask).rotate(angle = angle, expand = True))
        psf_gaussian = np.array(Image.fromarray(psf_gaussian).rotate(angle = angle, expand = True))
        
        psf_gaussian[np.where(rot_psf_mask == 0)] = 0
        rowpix, colpix = np.where(rot_psf_mask == 1)
        
        # Cut the required portion of PSF which actually has an impact
        psf = psf_gaussian[np.min(rowpix):np.max(rowpix) + 1, np.min(colpix):np.max(colpix) + 1]
        psf = psf / np.sum(psf)

        # Normalize and return the final PSF
        return np.round(psf, 4)

    def PSF(self, fwhm_x, fwhm_y):
        """
        PSF for accomodating change in pixels because of sensor observations
        Args:
            fwhm_x (_int_): _Useful for defining x side of pixel change effects_
            fwhm_y (_int_): _Useful for defining y side of pixel change effects_

        Returns:
            _numpy_arr_: _PSF array by modelling using gaussian function_
        """
        # TODO : Fix and try to check if it's opposite
        sd_x = fwhm_x / (2 * math.sqrt(2 * math.log(2)))
        sd_y = fwhm_y / (2 * math.sqrt(2 * math.log(2)))
        
        x_max = fwhm_x * 2
        y_max = fwhm_y * 2

        # Gaussian Function for both x and y
        gaussian_x = np.matrix(self.gaussian(x_max + 1, sd_x))
        gaussian_y = np.matrix(self.gaussian(y_max + 1, sd_y))
        gaussian_xy = np.matmul(gaussian_y.getH(), gaussian_x)

        # Combination of both gaussians
        psf = gaussian_xy / (np.sum(gaussian_xy))
        psf = np.round(psf, 4)
        return psf
        

    def gaussian(self, M, std):
        """
        Gaussian Function used to account for PSF
        Args:
            M (_float_): _Mean of the Gaussian distribution_
            std (_float_): _Standard Deviation of the Gaussian distribution_

        Returns:
            _numpy_arr_
        """
        Mn = (M - 1)/2
        n = np.array([i for i in range(-int(Mn), int(Mn) + 1, 1)])
        gwin = np.exp(-0.5*np.power((n/std), 2))
        return gwin