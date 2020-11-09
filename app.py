# Importing required libraries 
import tkinter
from tkinter import *
from tkinter import Tk
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

# Creating the class of the application
class Application(Tk):
    
    # Defining the __init__ function
    def __init__(self):
        super().__init__()
        self.geometry('750x2520')
        self.grid()

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

        self.groups = {}

        #Threshold to compare 2 points
        self.threshold = 1

        #Creating a frame for choose a directory in GUI
        f1=Frame(self,height=20,width=50, relief=RAISED, padx=15, pady=10, borderwidth=2)
        f1.pack(fill='x')

        f12=Frame(f1,height=20)
        f12.pack(fill='x')
 
        f11=Frame(f12,height=20)
        f11.pack(fill=BOTH, side=LEFT)

        # File labels 
        self.file_label=Label(f11, text = "Directory Not Chosen ." + self.dir_location)
        self.file_label.pack(fill=BOTH)

        #Creating the browse button for choosing the text file in the GUI
        self.browse = tkinter.Button(f11,text = "Choose Directory",command = self.set_dir_location)
        self.browse.pack(fill=BOTH)

        self.status = Label(f12, text="STATUS: RUNNING")
        self.status.config(font=("Helvatica", 16))
        self.status.config(foreground="green")
        self.status.pack(side=RIGHT)
        
        f21=Frame(self,height=20,width=50, relief=RAISED, padx=15, pady=10, borderwidth=2)
        f21.pack(fill='x')

        f2=Frame(f21,height=20,width=500, relief=RAISED, padx=15, pady=10, borderwidth=2)
        f2.pack(fill='x')

        #Creating tiles so as to show the groupings of GPX files(Similar to RecyclerView in android)
        f3=Frame(f2,height=20,width=50, relief=RAISED, padx=15, pady=10, borderwidth=2)
        f3.pack(padx=5, pady=10, side=LEFT)
        self.group1 = Label(f3, text="Group 1")
        self.group1.config(font=("Helvetica", 18))
        self.group1.pack()
        self.startPt1 = Label(f3, text="Start Point 1: " + self.startPoint1)
        self.startPt1.pack()
        self.endPt1 = Label(f3, text="End Point 1: " + self.endPoint1)
        self.endPt1.pack()
        self.numOfRides1 = Label(f3, text="Start Point 1: " + self.rides1)
        self.numOfRides1.pack()

        f4=Frame(f2,height=20,width=50, relief=RAISED, padx=15, pady=10, borderwidth=2)
        f4.pack(fill='x',padx=5, pady=10, side=RIGHT)
        self.group2 = Label(f4, text="Group 2")
        self.group2.config(font=("Helvetica", 18))
        self.group2.pack()
        self.startPt2 = Label(f4, text="Start Point 2: " + self.startPoint2)
        self.startPt2.pack()
        self.endPt2 = Label(f4, text="End Point 2: " + self.endPoint2)
        self.endPt2.pack()
        self.numOfRides2 = Label(f4, text="Start Point 2: " + self.rides2)
        self.numOfRides2.pack()

        f22=Frame(f21,height=20,width=500, relief=RAISED, padx=15, pady=10, borderwidth=2)
        f22.pack(fill='x')

        f5=Frame(f22,height=20,width=500, relief=RAISED, padx=15, pady=10, borderwidth=2)
        f5.pack(fill='x',padx=5, pady=10, side=LEFT)
        self.group3 = Label(f5, text="Group 3")
        self.group3.config(font=("Helvetica", 18))
        self.group3.pack()
        self.startPt3 = Label(f5, text="Start Point 3: " + self.startPoint3)
        self.startPt3.pack()
        self.endPt3 = Label(f5, text="End Point 3: " + self.endPoint3)
        self.endPt3.pack()
        self.numOfRides3 = Label(f5, text="Start Point 3: " + self.rides3)
        self.numOfRides3.pack()

        f6=Frame(f22,height=20,width=500, relief=RAISED, padx=15, pady=10, borderwidth=2)
        f6.pack(fill='x',padx=5, pady=10, side=RIGHT)
        self.group4 = Label(f6, text="Group 4")
        self.group4.config(font=("Helvetica", 18))
        self.group4.pack()
        self.startPt4 = Label(f6, text="Start Point 4: " + self.startPoint4)
        self.startPt4.pack()
        self.endPt4 = Label(f6, text="End Point 4: " + self.endPoint4)
        self.endPt4.pack()
        self.numOfRides4 = Label(f6, text="Start Point 4: " + self.rides4)
        self.numOfRides4.pack()

        self.genstat = Label(f21, text="General Stat")
        self.genstat.config(font=("Helvetica", 18))
        self.genstat.pack()
        self.DistvsDate = tkinter.Button(f21,text = "Distance Vs Date",command = self.distVsDate)
        self.DistvsDate.pack()
        self.SpeedVsDate = tkinter.Button(f21,text = "Speed Vs Date",command = self.allspeedVsdate)
        self.SpeedVsDate.pack()

        f=Frame(self,height=20,width=50, relief=RAISED, padx=15, pady=10, borderwidth=2)
        f.pack(fill='x')        

        #Creating the Label for the third point
        self.third = Label(f, text="3rd Point")
        self.third.config(font=("Helvetica", 18))
        self.third.pack()
        
        f31=Frame(f,height=20,width=50, relief=RAISED, borderwidth=2)
        f31.pack(fill='x')
        f32=Frame(f,height=20,width=50, relief=RAISED, borderwidth=2)
        f32.pack(fill='x')
        f33=Frame(f,height=20,width=50, relief=RAISED, borderwidth=2)
        f33.pack(fill='x')

        #Creating the label and entry box for the group number
        self.gno = Label(f31, text="Enter Group No: " + self.endPoint4)
        self.gno.pack(padx=5, pady=5, side=LEFT)
        self.group_no = Entry(f31, textvariable=self.groupNumber)
        self.group_no.pack(fill=X, expand=True)

        #Creating the label and entry box for the latitude
        self.enterlat = Label(f32, text="Enter Latitude:   " + self.endPoint4)
        self.enterlat.pack(padx=5, pady=5, side=LEFT)
        self.latitude = Entry(f32, textvariable=self.lat)
        self.latitude.pack(fill=X, expand=True)
        
        #Creating the label and entry box for the longitude
        self.enterlong = Label(f33, text="Enter Longitude: " + self.endPoint4)
        self.enterlong.pack(padx=5, pady=5, side=LEFT)
        self.longitude = Entry(f33, textvariable=self.long)
        self.longitude.pack(fill=X, expand=True)

        #Creating the submit button
        self.resolvethird = tkinter.Button(f,text = "Submit",command = self.resolve_third_point)
        self.resolvethird.pack()

        f8=Frame(self,height=20,width=50, relief=RAISED, padx=15, pady=10, borderwidth=2)
        f8.pack(fill='x')

        f7=Frame(f8,height=20,width=50, relief=RAISED, padx=15, pady=10, borderwidth=2)
        f7.pack(fill='x')
        
        #Displaying the final output
        self.stats = Label(f7, text="Group " + self.groupNumber.get() + " Stats")
        self.stats.config(font=("Helvetica", 18))
        self.stats.pack()
        self.SvsD = tkinter.Button(f7,text = "Speed Vs Date",command = self.speedVsDate)
        self.SvsD.pack()
        self.TvsD = tkinter.Button(f7,text = "Time Vs Date",command = self.timeVsDate)
        self.TvsD.pack()
        self.EvsD = tkinter.Button(f7,text = "Elevation-Speed Vs Date",command = self.elevationVsdate)
        self.EvsD.pack()
        
        self.routeLength = Label(f7, text="\nRoute Length: " + str(self.dist))
        self.routeLength.pack()
        self.eleRouteLength = Label(f7, text="Elevated Route Length: " + str(self.eleLen))
        self.eleRouteLength.pack()
        self.Speed = Label(f7, text="Average Speed: " + str(self.avgspeed))
        self.Speed.pack()
        self.Time = Label(f7, text="Average Time: " + str(self.avgtime))
        self.Time.pack()
        self.Highest = Label(f7, text="Highest Elevation Point: " + str(self.highEle))
        self.Highest.pack()
        self.Lowest = Label(f7, text="Lowest Elevation Point: " + str(self.lowEle))
        self.Lowest.pack()
        
        

    # Defining the function that sets the main text file location
    def set_dir_location(self):
        self.dir_location = filedialog.askdirectory()
        self.file_label.config(text = "File: " + self.dir_location)
        self.status.config(text="STATUS: PROCESSING")
        self.status.config(foreground="blue")
        messagebox.showinfo("Status","Start Processing?")
        self.fill_info()
        self.groups = self.group(self.dir_location)
        
        self.startPoint1 = "Lat: "+str(round(self.groups[0][0].loc[0]['lat'], 4)) + "\tLong: "+str(round(self.groups[0][0].loc[0]['lon'], 4))
        self.startPt1.config(text="Start Point 1: " + self.startPoint1)
        
        self.endPoint1 = "Lat: "+str(round(self.groups[0][0].loc[len(self.groups[0][0])-1]["lat"],4)) + "\tLong: "+str(round(self.groups[0][0].loc[len(self.groups[0][0])-1]["lon"],4))
        self.endPt1.config(text="End Point 1: " + self.endPoint1)
        
        self.numOfRides1.config(text="Number of Rides: "+str(len(self.groups[0])))
        
        if (len(self.groups) > 1):
            self.startPoint2 = "Lat: "+str(round(self.groups[1][0].loc[0]['lat'], 4)) + "\tLong: "+str(round(self.groups[1][0].loc[0]['lon'],4))
            self.startPt2.config(text="Start Point 2: " + self.startPoint2)
            
            self.endPoint2 = "Lat: "+str(round(self.groups[1][0].loc[len(self.groups[1][0])-1]["lat"],4)) + "\tLong: "+str(round(self.groups[1][0].loc[len(self.groups[1][0])-1]["lon"],4))
            self.endPt2.config(text="End Point 2: " + self.endPoint2)
            
            self.numOfRides2.config(text="Number of Rides: "+str(len(self.groups[1])))
        else:
            self.startPt2.config(text="N/A")
            self.endPt2.config(text="N/A")
            self.numOfRides2.config(text="N/A")
                                    
        if (len(self.groups) > 2 ):
            self.startPoint3 = "Lat: "+str(round(self.groups[2][0].loc[0]['lat'],4)) + "\tLong: "+str(round(self.groups[2][0].loc[0]['lon'],4))
            self.startPt3.config(text="Start Point 3: " + self.startPoint3)
            
            self.endPoint3 = "Lat: "+str(round(self.groups[2][0].loc[len(self.groups[2][0])-1]["lat"],4)) + "\tLong: "+str(round(self.groups[2][0].loc[len(self.groups[2][0])-1]["lon"],4))
            self.endPt3.config(text="End Point 3: " + self.endPoint3)
            
            self.numOfRides3.config(text="Number of Rides: "+str(len(self.groups[2])))
        else:
            self.startPt3.config(text="N/A")
            self.endPt3.config(text="N/A")
            self.numOfRides3.config(text="N/A")
                                    
        if (len(self.groups) > 3 ):
            self.startPoint4 = "Lat: "+str(round(self.groups[3][0].loc[0]['lat'],4)) + "\tLong: "+str(round(self.groups[3][0].loc[0]['lon'],4))
            self.startPt4.config(text="Start Point 4: " + self.startPoint4)
            
            self.endPoint4 = "Lat: "+str(round(self.groups[3][0].loc[len(self.groups[3][0])-1]["lat"],4)) + "\tLong: "+str(round(self.groups[3][0].loc[len(self.groups[3][0])-1]["lon"],4))
            self.endPt4.config(text="End Point 4: " + self.endPoint4)
            
            self.numOfRides4.config(text="Number of Rides: "+str(len(self.groups[3])))
        else:
            self.startPt4.config(text="N/A")
            self.endPt4.config(text="N/A")
            self.numOfRides4.config(text="N/A")

        self.status.config(text="STATUS: PROCESSED")
        self.status.config(foreground="green")
        messagebox.showinfo("Status","Processed")


    def fill_info(self):
        for file in os.listdir(self.dir_location):
            path = (str(self.dir_location+"/"+file))
            df = self.gpx_dataframe(path)

            ridedate = df.loc[0]["time"].date()
            self.alldates.append(ridedate)
            self.alldistances[ridedate] = self.route_len(df)
            self.alldurations[ridedate] = self.time(df)
            self.allupwardDurations[ridedate] = self.upward_time(df)
        
        self.alldates.sort()

    #Creating function to display the distance vs date graph
    def distVsDate(self):
        dates = []
        distances = []

        for i in self.alldates:
            dates.append(i.strftime("%m/%d/%Y"))
            distances.append(self.alldistances[i])
            
        plt.bar(dates,distances,align='center')
        plt.title('Plot for Distance Vs Date',fontweight ="bold") 
        plt.xlabel('Date (MM/DD/YYYY)',fontsize=15)
        plt.xticks(rotation=45)
        plt.ylabel('Distances (km)',fontsize=15)
        plt.show()

    #Creating function to display the speed vs date graph
    def allspeedVsdate(self):
        dates = []
        speed = []

        for i in self.alldates:
            dates.append(i.strftime("%m/%d/%Y"))
            speed.append((self.alldistances[i]*60)/self.alldurations[i])

        plt.bar(dates,speed,align='center')
        plt.title('Plot for Speed Vs Date',fontweight ="bold") 
        plt.xlabel('Date (MM/DD/YYYY)',fontsize=15)
        plt.xticks(rotation=45)
        plt.ylabel('Speed (Km/Hour) ',fontsize=15)
        plt.show()

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
        group = {}
        i = 0
        for file in os.listdir(path_to_dir):
            path = (str(path_to_dir+"/"+file))
            print(path)
            df = self.gpx_dataframe(path)

            flag = True
            keys = group.keys()
            for j in (keys):
                if(self.compare(group[j][0],df)):
                    group[j].append(df)
                    flag = False
                    break
            if(flag==True):
                g = [df]
                group[i] = g   
                i = i+1    
        return group

    #Function to calculate total time of ride
    def time(self, df):
        time_start = df.loc[0]["time"]
        time_end = df.loc[len(df)-1]["time"]
        timediff = time_end - time_start
        timediff = timediff.value * pow(10,-9)
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
        distance = 0
        for i in range(len(df)-1):
            long1 = df.loc[i]["lon"] 
            long2 = df.loc[i+1]["lon"] 
            lat1 = df.loc[i]["lat"] 
            lat2 = df.loc[i+1]["lat"] 
            R = 6373.0
            lat1 = math.radians(lat1)
            lon1 = math.radians(long1)
            lat2 = math.radians(lat2)
            lon2 = math.radians(long2)

            dlon = lon2 - lon1
            dlat = lat2 - lat1

            a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            d = R * c

            distance = distance + d
            
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

# Create and run the application
app = Application()
app.title("GPS-Route Analyser")
app.mainloop()
