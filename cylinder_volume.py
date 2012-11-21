#!/usr/bin/env python
'''
A simple script to find the volume of a cylinder from two args: height and radius.
'''

import math

'''
v = hπr2
To find the volume of a cylinder, multiply its height by its radius squared
find_volume will return an int or float value of the number of cubic centimetres and the
float or integer in litres. You can call the function like so:

print(find_volume(32, 18.25))

5 cubic centimetres is 0.005 litres
'''


def find_volume(height, radius):
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
