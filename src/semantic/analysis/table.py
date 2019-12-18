
class CustomTable:
  def __init__(self):
    self._data = []

  def add(self, dicionario = None, tipo = None, nome = None, node = None, scopo = None, e_funcao = None, args = None):
    item = {
      'tipo': tipo,
      'nome': nome,
      'node': node,
      'scopo': scopo,
      'funcao': e_funcao,
      'argumentos': args
    } if not dicionario else dicionario

    ja_existe = self.tem_ID(item["nome"], item["scopo"])

    if ja_existe:
      return False

    self._data.append(item)

    return True

  def tem_ID(self, nome, scopo):
    item = filter(lambda it: (it['nome'] == nome and it['scopo'] in scopo), self._data)

    if list(item):
      return True

    return False

  def get_item(self, nome, scopo):
    item = filter(lambda it: (it['nome'] == nome and it['scopo'] in scopo), self._data)

    return list(item)[-1]

  def get_ID(self, nome):
    itens = list(filter(lambda it: (it['nome'] == nome), self._data))

    if itens:
      return itens[-1]

    return None

  def get_funcao(self, nome):
    item = list(filter(lambda it: (it['nome'] == nome and it['e'] == 'funcao'), self._data))

    if item:
      return item[0]

    return None

  def get_funcoes(self):
    items = list(filter(lambda it: it['e'] == 'funcao', self._data))

    return items

  def lista(self):
    return self._data

  def __repr__(self):
    return str(list(self._data))

  pass
