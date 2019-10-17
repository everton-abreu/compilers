# src/__syntatic__.py

import sys
from anytree import RenderTree
from anytree.exporter import UniqueDotExporter
from lexer import tokenize
from syntatic import parse

if (len(sys.argv) < 2):
	exit(1)

file = open(sys.argv[1], 'r')
data = file.read()

tree = 'trees/' + sys.argv[1].split('.')[0].split('/')[-1]

logFile = open(tree + '.tree', 'w')

p = parse(data)

# print(RenderTree(p))

# graphviz needs to be installed for the next line!
UniqueDotExporter(p).to_picture(tree + '.png')