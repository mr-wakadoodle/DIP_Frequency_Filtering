# project-team-3 GUI

The GUI made use of for the project is Tkinter, before running the code please make sure you have tkinter installed on your editor or computer, 
otherwise you can install using the following command.
```
pip install tk
```
## UI does the following functionalities:
- It is capable of loading images, setting parameters, performing and image processing operations and displaying the results
- Apply filtering Low pass filters (Ideal, Butterworth, Gaussian) by specifying various parameters and view the output in the software.
- Apply filtering High pass filters (Ideal, Butterworth, Gaussian) by specifying various parameters and view the output in the software.
- Apply Sharpening filters (Using Laplacian, and unsharp masking) and view the output in the software.
- Apply filtering in the frequency domain using convolution theorem(inbuilt library) view the output in the software.

## Running and working 

In order to run the application, clone the application and on your command line execute the command below:
```
python main.py
```

In order to perform image processing operations in the GUI, first you need to upload an image to the GUI, we have made use of lenna.png 
which is also available in the GUI directory, after uploading the image we need to select the filtering that needs to be done, for this
there are two dropdown, the first is the filtering dropdown and the second dropdown is dependent on the first filter and changes on 
selecting different filters. By default the dropdowns would be set to "High Pass Filter" and "Ideal" there is an argument passing input
box where you can provide input, this is for 'High pass filters' and 'low pass filters' only where the first parameter is 'cut-off frequency' 
and second parameter is 'order' which is to be given seperated by a space, By default the values will be '100' and '10'.

The output for the operations would be displayed in the GUI and also a copy would be stored in `output` and `dft_output` folders, please make sure
those two folders are created in your local.
