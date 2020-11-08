# Importing required libraries 
import tkinter
from tkinter import *
from tkinter import Tk
from tkinter import Label
from tkinter import filedialog
from matplotlib import pyplot as plt
import numpy as np
import statistics as st
import gpxpy
import pandas as pd
import math
import os

# Creating the class of the application
class Application(Tk):
    
    # Defining the __init__ function
    def __init__(self):
        super().__init__()
        self.geometry('550x1520')
        self.grid()
        
        self.groupNumber=""
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

        self.groups = {}

        #Threshold to compare 2 points
        self.threshold = 1

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
        self.group_no = Entry(self, textvariable=self.groupNumber)
        self.group_no.pack()
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
        self.groups = self.group(self.dir_location)
        
        self.startPoint1 = "lat: "+str(self.groups[0][0].loc[0]['lat']) + "\tLong: "+str(self.groups[0][0].loc[0]['lon'])
        self.startPt1.config(text="Start Point 1: " + self.startPoint1)
        
        self.endPoint1 = "lat: "+str(self.groups[0][0].loc[len(self.groups[0][0])-1]["lat"]) + "\tLong: "+str(self.groups[0][0].loc[len(self.groups[0][0])-1]["lon"])
        self.endPt1.config(text="End Point 1: " + self.endPoint1)
        
        self.numOfRides1.config(text="Number of Rides: "+str(len(self.groups[0])))
        
        if (len(self.groups) > 1):
            self.startPoint2 = "lat: "+str(self.groups[1][0].loc[0]['lat']) + "\tLong: "+str(self.groups[1][0].loc[0]['lon'])
            self.startPt2.config(text="Start Point 2: " + self.startPoint2)
            
            self.endPoint2 = "lat: "+str(self.groups[1][0].loc[len(self.groups[1][0])-1]["lat"]) + "\tLong: "+str(self.groups[1][0].loc[len(self.groups[1][0])-1]["lon"])
            self.endPt2.config(text="End Point 2: " + self.endPoint2)
            
            self.numOfRides2.config(text="Number of Rides: "+str(len(self.groups[1])))
                                    
        if (len(self.groups) > 2 ):
            self.startPoint3 = "lat: "+str(self.groups[2][0].loc[0]['lat']) + "\tLong: "+str(self.groups[2][0].loc[0]['lon'])
            self.startPt3.config(text="Start Point 3: " + self.startPoint3)
            
            self.endPoint3 = "lat: "+str(self.groups[2][0].loc[len(self.groups[2][0])-1]["lat"]) + "\tLong: "+str(self.groups[2][0].loc[len(self.groups[2][0])-1]["lon"])
            self.endPt3.config(text="End Point 3: " + self.endPoint3)
            
            self.numOfRides3.config(text="Number of Rides: "+str(len(self.groups[2])))
                                    
        if (len(self.groups) > 3 ):
            self.startPoint4 = "lat: "+str(self.groups[3][0].loc[0]['lat']) + "\tLong: "+str(self.groups[3][0].loc[0]['lon'])
            self.startPt4.config(text="Start Point 4: " + self.startPoint4)
            
            self.endPoint4 = "lat: "+str(self.groups[3][0].loc[len(self.groups[3][0])-1]["lat"]) + "\tLong: "+str(self.groups[3][0].loc[len(self.groups[3][0])-1]["lon"])
            self.endPt4.config(text="End Point 4: " + self.endPoint4)
            
            self.numOfRides4.config(text="Number of Rides: "+str(len(self.groups[3])))
                                
        

    def speedVsDate(self):
        pass

    def timeVsDate(self):
        pass

    def elevationVsdate(self):
        pass

    def resolve_third_point(self):
        #for group in self.groups[self.groupNumber]:
        self.startPoint4 = "lat: "+str(self.groups[3][0].loc[0]['lat']) + "\tLong: "+str(self.groups[3][0].loc[0]['lon'])
        self.startPt4.config(text="Start Point 4: " + self.startPoint4)
        pass


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
    def comparedf(self, df1, df2):
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
                if(self.comparedf(group[j][0],df)):
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
            return time_end - time_start

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

       

        #Function to check if given latitude and longitude are part of a dataframe
        def point(self, df, long, lat):
            for i in range(len(df)):
                if(self.dis_points(df.loc[i]["lat"],df.loc[i]["lon"],lat,long)<=self.threshold):
                    return True
            return False

        def dateTime(self, groups):
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
            return max(df["ele"])

# Create and run the application
app = Application()
app.title("Statistics For the File")
app.mainloop()









# groups = group("/home/jahnvi/Downloads/LAP_Main Project/rider3")
