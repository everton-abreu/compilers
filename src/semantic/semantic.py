# src/semantic/semantic.py
from anytree.exporter import UniqueDotExporter
from semantic.pluning import s_programa
# pylint: disable=unused-wildcard-import
from semantic.analysis import *

def semantic(tree):

  if not a_tem_principal(tree):
    print('Erro: Função \'pricipal\' não foi declarada.')
  
  elif not a_principal_retorna_inteiro(tree):
    print('Erro: Tipo de retorno da função \'principal\' não foi especificado como inteiro.')

  elif not a_principal_retorna(tree):
    print('Erro: Função \'principal\' deveria retornar inteiro, mas retorna vazio.')


  else:
    s_programa(tree)
    UniqueDotExporter(tree).to_picture('test2.png')

  pass
