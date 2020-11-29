import tkinter
from tkinter import *
from tkinter import Tk
from tkinter import ttk
from tkinter import Label
from tkinter import StringVar
from tkinter import filedialog
from tkinter import messagebox
from matplotlib import pyplot as plt
import numpy as np
import statistics as st
import gpxpy
import pandas as pd
import math
from datetime import datetime
import os
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
# map functionality
import gpxpy
import mplleaflet
import matplotlib.pyplot as plt
import subprocess
        
# Creating the class of the application
class Application(Tk):
    
    # Defining the __init__ function
    def __init__(self):
        super().__init__()
        self.geometry('750x2520')
        self.grid()

        self.distancesR1 = []
        self.datesR1 = []
        self.timesR1 = []
        self.numR1 = 0
        self.speedR1 = []

        self.distancesR2 = []
        self.datesR2 = []
        self.timesR2 = []
        self.numR2 = 0
        self.speedR2 = []

        self.rider1 = []
        self.rider2 = []

        self.map_df = pd.DataFrame()

        self.routeDatesR1 = []
        self.routeSpeedR1 = []
        self.routeTimeR1 = []
        self.routeDatesR2 = []
        self.routeSpeedR2 = []
        self.routeTimeR2 = []

        self.dates = []
        self.durations = {}
        self.upwardDurations = {}

        self.alldates = []
        self.alldistances = {}
        self.alldurations = {}
        self.allupwardDurations = {}
        
        self.groupNumber=StringVar(self)
        self.lat=StringVar(self)
        self.long=StringVar(self)

        self.dir_location=""
        self.dir_location2=""
        self.dist=""
        self.avgtime=""
        self.avgspeed=""
        self.highEle=""
        self.lowEle=""
        self.eleLen=""
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
        self.avgspeed1=""
        self.avgspeed2=""
        self.avgtime1=""
        self.avgtime2=""
        
        #Created the variables for group number
        self.startLat=""
        self.startLon=""
        self.endLat=""
        self.endLon=""
        self.midLat=""
        self.midLon=""
        
        #Label Variables for group number
        self.startlat=""
        self.startlon=""
        self.endlat=""
        self.endlon=""
        self.midlat=""
        self.midlon=""
        
        #Entry Variables for group number
        self.startlat_entry=""
        self.startlon_entry=""
        self.endlat_entry=""
        self.endlon_entry=""
        self.midlat_entry=""
        self.midlon_entry=""
        
        self.groups = {}

        #Threshold to compare 2 points
        self.threshold = 1
        
        #Creating tabs for our GUI
        my_notebook=ttk.Notebook(self)
        my_notebook.pack()
        my_frame1=tkinter.Frame(my_notebook , width=700 , height=2400)
        my_frame2=tkinter.Frame(my_notebook , width=700 , height=2400)
        my_frame1.pack(fill="both" , expand=1)
        my_frame2.pack(fill="both" , expand=1)
        my_notebook.add(my_frame1, text="Tab1")
        my_notebook.add(my_frame2, text="Tab2")

        #Creating a frame for choose a directory in GUI
        
        
        f1=Frame(my_frame1,height=20,width=50, relief=RAISED, padx=15, pady=10, borderwidth=2)
        f1.pack(fill='x')

        f12=Frame(f1,height=20)
        f12.pack(fill='x')
 
        f11=Frame(f12,height=20)
        f11.pack(fill=BOTH, side=LEFT)

        # File labels 
        self.file_label=Label(f11, text = "Directory Not Chosen ." + self.dir_location)
        self.file_label.pack(fill=BOTH)

        #Creating the browse button for choosing the text file in the GUI
        self.browse1 = tkinter.Button(f11,text = "Choose Directory for Rider1",command = self.load_rider1)
        self.browse1.pack(fill=BOTH)
        
        self.browse2 = tkinter.Button(f11,text = "Choose Directory for Rider2",command = self.load_rider2)
        self.browse2.pack(fill=BOTH)

        self.status = Label(f12, text="STATUS: RUNNING")
        self.status.config(font=("Helvatica", 16))
        self.status.config(foreground="green")
        self.status.pack(side=RIGHT)
        
        
        f21=Frame(my_frame1,height=20,width=50, relief=RAISED, padx=15, pady=10, borderwidth=2)
        f21.pack(fill='x')
        
        
        f2=tkinter.Frame(f21,height=20,width=500, relief=RAISED, padx=15, pady=10, borderwidth=2)
        f2.pack(fill='x')

        #Creating tiles so as to show the groupings of GPX files(Similar to RecyclerView in android)
        f3=Frame(f2,height=20,width=50, relief=RAISED, padx=15, pady=10, borderwidth=2)
        f3.pack(padx=5, pady=10, side=LEFT)
        self.group1 = Label(f3, text="Rider 1")
        self.group1.config(font=("Helvetica", 18))
        self.group1.pack()
        self.dist1 = Label(f3, text="Distance: " + self.startPoint1)
        self.dist1.pack()
        self.avgs1 = Label(f3, text="Average Speed: " + self.endPoint1)
        self.avgs1.pack()
        self.numOfRides1 = Label(f3, text="Number of Rides: " + self.rides1)
        self.numOfRides1.pack()
        
        self.f22=Frame(f21,height=20,width=500, relief=RAISED, padx=15, pady=10, borderwidth=2)
        self.f22.pack(fill='x')
        
        f4=Frame(f2,height=20,width=50, relief=RAISED, padx=15, pady=10, borderwidth=2)
        f4.pack(fill='x',padx=5, pady=10, side=RIGHT)
        self.group2 = Label(f4, text="Rider 2")
        self.group2.config(font=("Helvetica", 18))
        self.group2.pack()
        self.dist2 = Label(f4, text="Distance: " + self.startPoint2)
        self.dist2.pack()
        self.avgs2 = Label(f4, text="Average Speed: " + self.endPoint2)
        self.avgs2.pack()
        self.numOfRides2 = Label(f4, text="Number of Rides: " + self.rides2)
        self.numOfRides2.pack()
        
        
        self.DistvsDate = tkinter.Button(self.f22,text = "Distance Vs Date",command = self.distVsDate)
        self.DistvsDate.pack()
        self.SpeedVsDate = tkinter.Button(self.f22,text = "Speed Vs Date",command = self.allspeedVsdate)
        self.SpeedVsDate.pack()
        
        
        self.fm = tkinter.Frame(my_frame1, width=800, height=320, padx=10 , pady=15 , bg="white")
        self.fm.pack(side=tkinter.TOP, expand=tkinter.NO, fill=tkinter.NONE)

        f=tkinter.Frame(my_frame1,height=20,width=50, relief=RAISED, padx=15, pady=10, borderwidth=2)
        f.pack(fill='x')        

        #Creating the Label for the third point
        self.third = Label(f, text="3rd Point")
        self.third.config(font=("Helvetica", 18))
        self.third.pack()
        
        
        #Frame for taking input of group points
        f41=Frame(f,height=20,width=50, relief=RAISED, borderwidth=2)
        f41.pack(fill='x')
        f42=Frame(f,height=20,width=50, relief=RAISED, borderwidth=2)
        f42.pack(fill='x')
        f43=Frame(f,height=20,width=50, relief=RAISED, borderwidth=2)
        f43.pack(fill='x')
        
        f44=Frame(f,height=20,width=50, relief=RAISED, borderwidth=2)
        f44.pack(fill='x')
        f45=Frame(f,height=20,width=50, relief=RAISED, borderwidth=2)
        f45.pack(fill='x')
        f46=Frame(f,height=20,width=50, relief=RAISED, borderwidth=2)
        f46.pack(fill='x')
        
        #Inputing the group points
        self.startlat = Label(f41, text="Enter Group Starting point latitude " )
        self.startlat.pack(padx=5, pady=5, side=LEFT)
        self.startlat_entry = Entry(f41 , width=55)
        self.startlat_entry.pack(side=RIGHT)
        
        self.startlon = Label(f42, text="Enter Group Starting point longitude " )
        self.startlon.pack(padx=5, pady=5, side=LEFT)
        self.startlon_entry = Entry(f42 , width=55)
        self.startlon_entry.pack(side=RIGHT)
        
        self.endlat = Label(f43, text="Enter Group Ending point latitude " )
        self.endlat.pack(padx=5, pady=5, side=LEFT)
        self.endlat_entry = Entry(f43 , width=55)
        self.endlat_entry.pack(side=RIGHT)
        
        self.endlon = Label(f44, text="Enter Group Ending point longitude " )
        self.endlon.pack(padx=5, pady=5, side=LEFT)
        self.endlon_entry = Entry(f44 , width=55)
        self.endlon_entry.pack(side=RIGHT)
        
        self.midlat = Label(f45, text="Enter Group Mid point latitude " )
        self.midlat.pack(padx=5, pady=5, side=LEFT)
        self.midlat_entry = Entry(f45 , width=55)
        self.midlat_entry.pack(side=RIGHT)
        
        self.midlon = Label(f46, text="Enter Group mid point longitude " )
        self.midlon.pack(padx=5, pady=5, side=LEFT)
        self.midlon_entry = Entry(f46 , width=55)
        self.midlon_entry.pack(side=RIGHT)
      
    
        #Creating the submit button
        self.resolvethird = tkinter.Button(f,text = "Submit",command = self.resolve_third_point)
        self.resolvethird.pack()

        f8=Frame(my_frame2,height=20,width=50, relief=RAISED, padx=15, pady=10, borderwidth=2)
        f8.pack(fill='x')

        f7=Frame(f8,height=20,width=50, relief=RAISED, padx=15, pady=10, borderwidth=2)
        f7.pack(fill='x')
        
        #Displaying the final output
        self.stats = Label(f7, text="Route " + self.groupNumber.get() + " Stats")
        self.stats.config(font=("Helvetica", 18))
        self.stats.pack()
        
        
        self.routeLength = Label(f7, text="\nRoute Length: " + str(self.dist))
        self.routeLength.pack()
        self.eleRouteLength = Label(f7, text="Elevated Route Length: " + str(self.eleLen))
        self.eleRouteLength.pack()
        self.Highest = Label(f7, text="Highest Elevation Point: " + str(self.highEle))
        self.Highest.pack()
        self.Lowest = Label(f7, text="Lowest Elevation Point: " + str(self.lowEle))
        self.Lowest.pack()
        self.map_button = tkinter.Button(f7,text = "Route Map",command = self.plot_map)
        self.map_button.pack()
        
        #f29=Frame(my_frame2,height=20,width=50, relief=RAISED, padx=15, pady=10, borderwidth=2)
        #f29.pack(fill='x')
        
        
    
        f2a=tkinter.Frame(my_frame2,height=20,width=500, relief=RAISED, padx=15, pady=10, borderwidth=2)
        f2a.pack(fill='x')

        #Creating tiles so as to show the groupings of GPX files(Similar to RecyclerView in android)
        f3a=Frame(f2a,height=20,width=50, relief=RAISED, padx=15, pady=10, borderwidth=2)
        f3a.pack(padx=5, pady=10, side=LEFT)
        self.group1a = Label(f3a, text="Rider 1")
        self.group1a.config(font=("Helvetica", 18))
        self.group1a.pack()
        self.avgSpeed1 = Label(f3a, text="Average Speed: " + str(self.avgspeed1))
        self.avgSpeed1.pack()
        self.avgsTime1 = Label(f3a, text="Average Time: " + str(self.avgtime1))
        self.avgsTime1.pack()
        
        f4a=Frame(f2a,height=20,width=50, relief=RAISED, padx=15, pady=10, borderwidth=2)
        f4a.pack(fill='x',padx=5, pady=10, side=RIGHT)
        self.group2a = Label(f4a, text="Rider 2")
        self.group2a.config(font=("Helvetica", 18))
        self.group2a.pack()
        self.avgSpeed2 = Label(f4a, text="Average Speed: " + str(self.avgspeed2))
        self.avgSpeed2.pack()
        self.avgsTime2 = Label(f4a, text="Average Time: " + str(self.avgtime2))
        self.avgsTime2.pack()
        
        self.f44=Frame(my_frame2,height=20,width=500, relief=RAISED, padx=15, pady=10, borderwidth=2)
        self.f44.pack(fill='x')
        
        self.averageSpeed = tkinter.Button(self.f44,text = "Speed vs Date",command = self.routeAverageSpeed)
        self.averageSpeed.pack()
        self.averageTime = tkinter.Button(self.f44,text = "Time vs Date",command = self.routeAverageTime)
        self.averageTime.pack()
        
        
        self.fn = tkinter.Frame(my_frame2, width=800, height=300, padx=10 , pady=15 , bg="white")
        self.fn.pack(side=tkinter.TOP, expand=tkinter.NO, fill=tkinter.NONE)
        
        


    # Defining the function that sets the main text file location
    def load_rider2(self):
        '''
        Utility function for selecting directory containing rider two's gpx files  

        Returns
        -------
        None.

        '''
        self.dir_location2 = filedialog.askdirectory()
        self.file_label.config(text = "File: " + self.dir_location2)
        self.status.config(text="STATUS: PROCESSING")
        self.status.config(foreground="blue")
        messagebox.showinfo("Status","Start Processing?")

        print("Choosed Directory for Rider2:\n" + self.dir_location2 + "\n")
        self.distancesR2, self.datesR2, self.timesR2, self.numR2 = self.group(self.dir_location2)

        self.speedR2 = []
        for i in range(len(self.distancesR2)):
            self.speedR2.append( self.distancesR2[i] / self.timesR2[i] )

        self.dist2.config(text="Distance: " + str(round(np.sum(self.distancesR2),2)) + " km")
        
        self.avgs2.config(text="Average Speed: " + str(round(np.sum(self.speedR2),2)) + " km/hour")
        
        self.numOfRides2.config(text="Number of Rides: "+str(self.numR2))

        self.status.config(text="STATUS: PROCESSED")
        self.status.config(foreground="green")
        messagebox.showinfo("Status","Processed")


    # Defining the function that sets the main text file location
    def load_rider1(self):
        '''
        Utility function for selecting directory containing rider one's gpx files  

        Returns
        -------
        None.

        '''
        self.dir_location = filedialog.askdirectory()
        self.file_label.config(text = "File: " + self.dir_location)
        self.status.config(text="STATUS: PROCESSING")
        self.status.config(foreground="blue")
        messagebox.showinfo("Status","Start Processing?")
        
        print("Choosed Directory for Rider1:\n" + self.dir_location + "\n")
        self.distancesR1, self.datesR1, self.timesR1, self.numR1 = self.group(self.dir_location)

        self.speedR1 = []
        for i in range(len(self.distancesR1)):
            self.speedR1.append( self.distancesR1[i] / self.timesR1[i] )

        self.dist1.config(text="Distance: " + str(round(np.sum(self.distancesR1),2)) + " km")
        
        self.avgs1.config(text="Average Speed: " + str(round(np.sum(self.speedR1),2)) + " km/hour")
        
        self.numOfRides1.config(text="Number of Rides: "+str(self.numR1))
        
        self.status.config(text="STATUS: PROCESSED")
        self.status.config(foreground="green")
        messagebox.showinfo("Status","Processed")


    #Creating function to display the distance vs date graph
    def distVsDate(self):     
        '''

        Utility function to display plot for distance vs date
        
        Returns
        -------
        None.
        
        '''        
        for widget in self.fm.winfo_children():
            widget.destroy()

        f=Figure(figsize = (8,3) , dpi=100)
        a=f.add_subplot(111)
        a.bar(self.datesR1 , self.distancesR1, width=0.8, label="Rider 1")
        
        a.bar(self.datesR2 , self.distancesR2, label="Rider 2")

        a.set_title("Distances Vs Dates")
        a.set_xlabel("Dates (in MM/DD/YYYY)")
        a.set_ylabel("Distances (in km)")
        plt.xticks(rotation=60)
        a.legend()

        canvas=FigureCanvasTkAgg(f , self.fm)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP , fill=tkinter.BOTH , expand=True)
    

    def in_viscinity(self, lat1, lon1, lat2, lon2):
        lat1 = round(lat1, 3)
        lon1 = round(lon1, 3)
        lat2 = round(lat2, 3)
        lon2 = round(lon2, 3)
        if((lat1 == lat2) and (lon1 == lon2)):
            return 1
        return 0

    def in_group(self, start_lat, start_lon, end_lat, end_lon, mid_lat, mid_lon, df):
        n = len(df)
        s = 0
        e = 0
        m = 0
        start_ind = 0
        end_ind = 0
        for i in range(n):
            if(s==0 and self.in_viscinity(start_lat,start_lon,df.iloc[i]["lat"], df.iloc[i]["lon"])):
                s = 1
                start_ind = i
            if(s!=0 and m==0 and self.in_viscinity(mid_lat,mid_lon,df.iloc[i]["lat"], df.iloc[i]["lon"])):
                m = 1
            if(s!=0 and e==0 and m!=0 and self.in_viscinity(end_lat,end_lon,df.iloc[i]["lat"], df.iloc[i]["lon"])):
                e = 1
                end_ind = i
        
        if(s==1 and e==1 and m==1 and start_ind<end_ind):
            return df.iloc[start_ind: end_ind+1]
        
        else:
            return -1


    #Creating function to display the speed vs date graph
    def allspeedVsdate(self):
        '''

        Utility function to display plot for speed vs date
        
        Returns
        -------
        None.
        
        '''        
        for widget in self.fm.winfo_children():
            widget.destroy()

        f=Figure(figsize = (8,3) , dpi=100)
        a=f.add_subplot(111)
        a.bar(self.datesR1 , self.speedR1, width=0.8, label="Rider 1")
        
        a.bar(self.datesR2 , self.speedR2, label="Rider 2")

        a.set_title("Speed Vs Dates")
        a.set_xlabel("Dates (in MM/DD/YYYY)")
        a.set_ylabel("Speed (in km/hour)")
        plt.xticks(rotation=60)
        a.legend()

        canvas=FigureCanvasTkAgg(f , self.fm)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP , fill=tkinter.BOTH , expand=True)

    #Creating function to display the plot for speed vs date graph
    def speedVsDate(self):
        '''

        Utility function to display plot for speed vs date
        
        Returns
        -------
        None.
        
        '''        
        dates = []
        speed = []

        for i in self.dates:
            dates.append(i.strftime("%m/%d/%Y"))
            speed.append((self.dist*60)/self.durations[i])

        plt.bar(dates,speed,align='center')
        plt.title('Plot for Speed of Same Ride Vs Date',fontweight ="bold") 
        plt.xlabel('Date (MM/DD/YYYY)',fontsize=15)
        plt.xticks(rotation=90)
        plt.ylabel('Speed (Km/Hour) ',fontsize=15)
        plt.show()

    #Creating function to display the time vs date graph
    def timeVsDate(self):
        '''

        Utility function to display plot for time vs date
        
        Returns
        -------
        None.
        
        '''        
        dates = []
        durations = []

        for i in self.dates:
            dates.append(i.strftime("%m/%d/%Y"))
            durations.append(self.durations[i])
            
        plt.bar(dates,durations,align='center')
        plt.title('Plot for Duration of Same Ride Vs Date',fontweight ="bold") 
        plt.xlabel('Date (MM/DD/YYYY)',fontsize=15)
        plt.xticks(rotation=45)
        plt.ylabel('Duration (Minutes)',fontsize=15)
        plt.show()

    #Creating function to display the elecation vs date graph
    def elevationVsdate(self):
        '''

        Utility function to display plot for elevation vs date
        
        Returns
        -------
        None.
        
        '''        
        dates = []
        durations = []

        for i in self.dates:
            dates.append(i.strftime("%m/%d/%Y"))
            durations.append(self.upwardDurations[i])
            
        plt.bar(dates,durations,align='center')
        plt.title('Plot for Elevation Duration of Same Ride Vs Date',fontweight ="bold") 
        plt.xlabel('Date (MM/DD/YYYY)',fontsize=15)
        plt.xticks(rotation=45)
        plt.ylabel('Duration (Minutes)',fontsize=15)
        plt.show()


    def resolve_third_point(self):
        
        self.startLat = float(self.startlat_entry.get())
        self.startLon = float(self.startlon_entry.get())
        self.midLat = float(self.midlat_entry.get())
        self.midLon = float(self.midlon_entry.get())
        self.endLat = float(self.endlat_entry.get())
        self.endLon = float(self.endlon_entry.get())

        self.status.config(text="STATUS: PROCESSING")
        self.status.config(foreground="blue")
        messagebox.showinfo("Status","Start Processing?")

        self.rider1 = []
        self.rider2 = []
        flag = True

        for file in os.listdir(self.dir_location):
            path = (str(self.dir_location+"/"+file))
            print(path)
            df = self.gpx_dataframe(path)
            df = self.in_group(self.startLat, self.startLon, self.endLat, self.endLon, self.midLat, self.midLon, df)
            
            if (type(df) != type(0)):
                df.reset_index(drop=True, inplace=True)
                self.rider1.append(df)
                
        for file in os.listdir(self.dir_location2):
            path = (str(self.dir_location2+"/"+file))
            print(path)
            df = self.gpx_dataframe(path)
            df = self.in_group(self.startLat, self.startLon, self.endLat, self.endLon, self.midLat, self.midLon, df)
            
            if (type(df) != type(0)):
                df.reset_index(drop=True, inplace=True)
                self.rider2.append(df)
        
     
        if (len(self.rider1) != 0):
            length = self.route_len(self.rider1[0])
            self.set_route_stats(self.rider1[0])
            self.map_df = self.rider1[0]
            flag = False

            self.routeDatesR1 = []
            self.routeTimeR1 = []
            self.routeSpeedR1 = []

            for df in self.rider1:
                time_df = self.time(df)
                self.routeTimeR1.append(time_df)
                self.routeSpeedR1.append(length/time_df)
                self.routeDatesR1.append(df.loc[0]["time"].date().strftime("%m/%d/%Y"))

            ''' Average Time'''
            self.avgtime1 = np.sum(self.routeTimeR1)/len(self.routeTimeR1)
            self.avgsTime1.config(text="Average Time: " + str(round(self.avgtime1,3)) + " hours")
            
            ''' Average Speed'''
            self.avgspeed1 = (length) / self.avgtime1
            self.avgSpeed1.config(text="Average Speed: " + str(round(self.avgspeed1,3)) + " km/hour")
            

        if (len(self.rider2) != 0):
            length = self.route_len(self.rider2[0])
            if (flag):
                self.set_route_stats(self.rider2[0])
                self.map_df = self.rider2[0]
            
            self.routeDatesR2 = []
            self.routeTimeR2 = []
            self.routeSpeedR2 = []

            for df in self.rider2:
                time_df = self.time(df)
                self.routeTimeR2.append(time_df)
                self.routeSpeedR2.append(length / time_df)
                self.routeDatesR2.append(df.loc[0]["time"].date().strftime("%m/%d/%Y"))

            ''' Average Time'''
            self.avgtime2 = np.sum(self.routeTimeR2)/len(self.routeTimeR2)
            self.avgsTime2.config(text="Average Time: " + str(round(self.avgtime2,3)) + " hours")
            
            ''' Average Speed'''
            self.avgspeed2 = (length) / self.avgtime2
            self.avgSpeed2.config(text="Average Speed: " + str(round(self.avgspeed2,3)) + " km/hour")

        self.status.config(text="STATUS: PROCESSED")
        self.status.config(foreground="green")
        messagebox.showinfo("Status","Processed\nSwitch to Tab 2 for Results")
        

    def set_route_stats(self, df):
        ''' Route Length'''
        self.dist = self.route_len(df)
        self.routeLength.config(text="\nRoute Length: " + str(round(self.dist,3)) + " km")
        
        ''' Maximum Elevation'''
        self.highEle = self.highest_ele(df)
        self.Highest.config(text="Maximum Elevation: " + str(self.highEle) + " feet")

        ''' Minimum Elevation'''
        self.lowEle = self.lowest_ele(df)
        self.Lowest.config(text="Minimum Elevation: " + str(self.lowEle) + " feet")
        
        ''' Upward Elevated Path'''
        self.eleLen = self.upward_route_len(df)
        self.eleRouteLength.config(text="Elevated Path: " + str(round(self.eleLen,3)) + " km")


    def plot_map(self):
        fig, ax = plt.subplots()
        df = self.map_df

        df = df.dropna()
        ax.plot(df['lon'], df['lat'],color='darkorange', linewidth=5, alpha=0.5)
        mplleaflet.save_html(fig,fileobj="map.html")
        opener="xdg-open"
        x = os.fork()
        if (x==0):
            subprocess.call([opener, "map.html"])

    #Takes file as input and returns the file data as a dataframe
    def gpx_dataframe(self, file):
        '''

        Parameters
        ----------
        file : gpx file
            Input gpx file

        Returns
        -------
        df : Pandas dataframe 
            Dataframe for corresponding ride
            
        '''
        gpx_file = open(file, 'r')
        gpx = gpxpy.parse(gpx_file)
        df = pd.DataFrame(columns=['lat', 'lon', 'ele', 'time'])
        for segment in gpx.tracks[0].segments: # all segments
            data = segment.points
            for point in data:
                df = df.append({'lon': point.longitude, 'lat' : point.latitude, 'ele' : point.elevation, 'time' : point.time}, ignore_index=True)
        return df
    
    #Creating a function to find out the distance between two locations
    def dis_points(self, lat1, lon1, lat2, lon2):
        '''

        Parameters
        ----------
        lat1 : Float 
            latitude of first location
        lon1 : Float 
            longitude of first location
        lat2 : Float 
            latitude of second location
        lon2 : Float 
            longitude of second location

        Returns
        -------
        distance : Integer 
            distance between the two locations(in km)

        '''
        R = 6373.0
        lat1 = math.radians(lat1)
        lon1 = math.radians(lon1)
        lat2 = math.radians(lat2)
        lon2 = math.radians(lon2)
        
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c
        return distance


    #Function returns true if 2 dataframes have same starting and ending point
    def compare(self, df1, df2):
        '''

        Parameters
        ----------
        df1 :  Pandas dataframe 
            Dataframe corresponding to first ride
        df2 :  Pandas dataframe 
            Dataframe corresponding to second ride

        Returns
        -------
        bool: True/False
            True if same starting and ending point else false

        '''
        start1_lat = df1.loc[0]["lat"]
        start1_long = df1.loc[0]["lon"]
        start2_lat = df2.loc[0]["lat"]
        start2_long = df2.loc[0]["lon"]
        end1_lat = df1.loc[len(df1)-1]["lat"]
        end1_long = df1.loc[len(df1)-1]["lon"]
        end2_lat = df2.loc[len(df2)-1]["lat"]
        end2_long = df2.loc[len(df2)-1]["lon"]

        if(self.dis_points(start1_lat,start1_long,start2_lat,start2_long)<=self.threshold and self.dis_points(end1_lat,end1_long,end2_lat,end2_long)<=self.threshold):
            return True
        else:
            return False

    #Function to put routes with same satarting and ending point in one group
    def group(self, path_to_dir):
        '''

        Parameters
        ----------
        path_to_dir : string  
            path to a directory containing gpx files

        Returns
        -------
        dist : List
            Distance for each ride
        dates : List
            dates for each ride
        times : List
            Time taken for each ride
        i : Integer
            Number of rides

        '''
        dist = []
        times = []
        dates = []
        i = 0

        print("Processing files:")
        for file in os.listdir(path_to_dir):
            path = (str(path_to_dir+"/"+file))
            print(path)
            df = self.gpx_dataframe(path)
            
            dates.append(df.loc[0]["time"].date().strftime("%m/%d/%Y"))
            dist.append(self.route_len(df))
            times.append(self.time(df))

            i += 1

        print("Processing finished\n")
        return dist, dates, times, i

    #Function to calculate total time of ride
    def time(self, df):
        '''

        Parameters
        ----------
        df : Pandas dataframe 
            Dataframe for corresponding ride

        Returns
        -------
        timediff : Integer 
            route travelling time in hours 

        '''
        time_start = df.loc[0]["time"]
        time_end = df.loc[len(df)-1]["time"]
        timediff = time_end - time_start
        timediff = timediff.value * pow(10,-9)
        timediff /= 3600
        return timediff

    #Function to calculate total time of ride
    def upward_time(self, df):
        '''
        
        Parameters
        ----------
        df : Pandas dataframe 
            Dataframe for corresponding ride

        Returns
        -------
        timediff : Integer 
            upward/elevation travelling time in hours  

        '''
        timediff = 0
        for i in range(len(df)-1):
            ele1 = df.loc[i]["ele"]
            ele2 = df.loc[i+1]["ele"]
            if (ele1 < ele2):
                time_start = df.loc[i]["time"]
                time_end = df.loc[i+1]["time"]
                temptime = time_end - time_start
                timediff += temptime.value * pow(10,-9)
        return timediff

    #Function to calculate distance travelled in a ride
    def route_len(self, df):
        """
        
        Parameters
        ----------
        df : Dataframe
            Dataframe for corresponding ride
        Returns
        -------
        distance : Integer
            route length of gpx file ride (in km)
        """
        distance = 0
        i = 0
        
        while (i + 64 < len(df)):
            long1 = df.iloc[i]["lon"] 
            long2 = df.iloc[i+64]["lon"] 
            lat1 = df.iloc[i]["lat"] 
            lat2 = df.iloc[i+64]["lat"]         
            
            distance += self.dis_points(lat1, long1, lat2, long2)
            i += 64
        
        return distance

    #Function to calculate distance travelled in a ride
    def upward_route_len(self, df):
        '''

        Parameters
        ----------
        df : Pandas dataframe
            Dataframe for corresponding ride

        Returns
        -------
        distance : Integer
                upward route length of gpx file ride (in km)  

        '''
        distance = 0
        i = 0
        
        while (i + 64 < len(df)):
            ele1 = df.loc[i]["ele"]
            ele2 = df.loc[i+1]["ele"]
            if (ele1 < ele2):
                long1 = df.iloc[i]["lon"] 
                long2 = df.iloc[i+64]["lon"] 
                lat1 = df.iloc[i]["lat"] 
                lat2 = df.iloc[i+64]["lat"]         
            
                distance += self.dis_points(lat1, long1, lat2, long2)
            i += 64
        return distance


    #Function to check if given latitude and longitude are part of a dataframe
    def point(self, df, long, lat):
        '''

        Parameters
        ----------
        df : Pandas dataframe
            Dataframe for corresponding ride
        long : Float 
            longitude
        lat : Float 
            latitude

        Returns
        -------
        bool : True or false
            Return true if given latitude and longitude are part of a dataframe else false

        '''
        for i in range(len(df)):
            print(self.dis_points(df.loc[i]["lat"],df.loc[i]["lon"],lat,long))
            if(self.dis_points(df.loc[i]["lat"],df.loc[i]["lon"],lat,long)<=self.threshold):
                return True
        return False
        
    def eleTime(self, groups):
        '''
        
        Parameters
        ----------
        groups : 

        Returns
        -------
        None.

        '''
        for i in range(len(groups)):
            plt.figure()
            plt.title("Time taken on different days for longitude: ",groups[i][0].loc[0]["lon"],"and latitude: ",groups[i][0].loc[0]["lat"])
            date=[]
            time=[]
            for j in range(len(groups[i])):
                date.append(groups[i][j].loc[0]["time"].date())
                time.append(groups[i][j].loc[0]["time"].time())
                plt.scatter(date,time)
                plt.xlabel("Date")
                plt.ylabel("Time")
        
    def highest_ele(self, df):
        '''
        
        Parameters
        ----------
        df : Pandas Dataframe
            Dataframe for corresponding ride

        Returns
        -------
        Highest elevation : Integer
                        Returns highest elevation

        '''
        return max(df["ele"])

    def lowest_ele(self, df):
        '''
        
        Parameters
        ----------
        df : Pandas dataframe
             Dataframe for corresponding ride

        Returns
        -------
        
        Lowest elevation : Integer
                        Returns lowest elevation

        '''
        return min(df["ele"])
    
    def routeAverageSpeed(self):
        for widget in self.fn.winfo_children():
            widget.destroy()

        f=Figure(figsize = (8,4) , dpi=100)
        a=f.add_subplot(111)
        a.bar(self.routeDatesR1 , self.routeSpeedR1, width=0.8, label="Rider 1")
        
        a.bar(self.routeDatesR2 , self.routeSpeedR2, label="Rider 2")

        a.set_title("Speed Vs Dates")
        a.set_xlabel("Dates (in MM/DD/YYYY)")
        a.set_ylabel("Speed (in km/hour)")
        plt.xticks(rotation=60)
        a.legend()

        canvas=FigureCanvasTkAgg(f , self.fn)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP , fill=tkinter.BOTH , expand=True)
        
    def routeAverageTime(self):
        for widget in self.fn.winfo_children():
            widget.destroy()

        f=Figure(figsize = (8,4) , dpi=100)
        a=f.add_subplot(111)
        a.bar(self.routeDatesR1 , self.routeTimeR1, width=0.8, label="Rider 1")
        
        a.bar(self.routeDatesR2 , self.routeTimeR2, label="Rider 2")

        a.set_title("Speed Vs Dates")
        a.set_xlabel("Dates (in MM/DD/YYYY)")
        a.set_ylabel("Time (in hour)")
        plt.xticks(rotation=60)
        a.legend()

        canvas=FigureCanvasTkAgg(f , self.fn)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP , fill=tkinter.BOTH , expand=True)


# Create and run the application
app = Application()
app.title("GPS-Route Analyser")
app.mainloop()
