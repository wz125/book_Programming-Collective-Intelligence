import numpredict
import os


print '\n\n\n'


def prepare():
  numpredict.wineprice(95.0,3.0)
  numpredict.wineprice(95.0,8.0)
  numpredict.wineprice(99.0,1.0)
  data=numpredict.wineset1()
  print data



prepare()
