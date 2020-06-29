
import glob
from pprint import pprint as pp
import re

#### get all filenames
mdfilepaths = []
filepaths = glob.glob('**', recursive=True)
for fp in filepaths:
  if fp.__contains__('.md'):
    mdfilepaths.append(fp)


### parse each for md formatted links
for f in mdfilepaths:
  with open(f, 'r') as fobj:
    data = fobj.read()
    data = data.split("\n")
  ### check if mdlinks are in filenames
  for line in data:
    if ".md)" in line: #  re.match("\**\(*\)", line):
      internallink = line.split('(')[1][:-1].split('./')[1]
      print (internallink)
      if internallink not in mdfilepaths:
        print ('is bad \n')
        pass