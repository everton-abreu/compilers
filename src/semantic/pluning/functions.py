# pylint: disable=unused-wildcard-import
from semantic.pluning.basics import *

def s_programa(node):
  lista = s_lista_declaracoes(node.children[0])

  node.children = [ lista ]
  pass

def s_lista_declaracoes(node):
  childs = node.children
  declaracao = ''

  if len(childs) == 2:
    lista_declaracoes = s_lista_declaracoes(childs[0])
    lista_declaracoes = list(lista_declaracoes) if type(lista_declaracoes) == tuple else [ lista_declaracoes ]
    declaracao = s_declaracao(childs[1])

    lista_declaracoes.append(declaracao)

    node.children = lista_declaracoes

    return node if node.parent.name != 'lista_declaracoes' else node.children

  else:
    declaracao = s_declaracao(childs[0])
    node.children = [ declaracao ]
    return node if node.parent.name != 'lista_declaracoes' else node.children

def s_declaracao(node):
  child = node.children[0]

  if child.name == 'declaracao_funcao':
    return s_declaracao_funcao(child)

  elif child.name == 'declaracao_variaveis':
    return s_declaracao_variaveis(child)

  elif child.name == 'inicializacao_variaveis':
    return s_inicializacao_variaveis(child)

  pass

def s_declaracao_funcao(node):
  childs = node.children

  if len(childs) == 2:
    tipo = s_tipo(childs[0])
    cabecalho = s_cabecalho(childs[1])

    cabecalho.children = [tipo] + list(cabecalho.children)

    return cabecalho

  elif len(childs) == 1:
    cabecalho = s_cabecalho(childs[0])

    return cabecalho

def s_declaracao_variaveis(node):
  childs = node.children

  tipo = s_tipo(childs[0])
  dois_pontos = s_dois_pontos(childs[1])
  lista = s_lista_variaveis(childs[2])
  childs[2].children = lista
  lista_variaveis = childs[2]

  # Poda do subarvore 'declaracao_de_variaveis'
  dois_pontos.children = [tipo, lista_variaveis]

  return dois_pontos

def s_inicializacao_variaveis(node):
  childs = node.children

  atribuicao = s_atribuicao(childs[0])

  return atribuicao

def s_cabecalho(node):
  childs = node.children

  nome = s_ID(childs[0])

  parametros = s_lista_parametros(childs[2])

  corpo = s_corpo(childs[4])

  nome.children = [ parametros, corpo ]

  return nome

def s_lista_parametros(node):
  childs = node.children
  parametro = ''

  if len(childs) == 3:
    lista_parametros = s_lista_parametros(childs[0])
    lista_parametros = list(lista_parametros) if type(lista_parametros) == tuple else [ lista_parametros ]
    parametro = s_parametro(childs[2])

    lista_parametros.append(parametro)

    node.children = lista_parametros

    return node if node.parent.name != 'lista_parametros' else node.children

  else:
    parametro = s_parametro(childs[0]) if childs[0].name != 'vazio' else childs[0]
    node.children = [ parametro ]
    return node if node.parent.name != 'lista_parametros' else node.children

def s_parametro(node):
  childs = node.children

  if childs[0].name == 'parametro':
    return s_parametro(childs[0])

  else:
    tipo = s_tipo(childs[0])
    dois_pontos = s_dois_pontos(childs[1])
    nome = s_ID(childs[2])

    dois_pontos.children = [ tipo, nome ]

    return dois_pontos

def s_corpo(node):
  return node

def s_atribuicao(node):
  childs = node.children

  var = s_var(childs[0])
  attr = s_ATRIBUICAO(childs[1])
  expr = s_expressao(childs[2])

  attr.children = [ var, expr ]

  return attr

def s_expressao(node):
  child = node.children[0]

  if child.name == 'expressao_logica':
    return s_expressao_logica(child)

  elif child.name == 'atribuicao':
    return s_atribuicao(child)
  pass

def s_expressao_logica(node):
  childs = node.children

  if len(childs) == 1:
    return s_expressao_simples(childs[0])

  elif len(childs) == 3:
    operador = s_operador(childs[1])

    expressao_logica = s_expressao_logica(childs[0])
    expressao_simples = s_expressao_simples(childs[2])

    operador.children = [ expressao_logica, expressao_simples ]

    return operador
  pass

def s_expressao_simples(node):
  childs = node.children

  if len(childs) == 1:
    return s_expressao_aditiva(childs[0])

  elif len(childs) == 3:
    operador = s_operador(childs[1])

    expressao_simples = s_expressao_simples(childs[0])
    expressao_aditiva = s_expressao_aditiva(childs[2])

    operador.children = [ expressao_simples, expressao_aditiva ]

    return operador
  pass

def s_expressao_aditiva(node):
  childs = node.children

  if len(childs) == 1:
    return s_expressao_multiplicativa(childs[0])

  elif len(childs) == 3:
    operador = s_operador(childs[1])

    expressao_aditiva = s_expressao_aditiva(childs[0])
    expressao_multiplicativa = s_expressao_multiplicativa(childs[2])

    operador.children = [ expressao_aditiva, expressao_multiplicativa ]

    return operador
  pass

def s_expressao_multiplicativa(node):
  childs = node.children

  if len(childs) == 1:
    return s_expressao_unaria(childs[0])

  elif len(childs) == 3:
    operador = s_operador(childs[1])

    expressao_multiplicativa = s_expressao_multiplicativa(childs[0])
    expressao_unaria = s_expressao_unaria(childs[2])

    operador.children = [ expressao_multiplicativa, expressao_unaria ]

    return operador
  pass

def s_expressao_unaria(node):
  childs = node.children

  if len(childs) == 1:
    return s_fator(childs[0])

  elif len(childs) == 3:
    operador = s_operador(childs[1])

    fator = s_fator(childs[0])

    operador.children = [ fator ]

    return operador
  pass

## pra baixo ta certo

def s_lista_variaveis(node):
  childs = node.children

  if len(childs) == 3:
    lista = s_lista_variaveis(childs[0])
    lista.append(s_var(childs[2]))
    return lista
  else:
    return [s_var(childs[0])]

def s_fator(node):
  childs = node.children

  if len(childs) == 3:
    expr = s_expressao(childs[1])

    return expr

  elif childs[0].name == 'chamada_funcao':
    return childs[0] # tem q fazer a auxiliar

  elif childs[0].name == 'var':
    return s_var(childs[0])

  elif childs[0].name == 'numero':
    return s_numero(childs[0])
  pass
