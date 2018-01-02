# [Box proximity](https://david-carlson.github.io/blog/box-proximity)
I wrote this to solve a challenge. In essence, decide whether a point is within a distance of a rectangle, which might be rotated. View the link above for further description of the math.

### Usage
```
python BoxProximity.py --rect "(0,0),(10,5),(1,0),(0,1)" --distance 5 --plotranges "(-15,15),(-10,10)"
```
```
usage: BoxProximity.py [-h] [-r RECT] [-d DISTANCE] [--plotranges PLOTRANGES]

Plots points within a distance to a rectangle

optional arguments:
  -h, --help            Show this help message and exit
  -r, --rect            Comma separated list of numbers describing the rectangle:
                          (X,Y),(Length,Height),(LocalX_X,LocalX_Y),(LocalY_X,LocalY_Y)
  -d, --distance        Acceptable distance to rectangle
  --plotranges          Plots a rectangle of points in the X and Y ranges:
                          (Xmin,Xmax),(Ymin,Ymax)
```
