# [3D Scatter Art](https://github.com/David-Carlson/PyScripts/tree/master/3DScatterPlot) -- [Blog Post](https://david-carlson.github.io/blog/3D-Scatter-plots)
This project aims to take input images and plot them as a 3D Scatter plot.


#### Usage
```
python PlotImage.py *.jpg --points 20000 --save --pprint
```
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
```
