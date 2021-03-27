support = 0.5
def firstpass(tr):
    adict = {}
    for t in tr:
        for item in t:
            if item in adict:
                adict[item] += 1
            else:
                adict[item] = 1
    return adict 
def pruning(Cand, support, totallines):
    adict={}
    for key in Cand:
        if ((float)(Cand[key]/totallines)) >= support:
            adict[key] = Cand[key]  
    return adict 
def gencand(keys):
    adict={}
    for i in keys:
        for j in keys:
            if i != j and (j,i) not in adict:
                adict[tuple([min(i,j),max(i,j)])] = 0
    return adict 
def frequency(Cand, tr):
    for key in Cand:
        for t in tr:
            if key[0] in t and key[1] in t:
                Cand[key] += 1
    return Cand 
f = open("iqbal.txt","r")
tr = []
totallines=0 
for line in f:
    split_line = line.split()
    tr.append(split_line)
    totallines = totallines + 1 
print(totallines) 
C1 = firstpass(tr)
print(C1)
L1 = pruning(C1,support,totallines)
print(L1)
C2 = gencand(L1.keys())
C2 = frequency(C2,tr)
print(C2)
L2 = pruning(C2,support,totallines)
print(L2)
