#!/bin/python

import feedfilter
import docclass


def train():
  cl=docclass.classifier(docclass.getwords)
  cl.setdb('test2.db')
  cl.train('the quick brown fox jumps over the lazy dog','good')
  cl.train('make quick money in the online casino','bad')
  print 'quick','good',cl.fcount('quick','good')
  print 'quick','bad',cl.fcount('quick','bad')
  print cl.fc
#Calculating Probabilities
def calculate():
  reload(docclass)
  cl=docclass.classifier(docclass.getwords)
  cl.setdb('test2.db')
  docclass.sampletrain(cl)
  print 'quick','good',cl.fprob('quick','good')
#Starting with a Reasonable Guess
def reasonableGuess():
  reload(docclass)
  cl=docclass.classifier(docclass.getwords)
  cl.setdb('test2.db')
  docclass.sampletrain(cl)
  print 'money','good',cl.weightedprob('money','good',cl.fprob)
  docclass.sampletrain(cl)
  print 'money','good',cl.weightedprob('money','good',cl.fprob)
# naive bayestrain
def naivebayestrain():
  reload(docclass)
  cl=docclass.naivebayes(docclass.getwords)
  cl.setdb('test2.db')
  docclass.sampletrain(cl)
  print cl.prob('quick rabbit','good')
  print cl.prob('quick rabbit','bad')
# Choosing a Category
def choose():
  reload(docclass)
  cl=docclass.naivebayes(docclass.getwords)
  docclass.sampletrain(cl)
  cl.classify('quick rabbit',default='unknown')
  cl.classify('quick money',default='unknown')
  cl.setthreshold('bad',3.0)
  cl.classify('quick money',default='unknown')
  for i in range(10): docclass.sampletrain(cl)
  cl.classify('quick money',default='unknown')
#Category Probabilities for Features
def probabilityFeatures():
  reload(docclass)
  cl=docclass.fisherclassifier(docclass.getwords)
  cl.setdb('test2.db')
  docclass.sampletrain(cl)
  print cl.cprob('quick','good')
  print cl.cprob('money','bad')
  print cl.weightedprob('money','bad',cl.cprob)
#Combining the Probabilities
def combinProbability():
  reload(docclass)
  cl=docclass.fisherclassifier(docclass.getwords)
  cl.setdb('test2.db')
  docclass.sampletrain(cl)
  cl.cprob('quick','good')
  print cl.fisherprob('quick rabbit','good')
  print cl.fisherprob('quick rabbit','bad')
#Classifying Items
def classify():
  reload(docclass)
  cl=docclass.fisherclassifier(docclass.getwords)
  cl.setdb('test2.db')
  docclass.sampletrain(cl)
  print cl.classify('quick rabbit')
  print cl.classify('quick money')
  cl.setminimum('bad',0.8)
  print cl.classify('quick money')
  cl.setminimum('good',0.4)
  print  cl.classify('quick money')
#Persisting the Trained Classifiers
def persist():
  reload(docclass)
  cl=docclass.fisherclassifier(docclass.getwords)
  cl.setdb('test1.db')
  docclass.sampletrain(cl)
  cl2=docclass.naivebayes(docclass.getwords)
  cl2.setdb('test1.db')
  print cl2.classify('quick money')


#train()
#calculate()
#reasonableGuess()
naivebayestrain()
#probabilityFeatures()
#combinProbability()
#classify()
#persist()




#Filtering Blog Feeds
def filterBlog():
  import feedfilter
  cl=docclass.fisherclassifier(docclass.getwords)
  cl.setdb('python_feed.db') # Only if you implemented SQLite
  feedfilter.read('python_search.xml',cl)
#probability of a category
def probabilityCat():
  cl=docclass.fisherclassifier(docclass.getwords)
  cl.setdb('python_feed.db') # Only if you implemented SQLite
  print cl.cprob('python','prog')
  print cl.cprob('python','snake')
  print cl.cprob('python','monty')
  print cl.cprob('eric','monty')
  print cl.fprob('eric','monty')
#Improving Feature Detection
def improv():
  reload(feedfilter)
  cl=docclass.fisherclassifier(feedfilter.entryfeatures)
  cl.setdb('python_feed.db') # Only if using the DB version
  feedfilter.read('python_search.xml',cl)
#Using Akismet
def akismet():
  import akismettest
  msg='Make money fast! Online Casino!'
  akismettest.isspam(msg,'spammer@spam.com','127.0.0.1')



#filterBlog()
#probabilityCat()
#improv();














