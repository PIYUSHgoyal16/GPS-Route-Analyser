# Importing required libraries 
import tkinter
from tkinter import *
from tkinter import Tk
from tkinter import Label
from tkinter import filedialog
from matplotlib import pyplot as plt
import numpy as np
import statistics as st

# Creating the class of the application
class Application(Tk):
    
    # Defining the __init__ function
    def __init__(self):
        super().__init__()
        self.geometry('550x1520')
        self.grid()
        

        self.dir_location=""
        self.dist=""
        self.avgtime=""
        self.avgspeed=""
        self.highEle=""
        self.lowEle=""
        self.eleLen=""
        self.lat=""
        self.long=""
        self.startPoint1=""
        self.endPoint1=""
        self.rides1=""
        self.startPoint2=""
        self.endPoint2=""
        self.rides2=""
        self.startPoint3=""
        self.endPoint3=""
        self.rides3=""
        self.startPoint4=""
        self.endPoint4=""
        self.rides4=""

        # File labels 
        self.file_label=Label(self, text = "Directory Not Chosen ." + self.dir_location)
        self.file_label.pack()

        #Creating the browse button for choosing the text file in the GUI
        self.browse = tkinter.Button(self,text = "Choose Directory",command = self.set_dir_location)
        self.browse.pack()

        # Tiles for Groups
        self.group1 = Label(self, text="\nGroup 1")
        self.group1.config(font=("Helvetica", 18))
        self.group1.pack()
        self.startPt1 = Label(self, text="Start Point 1: " + self.startPoint1)
        self.startPt1.pack()
        self.endPt1 = Label(self, text="End Point 1: " + self.endPoint1)
        self.endPt1.pack()
        self.numOfRides1 = Label(self, text="Start Point 1: " + self.rides1)
        self.numOfRides1.pack()

        self.group2 = Label(self, text="\nGroup 2")
        self.group2.config(font=("Helvetica", 18))
        self.group2.pack()
        self.startPt2 = Label(self, text="Start Point 2: " + self.startPoint2)
        self.startPt2.pack()
        self.endPt2 = Label(self, text="End Point 2: " + self.endPoint2)
        self.endPt2.pack()
        self.numOfRides2 = Label(self, text="Start Point 2: " + self.rides2)
        self.numOfRides2.pack()

        self.group3 = Label(self, text="\nGroup 3")
        self.group3.config(font=("Helvetica", 18))
        self.group3.pack()
        self.startPt3 = Label(self, text="Start Point 3: " + self.startPoint3)
        self.startPt3.pack()
        self.endPt3 = Label(self, text="End Point 3: " + self.endPoint3)
        self.endPt3.pack()
        self.numOfRides3 = Label(self, text="Start Point 3: " + self.rides3)
        self.numOfRides3.pack()

        self.group4 = Label(self, text="\nGroup 4")
        self.group4.config(font=("Helvetica", 18))
        self.group4.pack()
        self.startPt4 = Label(self, text="Start Point 4: " + self.startPoint4)
        self.startPt4.pack()
        self.endPt4 = Label(self, text="End Point 4: " + self.endPoint4)
        self.endPt4.pack()
        self.numOfRides4 = Label(self, text="Start Point 4: " + self.rides4)
        self.numOfRides4.pack()


        # 3rd Point
        self.third = Label(self, text="\n3rd Point")
        self.third.config(font=("Helvetica", 18))
        self.third.pack()
        self.latitude = Entry(self, textvariable=self.lat)
        self.latitude.pack()
        self.longitude = Entry(self, textvariable=self.long)
        self.longitude.pack()
        self.resolvethird = tkinter.Button(self,text = "Submit",command = self.resolve_third_point)
        self.resolvethird.pack()

        #Final Output
        self.stats = Label(self, text="\nStats")
        self.stats.config(font=("Helvetica", 18))
        self.stats.pack()
        self.SvsD = tkinter.Button(self,text = "Speed Vs Date",command = self.speedVsDate)
        self.SvsD.pack()
        self.TvsD = tkinter.Button(self,text = "Time Vs Date",command = self.timeVsDate)
        self.TvsD.pack()
        self.EvsD = tkinter.Button(self,text = "Elevation-Speed Vs Date",command = self.elevationVsdate)
        self.EvsD.pack()
        
        self.routeLength = Label(self, text="Route Length: " + str(self.dist))
        self.routeLength.pack()
        self.eleRouteLength = Label(self, text="Elevated Route Length: " + str(self.eleLen))
        self.eleRouteLength.pack()
        self.Speed = Label(self, text="Average Speed: " + str(self.avgspeed))
        self.Speed.pack()
        self.Time = Label(self, text="Average Time: " + str(self.avgtime))
        self.Time.pack()
        self.Highest = Label(self, text="Highest Elevation Point: " + str(self.highEle))
        self.Highest.pack()
        self.Lowest = Label(self, text="Lowest Elevation Point: " + str(self.lowEle))
        self.Lowest.pack()
        
        

    # Defining the function that sets the main text file location
    def set_dir_location(self):
        self.dir_location = filedialog.askdirectory()
        self.file_label.config(text = "File: " + self.dir_location)
        self.file_function()

    def speedVsDate(self):
        pass

    def timeVsDate(self):
        pass

    def elevationVsdate(self):
        pass

    def resolve_third_point(self):
        pass

# Create and run the application
app = Application()
app.title("Statistics For the File")
app.mainloop()