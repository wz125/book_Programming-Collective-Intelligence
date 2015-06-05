import os
import sys
import urllib2
import searchengine
import nn

reload(sys)
sys.setdefaultencoding( "utf-8")

#crawler html
def crawlertest():
  c=urllib2.urlopen('http://www.linuxidc.com/Linux/2012-09/70576.htm')
  contents=c.read( )
  print contents
def crawlerhtml():
  pagelist=['http://www.linuxidc.com/Linux/2012-09/70576.htm']
  crawler=searchengine.crawler('searchindex.db')
  #1 crawler.createindextables();
  #2 crawler.crawl(pagelist)
  #3 print [row for row in crawler.con.execute('select rowid from wordlocation where wordid=1')]
  #4 e.getmatchrows('sqlite3 python')
  #4 print [row for row in crawler.con.execute('select w0.urlid,w0.location,w1.location from wordlocation w0,wordlocation w1 where w0.wordid=23 and w0.urlid=w1.urlid and w1.wordid=16')]


def calculatepagerank():
  reload(searchengine)
  crawler=searchengine.crawler('searchindex.db')
  crawler.calculatepagerank( )
  cur=crawler.con.execute('select * from pagerank order by score desc')
  for i in range(3): print cur.next( )

def contentranking():
  reload(searchengine)
  #mynet=nn.searchnet('nn.db')
  #mynet.maketables()
  e=searchengine.searcher('searchindex.db')
  e.query('sqlite3 python')
'''
select w0.urlid,w0.location,w1.location from wordlocation w0,wordlocation w1 where w0.wordid=23 and w0.urlid=w1.urlid and w1.wordid=16
3.689655        http://www.linuxidc.com/Linux/2012-09/70576.htm
2.758592        http://www.linuxidc.com/Linux/2013-01/77324.htm
'''
#Word Frequency
def wordFrequency():
  reload(searchengine)
  e=searchengine.searcher('searchindex.db')
  e.query('sqlite3 python')

#Document Location
def documentLocation():
  reload(searchengine)
  e=searchengine.searcher('searchindex.db')
  e.query('sqlite3 python')

#Pge Rank Algorithm
def pageRank():
  reload(searchengine)
  crawler=searchengine.crawler('searchindex.db')
  e=searchengine.searcher('searchindex.db')
  #crawler.calculatepagerank( )
  cur=crawler.con.execute('select * from pagerank order by score desc')
  for i in range(3): 
   d=cur.next()
   print d,e.geturlname(d[0])

#Using the Link Text

#Learning from Clicks
def onclick():
  mynet=nn.searchnet('nn.db')
  wWorld,wRiver,wBank =101,102,103
  uWorldBank,uRiver,uEarth =201,202,203
  mynet.generatehiddennode([wWorld,wBank],[uWorldBank,uRiver,uEarth])
  for c in mynet.con.execute('select * from wordhidden'): print c
  for c in mynet.con.execute('select * from hiddenurl'): print c
  print mynet.getresult([wWorld,wBank],[uWorldBank,uRiver,uEarth])

def backpropagation():
  mynet=nn.searchnet('nn.db')
  wWorld,wRiver,wBank =101,102,103
  uWorldBank,uRiver,uEarth =201,202,203
  mynet.trainquery([wWorld,wBank],[uWorldBank,uRiver,uEarth],uWorldBank)
  print mynet.getresult([wWorld,wBank],[uWorldBank,uRiver,uEarth])

#Training Test
def trainingTest():
  mynet=nn.searchnet('nn.db')
  wWorld,wRiver,wBank =101,102,103
  uWorldBank,uRiver,uEarth =201,202,203
  allurls=[uWorldBank,uRiver,uEarth]
  for i in range(30):
    mynet.trainquery([wWorld,wBank],allurls,uWorldBank)
    mynet.trainquery([wRiver,wBank],allurls,uRiver)
    mynet.trainquery([wWorld],allurls,uEarth)
  print mynet.getresult([wWorld,wBank],allurls)
  print mynet.getresult([wRiver,wBank],allurls)
  print mynet.getresult([wBank],allurls)
  '''
  [0.8705623942300413, 0.010855480106425806, 0.012084979924815518]
  [-0.02021296014458584, 0.8852859851373397, 0.003354660406591399]
  [0.8749506589416379, 0.005900400330499424, -0.859269156107212]
  '''
##################################################################
#crawlerhtml()
#calculatepagerank()
#contentranking()
#wordFrequency()
#documentLocation()
#pageRank();
#onclick()
#backpropagation()
trainingTest()



