#!/usr/bin/python
#coding:utf-8
import numpredict
import os

print '\n\n\n'

data=dict();
def prepare():
  print '## prepare '
  global data
  numpredict.wineprice(95.0,3.0)
  numpredict.wineprice(95.0,8.0)
  numpredict.wineprice(99.0,1.0)
  data=numpredict.wineset1()
  print '{input:(rating,age),result:price}'
  print data[0]
  print data[1]

def defineSimilar():
  print '## Defining Similarity 定义相似度'
  global data
  reload(numpredict)
  print data[0]['input']
  print data[1]['input']
  print numpredict.euclidean(data[0]['input'],data[1]['input'])

def codeForKNearest():
  ''' 计算输入点与训练集距离最近的k=5各点，然后将这k个price取平均值作为预测价格
  '''
  print '## Code for k-Nearest Neighbors 计算KNN'
  global data
  reload(numpredict)
  print numpredict.knnestimate(data,(95.0,3.0))
  print numpredict.knnestimate(data,(99.0,3.0))
  print numpredict.knnestimate(data,(99.0,5.0))
  print numpredict.wineprice(99.0,5.0) # Get the actual price
  print numpredict.knnestimate(data,(99.0,5.0),k=1) # Try with fewer neighbors
def weightedNeighbors():
  ''' 依据距离的远近对价格结果进行加权
  '''
  print '## Weighted Neighbors 加权'
  reload(numpredict)
  print numpredict.subtractweight(0.1)
  print numpredict.inverseweight(0.1)
  print numpredict.gaussian(0.1)
  print numpredict.gaussian(1.0)
  print numpredict.subtractweight(1)
  print numpredict.inverseweight(1)
  print numpredict.gaussian(3.0)
def weightedkNN():
  print '## Weighted kNN'
  reload(numpredict)
  print numpredict.weightedknn(data,(99.0,5.0))

def knn3(d,v): return numpredict.knnestimate(d,v,k=3)
def knn1(d,v): return numpredict.knnestimate(d,v,k=1)
def knninverse(d,v):return numpredict.weightedknn(d,v,weightf=numpredict.inverseweight)
def crossValidation():
  ''' 将数据分成 训练集和验证集 '''
  print '## Cross-Validation 交叉验证'
  reload(numpredict)
  print numpredict.crossvalidate(numpredict.knnestimate,data)
  print numpredict.crossvalidate(knn3,data)
  print numpredict.crossvalidate(knn1,data)
  print numpredict.crossvalidate(numpredict.weightedknn,data)
  print numpredict.crossvalidate(knninverse,data)

def heterogeneousVariables():
  print '## Heterogeneous Variables 不同类型的变量'
  reload(numpredict)
  data=numpredict.wineset2()
  print numpredict.crossvalidate(knn3,data)
  print numpredict.crossvalidate(numpredict.weightedknn,data)

def addingtotheDataset():
  global data
  ''' 增加特征 并不一定能提高预测效果,因特征间是不平等的'''
  print '## Adding to the Dataset 增加特征'
  reload(numpredict)
  data=numpredict.wineset2( )
  print numpredict.crossvalidate(knn3,data)
  print numpredict.crossvalidate(numpredict.weightedknn,data)

def scalingDimensions():
  ''' 数据归一化 ''' 
  print '## Scaling Dimensions 按比例缩放'
  reload(numpredict)
  data=numpredict.wineset2( )
  sdata=numpredict.rescale(data,[10,10,0.5,0.5])
  print numpredict.crossvalidate(knn3,sdata)
  print numpredict.crossvalidate(numpredict.weightedknn,sdata)
def optimizingtheScale():
  print '## Optimizing the Scale 特征缩放比例结果优化'
  import optimization
  reload(numpredict)
  data=numpredict.wineset2( )
  costf=numpredict.createcostfunction(numpredict.knnestimate,data)
  print optimization.annealingoptimize(numpredict.weightdomain,costf,step=2)
  #print optimization.geneticoptimize(numpredict.weightdomain,costf,popsize=5,lrate=1,maxv=4,iters=20)
def unevenDistributions():
  ''' 对于某些关键特征，数据中并未体现，需要有种方式进行观测,比如部分数据是通过折扣店购买的！'''
  print '## Uneven Distributions 不对称性'
  reload(numpredict)
  data=numpredict.wineset3()
  print numpredict.wineprice(99.0,20.0)
  print numpredict.weightedknn(data,[99.0,20.0])
  print numpredict.crossvalidate(numpredict.weightedknn,data)
def probabilityDensity():
  print '## Estimating the Probability Density 估计概率密度'
  reload(numpredict)
  print '40 80   ',numpredict.probguess(data,[99,20],40,80)
  print '80 120  ',numpredict.probguess(data,[99,20],80,120)
  print '120 1000',numpredict.probguess(data,[99,20],120,1000)
  print '30 120  ',numpredict.probguess(data,[99,20],30,120)
def theProbabilities():
  global data
  print '## plot example'
  from pylab import *
  a=array([1,2,3,4])
  b=array([4,2,3,1])
  plot(a,b)
  show( )
  t1=arange(0.0,10.0,0.1)
  plot(t1,sin(t1))
  show( )

def theProbabilities1():
  print '## Graphing the Probabilities 概率密度'
  reload(numpredict)
  data1=numpredict.wineset3()
  numpredict.cumulativegraph(data1,(1,1),120)
  reload(numpredict)
  numpredict.probabilitygraph(data1,(1,1),6)

####################################################
prepare()
defineSimilar()
codeForKNearest()
weightedNeighbors()
weightedkNN()
#crossValidation()
#heterogeneousVariables()
#addingtotheDataset()
#scalingDimensions()
#optimizingtheScale()
#unevenDistributions()
probabilityDensity()
#theProbabilities()
theProbabilities1()
