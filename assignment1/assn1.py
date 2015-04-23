import sys
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

def merge_sort(k):
    if len(k) == 1
        return k
    mid = len(k)/2
    left = k[:mid]
    right = k[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(l, r)
    i,j,k = 0,0,0
    while l[i] < len(l) and r[j] < len(r):
        if l[i] < r[j]
            seq[k] = l[i]
            i++
        else
            seq[k] = r[j]
            j++
        k++

pointArr = parse()
print('done parsing\n')
print('there are %s points to compare' % (len(pointArr)))
shortestDistance = merge_sort(pointArr)
print(shortestDistance)