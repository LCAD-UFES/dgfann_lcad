#!/usr/bin/env python
# Author: Jacson R C Silva <jacsonrcsilva@gmail.com>

from sys import argv, exit, stdout
from os  import access, R_OK, W_OK

if len(argv) <> 4:
    print "Use: %s arqDoDataset arqComTodosPadroes arqSaida" % argv[0]
    exit(1)

files = {
         'dataset'  : argv[1],
         'fulldata' : argv[2],
         'output'   : argv[3]
        }

def checkFiles(f):
    if not access(f, R_OK):
        print "ERROR: It was impossible to access %s" % f
        exit(2)

checkFiles( files['fulldata'] )
checkFiles( files['dataset']  )

# full data
fulldata   = open(files['fulldata']).readlines()[1:]
# original dataset
dataset    = open(files['dataset'] ).readlines()
header     = dataset[0]
dataset    = dataset[1:]
# sorted dataset
sortedData = {}

print 'Sorting...'
size  = len(dataset)
count = 1.0
steps = size / 100
for p in dataset:
    if count % steps == 0:
        print '\b'*10, '%d%%' % int((count/size)*100),
        stdout.flush()
    sortedData[fulldata.index(p)] = p
    count+=1
print '\b'*10,'100%\nok'

open(files['output'], 'w').write(header);
open(files['output'], 'a').writelines(sortedData.values())
