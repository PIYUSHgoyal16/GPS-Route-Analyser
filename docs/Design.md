## Introduction
    
`GPS route Analyser` is a Graphical User Interface Driven Tool/Application that can be used to obtain statistical data about the routes given to the user in form of .gpx file format. It helps us in obtaining the relation between elevation-speed vs Date and Time vs Date.

This document describes the implementation details of the GPS route Analyser Tool.

The project is completely based on the python programming language.

## Introduction

1. ### Design Overview
    `GPS route Analyser` is a solely `Python` based Graphical User Interface (GUI) driven GPS routes Analysing Tool. It uses the Tkinter library to render the GUI. It also uses pandas and matplotlib to manipulate the data and plot histograms respectively. It uses gpxpy to parse and manipulate the files with `.gpx` format and datetime for manipulating dates, times, and time series.   

2. ### Intended Audience
    This document is intended for the software developers and designers. Dr. Padmanabhan Rajan, the client for the software may also read the document.

3. ### References
    [1] [Tkinter Official Documentation](https://docs.python.org/3/library/tkinter.html)
    <br>
    [2] [Guide to GUI Programming](https://realpython.com/python-gui-tkinter/)
    <br>
    [3] [Matplotlib Documentation](https://matplotlib.org/3.3.2/contents.html)
    <br>
    [4] [Pandas Documentation](https://pandas.pydata.org/)

***