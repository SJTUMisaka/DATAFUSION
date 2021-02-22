from math import *

sum = 0

def TestForOneCase(times):
    testFileName = "dataprinter\\data\\" + str(times) + ".txt"
    ansFileName = "answer\\" + str(times) + ".txt"
    testfile = open(testFileName,'r')
    ansFile = open(ansFileName,'w+')

    data = []

    for line in testfile:
        x = line.split()
        data.append(x)
    print data
    sourceNum = len(data)
    objectNum = len(data[0])

    view = [[0]*sourceNum for row in range(2)]
    fact = [[1]*objectNum for row in range(sourceNum)]

    def checkConverge():
        for i in range(sourceNum):
            if (view[0][i] - view[1][i] > 0.01 or view[1][i] - view[0][i] > 0.01):
                return False
        return True

    turn = 0

    while (True):
        maxFact = -1
        minFact = 2
        for j in range(objectNum):
            for i in range(sourceNum):
                if (data[i][j] == '0.00'):
                    continue
                posViews = 0
                negViews = 0
                nbViews = 0
                for k in range(sourceNum):
                    if (data[k][j] == data[i][j]):
                        posViews = posViews + 1 - view[turn%2][k]
                        nbViews = nbViews + 1
                    elif (data[k][j] != '0.00'):
                        negViews = negViews + view[turn%2][k]
                        nbViews = nbViews + 1
                fact[i][j] = (posViews + negViews) * 1.0 / nbViews
                if (fact[i][j] > maxFact):
                    maxFact = fact[i][j]
                if (fact[i][j] < minFact):
                    minFact = fact[i][j]
        for j in range(objectNum):
            for i in range(sourceNum):
                if (data[i][j] == '0.00'):
                    continue
                value1 = (fact[i][j] - minFact) * 1.0 / (maxFact - minFact)
                value2 = fact[i][j]     #round(...)?
                factor = 0.99 - 0.01 * turn
                if (factor < 0):
                    factor = 0
                fact[i][j] = factor * value1 + (1 - factor) * value2
        turn = turn + 1
        for i in range(sourceNum):
            posFacts = 0
            negFacts = 0
            nbFacts = 0
            for j in range(objectNum):
                if (data[i][j] == '0.00'):
                    continue
                for k in range(sourceNum):
                    if (data[k][j] == data[i][j]):
                        posFacts = posFacts + 1 - fact[k][j]
                        nbFacts = nbFacts + 1
                    elif (data[k][j] != '0.00'):
                        negFacts = negFacts + fact[k][j]
                        nbFacts = nbFacts + 1
            view[turn%2][i] = (posFacts + negFacts) * 1.0 / nbFacts
        #print view[turn%2] 
        if (checkConverge() == True):
            break
    trueNum = 0   
    for j in range(objectNum):
        max = -1000000
        ans = 0
        for i in range(sourceNum):
            if (fact[i][j] > max and data[i][j] != '0.00'):
                max = fact[i][j]
                ans = data[i][j]
        ansFile.write(ans+' ')
        if (ans == "1"):
            trueNum = trueNum + 1
    ansFile.write("\n" + str(trueNum))
    print trueNum
    return trueNum

print "start testing..."
for t in range(1):
    print "test case "+ str(t) + "..."
    sum = sum + TestForOneCase(t)

print sum / 1.0                



            
