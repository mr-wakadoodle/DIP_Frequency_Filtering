Project Title: Frequency Filtering

Objectives & there Solution:

a. Compute a fast Fourier transform of a matrix.
  i. Leverage the symmetry property of DFT to compute a faster version of the DFT implementation from the assignment.
  ii. Apply Cooley-Tukey FFT algorithm to improve on the above method.
  
  The above mentioned code can be found under the folder 'part a' containing files - 
  
  DFT.py: code for naive implementation of DFT is present in this file.
  
  symmetryDFT.py: code to compute a faster version of the DFT leveraging the symmetry property of DFT is present in this file.
  
  cooleytukeyFFT.py:  Cooley-Tukey FFT algorithm implementing a faster version of computing DFT is present in this file.
  
  Each of these files can be run using the command 'python <filename>.py'. You will be asked to input the matrix dimensions.

b. Study and compare the computational times of a naïve implementation of the DFT with the above methods as the size of a square matrix increases.
  Detailed comparison and computed result is present in the file 'part_b.txt' under the folder 'part b'.
  
  
e,f. Apply filtering Low pass filters and High pass filters(Ideal, Butterworth, Gaussian) by specifying various parameters and view the output in the software.

Filtering.py : There is a function definition for each of the six filters to generate the masks in this file. This also includes functions post_process_image() to perform full contrast stretch and and filtering() function to perform fft, ifft and shifted ifft using in-built functions.

All the associated files for the above are available in Part_E_F folder.

Below command structure can be used to execute any filter function:
python Part_E_F/Filtering.py Part_E_F/Lenna.png Filter_name(ex: Ideal_HPF) Cutoff_frequency Order(Only for Butterworth)
  
  
g. Implementation of Sharpening filters using Laplacian and unsharp masking by specifying various parameters.
  
   Laplacian_Unsharp_Masking.py: This file contains two functions, one for Laplacian filter and the other one is for Unsharp filtering. Based upon the filter name given as         paramter, the filter function calls the corresponding filtering functions among the two.
  
Part d "filtering in the frequency domain using convolution theorem" is included in the GUI/main.py file -- https://github.com/UHCSDigitalImageProcessing/bonus-project-team-3/blob/270ab8430e7aac8c9a15c96d3e14b0f8e40280b5/GUI/main.py#L106
  
README file for GUI is present in the GUI folder.
