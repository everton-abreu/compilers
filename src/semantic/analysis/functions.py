# pylint: disable=unused-wildcard-import
from semantic.pluning.basics import *
from semantic.analysis.basics import *
from pprint import pprint

def a_tem_principal(node):
  principal = g_principal(node)

  return True if principal else False

def a_principal_retorna_inteiro(node):
  principal = g_principal(node)

  if len(dict.keys(principal)) != 3:
    return False

  elif principal['tipo'] != 'inteiro':
    return False

  else:
    return True

def a_principal_retorna(node):
  principal = g_principal(node)

  pprint(principal)

  return False
