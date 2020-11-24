#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 06:53:40 2020

@author: piyush
"""
import time
import pandas as pd
import matplotlib.pyplot as plt
import os
import gpxpy
import math

def gpx_dataframe(file):
    """
    
    Parameters
    ----------
    file : string
        path of the gpx file

    Returns
    -------
    df : pd.Dataframe
        Dataframe of gpx xml file        

    """
    gpx_file = open(file, 'r')
    gpx = gpxpy.parse(gpx_file)
    df = pd.DataFrame(columns=['lat', 'lon', 'ele', 'time'])
    for segment in gpx.tracks[0].segments: # all segments
        data = segment.points
        for point in data:
            df = df.append({'lon': point.longitude, 'lat' : point.latitude, 'ele' : point.elevation, 'time' : point.time}, ignore_index=True)
    return df


def dis_points(lat1, lon1, lat2, lon2):
    """
    
    Parameters
    ----------
    lat1 : Integer
        Latitude of first point
    lon1 : Integer
        Longitude of first point
    lat2 : Integer
        Latitude of second point
    lon2 : Integer
        Longitude of second point

    Returns
    -------
    distance : Integer
        distance between two points in kilometers

    """
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


def dist(file, diff):
    """
    
    Parameters
    ----------
    file : String
        The path of the gpx file whose distance needs to be calculated
    diff : Integer
        The difference between consecutive frames taken into consideration

    Returns
    -------
    exectime : Integer
        time required to calculate distance 
    distance : Integer
        route length of gpx file ride

    """

    df = gpx_dataframe(file)
    distance = 0
    i = 0
    
    # Start recording time and calculate distance
    start = time.time()
    
    while (i+distance < len(df)):
        long1 = df.loc[i]["lon"] 
        long2 = df.loc[i+diff]["lon"] 
        lat1 = df.loc[i]["lat"] 
        lat2 = df.loc[i+diff]["lat"]         
        
        distance += dis_points(lat1, long1, lat2, long2)
    
    end = time.time()
    exectime = end - start
    
    return exectime, distance

        
dir = "/home/piyush/IIT Mandi/GPS-Route-Analyser/sample_files"

observations = [2, 4, 6, 8, 16, 32, 64, 128]
times = []
dist_errors = []
actual_dist = []

# Initialise values
for i in range(len(observations)+1):
    times.append(0)
    dist_errors.append(0)


for i in observations:
    start = time.time()
    for file in os.listdir(dir):
        dist_error += 
    end = time.time()
    times.append(end-start)
    
for file in os.listdir(dir):

    # Calculate for most accurate case, i.e. diff = 1    
    tim, dis = dist(dir+"/"+file, 1)
    times[0] += tim
    
    t = 1
    for i in observations:
        obs_time, obs_dist = dist(dir+"/"+file, i)
        times[t] += obs_time 
        dist_error = pow((obs_dist - dis),2)
        dist_errors[t] += dist_error
        t += 1

observations = [1] + observations

# Plot the Results
plt.figure()
plt.plot(observations, times)
plt.xlabel("Difference between consecutive frames")
plt.ylabel("Time (in seconds)")
plt.title("Computation Time Analysis")
plt.legend()
plt.show()

plt.figure()
plt.plot(observations, dist_errors)
plt.xlabel("Difference between consecutive frames\n(In log scale)")
plt.ylabel("Percentage Error (in %)")
plt.xscale("log")
plt.title("Accuracy Analysis")
plt.legend()
plt.show()
 