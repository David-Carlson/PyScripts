import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv, norm
from collections import namedtuple
from operator import xor
from itertools import product
import argparse
import re

def isPointNearRect(point, rect, distance):
    """ Returns true when point is distance units away from rect """
    p_rect = pointInRectLocalCoords(point, rect)
    p_absolute = abs(p_rect)

    # Point relative to upper right corner of rect
    p_corner = p_absolute - rect.dimensions
    if np.all(p_corner <= 0):
        return True
    if np.all(p_corner > 0):
        return norm(p_corner) <= distance
    else:
        return np.any((0 < p_corner) & (p_corner < distance))
def getColor(isInside):
    """ Returns color of points depending on if they're close to rect """
    if isInside:
        return 'green'
    else:
        return 'red'
def getSize(isInside):
    """ Returns size of points depending on if they're close to rect """
    if isInside:
        return 1.5
    else:
        return 0.2
def pointInRectLocalCoords(point, rect):
    """ Returns the coordinates of point relative to rect.
        Effectively reverses the rotation and translation of the rect """
    # V_world = P * V_rect, where P are the rect's axes
    # V_rect = P^-1 * V_world
    p_relative = point - rect.center
    x_axis = np.array((rect.localX[0], rect.localX[1]))
    y_axis = np.array((rect.localY[0], rect.localY[1]))
    p_inverse = inv(np.column_stack([x_axis, y_axis]))
    p_relativeAfterRot = p_inverse.dot(p_relative)
    return p_relativeAfterRot

def graphPoints(rect, dist, x_range, y_range):
    """ Graphs points within dist of rect as green, otherwise red.
            Rect: namedtuple representing rectangle
                center    : 2d Vec for position
                localX    : 2d Vec showing dir of X axis
                localY    : 2d Vec showing dir of Y x_axis
                dimensions: 2d Vec showing length and width
            Dist: Acceptable distance to rect
            x_range: A range showing which x points to graph
            y_range: A range showing which y points to graph
    """
    for (x, y) in product(x_range, y_range):
        isInside = isPointNearRect(np.array([x,y]), rect, dist)
        plt.scatter(x, y,
            c=getColor(isInside),
            s=getSize(isInside))
    plt.axis('off')
    plt.show()

def normalize(v):
    """ Creates a new normalized vector given a vector """
    norm=np.linalg.norm(v, ord=1)
    if norm==0:
        norm=np.finfo(v.dtype).eps
    return v/norm

def turnStringToNumList(argcount, numString):
    """ Creates a list of numbers from CSV (can include parentheses for grouping)
        Only returns if list has length of argcount
        i.e (5,2),(10,10),(1,0),(0,1) """
    try:
        # print(numString)
        withoutparens = re.sub('[()]','',  numString)
        # print(withoutparens)
        nums = [float(x) for x in withoutparens.split(',')]
        if len(nums) != argcount:
            raise argparse.ArgumentTypeError('Wrong number of arguments')
        return nums
    except ValueError:
        raise argparse.ArgumentTypeError('Values have to be numeric')

if __name__=="__main__":
    """ Plots all points within Distance to a rectangle
    e.g python BoxProximity.py --rect "(5,2),(10,10),(1,0),(0,1)" --distance 5
    Would plot the rect centered at (5,2), dimensions (10,10) and unchanged x/y axes
    """
    parser = argparse.ArgumentParser(description='Plots points near a rectangle')
    parser.add_argument('-r', '--rect',
        help="Comma separated list of the rect's position, dimensions, x-axis, y-axis",
        type=lambda x: turnStringToNumList(8, x),
        default=[0,0,10,5,1,0,0,1])
    parser.add_argument('-d', '--distance', help='Acceptable distance to rectangle',
        type=float, default=0.0)
    parser.add_argument('--plotranges',
        help='Plots all points in the x and y Range, (xmin,xmax),(ymin,ymax)',
        type=lambda x: turnStringToNumList(4, x),
        default=[-15,15,-15,15])
    args = parser.parse_args()
    r = args.rect
    Rectangle = namedtuple("Rect", "center dimensions localX localY")
    rect = Rectangle(
         np.array(r[0:2]),             # center
         np.array(r[2:4]),             # dimensions
         normalize(np.array(r[4:6])),  # localX
         normalize(np.array(r[6:8])))  # localY

    pr = [int(x) for x in args.plotranges]
    graphPoints(rect, args.distance, range(pr[0], pr[1]), range(pr[2], pr[3]))
