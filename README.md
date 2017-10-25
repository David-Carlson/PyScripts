# PyScripts

This is a collection of small scripts I've created to make my life easier, do graphic visualization, or anything my heart desires!

### 1. 3D Scatter Plot
This project aims to take input images and plot them as a 3D Scatter plot.

#### Usage
```
python PlotImage.py *.jpg --points 20000 --save --pprint
```
PlotImage.py [-h] [-p POINTS] [-pp] [-s] IMG_PATHS [IMG_PATHS ...]

Creates a 3D scatter plot of the colors present in an image

positional arguments:
  IMG_PATHS             Image filepaths to plot

optional arguments:
  -h, --help            show this help message and exit
  -p, --points POINTS   Max number of pixels to plot
  -pp, --pprint         Pretty prints the scatter plots without extra information
  -s, --save            Saves each plotted image as pprint-originalfilename

### 2.  Processing Reddit links
This script takes a list of links and regular text as input, 
