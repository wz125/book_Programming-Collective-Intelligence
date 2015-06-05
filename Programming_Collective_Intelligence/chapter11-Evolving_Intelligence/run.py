#!/usr/bin/python
#coding:utf-8
import os
import gp

print '\n\n\n'
'''
'''

def buildingAndEvaluatingTrees():
  print 'Building and Evaluating Trees'
  exampletree=gp.exampletree( )
  print exampletree.evaluate([2,3])
  print exampletree.evaluate([5,3])
def displayingTheProgram():
  print 'Displaying the Program'
  reload(gp)
  exampletree=gp.exampletree( )
  exampletree.display( )
def creatingTheInitialPopulation():
  print 'Creating the Initial Population'
  random1=gp.makerandomtree(2)
  random1.evaluate([7,1])
  random1.evaluate([2,4])
  random2=gp.makerandomtree(2)
  random2.evaluate([5,3])
  random2.evaluate([5,20])
  random1.display( )
  random2.display( )
def aSimpleMathematicalTest():
  print 'A Simple Mathematical Test'
  reload(gp)
  hiddenset=gp.buildhiddenset( )
  print hiddenset
def measuringSuccess():
  print 'Measuring Success'
  reload(gp)
  random1=gp.makerandomtree(2)
  random2=gp.makerandomtree(2)
  hiddenset=gp.buildhiddenset( )
  print gp.scorefunction(random2,hiddenset)
  print gp.scorefunction(random1,hiddenset)
def mutatingPrograms():
  print 'Mutating Programs 变异'
  hiddenset=gp.buildhiddenset( )
  random2=gp.makerandomtree(2)
  random2.display()
  muttree=gp.mutate(random2,2)
  muttree.display()
  print gp.scorefunction(random2,hiddenset)
  print gp.scorefunction(muttree,hiddenset)
def crossover():
  print 'Crossover 交叉'
  random1=gp.makerandomtree(2)
  random1.display( )
  random2=gp.makerandomtree(2)
  random2.display( )
  cross=gp.crossover(random1,random2)
  cross.display( )
def buildingTheEnvironment():   
  print 'Building the Environment'
  reload(gp)
  rf=gp.getrankfunction(gp.buildhiddenset( ))
  gp.evolve(2,500,rf,mutationrate=0.2,breedingrate=0.1,pexp=0.7,pnew=0.1)
# The Importance of Diversity 多样性的重要价值
def aSimpleGame():
  print 'A Simple Game 游戏竞争'
  reload(gp)
  p1=gp.makerandomtree(5)
  p2=gp.makerandomtree(5)
  print gp.gridgame([p1,p2])
def aRoundRobinTournament(): 
  print 'A Round-Robin Tournament 循环赛'
  reload(gp)
  winner=gp.evolve(5,100,gp.tournament,maxgen=50)
def alayingAgainstRealPeople():
  print 'Playing Against Real People'
  reload(gp)
  winner=gp.evolve(5,100,gp.tournament,maxgen=50)
  gp.gridgame([winner,gp.humanplayer()])
#Further Possibilities
#More Numerical Functions
#Memory
#Different Datatypes


#buildingAndEvaluatingTrees();
#displayingTheProgram();
#creatingTheInitialPopulation();
#aSimpleMathematicalTest();
#measuringSuccess();
#mutatingPrograms(); 
#crossover()
buildingTheEnvironment()
#aSimpleGame()
#aRoundRobinTournament()
#alayingAgainstRealPeople()





