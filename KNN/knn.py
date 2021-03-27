import csv

def csvvalue(path):
    f = open(path,'r')
    data = csv.reader(f)
    keys = next(data)
    n = len(keys)
    csvData = []
    for row in data:
        d = {}
        for i in range(0,n):
            key = keys[i]
            if(key=="P1" or key == "P2"):
                d[key] = int(row[i])
            else:
                d[key] = row[i]
        csvData.append(d)
    return csvData

def calculateEuclideanDistance(inp,tup):
    square_sum = 0.0
    for key in inp:
        x1 = inp[key]
        x2 = tup[key]
        square_sum += pow((x1-x2),2)
    return pow(square_sum,0.5)

def kNearestNeighbour(k,inp,data):
    distance = {}
    for tup in data:
        eDist = calculateEuclideanDistance(inp,tup)
        distance[tup["SNo"]] = eDist
    print(distance)
    
    sortedDistance = distance.keys()
    sortedDistance = sorted(sortedDistance,key = lambda x:distance[x])
    sortedDistance = sortedDistance[0:k]
    
    print(k,"nearest:",sortedDistance)
    
    valueDict = {}
    
    for tup in data:
        if tup["SNo"] in sortedDistance:
            valueDict[tup["SNo"]] = tup["Class"]
            
    return valueDict

def most_frequent(li):
    countDict = {}
    for item in li:
        if item not in countDict:
            countDict[item] = 1
        else:
            countDict[item] += 1
    maxV = 0
    maxK = "NA"
    for key in countDict:
        if(countDict[key] > maxV):
            maxV = countDict[key]
            maxK = key
    return maxK

data = csvvalue("iqbal.csv")

print(data)

inp = {}
inp["P1"] = int(input("Enter P1: "))
inp["P2"] = int(input("Enter P2: "))

vD = kNearestNeighbour(3,inp,data)
print(vD)

value = most_frequent(vD.values())
print("Class: "+value)