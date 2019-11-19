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

    ja_existe = self.tem_ID(item["nome"], item["scopo"])

    if ja_existe:
      return False

    self._data.append(item)

    return True

  def tem_ID(self, nome, scopo):
    item = filter(lambda it: (it['nome'] == nome and it['scopo'] == scopo), self._data)

    if list(item):
      return True

    return False

  def get_ID(self, nome):
    itens = list(filter(lambda it: (it['nome'] == nome), self._data))

    if itens:
      return itens[-1]

    return None

  def lista(self):
    return self._data

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

    [ print(v) for v in self._table.lista() ]

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

  def __varre(self, node, level = 'global'):
    childs = node.children

    if node.name == 'lista_declaracoes':
      lista_declaracoes = g_alinha_declaracoes(node)

      [ self.__varre(declaracao, level) for declaracao in lista_declaracoes ]

    elif node.name == 'declaracao_variaveis':
      self.__a_declaracao_variaveis(node, level)

    elif node.name == 'corpo':
      self.__a_corpo(node, level)

    elif node.name == 'vazio':
      pass

    else:
      for ind, child in enumerate(childs):

        current_level = level if (not novo_scopo(child)) else novo_scopo(child, level = level, index = ind)

        self.__varre(child, current_level)

      pass

    pass

  def __a_declaracao_variaveis(self, node, level):
    childs = node.children

    tipo = g_tipo(childs[0])
    variaveis = g_variaveis(childs[2])

    scopo = [ level ]

    scopos_ancestrais = slice_scopo(scopo)
    scopos_ancestrais = scopos_ancestrais

    for v in variaveis:
      variavel = {
        'tipo': tipo,
        'nome': v[0].name,
        'node': None,
        'scopo': level,
      }

      # if (not self.__a_indices(level, v[1])):
      #   print('indices invalidos')

      if (not self._table.tem_ID(variavel["nome"], variavel["scopo"])):
        self._table.add(variavel)

      else:
        print("ja existe", variavel)

    pass

  def __a_corpo(self, node, level):
    acoes = g_alinha_acoes(node)

    [ print(ind, acao.name) for ind, acao in enumerate(acoes) ]

    for ind, child in enumerate(acoes):

      current_level = level if (not novo_scopo(child)) else novo_scopo(child, level = level, index = ind)

      self.__varre(child, current_level)

    pass

  def __erro(self, node, code = 0):

    if code == 0:
      print('ERRROOOU:', node.name, ' não foi declarado')

    elif code == 1:
      print('WARNING:', node.name, ' não foi inicializado')

    elif code == 2:
      print('ERRROOOU:', node.name, ' tipo invalido')

    else:
      print('ERRROOOU:', node.name, ' não foi')

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
    principal = principal

    return True

  def __a_indices(self, scopo, indices = None):
    invalido = False

    if (not indices):
      return True

    for ind in indices:
      if (not self._table.tem_ID(ind.name, scopo)):
        self.__erro(ind, 0)

      else:
        invalido = True

    return invalido
