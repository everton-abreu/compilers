# pylint: disable=unused-wildcard-import
from semantic.pluning.basics import *
from semantic.analysis.basics import *
from pprint import pprint

class Semantic:
  def __init__(self, root):
    self._root = root
    self._table = []

    pass

  def tests(self):
    return True
    if not self.a_tem_principal(self._root):
      print('Erro: Função \'pricipal\' não foi declarada.')
      return False
    
    elif not self.a_principal_retorna_inteiro(self._root):
      print('Erro: Tipo de retorno da função \'principal\' não foi especificado como inteiro.')
      return False

    elif not self.a_principal_retorna(self._root):
      print('Erro: Função \'principal\' deveria retornar inteiro, mas retorna vazio.')
      return False


  def a_tem_principal(self, node):
    principal = g_principal(node)

    return True if principal else False

  def a_principal_retorna_inteiro(self, node):
    principal = g_principal(node)

    if len(dict.keys(principal)) != 3:
      return False

    elif principal['tipo'] != 'inteiro':
      return False

    else:
      return True

  def a_principal_retorna(self, node):
    principal = g_principal(node)

    pprint(principal)

    return False
