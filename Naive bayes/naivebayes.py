import csv

def csvvalue(path):
    f = open(path, 'r')
    data = csv.reader(f)
    keys = next(data)
    n = len(keys)
    csvData = []
    for row in data:
        d = {}
        for i in range(0,n):
            key = keys[i]
            d[key] = row[i]
        csvData.append(d)        
    return csvData

def probability(classVar, value, data):
    countValue = 0
    for tup in data:
        if(tup[classVar] == value):
            countValue += 1
    return countValue/len(data)

def conditionalProbability(inpX,classVarY,valueY,data):
    countValueX = {}
    for key in inpX:
        countValueX[key] = 0
    nY = 0
    for tup in data:
        if(tup[classVarY] == valueY):
            nY += 1
            for key in inpX:
                if(tup[key] == inpX[key]):
                    countValueX[key] += 1
    condProb = 1.0
    for key in countValueX:
        condProb *= countValueX[key]/nY
    return condProb

def getValues(classVar,data):
    values = []
    for tup in data:
        value = tup[classVar]
        if value not in values:
            values.append(value)
    return values

def naiveBayesClassifier(inp, data):
    values = getValues("PlayGolf", data)
    valuesProbability = {}
    for value in values:
        p_y = probability("PlayGolf",value,data)
        p_y_x = conditionalProbability(inp,"PlayGolf",value,data)
        p_x_y = p_y*p_y_x
        valuesProbability[value] = p_x_y
    return valuesProbability

data = csvvalue("iqbal.csv")

print("Enter values:")
inp = {}
keys = list(data[0].keys())
keys.remove("Tid")
keys.remove("PlayGolf")
for key in keys:
    inp[key] = input("Enter "+key+": ")
vP = naiveBayesClassifier(inp,data)
print("\nProbabilities: ")
print(vP)

maxV = 0.0
maxK = "NA"
for key in vP:
    if(vP[key] > maxV):
        maxV = vP[key]
        maxK = key

print("\nPlay Golf:", maxK)