import os
import re
import sys
import time

graphRE=re.compile("(\\d+)\\s(\\d+)")
edgeRE=re.compile("(\\d+)\\s(\\d+)\\s(\\d+)")

INFINITE = 100000

def BellmanFord(G):
    pathPairs=[]
    d = []
    #print(G[0])         #list of vertices
    #print(G[1])         #list of all lists of edges
    #print(G[1][1])      #list of edges associated with vertex 1
    #print(G[1][0][2])   #weight of vertex 0's connection to vertex 2

    # Fill in your Bellman-Ford algorithm here
    # The pathPairs will contain a matrix of path lengths:
    #    0   1   2 
    # 0 x00 x01 x02
    # 1 x10 x11 x12
    # 2 x20 x21 x22
    # Where xij is the length of the shortest path between i and j
   
    for source in range(len(G[0])):            #iterate through every node
        d = [INFINITE]*(len(G[0]))              #start a fresh list of infinite edge lengths
        d[source] = 0                               #the source node has 0 distance to itself    
        for k in range(1, len(G[0])-1):
            for i in range(len(G[0])):             #iterate through all vertices
                for j in range(len(G[0])):           #iterate through 
                    if(G[1][i][j] < INFINITE):     #Check that the edge exists
                        if(d[j] > d[i] + int(G[1][i][j])):     #Check if d[v] > d[u]+d(u,v)
                            d[j] = d[i] + int(G[1][i][j])    #Relax d[v] if shorter
        pathPairs.append(d)                                 #stick the list into pathPairs
        d = []                                              #reset d list

    return pathPairs


def FloydWarshall(G):
    d = []
    #d = [[INFINITE]*len(G[0]) for i in range(len(G[0]))]


    for i in range(len(G[0])):
        row = []
        for j in range(len(G[0])):
            row.append(INFINITE)
        d.append(row)
    # Fill in your Floyd-Warshall algorithm here
    # The pathPairs will contain a matrix of path lengths:
    #    0   1   2 
    # 0 x00 x01 x02
    # 1 x10 x11 x12
    # 2 x20 x21 x22
    # Where xij is the length of the shortest path between i and j

    for i in range(len(G[0])):                   #iterate by rows
        for j in range(len(G[0])):             #iterate by columns
            if i == j:
                d[i][j] = 0
            elif int(G[1][i][j]) != INFINITE:
                d[i][j] = int(G[1][i][j])
            else:
                d[i][j] = INFINITE
    for k in range(len(G[0])):                   #iterate by rows
        for i in range(len(G[0])):             #iterate by columns
            for j in range(len(G[0])):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]
    return d

def readFile(filename):
    # File format:
    # <# vertices> <# edges>
    # <s> <t> <weight>
    # ...
    inFile=open(filename,'r')
    line1=inFile.readline()
    graphMatch=graphRE.match(line1)
    if not graphMatch:
        print(line1+" not properly formatted")
        quit(1)
    vertices=list(range(int(graphMatch.group(1))))
    edges=[]
    for i in range(len(vertices)):
        row=[]
        for j in range(len(vertices)):
            row.append(INFINITE)
        edges.append(row)
    for line in inFile.readlines():
        line = line.strip()
        edgeMatch=edgeRE.match(line)
        if edgeMatch:
            source=edgeMatch.group(1)
            sink=edgeMatch.group(2)
            if int(source) >= len(vertices) or int(sink) >= len(vertices):
                print("Attempting to insert an edge between "+str(source)+" and "+str(sink)+" in a graph with "+str(len(vertices))+" vertices")
                quit(1)
            weight=edgeMatch.group(3)
            edges[int(source)][int(sink)]=weight
    # TODO: Debugging
    #for i in G:
        #print(i)
    return (vertices,edges)

def writeFile(lengthMatrix,filename):
    filename=os.path.splitext(os.path.split(filename)[1])[0]
    outFile=open('output/'+filename+'_output.txt','w')
    for vertex in lengthMatrix:
        for length in vertex:
            outFile.write(str(length)+',')
        outFile.write('\n')


def main(filename,algorithm):
    algorithm=algorithm[1:]
    G=readFile(filename)
    # G is a tuple containing a list of the vertices, and a list of the edges
    # in the format ((source,sink),weight)
    pathLengths=[]
    if algorithm == 'b' or algorithm == 'B':
        pathLengths=BellmanFord(G)
    if algorithm == 'f' or algorithm == 'F':
        pathLengths=FloydWarshall(G)
    if algorithm == "both":
        start=time.clock()
        BellmanFord(G)
        end=time.clock()
        BFTime=end-start
        FloydWarshall(G)
        start=time.clock()
        end=time.clock()
        FWTime=end-start
        print("Bellman-Ford timing: "+str(BFTime))
        print("Floyd-Warshall timing: "+str(FWTime))
    writeFile(pathLengths,filename)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("python bellman_ford.py -<f|b> <input_file>")
        quit(1)
    main(sys.argv[2],sys.argv[1])
