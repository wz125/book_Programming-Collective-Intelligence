import clusters
import os
import sys
reload(sys)
sys.setdefaultencoding( "utf-8")

# 
def parserblog():
  os.system('python generatefeedvector.py')
def countword():
  blognames,words,data=clusters.readfile('blogdata1.txt')
  clust=clusters.hcluster(data)
def printclust():
  reload(clusters)
  clusters.printclust(clust,labels=blognames)
# create image
def drawingtheDendrogram():
  blognames,words,data=clusters.readfile('blogdata1.txt')
  clust=clusters.hcluster(data)
  reload(clusters)
  clusters.drawdendrogram(clust,blognames,jpeg='blogclust.jpg')
#Column Clustering
def ColumnClustering():
  reload(clusters)
  blognames,words,data=clusters.readfile('blogdata1.txt')
  rdata=clusters.rotatematrix(data)
  wordclust=clusters.hcluster(rdata)
  clusters.drawdendrogram(wordclust,labels=words,jpeg='wordclust.jpg')

#parserblog()
#countword()
#printclust()
#drawingtheDendrogram()
#ColumnClustering()

#K-Means Clustering
def kmean():
  reload(clusters)
  rownames,words,data=clusters.readfile('blogdata.txt')
  kclust=clusters.kcluster(data,k=2)
  [rownames[r] for r in kclust[0]]
  [rownames[r] for r in kclust[1]]

# http://crummy.com/software/BeautifulSoup
import urllib2
from bs4 import BeautifulSoup
def beauty():
  c=urllib2.urlopen('http://blog.chinaunix.net/uid-24567872-id-3927355.html')
  soup=BeautifulSoup(c.read( ))
  links=soup('a')
  print links[10]
  print links[10]['href']

#beauty()


#Clusters of Preferences 
def prefer():
  reload(clusters)
  wants,people,data=clusters.readfile('zebo.txt')
  clust=clusters.hcluster(data,distance=clusters.tanamoto)
  clusters.drawdendrogram(clust,wants)
def prefer2d():
  reload(clusters)
  blognames,words,data=clusters.readfile('blogdata.txt')
  coords=clusters.scaledown(data)
  clusters.draw2d(coords,blognames,jpeg='blogs2d.jpg')

#prefer()
#prefer2d()




