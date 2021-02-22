import numpy

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

    count = [[0]*len(data[0]) for row in range(len(data))]

    for i in range(len(data)):
        for j in range(len(data[i])):
            for k in range(len(data)):
                if(data[i][j]==data[k][j]):
                    count[k][j] = count[k][j] + 1
                
    trueNum = 0
    for j in range(len(data[0])):
        max = 0
        ans = 0
        for i in range(len(data)):
            if (count[i][j] > max and data[i][j] != '0.00'):
                max = count[i][j]
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
