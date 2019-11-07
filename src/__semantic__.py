# src/__semantic__.py

import sys
from anytree import RenderTree
from anytree.exporter import UniqueDotExporter
from lexer import tokenize
from syntatic import parse
from semantic import semantic

if (len(sys.argv) < 2):
  print("verifique os argumetos")
  exit(1)

file = open(sys.argv[1], 'r')
data = file.read()

tree = parse(data)
treeFile = 'logs/symbols/base-tree-' + sys.argv[1].split('.')[0].split('/')[-1]

UniqueDotExporter(tree).to_picture(treeFile + '.png')

newTree = semantic(tree)

UniqueDotExporter(newTree).to_picture(treeFile + '-plunned.png')
