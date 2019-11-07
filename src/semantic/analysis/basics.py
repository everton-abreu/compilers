# pylint: disable=unused-wildcard-import
from semantic.pluning.basics import *

def g_alinha_declaracoes(node):
  childs = node.children

  if len(childs) == 2:
    declaracao = g_declaracao(childs[1])
    declaracoes = g_alinha_declaracoes(childs[0]) + [ declaracao ]

    return declaracoes

  elif len(childs) == 1:
    declaracao = g_declaracao(childs[0])
    return [ declaracao ]

  pass

def g_declaracao(node):
  return node.children[0]

def g_funcoes(node):
  declaracoes = g_alinha_declaracoes(node)

  funcoes = g_declaracao_funcoes(declaracoes)

  return funcoes

def g_declaracao_funcoes(nodes = []):
  funcoes = filter(lambda node: node.name == 'declaracao_funcao', nodes)

  return list(funcoes)

def g_funcao(node):
  childs = node.children

  tipo = ''
  nome = ''

  if len(childs) == 2:
    cabecalho = childs[1]

    tipo = s_tipo(childs[0])
    nome = s_ID(cabecalho.children[0])

    return { "tipo": tipo.name, "nome": nome.name, "node": node }

  if len(childs) == 1:
    cabecalho = childs[0]

    tipo = None
    nome = s_ID(cabecalho.children[0])

    return { "tipo": tipo, "nome": nome.name, "node": node }

  pass

def g_principal(node):
  childs = node.children

  funcoes = g_funcoes(childs[0])

  funcoes_spec = [ g_funcao(funcao) for funcao in funcoes ]

  match = list(filter(lambda el: el['nome'] == 'principal', funcoes_spec))

  principal = dict(match[0]) if len(match) else None

  return principal

def novo_scopo(node, level = None, index = 0):
  childs = node.children
  nome = node.name

  if nome == 'declaracao_funcao':
    funcao = s_ID(childs[-1].children[0])

    return True if (not level) else (funcao.name)
  elif nome == 'se':
    return True if (not level) else (level + ' se ' + str(index))
  elif nome == 'repita':
    return True if (not level) else (level + ' repita ' + str(index))

  return False

def g_tipo(node):
  tipo = s_tipo(node)

  return tipo.name

def g_variaveis(node):
  childs = node.children

  if len(childs) == 3:
    variavel = g_variavel(childs[2])
    variaveis = g_variaveis(childs[0]) + [ variavel ]

    return variaveis

  elif len(childs) == 1:
    variavel = g_variavel(childs[0])
    return [ variavel ]

def g_variavel(node):
  return node