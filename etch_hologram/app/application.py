import tkinter as tk
from tkinter import filedialog

class Application(tk.Frame):
    def __init__(self, master=None):
        """
        This is a constructor for a tkinter Frame object. It initializes the object and creates the widgets for the frame.
        @param master - the parent widget
        @return None
        """
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        

    def createWidgets(self):
        """
        This code defines a function that creates a GUI with several widgets. 
        """
        # Create a Frame for the file button
        file_frame = tk.Frame(self)
        file_frame.pack(side="top", pady=10)

        # Create the file button and add it to the frame
        self.file_button = tk.Button(file_frame, text="Open File", command=self.open_file)
        self.file_button.pack(side="left", padx=10)

        # Create a Frame for the sliders
        slider_frame = tk.Frame(self)
        slider_frame.pack(side="top", pady=10)

        # Create the sliders and add them to the frame
        self.rotation_slider = tk.Scale(slider_frame, from_=-2, to=2, showvalue=True, resolution=0.1, orient="horizontal", borderwidth=2, relief="groove", label="Rotation")
        self.rotation_slider.pack(side="left", padx=10)
        self.density_slider = tk.Scale(slider_frame, from_=2, to=50, showvalue=True, resolution=0.1, orient="horizontal", borderwidth=2, relief="groove", label="Density")
        self.density_slider.pack(side="left", padx=10)
        self.x_adjust_slider = tk.Scale(slider_frame, from_=-500, to=500, showvalue=True, resolution=0.1, orient="horizontal", borderwidth=2, relief="groove", label="X Adjustment")
        self.x_adjust_slider.pack(side="left", padx=10)


        # Create the y_adjust slider and add it beside the canvas
        self.y_adjust_slider = tk.Scale(self, from_=-500, to=500, showvalue=True, resolution=0.1, orient="vertical", borderwidth=2, relief="groove", label="Y Adjustment")
        self.y_adjust_slider.pack(side="left", padx=10)
        self.canvas = tk.Canvas(self, width=1000, height=1000, borderwidth=2, relief="solid")
        self.canvas.pack(side="left")

        # Configure the sliders to call the on_slider_change method when their value changes
        self.rotation_slider.config(command=self.on_slider_change)
        self.density_slider.config(command=self.on_slider_change)
        self.x_adjust_slider.config(command=self.on_slider_change)
        self.y_adjust_slider.config(command=self.on_slider_change)

    def open_file(self):
        """
        This function opens a file dialog box and allows the user to select a file. 
        @return The file path of the selected file.
        """
        file_path = tk.filedialog.askopenfilename()
        # Do something with the file_path, such as load an image onto the canvas

    def on_slider_change(self, value):
        """
        This function is called when a slider is changed. It prints the new value of the slider and deletes all items from a canvas.
        @param self - the object instance
        @param value - the new value of the slider
        """
        print("Slider value changed to", value)
        self.canvas.delete("all")





Application().mainloop()