#import sys
import math

class Point:
    def __init__(self):
        x = 0
        y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "%s, %s" % (self.x, self.y)
def distance(a, b):
    return sqrt(pow(a.x-b.x,2)+pow(a.y-b.y,2))

def printPoint():
    print('X: ' + self.x + ' Y: ' + self.y)

def parse():
    # open file
    with open('input.txt', 'r') as file:
        temp = file.read()
        file.close()

    # convert string into a list
    temp = temp.split()
    i = 0
    # convert coordinates into points
    while i < len(temp):
        pointArr.append(Point(temp[i], temp[i+1]))
        i += 2

pointArr = []
parse()
print(pointArr[0])