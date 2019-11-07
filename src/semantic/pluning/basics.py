

def s_operador(node):
  operador = s_OPERADOR(node.children[0])

  return operador

def s_OPERADOR(node):
  operador = node.children[0]

  return operador

def s_ATRIBUICAO(node):
  attr = node.children[0]

  return attr

def s_tipo(node):
  tipo = s_TIPO(node.children[0])

  return tipo

def s_TIPO(node):
  tipo = node.children[0]

  return tipo

def s_dois_pontos(node):
  dois_pontos = node.children[0]

  return dois_pontos

def s_ID(node):
  return node.children[0]

def s_numero(node):
  numero = s_NUMERO(node.children[0])

  return numero

def s_NUMERO(node):
  numero = node.children[0]

  return numero
