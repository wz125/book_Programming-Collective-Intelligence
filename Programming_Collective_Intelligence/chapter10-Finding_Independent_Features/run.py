#!/usr/bin/python
#coding:utf-8
from pylab import *
import pickle
import os

print '\n\n\n'
'''
	https://packages.debian.org/stable/python/python-pysqlite2
'''

data=dict();
def convertingMatrix():
  print '##  Converting to a Matrix'
  import newsfeatures
  allw,artw,artt= newsfeatures.getarticlewords( )
  wordmatrix,wordvec= newsfeatures.makematrix(allw,artw)
  f_allw = open ( 'allw.txt', 'w' )  
  f_artw = open ( 'artw.txt', 'w' )  
  f_artt = open ( 'artt.txt', 'w' )  
  pickle.dump ( allw, f_allw )  
  pickle.dump ( artw, f_artw )  
  pickle.dump ( artt, f_artt )  
  f_allw.close()  
  f_artw.close()  
  f_artt.close()  
  print wordvec[0:10]
  print artt[1]
  print wordmatrix[1][0:10]
def readpickle():
  import newsfeatures
  f_allw = open ( 'allw.txt')  
  f_artw = open ( 'artw.txt')  
  f_artt = open ( 'artt.txt')  
  allw=pickle.load (  f_allw )  
  artw=pickle.load (  f_artw )  
  artt=pickle.load (  f_artt )  
  f_allw.close()  
  f_artw.close()  
  f_artt.close()  
  wordmatrix,wordvec= newsfeatures.makematrix(allw,artw)
  return allw,artw,artt,wordmatrix,wordvec
  print wordvec[0:10]
  print artt[20].encode("utf-8")
  print wordmatrix[1][0:10]

def bayesianClassification():
  print '## Bayesian Classification'
  allw,artw,artt,wordmatrix,wordvec=readpickle()
  def wordmatrixfeatures(x):
    return [wordvec[w] for w in range(len(x)) if x[w]>0]
  wordmatrixfeatures(wordmatrix[0])
  #sys.path.append("../chapter6-filtering")
  import docclass
  classifier=docclass.naivebayes(wordmatrixfeatures)
  classifier.setdb('newstest.db')
  print artt[0].encode("utf-8")
  # Train this as an 'iraq' story
  classifier.train(wordmatrix[0],'iraq')
  print artt[1].encode("utf-8")
  # Train this as an 'india' story
  classifier.train(wordmatrix[1],'india')
  print artt[2].encode("utf-8")
  # How is this story classified?
  print classifier.classify(wordmatrix[1])

def clustering():
  print '## Clustering'
  import clusters
  allw,artw,artt,wordmatrix,wordvec=readpickle()
  clust=clusters.hcluster(wordmatrix)
  clusters.drawdendrogram(clust,artt,jpeg='cluster.jpg')
def nonNegativeMatrixFactorization():
  print '## Non-Negative Matrix Factorization'


#convertingMatrix()
#readpickle()
bayesianClassification()
clustering()
nonNegativeMatrixFactorization()
