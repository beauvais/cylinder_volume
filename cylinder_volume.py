#!/usr/bin/env python
'''
A simple script to find the volume of a cylinder (in cc and l) from two arguments: height(cm) and radius(cm).
'''

import math

'''
v = hπr2
To find the volume of a cylinder, multiply its height by its radius squared.
find_volume will return a value (int or float) for the number of cubic centimetres and the
number of litres.

You can call the function like so:

print(find_volume(32, 18.25))
'''


def find_volume(height, radius):  # height and radius should be numbers (int or float values) in cm
    pi = math.pi
    rsq = math.pow(radius, 2)
    cc = height * pi * rsq
    litres = cc * .001
    # print("height is " + str(height))  # printing steps for sense-checking
    # print("π is " + str(pi))
    # print("radius is " + str(radius))
    # print("radius squared is " + str(rsq))
    # print("cubic centimetres (cc) is " + str(cc))
    # print("volume in litres is " + str(litres))

    return cc
    return litres
