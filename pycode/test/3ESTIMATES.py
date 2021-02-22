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

    sourceNum = len(data) - 1
    objectNum = len(data[0])

    view = [[0]*sourceNum for row in range(2)]
    fact = [[1]*objectNum for row in range(sourceNum)]
    facthard = [[0.1]*objectNum for row in range(sourceNum)]

    def checkConverge():
        for i in range(sourceNum):
            if (view[0][i] - view[1][i] > 0.01 or view[1][i] - view[0][i] > 0.01):
                return False
        return True

    turn = 0

    while (True):
        maxFact = -100
        minFact = 100
        for j in range(2,objectNum):
            for i in range(sourceNum):
                if (data[i][j] == '0.00'):
                    continue
                posViews = 0
                negViews = 0
                nbViews = 0
                for k in range(sourceNum):
                    if (data[k][j] == data[i][j]):
                        posViews = posViews + 1 - view[turn%2][k]*facthard[k][j]
                        nbViews = nbViews + 1
                    elif (data[k][j] != '0.00'):
                        negViews = negViews + view[turn%2][k]*facthard[k][j]
                        nbViews = nbViews + 1
                fact[i][j] = (posViews + negViews) * 1.0 / nbViews
        for j in range(2,objectNum):
            for i in range(sourceNum):
                if (data[i][j] == '0.00'):
                    continue
                value1 = (fact[i][j] - minFact) * 1.0 / (maxFact - minFact)
                value2 = fact[i][j]     #round(...)?
                factor = 0.99 - 0.1 * turn
                if (factor < 0):
                    factor = 0
                fact[i][j] = factor * value1 + (1 - factor) * value2
        if (turn != 0):
            for j in range(2,objectNum):
                for i in range(sourceNum):
                    if (data[i][j] == '0.00'):
                        continue
                    posViews = 0
                    negViews = 0
                    nbViews = 0
                    for k in range(sourceNum):
                        if (view[turn%2][k] == 0):
                            continue
                        if (data[k][j] == data[i][j]):
                            posViews = posViews + (1 - fact[k][j]) * 1.0 / view[turn%2][k]
                            nbViews = nbViews + 1
                        elif (data[k][j] != '0.00'):
                            negViews = negViews + fact[k][j] * 1.0 / view[turn%2][k]
                            nbViews = nbViews + 1
                    facthard[i][j] = (posViews + negViews) * 1.0 / nbViews
        turn = turn + 1
        for i in range(sourceNum):
            posFacts = 0
            negFacts = 0
            nbFacts = 0
            for j in range(2,objectNum):
                if (data[i][j] == '0.00'):
                    continue
                for k in range(sourceNum):
                    if (facthard[k][j] == 0):
                        continue
                    if (data[k][j] == data[i][j]):
                        posFacts = posFacts + (1 - fact[k][j]) * 1.0 / facthard[k][j]
                        nbFacts = nbFacts + 1
                    elif (data[k][j] != '0.00'):
                        negFacts = negFacts + fact[k][j] * 1.0 / facthard[k][j]
                        nbFacts = nbFacts + 1
            view[turn%2][i] = (posFacts + negFacts) * 1.0 / nbFacts
        #print view[turn%2]     
        if (checkConverge() == True):
                break
    trueNum = 0 
    for j in range(2,objectNum):
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
for t in range(20):
    print "test case "+ str(t) + "..."
    sum = sum + TestForOneCase(t)
print sum / 20.0


