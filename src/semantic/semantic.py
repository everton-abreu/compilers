# src/semantic/semantic.py
from anytree.exporter import UniqueDotExporter
from semantic.pluning import s_programa
# pylint: disable=unused-wildcard-import
from semantic.analysis import Semantic

def semantic(tree):
  sem = Semantic(tree)

  if not sem.tests():
    print('Erros semanticos encontrados')

    exit(0)

  else:
    s_programa(tree)

    return tree

  pass
