# src/__syntatic__.py

import sys
from lexer.lexer import tokenize
from syntatic.syntatic import syntatic

if (len(sys.argv) < 2):
	exit(1)

file = open(sys.argv[1], 'r')
data = file.read()

logFile = open('trees/' + sys.argv[1].split('.')[0].split('/')[-1] + '.tree', 'w')

tokens = tokenize(data)

for token in tokens:
	logFile.write(str(token) + '\n')
