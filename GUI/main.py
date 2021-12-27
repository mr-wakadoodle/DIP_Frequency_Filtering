import tkinter
import cv2
from tkinter import *
from tkinter import ttk

# loading Python Imaging Library
import numpy as np
from PIL import ImageTk, Image

# To get the dialog box to open when required
from tkinter import filedialog

from Filtering import Filtering
import Filters


# Begin the app
class App:

    def openfilename(self):
        # open file dialog box to select image
        # The dialogue box has a title "Open"
        self.filename = filedialog.askopenfilename(title='"pen')
        return self.filename

    def open_img(self):
        # Select the Imagename  from a folder
        x = self.openfilename()

        # opens the image
        img = Image.open(x)

        # resize the image and apply a high-quality down sampling filter
        img = img.resize((600, 500), Image.ANTIALIAS)

        # PhotoImage class is used to add image to widgets, icons etc
        img = ImageTk.PhotoImage(img)
        self.canvas.create_image(50, 10, image=img, anchor=tkinter.NW)
        self.canvas.image = img

    def pick_dropdown(self, e):
        SUB_FILTER = ["IDEAL", "BUTTERWORTH","GAUSSIAN"]
        SHARPENING = ["UNSHARP", "LAPLACIAN"]
        filter_selection = ["High-Pass filter", "Low-Pass filter"]
        if self.variable.get() in filter_selection:
            self.variable1.config(value=SUB_FILTER)
            self.variable1.current(0)
        if self.variable.get() == "Sharpening":
            self.variable1.config(value=SHARPENING)
            self.variable1.current(0)
        if self.variable.get() == "Convolution":
            self.variable1.config(value=[" "])
            self.variable1.current(0)

    def submit_data(self):
        filter_selection = ["High-Pass filter", "Low-Pass filter"]
        input_image = cv2.imread(self.filename, 0)
        output_dir = 'output/'

        if self.variable.get() in filter_selection:
            filter_select = ""
            cutoff_frequency = 100
            order = 10
            if self.args_holder.get() != "":
                temp = self.args_holder.get().split(" ")
                cutoff_frequency = int(temp[0])
                if len(temp) > 1:
                    order = int(temp[1])
            if self.variable.get() == "High-Pass filter":
                if self.variable1.get() == "IDEAL":
                    filter_select = "Ideal_HPF"
                elif self.variable1.get() == "BUTTERWORTH":
                    filter_select = "Butterworth_HPF"
                else:
                    filter_select = "Gaussian_HPF"
            else:
                if self.variable1.get() == "IDEAL":
                    filter_select = "Ideal_LPF"
                elif self.variable1.get() == "BUTTERWORTH":
                    filter_select = "Butterworth_LPF"
                else:
                    filter_select = "Gaussian_LPF"
            output = Filters.main(input_image, filter_select, cutoff_frequency, order)
            output_image_name = output_dir + filter_select + '_Filtered_Image' + ".jpg"
            cv2.imwrite(output_image_name, output)
            out = Image.open(output_image_name)
            out = out.resize((600, 500), Image.ANTIALIAS)
            out = ImageTk.PhotoImage(out)
            self.canvas2.create_image(50, 10, image=out, anchor=tkinter.NW)
            self.canvas2.image = out

        if self.variable.get() == "Sharpening":
            image_name = 'lenna'
            f = Filtering(input_image)
            output = f.filter(self.variable1.get())
            if self.variable1.get() == 'LAPLACIAN':
                output_image_name = output_dir + image_name + "_laplacian.jpg"
            else:
                output_image_name = output_dir + image_name + "_unsharp.jpg"
            cv2.imwrite(output_image_name, output)
            out = Image.open(output_image_name)
            out = out.resize((600, 500), Image.ANTIALIAS)
            out = ImageTk.PhotoImage(out)
            self.canvas2.create_image(50, 10, image=out, anchor=tkinter.NW)
            self.canvas2.image = out
        if self.variable.get() == "Convolution":
            image_name = "lenna"
            kernel = np.ones((3, 3), np.float32) / 9
            output_img = cv2.filter2D(input_image, -1, kernel)
            output_image_path = output_dir + image_name + "_convolution.jpg"
            cv2.imwrite(output_image_path, output_img)
            output_img = Image.open(output_image_path)
            output_img = output_img.resize((600, 500), Image.ANTIALIAS)
            output_img = ImageTk.PhotoImage(output_img)
            self.canvas2.create_image(50, 10, image=output_img, anchor=tkinter.NW)
            self.canvas2.image = output_img

    def __init__(self,	window,	window_title):
        self.window	= window
        self.window.title(window_title)
        OPTIONS = [
            "High-Pass filter",
            "Low-Pass filter",
            "Sharpening",
            "Convolution"
        ]
        SUB_FILTER = ["IDEAL", "BUTTERWORTH", "GAUSSIAN"]

        # Create	a	canvas	that	can	fit	the	above	video	source	size
        self.canvas = tkinter.Canvas(window, width=800, height=700)
        self.canvas.grid(row=0, column=1, rowspan=15, columnspan=5)

        # Button	that	lets	the	user	take	a	snapshot
        self.b_snap = tkinter.Button(window, text="Upload Input Image", width=50, command=self.open_img)
        self.b_snap.grid(row=12, column=2, rowspan=4)

        self.canvas2 = tkinter.Canvas(window, width=800, height=700)
        self.canvas2.grid(row=0, column=13, rowspan=15, columnspan=5)

        self.variable = ttk.Combobox(window, value=OPTIONS)
        self.variable.current(0)
        self.variable.grid(row=12, column=13)

        # bind the combobox to another dropdown value setting
        self.variable.bind("<<ComboboxSelected>>", self.pick_dropdown)

        # self.variable1 = ttk.Combobox(window, value=[" "])
        self.variable1 = ttk.Combobox(window, value=SUB_FILTER)
        self.variable1.current(0)
        self.variable1.grid(row=12, column=15)

        self.args_holder = tkinter.Entry(window)
        self.args_holder.grid(row=13, column=13)

        self.submit = tkinter.Button(window, text="Submit", width=15, bg='blue', command=self.submit_data)
        self.submit.grid(row=13, column=15)

        self.window.mainloop()


App(tkinter.Tk(), 'DIP-Team-3')
