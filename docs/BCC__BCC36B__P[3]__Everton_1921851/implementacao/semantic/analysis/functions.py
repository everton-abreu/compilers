# pylint: disable=unused-wildcard-import
from anytree import search
from semantic.analysis.basics import *
from semantic.analysis.table import CustomTable

class Semantic:
  def __init__(self, root):
    self.__root = root
    self.__table = CustomTable()
    self.success = True
    self.__scopo = "global"

    pass

  def tests(self):

    lista_declaracoes = self.__root.children[0]

    # print('******************** Iniciando testes ********************')

    self.__check_lista_declaracoes(lista_declaracoes)
    # print('*************** lista declaracoes = False ****************')

    self.__check_variaveis_nao_utilizadas()

    self.__check_retornos()

    if not self.__check_declaracao_principal(lista_declaracoes):
      print('Erro: Função principal não declarada')

    # print('******************* Finalizando testes *******************')
    # print('******************* Tabela de simbolos *******************')

    # [ print(item) for item in self.__table.lista() ]

    return True

  def __check_lista_declaracoes(self, node):
    declaracoes = get_lista_declaracoes(node)

    results = [ self.__check_declaracao(declaracao) for declaracao in declaracoes ]

    return True if False not in results else False

  def __check_declaracao(self, node):
    name = node.name

    if name == 'declaracao_variaveis':
      return self.__check_declaracao_variaveis(node)

    elif name == 'inicializacao_variaveis':
      return self.__check_declaracao_inicializacao(node)

    else:
      return self.__check_declaracao_funcao(node)

    pass

  def __check_declaracao_variaveis(self, node):
    childs = node.children

    node_tipo = get_tipo(childs[0])

    tipo = node_tipo.name

    variaveis = get_lista_variaveis(childs[2])

    for v in variaveis:
      variavel = {
        'tipo': tipo,
        'nome': get_tipo(v).name,# A funcao pega o primeiro no filho do primeiro filho
        'node': None,
        'scopo': self.__scopo,
        'e': 'variavel',
        'inicializada': False,
        'usada': False,
        'warning': False,
        'dimensao': 0
      }

      if len(v.children) > 1:
        dimensao = self.__check_indice(v.children[1])

        variavel['dimensao'] = dimensao[0]
        
        if False in dimensao[1]:
          print('Erro: índice de array \'%s\' não inteiro' % (variavel['nome']))

      if (not self.__table.tem_ID_no_scopo(variavel["nome"], variavel["scopo"])):
        self.__table.add(variavel)

      else:
        var = self.__table.get_item(variavel['nome'], variavel['scopo'])
        if not var["warning"]:
          var['warning'] = True
          print("Aviso: Variável '%s' já declarada anteriormente" % variavel["nome"])

    return True

  def __check_indice(self, node):
    childs = node.children
    indices = []

    if len(childs) > 3:
      indices = self.__check_indice(childs[0])
      indice = self.__check_tipo_indice(childs[2])

      indices.append(indice[1] if (indice[0] == 'inteiro') else False)

    elif len(childs) == 3:
      indice = self.__check_tipo_indice(childs[1])

      indices.append(indice[1] if (indice[0] == 'inteiro') else False)

    if node.parent.name == 'indice':
      return indices
    else:
      return len(indices), indices

  def __check_tipo_indice(self, node):
    indice = get_indice(node, self.__table)
    return indice

  def __check_declaracao_inicializacao(self, node):

    return True

  def __check_declaracao_funcao(self, node):
    childs = node.children
    scopo_antigo = self.__scopo
    tipo = None

    if len(childs) > 1:
      tipo = get_tipo(childs[0]).name
      nome = get_tipo(childs[1]).name
      self.__scopo = scopo_antigo + '.' + nome

      self.__check_corpo(childs[1].children[4])

      funcao = {
          'tipo': tipo,
          'nome': nome,
          'node': node,
          'scopo': self.__scopo,
          'e': 'funcao',
          'usada': False,
          'parametros': []
      }

      if (not self.__table.get_funcao(nome)):
          self.__table.add(funcao)

      else:
        print("ja existe a função '%s'" % (nome))

    else:
      nome = get_tipo(childs[0]).name
      self.__scopo = scopo_antigo + '.' + nome

      funcao = {
          'tipo': tipo,
          'nome': nome,
          'node': node,
          'scopo': self.__scopo,
          'e': 'funcao',
          'usada': False,
          'parametros': []
      }

      if (not self.__table.get_funcao(nome)):
          self.__table.add(funcao)

      else:
        print("ja existe a função '%s'" % (nome))

    self.__scopo = scopo_antigo
    pass

  def __check_chamada_funcao(self, node):
    childs = node.children
    id = get_tipo(node).name

    funcao = self.__table.get_funcao(id)

    if not funcao:
      print("Erro: Chamada a função '%s' que não foi declarada" % (id))
      self.success = False

    pass

  def __check_corpo(self, node):
    acoes = get_corpo(node)

    for acao in acoes:
      self.__check_acao(acao)
    pass

  def __check_acao(self, node):
    nome = node.name

    if nome == 'expressao':
      self.__check_expressao(node.children[0])
    
    elif nome == 'declaracao_variaveis':
      self.__check_declaracao_variaveis(node)

  def __check_expressao(self, node):
    childs = node.children
    nome = node.name

    if ("expressao" in nome and len(childs) == 1):
      return self.__check_expressao(childs[0])
    if nome == 'atribuicao':
      self.__check_atribuicao(node)

    if nome == 'fator':
      if childs[0].name =='chamada_funcao':
        self.__check_chamada_funcao(childs[0])
        pass

  def __check_atribuicao(self, node):
    childs = node.children

    var = None
    if len(childs[0].children) > 1:
      var = (get_tipo(childs[0]).name, self.__check_indice(childs[0].children[1]))
    
    else:
      var = (get_tipo(childs[0]).name,  (0, 0))

    if self.__table.tem_ID(var[0], self.__scopo):
      symbol = self.__table.get_item(var[0], self.__scopo)
      symbol['inicializada'] = True

      nodes = search.findall(childs[2],
        filter_ = lambda n: (n.name == 'chamada_funcao'
          or (n.name == 'numero'
            and not 'chamada_funcao' in [ancestor.name for ancestor in n.ancestors ])
          or n.name == 'var'))

      vars = list(filter(lambda n: n.name == "var" , nodes))
      funcs = list(filter(lambda n: n.name == "chamada_funcao" , nodes))
      numeros = list(filter(lambda n: n.name == "numero" , nodes))

      for v in vars:
        v_name = get_tipo(v).name
        if not self.__table.tem_ID(v_name, self.__scopo):
          print("Erro: Variável '%s' não declarada" % (v_name))
        else:
          var = self.__table.get_ID(v_name)
          var["usada"] = True

          if symbol['tipo'] != var['tipo']:
            print("Aviso: Atribuição de tipos distintos '%s' %s e '%s' %s" % (symbol["nome"], symbol["tipo"], var['nome'], var['tipo']))

      for f in funcs:
        symbol['usada'] = True
        f_nome = get_tipo(f).name
        if not self.__table.get_funcao(f_nome):
          print("Erro: Chamada a função '%s' que não foi declarada" % (f_nome))
        else:
          func = self.__table.get_funcao(f_nome)

          if symbol['tipo'] != func['tipo']:
            print("Aviso: Atribuição de tipos distintos '%s' %s e '%s' %s" % (symbol["nome"], symbol["tipo"], func['nome'], "retorna " + func['tipo']))

      for n in numeros:
        symbol['usada'] = True

        n_tipo = get_tipo(n.parent).name
      
        if symbol['tipo'] != n_tipo:
          print("Aviso: Coerção implícita do valor de '%s'" % (symbol["nome"]))

    pass

  def __check_declaracao_principal(self, node):
    declaracoes = get_lista_declaracoes(node)

    results = [ self.__check_principal(declaracao) for declaracao in declaracoes ]

    return True if True in results else False

  def __check_principal(self, node):
    name = node.name
    childs = node.children

    if (name != 'declaracao_funcao'):
      return False
    if get_tipo(childs[-1]).name != 'principal':# A funcao pega o primeiro no filho do primeiro filho
      return False
    returns = list(search.findall(node, filter_ = lambda n: (n.name == 'retorna' and n.parent.name == 'acao')))

    if len(returns) < 1:
      print("Erro: Função principal deveria retornar inteiro, mas retorna vazio")
    return True

  def __check_variaveis_nao_utilizadas(self):
    variaveis = self.__table.lista()

    nao_inicializadas = list(filter(lambda x: (x['e'] == 'variavel' and (x['inicializada'] == False or x['usada'] == False)), variaveis))

    for v in nao_inicializadas:
      if not v['warning']:
        if v['usada'] == False:
          print('Aviso: variavel \'%s\' do scopo \'%s\' declarada e nao utilizada' % (v['nome'], v['scopo']))

        elif v['inicializada'] == False:
          print('Aviso: variavel \'%s\' do scopo \'%s\' declarada e nao inicializada' % (v['nome'], v['scopo']))

    pass

  def __check_retornos(self):
    funcoes = self.__table.get_funcoes()

    for funcao in funcoes:
      pass
    return True
  pass
