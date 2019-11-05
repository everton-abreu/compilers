from semantic.pluning.basics import *

def s_programa(node):
  s_lista_declaracoes(node.children[0])
  pass

def s_lista_declaracoes(node):
  if len(node.children) == 2:
    s_lista_declaracoes(node.children[0])
    s_declaracao(node.children[1])

  else:
    s_declaracao(node.children[0])

  pass

def s_declaracao(node):
  child = node.children[0]

  if child.name == 'declaracao_funcao':
    s_declaracao_funcao(child)

  elif child.name == 'declaracao_variaveis':
    s_declaracao_variaveis(child)

  elif child.name == 'inicializacao_variaveis':
    s_inicializacao_variaveis(child)

  pass

def s_declaracao_funcao(node):
  pass

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

  node.children = [ s_atribuicao(childs[0]) ]
  pass

def s_atribuicao(node):
  childs = node.children

  var = s_var(childs[0])
  attr = s_ATRIBUICAO(childs[1])
  expr = s_expressao(childs[2])

  attr.children = [ var, expr ]
  node.children = [ attr ]

  return node

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
