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

class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
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
        self.avgs1=""
        self.avgs2=""
        self.avgt1=""
        self.avgt2=""
        
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
        self.browse1 = tkinter.Button(f11,text = "Choose Directory for Rider1",command = self.set_dir_location)
        self.browse1.pack(fill=BOTH)
        
        self.browse2 = tkinter.Button(f11,text = "Choose Directory for Rider2",command = self.rider2)
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
        self.startlat_entry = Entry(f41)
        self.startlat_entry.pack(fill=X, expand=True)
        
        self.startlon = Label(f42, text="Enter Group Starting point longitude " )
        self.startlon.pack(padx=5, pady=5, side=LEFT)
        self.startlon_entry = Entry(f42)
        self.startlon_entry.pack(fill=X, expand=True)
        
        self.endlat = Label(f43, text="Enter Group Ending point latitude " )
        self.endlat.pack(padx=5, pady=5, side=LEFT)
        self.endlat_entry = Entry(f43)
        self.endlat_entry.pack(fill=X, expand=True)
        
        self.endlon = Label(f44, text="Enter Group Ending point longitude " )
        self.endlon.pack(padx=5, pady=5, side=LEFT)
        self.endlon_entry = Entry(f44)
        self.endlon_entry.pack(fill=X, expand=True)
        
        self.midlat = Label(f45, text="Enter Group Mid point latitude " )
        self.midlat.pack(padx=5, pady=5, side=LEFT)
        self.midlat_entry = Entry(f45)
        self.midlat_entry.pack(fill=X, expand=True)
        
        self.midlon = Label(f46, text="Enter Group mid point longitude " )
        self.midlon.pack(padx=5, pady=5, side=LEFT)
        self.midlon_entry = Entry(f46)
        self.midlon_entry.pack(fill=X, expand=True)
        
 
        
      

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
        """
        self.SvsD = tkinter.Button(f7,text = "Speed Vs Date",command = self.speedVsDate)
        self.SvsD.pack()
        self.TvsD = tkinter.Button(f7,text = "Time Vs Date",command = self.timeVsDate) 
        self.TvsD.pack()
        self.EvsD = tkinter.Button(f7,text = "Elevation-Speed Vs Date",command = self.elevationVsdate)
        self.EvsD.pack()
        """
        
        self.routeLength = Label(f7, text="\nRoute Length: " + str(self.dist))
        self.routeLength.pack()
        self.eleRouteLength = Label(f7, text="Elevated Route Length: " + str(self.eleLen))
        self.eleRouteLength.pack()
        #self.Speed = Label(f7, text="Average Speed: " + str(self.avgspeed))
        #self.Speed.pack()
        #self.Time = Label(f7, text="Average Time: " + str(self.avgtime))
        #self.Time.pack()
        self.Highest = Label(f7, text="Highest Elevation Point: " + str(self.highEle))
        self.Highest.pack()
        self.Lowest = Label(f7, text="Lowest Elevation Point: " + str(self.lowEle))
        self.Lowest.pack()
        
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
        self.avgSpeed1 = Label(f3a, text="Average Speed: " + str(self.avgs1))
        self.avgSpeed1.pack()
        self.avgsTime1 = Label(f3a, text="Average Time: " + str(self.avgt1))
        self.avgsTime1.pack()
        
        f4a=Frame(f2a,height=20,width=50, relief=RAISED, padx=15, pady=10, borderwidth=2)
        f4a.pack(fill='x',padx=5, pady=10, side=RIGHT)
        self.group2a = Label(f4a, text="Rider 2")
        self.group2a.config(font=("Helvetica", 18))
        self.group2a.pack()
        self.avgSpeed1 = Label(f4a, text="Average Speed: " + str(self.avgs2))
        self.avgSpeed1.pack()
        self.avgsTime1 = Label(f4a, text="Average Time: " + str(self.avgt2))
        self.avgsTime1.pack()
        
        self.f44=Frame(my_frame2,height=20,width=500, relief=RAISED, padx=15, pady=10, borderwidth=2)
        self.f44.pack(fill='x')
        
        self.averageSpeed = tkinter.Button(self.f44,text = "Speed vs Date",command = self.averageSpeed)
        self.averageSpeed.pack()
        self.averageTime = tkinter.Button(self.f44,text = "Time vs Date",command = self.averageTime)
        self.averageTime.pack()
        self.elevationspeed = tkinter.Button(self.f44,text = "Elevation vs Date",command = self.averageTime)
        self.elevationspeed.pack()
        
        
        self.fn = tkinter.Frame(my_frame2, width=800, height=300, padx=10 , pady=15 , bg="white")
        self.fn.pack(side=tkinter.TOP, expand=tkinter.NO, fill=tkinter.NONE)
        
        


    # Defining the function that sets the main text file location
    def rider2(self):
        global my_notebook
        self.dir_location2 = filedialog.askdirectory()
        self.file_label.config(text = "File: " + self.dir_location2)
        self.status.config(text="STATUS: PROCESSING")
        self.status.config(foreground="blue")
        messagebox.showinfo("Status","Start Processing?")
        self.fill_info()

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
    def set_dir_location(self):
        self.dir_location = filedialog.askdirectory()
        self.file_label.config(text = "File: " + self.dir_location)
        self.status.config(text="STATUS: PROCESSING")
        self.status.config(foreground="blue")
        messagebox.showinfo("Status","Start Processing?")
        
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
        for widget in self.fm.winfo_children():
            widget.destroy()

        f=Figure(figsize = (8,4) , dpi=100)
        a=f.add_subplot(111)
        a.bar(self.datesR1 , self.distancesR1, width=0.8, label="Rider 1")
        
        a.bar(self.datesR2 , self.distancesR2, label="Rider 2")

        a.set_title("Distances Vs Dates")
        a.set_xlabel("Dates (in MM/DD/YYYY)")
        a.set_ylabel("Distances (in km)")
        a.legend()

        canvas=FigureCanvasTkAgg(f , self.fm)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP , fill=tkinter.BOTH , expand=True)

    #Creating function to display the speed vs date graph
    def allspeedVsdate(self):
        for widget in self.fm.winfo_children():
            widget.destroy()

        f=Figure(figsize = (8,4) , dpi=100)
        a=f.add_subplot(111)
        a.bar(self.datesR1 , self.speedR1, width=0.8, label="Rider 1")
        
        a.bar(self.datesR2 , self.speedR2, label="Rider 2")

        a.set_title("Speed Vs Dates")
        a.set_xlabel("Dates (in MM/DD/YYYY)")
        a.set_ylabel("Speed (in km/hour)")
        a.legend()

        canvas=FigureCanvasTkAgg(f , self.fm)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP , fill=tkinter.BOTH , expand=True)

    #Creating function to display the plot for speed vs date graph
    def speedVsDate(self):
        dates = []
        speed = []

        for i in self.dates:
            dates.append(i.strftime("%m/%d/%Y"))
            speed.append((self.dist*60)/self.durations[i])

        plt.bar(dates,speed,align='center')
        plt.title('Plot for Speed of Same Ride Vs Date',fontweight ="bold") 
        plt.xlabel('Date (MM/DD/YYYY)',fontsize=15)
        plt.xticks(rotation=45)
        plt.ylabel('Speed (Km/Hour) ',fontsize=15)
        plt.show()

    #Creating function to display the time vs date graph
    def timeVsDate(self):
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
        self.status.config(text="STATUS: PROCESSING")
        self.status.config(foreground="blue")
        messagebox.showinfo("Status","Start Processing?")
        for group in self.groups[int(self.groupNumber.get())-1]:
            if (self.point(group, float(self.long.get()), float(self.lat.get()))):
                ridedate = group.loc[0]["time"].date()
                self.dates.append(ridedate)
                dur = self.time(group) / 60
                self.durations[ridedate] = dur
                upward_dur = self.upward_time(group) / 60
                self.upwardDurations[ridedate] = upward_dur
                
        self.dates.sort()

        ''' Route Length'''
        self.dist = self.route_len(self.groups[int(self.groupNumber.get())-1][0])
        self.routeLength.config(text="\nRoute Length: " + str(round(self.dist,3)) + " km")
        
        ''' Average Time'''
        self.avgtime = self.time(self.groups[int(self.groupNumber.get())-1][0])
        self.Time.config(text="Average Time: " + str(round(self.avgtime/3600,3)) + " hours")
        
        ''' Average Speed'''
        self.avgspeed = (self.dist*3600) / self.avgtime
        self.Speed.config(text="Average Speed: " + str(round(self.avgspeed,3)) + " km/hour")
        
        ''' Maximum Elevation'''
        self.highEle = self.highest_ele(self.groups[int(self.groupNumber.get())-1][0])
        self.Highest.config(text="Maximum Elevation: " + str(self.highEle))

        ''' Minimum Elevation'''
        self.lowEle = self.lowest_ele(self.groups[int(self.groupNumber.get())-1][0])
        self.Lowest.config(text="Minimum Elevation: " + str(self.lowEle))
        
        ''' Upward Elevated Path'''
        self.eleLen = self.upward_route_len(self.groups[int(self.groupNumber.get())-1][0])
        self.eleRouteLength.config(text="Elevated Path: " + str(round(self.eleLen,3)) + " km")
        self.status.config(text="STATUS: PROCESSED")
        self.status.config(foreground="green")
        messagebox.showinfo("Status","Processed")
        

    #Takes file as input and returns the file data as a dataframe
    def gpx_dataframe(self, file):
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
        print(path_to_dir)
        dist = []
        times = []
        dates = []
        i = 0

        for file in os.listdir(path_to_dir):
            path = (str(path_to_dir+"/"+file))
            print(path)
            df = self.gpx_dataframe(path)
            
            dates.append(df.loc[0]["time"].date().strftime("%m/%d/%Y"))
            dist.append(self.route_len(df))
            times.append(self.time(df))

            i += 1

        return dist, dates, times, i

    #Function to calculate total time of ride
    def time(self, df):
        time_start = df.loc[0]["time"]
        time_end = df.loc[len(df)-1]["time"]
        timediff = time_end - time_start
        timediff = timediff.value * pow(10,-9)
        timediff /= 3600
        return timediff

    #Function to calculate total time of ride
    def upward_time(self, df):
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
        distance = 0
        for i in range(len(df)-1):
            ele1 = df.loc[i]["ele"]
            ele2 = df.loc[i+1]["ele"]
            if (ele1 < ele2):
                long1 = df.loc[i]["lon"] 
                long2 = df.loc[i+1]["lon"] 
                lat1 = df.loc[i]["lat"] 
                lat2 = df.loc[i+1]["lat"] 
                distance = distance + self.dis_points(lat1, long1, lat2, long2)    
        return distance


    #Function to check if given latitude and longitude are part of a dataframe
    def point(self, df, long, lat):
        for i in range(len(df)):
            print(self.dis_points(df.loc[i]["lat"],df.loc[i]["lon"],lat,long))
            if(self.dis_points(df.loc[i]["lat"],df.loc[i]["lon"],lat,long)<=self.threshold):
                return True
        return False
        
    def eleTime(self, groups):
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
        return max(df["ele"])

    def lowest_ele(self, df):
        return min(df["ele"])
    
    def averageSpeed(self):
        for widget in self.fn.winfo_children():
            widget.destroy()
        f=Figure(figsize = (8,3) , dpi=100)
        a=f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8] , [8,6,3,2,1,4,7,5])
        canvas=FigureCanvasTkAgg(f , self.fn)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP , fill=tkinter.BOTH , expand=True)
        
    def averageTime(self):
        for widget in self.fn.winfo_children():
            widget.destroy()
        f=Figure(figsize = (8,3) , dpi=100)
        a=f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8] , [1,5,8,7,4,2,3,6])
        canvas=FigureCanvasTkAgg(f , self.fn)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP , fill=tkinter.BOTH , expand=True)

# Create and run the application
app = Application()
app.title("GPS-Route Analyser")
app.mainloop()
