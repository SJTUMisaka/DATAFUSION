from math import *

def TestForOneCase(times):
    testFileName = "dataprinter\\data\\" + str(times) + ".txt"
    ansFileName = "answer\\" + str(times) + ".txt"
    testfile = open(testFileName,'r')
    ansFile = open(ansFileName,'w+')

    data = []

    for line in testfile:
        x = line.split()
        data.append(x)

    sourceNum = len(data)
    objectNum = len(data[0])

    view = [[0]*sourceNum for row in range(2)]
    fact = [[1]*objectNum for row in range(sourceNum)]

    for i in range(sourceNum):
        pos = 0
        neg = 0
        for j in range(objectNum):
            if (data[i][j] == '0.00'):
                continue
            for k in range(sourceNum):
                if (data[i][j] == data[k][j]):
                    pos = pos + 1
                elif (data[k][j] != '0.00'):
                    neg = neg + 1
        view[0][i] = (pos - neg) * 1.0 / (pos + neg)

    turn = 0

    def checkConverge():
        for i in range(sourceNum):
            if (view[0][i] - view[1][i] > 0.001 or view[1][i] - view[0][i] > 0.001):
                return False
        return True

    while (checkConverge() == False):
        for i in range(sourceNum):
            posFacts = 0
            negFacts = 0
            squareSum = 0
            for j in range(objectNum):
                if (data[i][j] == '0.00'):
                    continue
                for k in range(sourceNum):
                    if (data[k][j]==data[i][j]):
                        posFacts = posFacts + fact[k][j]
                        squareSum = squareSum + (fact[k][j])**2
                    elif (data[k][j] != '0.00'):
                        negFacts = negFacts + fact[k][j]
                        squareSum = squareSum + (fact[k][j])**2
            norm = ((posFacts + negFacts) * squareSum) ** 0.5
            view[(turn + 1) % 2][i] = 0.8 * view[turn][i] + 0.2 * (posFacts + negFacts) / norm
        turn = (turn + 1) % 2
        for j in range(objectNum):
            for i in range(sourceNum):
                if (data[i][j] == '0.00'):
                    continue 
                posViews = 0
                negViews = 0
                for k in range(sourceNum):
                    if (data[i][j]==data[k][j]):
                        posViews = posViews + (view[turn][k])**3
                    elif (data[k][j] != '0.00'):
                        negViews = negViews + (view[turn][k])**3
                fact[i][j] = (posViews - negViews) * 1.0 / (posViews + negViews)

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

print "start testing..."
for t in range(20):
    print "test case "+ str(t) + "..."
    TestForOneCase(t)        
