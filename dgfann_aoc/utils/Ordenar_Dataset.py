#!/usr/bin/env python
# Author: Jacson R C Silva <jacsonrcsilva@gmail.com>

from sys import argv, exit, stdout
from os  import access, R_OK, W_OK

if len(argv) <> 4:
    print "Use: %s arqDoDataset arqComTodosPadroes arqSaida" % argv[0]
    exit(1)

def printF(msg, newLine=True):
    if newLine: print msg
    else:       print msg,
    stdout.flush()

def checkFiles(f):
    if not access(f, R_OK):
        print "ERROR: It was impossible to access %s" % f
        exit(2)

files = {
         'dataset'  : argv[1],
         'fulldata' : argv[2],
         'output'   : argv[3]
        }

checkFiles( files['fulldata'] )
checkFiles( files['dataset']  )

# full data
fulldata   = open(files['fulldata']).readlines()[1:]
# original dataset
dataset    = open(files['dataset'] ).readlines()
header     = dataset[0]
dataset    = dataset[1:]

printF('Sorting...', False)
dataset.sort(key=fulldata.index)
printF('ok')

printF('Saving...', False)
o = open(files['output'], 'w')
o.write( header )
o.writelines( dataset )
o.close()
printF('ok\nDone.')
