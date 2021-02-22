from math import *

sum = 0

def TestForOneCase(times):
    testFileName = "dataprinter\\data\\" + str(times) + ".txt"
    ansFileName = "answer\\" + str(times) + ".txt"
    testfile = open(testFileName,'r')
    ansFile = open(ansFileName,'w+')

    data = []
    e = 2.71828
    adjust = 0.3
    d = 0.5

    for line in testfile:
        x = line.split()
        data.append(x)

    sourceNum = len(data)
    objectNum = len(data[0])

    confidence = [[0]*objectNum for row in range(sourceNum)]
    confidenceScore = [[0]*objectNum for row in range(sourceNum)]
    adjustedConfidencescore = [[0]*objectNum for row in range(sourceNum)]
    ifrepeat = [[0]*objectNum for row in range(sourceNum)]
    trustWorthiness = [[0]*sourceNum for row in range(2)]

    def checkConverge():
        for i in range(sourceNum):
            if (trustWorthiness[0][i] - trustWorthiness[1][i] > 0.1 or
                trustWorthiness[1][i] - trustWorthiness[0][i] > 0.1):
                return False
        return True

    def imp(a,b):
        answer = (0.1 * (abs(a) + abs(b)) - abs(a - b)) / (abs(a) + abs(b))
        return answer

    for i in range(sourceNum):
        trustWorthiness[0][i] = 0.5

    turn = 0

    while (checkConverge()==False):
        for j in range(objectNum):
            for i in range(sourceNum):
                nowValue = data[i][j]
                temp = 0.0
                for k in range(sourceNum):
                    if (data[k][j] == nowValue):
                        temp = temp - log(1 - trustWorthiness[turn][k])
                        #print trustWorthiness[turn][k]
                        ifrepeat[k][j] = 1
                #print confidence[i][j]
                confidenceScore[i][j] = temp
            for i in range(sourceNum):
                nowValue = data[i][j]
                temp = 0
                for k in range(sourceNum):
                    if (data[k][j]!=nowValue and data[k][j]!='0.00' and ifrepeat[k][j] == 0):
                        temp = temp + confidenceScore[k][j] * imp(float(nowValue),float(data[k][j]))
                adjustedConfidencescore[i][j] = confidenceScore[i][j] + adjust * temp;
        turn = (turn + 1) % 2
        #print 'haha'
        for i in range(sourceNum):
            Sum = 0
            nonzero = 0
            for j in range(objectNum):
                if (data[i][j]!= '0.00'):
                    confidence[i][j] = 1 / (1 + e**(-d*adjustedConfidencescore[i][j]))
                    Sum = Sum + confidence[i][j]
                    nonzero = nonzero + 1
            trustWorthiness[turn][i] = Sum / nonzero

    trueNum = 0                    
    for j in range(objectNum):
        max = 0
        ans = 0
        for i in range(sourceNum):
            if (confidence[i][j] > max and data[i][j] != '0.00'):
                max = confidence[i][j]
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
    sum =sum + TestForOneCase(t)
print sum / 20.0
