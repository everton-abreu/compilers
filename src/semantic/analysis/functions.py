# pylint: disable=unused-wildcard-import
from semantic.pluning.basics import *
from semantic.analysis.basics import *
from pprint import pprint

class CustomTable:
  def __init__(self):
    self._data = []

  def add(self, dicionario = None, tipo = None, nome = None, node = None, scopo = None, e_funcao = None, args = None):
    item = {
      'tipo': tipo,
      'nome': nome,
      'node': node,
      'scopo': scopo,
      'e_funcao': e_funcao,
      'argumentos': args
    } if not dicionario else dicionario

    ja_existe = self.tem_ID(item["nome"])

    if ja_existe:
      return False

    self._data.append(item)

    return True

  def tem_ID(self, nome):
    item = filter(lambda it: it['nome'] == nome, self._data)

    if list(item):
      return True

    return False

  def __repr__(self):
    return str(list(self._data))

  pass

class Semantic:
  def __init__(self, root):
    self.__root = root
    self._table = CustomTable()

    pass

  def tests(self):
    self.__varre(self.__root)

    if not self.__a_tem_principal(self.__root):
      print('Erro: Função \'pricipal\' não foi declarada.')
      return False

    elif not self.__a_principal_retorna_inteiro(self.__root):
      print('Erro: Tipo de retorno da função \'principal\' não foi especificado como inteiro.')
      return False

    elif not self.__a_principal_retorna(self.__root):
      print('Erro: Função \'principal\' deveria retornar inteiro, mas retorna vazio.')
      return False

    return True

  def __salva_aids(self, node, level, function):
    function(node)

    pass

  def __varre(self, node, level = 'global'):
    childs = node.children

    if node.name == 'lista_declaracoes':
      lista_declaracoes = g_alinha_declaracoes(node)

      print([ declaracao.name for declaracao in lista_declaracoes ])

      [ self.__varre(declaracao, level) for declaracao in lista_declaracoes ]

    elif node.name == 'declaracao_variaveis':
      tipo = g_tipo(childs[0])
      variaveis = g_variaveis(childs[2])
      print(tipo, [ v.name for v in variaveis ])
      # self.__salva_aids(node, level, lambda n: print('oi'))

    else:
      # self.__salva_aids(node, level, lambda n: print(''))

      for ind, child in enumerate(childs):

        current_level = level if (not novo_scopo(node)) else novo_scopo(node, level = level, index = ind)

        self.__varre(child, current_level)

      pass

    pass

  def __a_tem_principal(self, node):
    principal = g_principal(node)

    return True if principal else False

  def __a_principal_retorna_inteiro(self, node):
    principal = g_principal(node)

    if not principal['tipo']:
      return False

    elif principal['tipo'] != 'inteiro':
      return False

    else:
      return True

  def __a_principal_retorna(self, node):
    principal = g_principal(node)

    self._table.add(tipo = principal['tipo'], nome = principal['nome'], node = principal['node'])

    self._table.add(dicionario = principal)

    return True
