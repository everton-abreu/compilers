# __main__.py

import sys
from lexer.lexer import tokenize

if (len(sys.argv) < 2):
	exit(1)
	
file = open(sys.argv[1], 'r')
data = file.read()

tokens = tokenize(data)

for token in tokens:
	print(token)
