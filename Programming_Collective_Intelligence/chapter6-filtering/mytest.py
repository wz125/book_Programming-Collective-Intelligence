from sqlite3 import dbapi2 as sqlite
import re
import math

def getwords(doc):
  splitter=re.compile('\\W*')
  # Split the words by non-alpha characters
  print splitter.split(str(doc))
  words=[s.lower() for s in splitter.split(str(doc)) if len(s)>2 and len(s)<20]
  
  # Return the unique set of words only
  return dict([(w,1) for w in words])



print getwords('aaa aaa..>>bbb!#@%bbbbbb@ccc ccc cccc')
