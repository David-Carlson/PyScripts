import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv, norm
from collections import namedtuple
from operator import xor
from itertools import product

def isPointNearRect(point, rect, distance):
    """ Returns true when point is distance units away from rect """
    p_rect = pointInRectLocalCoords(point, rect)
    p_absolute = abs(p_rect)

    # Point relative to upper right corner of rect
    p_corner = p_absolute - rect.extents
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
        return 1.1
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
                center : 2d Vec for position
                localX : 2d Vec showing dir of X axis
                localY : 2d Vec showing dir of Y x_axis
                extents: 2d Vec showing length and width
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


if __name__=="__main__":
    Rectangle = namedtuple("Rect", "center localX localY extents")
    rect = Rectangle(np.array([0, 0]), # center
                     normalize(np.array([1, 0])),   # localX
                     normalize(np.array([0, 1])),   # localY
                     np.array([0, 0])) # extents
    point = np.array([-10, -10])

    graphPoints(rect, 20, range(-30, 30), range(-30, 30))
