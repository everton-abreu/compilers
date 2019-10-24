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

semantic()
