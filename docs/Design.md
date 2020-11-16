## Introduction
    
`GPS route Analyser` is a Graphical User Interface Driven Tool/Application that can be used to obtain statistical data about the routes given by the user in form of `.gpx` file format. It helps us in obtaining the relation between elevation-speed vs Date and Time vs Date and many such statistics.

This document describes the implementation details of the GPS route Analyser Tool.

The project is completely based on the python programming language.

## Introduction

1. ### Design Overview
    `GPS route Analyser` is a solely `Python` based Graphical User Interface (GUI) driven GPS routes Analysing Tool. It uses the Tkinter library to render the GUI. It also uses pandas and matplotlib to manipulate the data and plot histograms respectively. It uses gpxpy to parse and manipulate the files with `.gpx` format and datetime for manipulating data of the following types - dates, times and time series.   

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
    <br>
    [5] [Gpxpy Documentation](https://pypi.org/project/gpxpy/)
    <br>
    [6] [Datetime Documentation](https://docs.python.org/3/library/datetime.html)

***

## Detailed Design

1. ### Architecture

   ![Ankit Drive](https://github.com/ankitbaluni123/NLP-Deployment-Heroku/blob/master/Untitled%20Diagram%20(2).png)
    1. ### Components

    * **Input Module (Loading the data)**  : First we load our data, the `.gpx` files, into a pandas dataframe, which makes the data readable and presentable and will help in data manipulations. Information of a third point in a path will be required in the later stages of analysing routes. 

    * **Processing Module** : We grouped the data according to different paths and then analysed it between the different groups. For further analysis we required an additional third point in a path. We displayed our analysis by plotting different types of graphs and histograms so as to visualize variation and to show relationships between different statistics like elevation-speed vs Date and Time vs Date. 

    * **Output Module** : The results show the acquired useful and usable information we got after analysing the `.gpx` files.

2. ### Algorithms and Data Structures

    The project uses the following data structures:
 
    1. **Array** : We used arrays so as to contain all the required dates, distances, time etc. from the `.gpx` file.

        Below are some advantages of the array:
        * In an array, accessing an element is very easy by using the index number in O(1) time.
        * The search process can be applied to an array easily O(n) time.
        * For any reason a user wishes to store multiple values of similar type then the Array can be used and utilized efficiently.

        **Alternatives / different tradeoff** : We can use linked lists or vectors in place of arrays which are more useful from memory allocation point of view.

    2. **Map** : We used maps for grouping, that is to store the routes with same starting and ending point and also information regarding the third point.
    
        * map is a fairly well-rounded dictionary-type container that provides several advantages over std:list (linked lists) and std:vector (arrays).
    
        * Lookup Time : A map lets you maintain reasonable lookup performance (O(log(n))), but only takes up 2 spots to store the memory. A map also lets you lookup on any type that defines a < operator or specifies to the map through a template argument how to compare keys. So you can have a reasonable lookup on maps of strings -> another value. 

        **Alternatives / different tradeoffs** : 
        * multimap is like map but allows the keys to be not unique
        * unordered_map is a map that does not store items in order, but can provide better lookup performance if a good hash function is provided.

      3. **Pandas DataFrame** :Two-dimensional, size-mutable, potentially heterogeneous tabular data.

         * Data structure also contains labeled axes (rows and columns). Arithmetic operations align on both row and column labels. Can be 
          thought of as a dict-like container for Series objects. The primary pandas data structure.


3. ### Technologies and Dependencies

    The project solely uses `Python` language for scripting.

    It uses several libraries in its aid for development. Some of them include:

    * tkinter: A standard GUI library for the Python programming language, which permits to create of the GUI application. We have used this library to design our tool and also to obtain its various controls, such as buttons, labels, and text boxes.

    * statistics: A Python library for calculating mathematical statistics of numeric(Real-valued) data, such as mean, standard deviation, variance, mode, etc.

    * matplotlib: A plotting library for the Python programming language. We have used this library to plot the histograms for visualising relationships between various statistics like Elevation-Time, Speed-Time, etc.

    * NumPy: A Python library that provides efficient operations, especially with arrays. We have used this library to store the list of distances, speeds, elevations, etc.
    
    * gpxpy: A Python library for parsing and manipulating files which are of .gpx format. 

    * datetime: A Python library that provides classes for manipulating dates and times. These classes provide a number of functions to work with dates, times, time intervals, etc.

    * pandas: A Python library that provides fast, flexible data structures designed to make working with time series data, tabular/multi-dimensional data etc, a lot easy and intuitive.
 

___
