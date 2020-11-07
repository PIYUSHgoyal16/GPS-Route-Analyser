# Software Requirements Document

## Table of Content
1. [Introduction](#intro)
    1. [Need and Purpose](#need)  
    2. [Intended Audience](#audience)
    3. [Referances](#referances)

<br>

2. [Description](#description)
    1. [Features and Functions](#ff)
        1. [Features](#features)
        2. [Functions](#func)
    2. [Users](#users)
    3. [Operating Environment](#os)
        1. [Hardware](#hardware)
        2. [Software](#software)

<br>

3. [Specific Requirements](#specific)
    1. [Software Constraints](#softconst)
    2. [Additional Comments](#additional)

<h2 id="intro"> Introduction </h2>
    
`GPS-Route-Analyser` is a Graphical User Interface Driven Tool/Application that can be used to obtain statistical information about the cycling or jogging rides present in a GPX file that will be provided by the user as input.

The project is completely based on the python programming language.

This document describes the details of the requirements this tool is expected to incorporate and fulfill.

1. <h3 id="need"> Need and Purpose </h3>

    The health benefits of regular exercise and physical activity are hard to ignore. Everyone benefits from exercise, regardless of age, sex, or physical ability. Cycling and running are the most popular forms of cardio.

    With the introduction of new technologies like GPS tracking and services like Strava, it is convenient to track human exercises. Strava alone has over 50 million users and 1 million new users are joining each month. However, analyzing this information is equally important.

    Since tools like Strava adopt a freemium model, offering the analyzing part in an only paid subscription, make it hard for the users to actually keep a track of their progress `GPS-Route-Analyser` tries to capture the essence of quick and productive analysis by means of statistical data and plots, helping the users to establish a baseline, remind progress and helping them achieve their goals.

2. <h3 id="audience"> Intended Audience </h3>
    This document is intended for software developers and designers. Dr. Padmanabhan Rajan, the client, and professor under whose guidance this project is implemented may also read the document.
    

3. <h3 id="referances"> Referances </h3>
    [1] <a href="https://kivy.org/doc/stable/">Kivy Official Documentation</a>
    <br>
    [2] <a href="https://en.wikipedia.org/wiki/Strava">Strava Wikipedia</a>
    <br>
    [3] <a href="https://www.strava.com/">Strava</a>
    <br>
    [4] <a href="https://en.wikipedia.org/wiki/GPS_Exchange_Format">GPX Files</a>
    <br>
    [5] <a href="https://towardsdatascience.com/reverse-geocoding-in-python-a915acf29eb6">Reverse Geocoding in Python</a>

___

<h2 id="description"> Description </h2>

1. <h3 id="ff"> Features and Functions </h3>

    1. <h3 id="features"> Features </h3>

        * The tool is expected to provide an option for the user to navigate and choose any directory containing a bunch of GPX files on his system and allow him to obtain statistical data about the rides present in those GPX files. Need to handle only GPX files, other formats not needed.

        * The tool should group the rides between the same start and endpoints and generate the intergroup stats.

        * It should allow the user to choose any particular group and view the intragroup stats for the same.

        * In case of multiple paths, between the same endpoints, the user should be able to enter the coordinates of a third point, which is expected to resolve the ambiguity.


    2. <h3 id="func"> Functions </h3>

        Inter-Group Stats statistical information to be generated includes -

        * Number of rides

        Intra-Group Stats statistical information to be generated includes -
        
        * Date Vs Time
        * Date Vs Speed
        * Elevation Vs Time
        * Length of the path
        * Average Speed
        * Average Time
        * Elevated Path
        * Highest Elevation Point
        * Lowest Elevation Point 


2. <h3 id="users">Users</h3>

    * Athletes
    * Cyclist
    * Fitness Freaks

3. <h3 id="os"> Operating Environment</h3>

    1. <h3 id="hardware"> Hardware </h3>

        `GPS-Route-Analyser` requires an entry-level PC for a small number of `GPX` files.

    1. <h3 id="software"> Software</h3>

        `GPS-Route-Analyser` can run on any recent version of Linux, such as Ubuntu, Debian, Fedora Core, Redhat Enterprise, etc.

        It should solely use `Python3.6 or later` language for scripting. It may use several libraries in its aid for development.

___

<h2 id="specific"> Specific Requirements </h2>

* <h3 id="softconst">Software Constraints</h3>

    * Need to handle only `GPX` files.

    * Only use `Python` and its libraries for development. No need to use any Web-based framework like `Django` and `Flask` for the GUI. 
    
    * Libraries like `kivy` and `tkinter` can be used to create the GUI.

* <h3 id="additional"> Additional Requirements </h3>

    * **Comparision between Riders**
    <br>Since one of the main features of Strava includes the social networking features, `GPS-Route-Analyser` should allow the user to compare his/her progress with his/her friends. 

    * **Display a Map (Optional)**
    <br>If time and scope of the project permits displaying the path on a Map, rather than raw latitude and longitude data would significantly increase the user experience.

___