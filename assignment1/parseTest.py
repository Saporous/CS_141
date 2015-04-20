#import sys
import math

class Point:
    def __init__(self):
        x = 0
        y = 0
    def __init__(self, X, Y):
        x = X
        y = Y

def distance(a, b):
    return sqrt(pow(a.x-b.x,2)+pow(a.y-b.y,2))

def parse():
    # open file
    with open('input.txt', 'r') as file:
        # read in all data
        print(file.readline())
    file.close()

n = 0
pointArr = []
parse()
s = 'The first line is: ' #+ str(pointArr[0].x)
print(s)
