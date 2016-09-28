#!/usr/bin/python
import csv, random

def generateDict():
    d = {}
    with open('data/occupations.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if (row[0] != "Job Class" and row[0] != "Total"):
                d[row[0]] = row[1]
    return d

d = generateDict()
def getDict():
    return d

def randomOcc():
    li = []
    for x in d.keys():
        for i in range( int(float(d[x]) * 10)):
            li.append(x)
    return random.choice(li)

#print(getDict())

