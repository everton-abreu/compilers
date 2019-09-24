# src/syntatic/__test__.py

import sys
from syntatic import syntatic

if (len(sys.argv) < 2):
	exit(1)

file = open(sys.argv[1], 'r')
data = file.read()

logFile = open('trees/' + sys.argv[1].split('.')[0].split('/')[-1] + '.tree', 'w')

logFile.write(sys.argv[1])
