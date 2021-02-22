# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 11:51:43 2017

@author: 10519
"""
#生成data
from numpy import *
import numpy
from string import *
import string


def printer(times):
    sou=10#source个数
    att=100#attribute个数

    hou=[10]*att#候选值个数
    tru=[1]*att#真值

    cor1=[0.1]*sou#设定source准确率
    cor2=[]#数据生成后重新统计正确率
    
    val=numpy.zeros((sou,att))
    for i in range(sou):
        t=0
        for j in range(att):
            if(numpy.random.binomial(1,cor1[i])):#让source以一定的准确率去生成值
                val[i][j]=tru[j]
                t=t+1
            else:
                val[i][j]=numpy.random.randint(2,hou[j])
                #这里应该是 如果没有选到真值，就从剩下的候选值选一个，这里默认候选值是1-hou[j],真值是1，所以剩下的候选值就是2-hou[j]
        cor2.append((t*1.0/att))

    print "truth",tru
    print "source accuracy",cor2
    print val

    dataFileName = "data\\" + str(times) + ".txt"
    truthFileName = "truth\\" + str(times) + ".txt"
    accuracyFileName = "accuracy\\" + str(times) + ".txt"
    
    numpy.savetxt(dataFileName,val,'%d')
    numpy.savetxt(truthFileName,tru,'%d')
    numpy.savetxt(accuracyFileName,cor2,'%.2f')

#有两个问题，问题一：数组输出是科学记数法，有好多零
#bhcao: savetxt函数的参数不止两个，可以去网上查一下它的文档。
#问题二：numpy.savetxt不能在同一个txt里面保存 val，tru，cor
#bhcao: 我也不会，分多个文件存吧

def main():
    for t in range(20):
        printer(t)

main()
