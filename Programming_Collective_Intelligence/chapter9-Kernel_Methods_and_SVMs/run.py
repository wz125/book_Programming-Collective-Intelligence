#!/usr/bin/python
#coding:utf-8
import advancedclassify
from pylab import *
import os

print '\n\n\n'

agesonly=advancedclassify.loadmatch('agesonly.csv',allnum=True)

data=dict();
def makerDataset():
  print '##  Matchmaker Dataset'
  import advancedclassify
  agesonly=advancedclassify.loadmatch('agesonly.csv',allnum=True)
  matchmaker=advancedclassify.loadmatch('matchmaker.csv')
  print ', '.join(['%s:%s' % item for item in matchmaker[0].__dict__.items()])

def dataPlot():
  print '## Difficulties with the Data'
  reload(advancedclassify)
  advancedclassify.plotagematches(agesonly)
def basicLinearClassification():
  print '## Basic Linear Classification'
  reload(advancedclassify)
  avgs=advancedclassify.lineartrain(agesonly)
  print avgs
  for (k,v) in  avgs.items(): 
    if k==0:
      p='b%s' % ('o')
    if k==1:
      p='b%s' % ('+')
    plot(v[0],v[1],p)
  show()
  print '30,30',advancedclassify.dpclassify([30,30],avgs)
  print '30,25',advancedclassify.dpclassify([30,25],avgs)
  print '25,40',advancedclassify.dpclassify([25,40],avgs)
  print '48,20',advancedclassify.dpclassify([48,20],avgs)
def CalculatingTheDistance():
  print '## alculating the Distance'
  reload(advancedclassify)
  print advancedclassify.getlocation('1 alewife center, cambridge, ma')
  print advancedclassify.milesdistance('cambridge, ma','new york,ny')

def creatingTheNewDataset():
  print '## Creating the New Dataset'
  reload(advancedclassify)
  numericalset=advancedclassify.loadnumerical( )
  print numericalset[0].data

def scalingTheData():
  print '## Scaling the Data'
  reload(advancedclassify)
  numericalset=advancedclassify.loadnumerical( )
  scaledset,scalef=advancedclassify.scaledata(numericalset)
  avgs=advancedclassify.lineartrain(scaledset)
  print 'numericalset[0].data',numericalset[0].data
  print 'numericalset[0].match', numericalset[0].match
  print advancedclassify.dpclassify(scalef(numericalset[0].data),avgs)
  print 'numericalset[11].match', numericalset[11].match
  print advancedclassify.dpclassify(scalef(numericalset[11].data),avgs)

def theKernelTrick():
  print '## The Kernel Trick'
  offset=0
  print advancedclassify.nlclassify([30,30],agesonly,offset)
  print advancedclassify.nlclassify([30,25],agesonly,offset)
  print advancedclassify.nlclassify([25,40],agesonly,offset)
  print advancedclassify.nlclassify([48,20],agesonly,offset)

def theKernelTrick1():
  print '## The Kernel Trick'
  numericalset=advancedclassify.loadnumerical( )
  scaledset,scalef=advancedclassify.scaledata(numericalset)
  ssoffset=advancedclassify.getoffset(scaledset)
  print 'offset',ssoffset
  print numericalset[0].match
  print advancedclassify.nlclassify(scalef(numericalset[0].data),scaledset,ssoffset)
  print numericalset[1].match
  print advancedclassify.nlclassify(scalef(numericalset[1].data),scaledset,ssoffset)
  print numericalset[2].match
  print advancedclassify.nlclassify(scalef(numericalset[2].data),scaledset,ssoffset)
  newrow=[28.0,-1,-1,26.0,-1,1,2,0.8] # Man doesn't want children, woman does
  print advancedclassify.nlclassify(scalef(newrow),scaledset,ssoffset)
  newrow=[28.0,-1,1,26.0,-1,1,2,0.8] # Both want children
  print advancedclassify.nlclassify(scalef(newrow),scaledset,ssoffset)

def supportVectorMachines():
  print '## Support-Vector Machines'
  from svm import *
  prob = svm_problem([1,-1],[[1,0,1],[-1,0,-1]])
  #param = svm_parameter(kernel_type = LINEAR, C = 10)
  #print m.predict([1, 1, 1])
  param = svm_parameter('-t 4 -c 4 -b 1')
  m = libsvm.svm_train(prob, param)
  x0, max_idx = gen_svm_nodearray({1:1,3:1})
  print 'x0',x0,'max_idx',max_idx
  label = libsvm.svm_predict(m, x0)
  print 'label',label
  #m.save(test.model)
  #m=svm_model(test.model)

def applyingSVMToTheMatchmakerDataset():
  print '## Applying SVM to the Matchmaker Dataset'
  from svm import *
  numericalset=advancedclassify.loadnumerical( )
  scaledset,scalef=advancedclassify.scaledata(numericalset)
  answers,inputs=[r.match for r in scaledset],[r.data for r in scaledset]
  inputs1=[]
  for i in inputs:
    data={};
    for m in range(len(i)):
      data[m+1]=i[m]
    inputs1.append(data)
  print inputs1[0]
  print 'answers[0]',answers[0],'inputs[0]',inputs[0],'all',len(answers)
  ''' answers inputs <类别号> <索引1>：<特征值1> <索引2>：<特征值2>.'''
  prob = svm_problem(answers,inputs1)   #, isKernel=True
  param = svm_parameter()
  print 'param--->',param,'<----'
  m = libsvm.svm_train(prob, param)
  newrow=[28.0,-1,-1,26.0,-1,1,2,0.8] # Man doesn't want children, woman does
  x0, max_idx = gen_svm_nodearray(scalef(newrow))
  print '*** ',libsvm.svm_predict(m,x0)
  newrow=[28.0,-1,1,26.0,-1,1,2,0.8] # Both want children
  x0, max_idx = gen_svm_nodearray(scalef(newrow))
  print '*** ',libsvm.svm_predict(m,x0)
  #guesses = cross_validation(prob, param, 4)
  #print guesses
  #print sum([abs(answers[i]-guesses[i]) for i in range(len(guesses))])

def libsvmtest():
  print '## libsvm testg '
  from svm import *
  prob = svm_problem([1,-1], [{1:1, 3:1}, {1:-1,3:-1}])
  param = svm_parameter()
  m = libsvm.svm_train(prob, param) # m is a ctype pointer to an svm_model
  # Convert a Python-format instance to svm_nodearray, a ctypes structure
  x0, max_idx = gen_svm_nodearray({1:1, 3:1})
  label = libsvm.svm_predict(m, x0)
  print label
####################################################
#makerDataset()
#dataPlot()
#basicLinearClassification()
#categoricalFeatures()
#CalculatingTheDistance()
#creatingTheNewDataset()
#scalingTheData()
#theKernelTrick()
#theKernelTrick1()
#supportVectorMachines()
applyingSVMToTheMatchmakerDataset()
libsvmtest()
