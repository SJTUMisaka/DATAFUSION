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

    sourceNum = len(data)
    objectNum = len(data[0])

    view = [[0.5]*sourceNum for row in range(2)]
    fact = [[0]*objectNum for row in range(sourceNum)]
    factNum = [0]*sourceNum

    def checkConverge():
        for i in range(sourceNum):
            if (view[0][i] - view[1][i] > 0.01 or view[1][i] - view[0][i] > 0.01):
                return False
        return True


    for i in range(sourceNum):
        factN = 0
        for j in range(objectNum):
            if (data[i][j] != '0.00'):
                factN = factN + 1
        factNum[i] = factN

    for j in range(objectNum):
        Sd = 0
        for i in range(sourceNum):
            if (data[i][j] != '0.00'):
                Sd = Sd + 1
        for i in range(sourceNum):
            if (data[i][j] == '0.00'):
                continue
            Sc = 0
            for k in range(sourceNum):
                if (data[k][j] == data[i][j]):
                    Sc = Sc + 1
            fact[i][j] = Sc * 1.0 / Sd

    turn = 0

    while (True):
        for i in range(sourceNum):
            trustWorthiness = 0
            for j in range(objectNum):
                if (data[i][j] == '0.00'):
                    continue
                temp = 0
                for k in range(sourceNum):
                    if (data[k][j] == data[i][j]):
                        temp = temp + view[turn%2][k] * 1.0 / factNum[k]
                trustWorthiness = trustWorthiness + fact[i][j] / temp
            view[(turn+1)%2][i] = trustWorthiness * view[turn%2][i] * 1.0 / factNum[i]
        #print view[(turn+1)%2]
        turn = turn + 1
        for i in range(sourceNum):
            for j in range(objectNum):
                if (data[i][j] == '0.00'):
                    continue
                temp = 0
                for k in range(sourceNum):
                    if (data[k][j] == data[i][j]):
                        temp = temp + view[turn%2][k] * 1.0 / factNum[k]
                fact[i][j] = temp ** 1.2
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
print sum / 20.0


    
    



    
