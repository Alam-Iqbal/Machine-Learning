n = [1,2,3,4,5,11,12,13,14,25]

k = int(input("Enter k: "))

m = []

for i in range(0,k):
    cent = int(input("Enter m"+str(i+1)+": "))
    m.append(cent)

def calEucDis(n,m):
    square_diff = pow((n-m),2)
    return pow(square_diff,0.5)

def partition(n,k,m):
    output = {}
    for item in n:
        nm = calEucDis(item,m[0])
        kClass = 1
        l = len(m)
        for j in range(1,l):
            nm_temp = calEucDis(item,m[j])
            if(nm_temp<nm):
                nm = nm_temp
                kClass = j+1
        
        if kClass not in output:
            output[kClass] = [item]
        else:
            l = output[kClass]
            l.append(item)
            output[kClass] = l
    return output
    
def checkOutput(o1,o2):
    flag = True
    for key in o1:
        if(o1[key] != o2[key]):
            flag = False
            break
    return flag
        
def kMeansClustering(n,k,m):
    outputTable = {}
    firstOutput = partition(n,k,m)
    print(firstOutput)
    outputTable[1] = firstOutput
    flag = False
    i = 1
    while(flag == False):
        lastOutput = outputTable[i]
        m = []
        print("")
        for key in lastOutput:
            l = lastOutput[key]
            m.append(sum(l)/len(l))
        for i in range(0,len(m)):
            print("m" + str(i+1) + ": " + str(m[i]))
        output = partition(n,k,m)
        print(output)
        i += 1
        outputTable[i] = output
        flag = checkOutput(lastOutput,output)
    return outputTable[i]
        
output = kMeansClustering(n,k,m)

print("\nOutput:", output)