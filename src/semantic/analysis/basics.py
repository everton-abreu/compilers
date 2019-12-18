# pylint: disable=unused-wildcard-import

def get_lista_declaracoes(node):
  childs = node.children

  if len(childs) > 1:
    left = get_lista_declaracoes(childs[0])
    right = childs[1].children[0]

    left.append(right)
    return left

  else:
    child = childs[0].children[0]

    return [ child ]

  pass

def get_tipo(node):
  child = node.children[0]

  return child.children[0]

def get_lista_variaveis(node):
  childs = node.children

  if len(childs) > 1:
    left = get_lista_variaveis(childs[0])
    right = childs[2]

    left.append(right)
    return left

  else:
    child = childs[0]

    return [ child ]

  pass

def get_indice(node, table):
  childs = node.children

  if 'expressao' in node.name:
    if len(childs) > 1:
      return ('expressao', False)

    return get_indice(node.children[0], table)

  elif 'atribuicao' in node.name:
    return ('expressao', False)

  elif 'fator' in node.name:
    if len(childs) > 1:
      return ('expressao', False)

    elif 'chamada_funcao' == childs[0].name:
      func = get_tipo(childs[0]).name

      exists = table.get_funcao(func)

      if not exists:
        print('Erro: Chamada a função \'%s\' que não foi declarada.' % (func))
        return ('funcao')
      elif exists['tipo'] == 'inteiro':
        exists['usada'] = True
        return ('inteiro', -1)

    elif 'var' == childs[0].name:
      var = get_tipo(childs[0]).name
      exists = table.get_ID(var)

      if not exists:
        print('Aviso: Variável \'%s\' não declarada.' % (var))
      
      elif exists['tipo'] == 'inteiro':
        return 
      else:
        exists['usada'] = True
      return ('inteiro', -2)

    elif 'numero' == childs[0].name:
      return (get_tipo(node).name, get_tipo(childs[0]).name) # (tipo, valor)
  return node

def get_corpo(node):
  childs = node.children

  if len(childs) > 1:
    left = get_corpo(childs[0])
    right = childs[1].children[0]

    left.append(right)
    return left

  else:
    return [ ]

  pass