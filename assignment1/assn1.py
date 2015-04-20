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
    file = open('input.txt', 'r')
    while True:
        tempX = file.read()
        tempY = file.read()
        if tempX == '' or tempY == '':
            break
        tempPoint = Point(tempX, tempY)
        pointArr.append(tempPoint)
        print('read stuff')
    return

n = 0
pointArr = []
parse()
s = 'The first line is: ' #+ str(pointArr[0].x)
print(s)
