import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv, norm
from collections import namedtuple
from operator import xor
from itertools import product

def isPointNearRect(point, rect, distance):
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
    if isInside:
        return 'green'
    else:
        return 'red'
def getSize(isInside):
    if isInside:
        return 1.1
    else:
        return 0.2
def pointInRectLocalCoords(point, rect):
    # V_world = P * V_rect, where P are the rect's axes
    # V_rect = P^-1 * V_world
    p_relative = point - rect.center
    x_axis = np.array((rect.localX[0], rect.localX[1]))
    y_axis = np.array((rect.localY[0], rect.localY[1]))
    p_inverse = inv(np.column_stack([x_axis, y_axis]))
    p_relativeAfterRot = p_inverse.dot(p_relative)
    return p_relativeAfterRot

def graphPoints(rect, dist, x_range, y_range):
    for (x, y) in product(x_range, y_range):
        isInside = isPointNearRect(np.array([x,y]), rect, dist)
        plt.scatter(x, y,
            c=getColor(isInside),
            s=getSize(isInside))
    plt.axis('off')
    plt.show()

def normalize(v):
    norm=np.linalg.norm(v, ord=1)
    if norm==0:
        norm=np.finfo(v.dtype).eps
    return v/norm


if __name__=="__main__":
    Rectangle = namedtuple("Rect", "center localX localY extents")
    rect = Rectangle(np.array([0, 0]), # center
                     normalize(np.array([1, 1])),   # localX
                     normalize(np.array([-1, 1])),   # localY
                     np.array([10, 5])) # extents
    point = np.array([-10, -10])

    graphPoints(rect, 10, range(-30, 30), range(-30, 30))
