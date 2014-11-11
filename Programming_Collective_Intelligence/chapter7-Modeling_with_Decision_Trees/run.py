import treepredict
import os


print '\n\n\n'


def Training_the_Tree():
  print '>>Training the Tree'
  setdata=treepredict.divideset(treepredict.my_data,2,'yes')
  print setdata[0]
  print setdata[1]


def Choosing_the_Best_Split():
  print '>>Choosing the Best Split'
  reload(treepredict)
  print treepredict.giniimpurity(treepredict.my_data)
  print treepredict.entropy(treepredict.my_data)
  set1,set2=treepredict.divideset(treepredict.my_data,2,'yes')
  print treepredict.entropy(set1)
  print treepredict.giniimpurity(set1)

def Recursive_Tree_Building():
  print '>>Recursive Tree Building'
  reload(treepredict)
  tree=treepredict.buildtree(treepredict.my_data)
  treepredict.printtree(tree)

def Graphical_Display():
  print '>>Graphical Display'
  treepredict.drawtree(tree,jpeg='treeview.jpg')

def Classifying_New_Observations():
  reload(treepredict)
  tree=treepredict.buildtree(treepredict.my_data)
  print '>>Classifying New Observations'
  print treepredict.classify(['(direct)','USA','yes',5],tree)

def Pruning_the_Tree():
  print '>>Pruning the Tree'
  reload(treepredict)
  tree=treepredict.buildtree(treepredict.my_data)
  print '------------------'
  treepredict.prune(tree,0.1)
  treepredict.printtree(tree)
  treepredict.prune(tree,1.0)
  treepredict.printtree(tree)
  
def Dealing_with_Missing_Data():
  print '>>Dealing with Missing Data'
  reload(treepredict)
  tree=treepredict.buildtree(treepredict.my_data)
  print '------------------'
  print treepredict.mdclassify(['google',None,'yes',None],tree)
  print treepredict.mdclassify(['google','France',None,None],tree)

#Dealing with Numerical Outcomes

def Modeling_Home_Prices(): 
  print '>>Modeling Home Prices'
  import zillow
  if os.path.exists('housedata.txt'):
    f=open('housedata.txt','r')
    lines=f.readlines()
    housedata=[]
    for line in lines:
      fields=line.split('\t')
      l1=[fields[0],fields[1],fields[2],fields[3],fields[4],fields[5],fields[6]]
      housedata.append(l1)
    f.close();
  else:
    housedata=zillow.getpricelist( )
    f=open('housedata.txt','w')
    for l in housedata:
      if l is None:
        continue
      print l
      for k in l:
        f.write('%s\t' % (k))
      f.write('\n')
    f.close
  reload(treepredict)
  housetree=treepredict.buildtree(housedata,scoref=treepredict.variance)
  treepredict.drawtree(housetree,'housetree.jpg')

def Modeling_Htness():
  print '>>Modeling_Htness'
  import hotornot
  l1=hotornot.getrandomratings(500)
  print len(l1)
  pdata=hotornot.getpeopledata(l1)
  print pdata[0]
  #hottree=treepredict.buildtree(pdata,scoref=treepredict.variance)
  #treepredict.prune(hottree,0.5)
  #treepredict.drawtree(hottree,'hottree.jpg')

#Training_the_Tree()
#Choosing_the_Best_Split()
#Recursive_Tree_Building()
#Graphical_Display()
#Classifying_New_Observations()
#Pruning_the_Tree()
#Dealing_with_Missing_Data()
#Modeling_Home_Prices()
#Modeling_Htness()

