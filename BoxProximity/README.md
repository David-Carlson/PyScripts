# [Box proximity](https://david-carlson.github.io/blog/box-proximity)
I wrote this to solve a challenge. In essence, decide whether a point is within a distance of a rectangle, which might be rotated. View the link above for further description of the math.

### Usage
```
python BoxProximity.py --rect "(0,0),(10,10),(1,0),(0,1)" --distance 5
```
```
usage: BoxProximity.py [-h] [-r RECT] [-d DISTANCE] [--plotranges PLOTRANGES]

Plots points near a rectangle

optional arguments:
  -h, --help            show this help message and exit
  -r, --rect  Comma separated list of the rect's position,
                        dimensions, x-axis, y-axis
  -d, --distance         Acceptable distance to rectangle
  --plotranges PLOTRANGES
                        Plots all points in the x and y Range,
                        (xmin,xmax),(ymin,ymax)
```
