
import os
import sys
import urllib2
import time
import random
import math
import optimization
import dorm

reload(sys)
sys.setdefaultencoding( "utf-8")

def personOrigin():
  s=[1,4,3,2,7,3,6,3,2,4,5,3]
  print 'name','origin','from','time','price','to','time','price'
  optimization.printschedule(s)
def costFunction():
  reload(optimization)
  s=[1,4,3,2,7,3,6,3,2,4,5,3]
  print 'cost:',optimization.schedulecost(s)
#Random Searching
def randomSearching():
  reload(optimization) 
  domain=[(0,8)]*(len(optimization.people)*2)
  s=optimization.randomoptimize(domain,optimization.schedulecost)
  print optimization.schedulecost(s)
  optimization.printschedule(s)
#Hill Climbing
def hillClimb():
  domain=[(0,8)]*(len(optimization.people)*2)
  s=optimization.hillclimb(domain,optimization.schedulecost)
  print optimization.schedulecost(s)
  print optimization.printschedule(s)
#Simulated Annealing
def simulatedAnneal():
  reload(optimization)
  domain=[(0,8)]*(len(optimization.people)*2)
  s=optimization.annealingoptimize(domain,optimization.schedulecost)
  print optimization.schedulecost(s)
  print optimization.printschedule(s)
#Genetic Algorithms
def geneticAlgorithms():
  domain=[(0,8)]*(len(optimization.people)*2)
  s=optimization.geneticoptimize(domain,optimization.schedulecost)
  print optimization.printschedule(s)


#personOrigin()
#costFunction()
#randomSearching()
#hillClimb()
#simulatedAnneal()
#geneticAlgorithms()

######################################################


#minidom Package
import xml.dom.minidom
import kayak

def minidomPackage():
  dom=xml.dom.minidom.parseString('<data><rec>Hello!</rec></data>')
  print dom
  r=dom.getElementsByTagName('rec')
  print r,r[0].firstChild,r[0].firstChild.data

#Flight Searches
def flightSearches():
  sid=kayak.getkayaksession( )
  searchid=kayak.flightsearch(sid,'BOS','LGA','9/1/2014')
  f=kayak.flightsearchresults(sid,searchid)
  print f[0:3]
def optimizeFlight():
  reload(kayak)
  f=kayak.createschedule(optimization.people[0:2],'LGA','11/17/2006','11/19/2006')
  optimization.flights=f
  domain=[(0,30)]*len(f)
  optimization.geneticoptimize(domain,optimization.schedulecost)
  print optimization.printschedule(s)



#minidomPackage()
#flightSearches()
#optimizeFlight()

#########################################################
#Student Dorm Optimization
import random
import math

def test():
  reload(dorm)
  dorm.printsolution([0,0,0,0,0,0,0,0,0,0])
#The Cost Function
def costFunction1():
  reload(dorm)
  s=optimization.randomoptimize(dorm.domain,dorm.dormcost)
  print s
  dorm.dormcost(s)
  optimization.geneticoptimize(dorm.domain,dorm.dormcost)
  dorm.printsolution(s)

#test()
#costFunction1()

#########################################################

import socialnetwork
from socialnetwork import drawnetwork
#Counting Crossed Lines
def countCross():
  sol=optimization.randomoptimize(socialnetwork.domain,socialnetwork.crosscount)
  socialnetwork.crosscount(sol)
  sol=optimization.annealingoptimize(socialnetwork.domain,socialnetwork.crosscount,step=50,cool=0.99)
  socialnetwork.crosscount(sol)
  print sol
  return sol

#Drawing the Network
def drawNet():
  reload(socialnetwork) 
  sol=countCross()
  #sol=[326, 180, 302, 370, 350, 233, 166.0, 370, 364, 63, 284, 118, 109, 309, 205.0, 42]
  drawnetwork(sol)

#countCross()
drawNet()















