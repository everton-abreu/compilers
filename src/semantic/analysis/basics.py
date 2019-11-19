# pylint: disable=unused-wildcard-import
from semantic.pluning.basics import *
from semantic.pluning.functions import s_indices

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

def g_alinha_acoes(node):
  childs = node.children

  if len(childs) == 2:
    acao = childs[1].children[0]
    acoes = g_alinha_acoes(childs[0]) + [ acao ]

    return acoes

  elif len(childs) == 1:
    acao = [ childs[0] ] if childs[0].name != 'vazio' else []
    return acao

  pass

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

    return True if (not level) else (level + ' ' + funcao.name)
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
  childs = node.children

  if len(childs) == 1:
    id = childs[0].children[0]
    return tuple([ id ])

  else:
    id = childs[0].children[0]
    indice = childs[1]

    return tuple([ id, indice ])

  pass

def slice_scopo(scopo):
  count = 0

  while len(scopo[-1]) or count == 0:
    scopo_parcionado = scopo[-1].split(' ')

    ancestral = scopo_parcionado

    if len(scopo_parcionado) > 1:
      try:
        if (type(int(scopo_parcionado[-1])) == int):
          ancestral = scopo_parcionado[: -2]
      except BaseException as error:
        error = error
        pass
    if count == 0:
      ancestral = ancestral if scopo[0] != ' '.join(ancestral) else ancestral[: -1]
      scopo = [ ' '.join(ancestral) ]
      count = 1

    else:
      scopo.append(' '.join(ancestral[: -1]))

  return scopo[: -1]
