import sys
import math
import time

class Point:
    def __init__(self):
        x = 0
        y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "%s, %s" % (self.x, self.y)

def distance(x1, y1, x2, y2):
    return math.sqrt(pow(x1 - x2,2) + pow(y1 - y2,2))

def printPoint():
    print('X: ' + self.x + ' Y: ' + self.y)

def parse():
    arr = []
    # open file
    with open(str(sys.argv[1]), 'r') as file:
        temp = file.read()
        # print(temp)
        print('\nthere are %s datas' % (len(temp.split())))
        file.close()

    # convert string into a list
    temp = temp.split()
    i = 0
    # convert coordinates into points
    while i < len(temp):
        arr.append(Point(float(temp[i]), float(temp[i+1])))
        i += 2
    return arr

def brute_force(arr):
    i = 0
    j = 1
    
    dist = distance(arr[0].x, arr[0].y, arr[1].x, arr[1].y)
    while i < len(arr):
        while j < len(arr):
            temp = distance(arr[i].x, arr[i].y, arr[j].x, arr[j].y)
            #print('distance between index %s and index %s is: ' % (str(i),str(j)) + str(temp) + '\n')
            if(temp < dist):
                dist = temp
            j += 1
        i += 1
    return dist

pointArr = parse()
print('done parsing\n')
print('there are %s points to compare' % (len(pointArr)))
start = time.time()
shortestDistance = brute_force(pointArr)
print(time.time()-start)
print(shortestDistance)

#print(pointArr[0])

