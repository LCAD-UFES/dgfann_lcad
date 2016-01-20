#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv, exit

if len(argv) <> 3:
    print 'Use: %s inputFilename outputFilename' % argv[0]
    exit(1)

inputFilename  = argv[1]
outputFilename = argv[2]

print "Openning '%s'" % inputFilename
contents = open(inputFilename).readlines()

#Resultado: -0.005109 Original: -0.003518 Erro: 0.001591 S: -0.157991 CC: -0.002198
title = map(lambda x: x.replace(':','').replace('\n',''), contents[0].split()[0::2])
title = ','.join(title)
if title[-1] <> '\n': title += '\n'

patterns = map(lambda x: x.split()[1::2], contents)
patterns = map(lambda x: (','.join(x))+'\n', patterns)

try:
    if argv[2][-4:] <> '.csv':
        outputFilename += '.csv'
except:
    outputFilename += '.csv'

print "Saving '%s'" % outputFilename
out = open(outputFilename,'w')
out.write(title)
out.writelines(patterns)
out.close()
