import math
import numpy as np
import cv2
import sys


def Ideal_LowPass_Filter(image, cutoff_frequency):
    R, C = np.shape(image)
    result_mask = np.zeros((R, C))
    D0 = cutoff_frequency
    for i in range(R):
        for j in range(C):
            Distance = math.sqrt((i- R//2)**2 + (j - C//2)**2)
            if Distance <= cutoff_frequency:
                result_mask[i,j] = 1
            else:
                result_mask[i, j] = 0

    return result_mask


def Ideal_HighPass_Filter(image, cutoff_frequency):
    result_mask = 1 - Ideal_LowPass_Filter(image, cutoff_frequency)
    return result_mask


def Butterworth_LowPass_Filter(image, cutoff_frequency, order = 0):
    R, C = np.shape(image)
    result_mask = np.zeros((R, C))
    D0 = cutoff_frequency
    n = order
    for i in range(R):
        for j in range(C):
            Distance = math.sqrt((i- R//2)**2 + (j - C//2)**2)
            result_mask[i,j] = 1/(1+ (Distance/D0)**(2*n))

    return result_mask


def Butterworth_HighPass_Filter(image, cutoff_frequency, order = 0):
    R, C = np.shape(image)
    result_mask = np.zeros((R, C))
    D0 = cutoff_frequency
    n = order
    for i in range(R):
        for j in range(C):
            Distance = math.sqrt((i - R // 2) ** 2 + (j - C // 2) ** 2)
            if Distance != 0:
                result_mask[i, j] = 1 / (1 + (D0 / Distance) ** (2 * n))
    return result_mask


def Gaussian_LowPass_Filter(image, cutoff_frequency):
    R, C = np.shape(image)
    result_mask = np.zeros((R, C))
    D0 = cutoff_frequency
    for i in range(R):
        for j in range(C):
            Distance = math.sqrt((i - R // 2) ** 2 + (j - C // 2) ** 2)
            result_mask[i, j] = np.exp((-1 * (Distance ** 2))/(2 * (D0 ** 2)))

    return result_mask


def Gaussian_HighPass_Filter(image, cutoff_frequency):
    result_mask = 1 - Gaussian_LowPass_Filter(image, cutoff_frequency)
    return result_mask


def main(image, filter_name, cutoff_frequency, order):
    if filter_name == 'Butterworth_HPF':
        mask = Butterworth_HighPass_Filter(image, cutoff_frequency, int(order))
    elif filter_name == 'Butterworth_LPF':
        mask = Butterworth_LowPass_Filter(image, cutoff_frequency, int(order))
    elif filter_name == 'Ideal_LPF':
        mask = Ideal_LowPass_Filter(image, cutoff_frequency)
    elif filter_name == 'Ideal_HPF':
        mask = Ideal_HighPass_Filter(image, cutoff_frequency)
    elif filter_name == 'Gaussian_LPF':
        mask = Gaussian_LowPass_Filter(image, cutoff_frequency)
    elif filter_name == 'Gaussian_HPF':
        mask = Gaussian_HighPass_Filter(image, cutoff_frequency)

    output = filtering(image, mask)

    # Filtered_Image = 'output/' + filter_name + '_Filtered_Image' + ".jpg"
    # cv2.imwrite(Filtered_Image, output[0])
    DFT = 'dft_output/' + filter_name +  '_DFT' + ".jpg"
    cv2.imwrite(DFT, output[1])
    Filtered_DFT = 'dft_output/' + filter_name +  '_Filtered_DFT' + ".jpg"
    cv2.imwrite(Filtered_DFT, output[2])

    return output[0]


def filtering(image, mask):
    input_image = image
    FFT = np.fft.fft2(input_image)

    Shift_fft = np.fft.fftshift(FFT)
    magnitude_dft = np.log(np.abs(Shift_fft))
    DFT = post_process_image(magnitude_dft)

    filtered_image = np.multiply(mask,Shift_fft)
    magnitude_filtered_dft = np.log(np.abs(filtered_image) + 1)
    filtered_dft = post_process_image(magnitude_filtered_dft)

    Shift_inverse_fft = np.fft.ifftshift(filtered_image)
    inverse_fft = np.fft.ifft2(Shift_inverse_fft)
    magnitude_inverse_fft = np.abs(inverse_fft)
    filtered_image = post_process_image(magnitude_inverse_fft)

    return [np.uint8(filtered_image), np.uint8(DFT), np.uint8(filtered_dft)]

def post_process_image(image):
    input_image = image
    rows,columns = np.shape(image)
    low = 0
    high = 255
    maxvalue_in_image = np.max(image)
    minvalue_in_image = np.min(image)
    for u in range(rows):
        for v in range(columns):
            if maxvalue_in_image - minvalue_in_image == 0:
                input_image[u,v] = ((high - low)/ 0.000001) * (image[u,v] - minvalue_in_image) + low
            else:
                input_image[u,v] = ((high - low) / (maxvalue_in_image - minvalue_in_image)) * (image[u,v]  - minvalue_in_image) + low

    return np.uint8(input_image)
