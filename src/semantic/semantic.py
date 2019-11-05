# src/semantic/semantic.py
from anytree.exporter import UniqueDotExporter
from semantic.pluning import s_programa

def semantic(tree):
  s_programa(tree)

  UniqueDotExporter(tree).to_picture('test2.png')

  pass
