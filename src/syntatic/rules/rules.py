# src/syntatic/rules/rules.py
from anytree import Node
from ply import yacc

def p_programa(p):
	'programa : lista_declaracoes'

	programa = Node('programa', children=[p[1]])
	p[0] = programa

	pass

def p_lista_declaracoes(p):
	'''lista_declaracoes : lista_declaracoes declaracao
	| declaracao'''

	lista_declaracoes = Node('lista_declaracoes')
	p[0] = lista_declaracoes

	if len(p) == 2:
		p[0].children = [p[1]]
	elif len(p) == 3:
		p[0].children = [p[1], p[2]]

	pass

def p_declaracao(p):
	'''declaracao : declaracao_variaveis
	| inicializacao_variaveis
	| declaracao_funcao'''

	declaracao = Node('declaracao', children=[p[1]])
	p[0] = declaracao
	pass

def p_declaracao_variaveis(p):
	'declaracao_variaveis : tipo DOIS_PONTOS lista_variaveis'

	DOIS_PONTOS = Node('DOIS_PONTOS', children=[Node(p[2])])

	declaracao_variaveis = Node('declaracao_variaveis', children=[p[1], DOIS_PONTOS, p[3]])
	p[0] = declaracao_variaveis
	pass

def p_inicializacao_variaveis(p):
	'inicializacao_variaveis : atribuicao'

	inicializacao_variaveis = Node('inicializacao_variaveis', children=[p[1]])
	p[0] = inicializacao_variaveis
	pass

def p_lista_variaveis(p):
	'''lista_variaveis : lista_variaveis VIRGULA var
	| var'''

	lista_variaveis = Node('lista_variaveis')
	p[0] = lista_variaveis

	if len(p) == 4:
		VIRGULA = Node('VIRGULA', children=[Node(p[2])])
		p[0].children = [p[1], VIRGULA, p[3]]
	elif len(p) == 2:
		p[0].children = [p[1]]
	
	pass

def p_var(p):
	'''var : ID
	| ID indice'''

	var = Node('var')
	p[0] = var

	ID = Node('ID', children=[Node(p[1])])

	if len(p) == 2:
		p[0].children = [ID]
	elif len(p) == 3:
		p[0].children = [ID, p[2]]
	pass

def p_indice(p):
	'''indice : indice ABRE_COLCHETES expressao FECHA_COLCHETES
	| ABRE_COLCHETES expressao FECHA_COLCHETES'''

	indice = Node('indice')


	if len(p) == 4:
		ABRE_COLCHETES = Node('ABRE_COLCHETES', children=[Node(p[1])])
		FECHA_COLCHETES = Node('FECHA_COLCHETES', children=[Node(p[3])])

		indice.children = [ABRE_COLCHETES, p[2], FECHA_COLCHETES]
	elif len(p) == 5:
		ABRE_COLCHETES = Node('ABRE_COLCHETES', children=[Node(p[2])])
		FECHA_COLCHETES = Node('FECHA_COLCHETES', children=[Node(p[4])])

		indice.children = [p[1], ABRE_COLCHETES, p[3], FECHA_COLCHETES]

	p[0] = indice
	pass

def p_tipo(p):
	'''tipo : INTEIRO
	| FLUTUANTE'''

	NO = Node('TIPO', children=[Node(p[1])])
	tipo = Node('tipo', children=[NO])

	p[0] = tipo
	pass

def p_declaracao_funcao(p):
	'''declaracao_funcao : tipo cabecalho
	| cabecalho'''

	declaracao_funcao = Node('declaracao_funcao')

	if len(p) == 2:
		declaracao_funcao.children = [p[1]]
	elif len(p) == 3:
		declaracao_funcao.children = [p[1], p[2]]

	p[0] = declaracao_funcao
	pass

def p_cabecalho(p):
	'''cabecalho : ID ABRE_PARENTES lista_parametros FECHA_PARENTES corpo FIM'''

	ID = Node('ID', children=[Node(p[1])])

	ABRE_PARENTES = Node('ABRE_PARENTES', children=[Node(p[2])])

	FECHA_PARENTES = Node('FECHA_PARENTES', children=[Node(p[4])])

	FIM = Node('FIM', children=[Node(p[6])])

	cabecalho = Node('cabecalho', children=[ID, ABRE_PARENTES, p[3], FECHA_PARENTES, p[5], FIM])
	p[0] = cabecalho

	pass

def p_lista_parametros(p):
	'''lista_parametros : lista_parametros VIRGULA parametro
	| parametro
	| vazio'''

	lista_parametros = Node('lista_parametros')

	if len(p) == 4:
		VIRGULA = Node('VIRGULA', children=[Node(p[2])])

		lista_parametros.children = [p[1], VIRGULA, p[3]]
	elif len(p) == 2 and p[1]:
		lista_parametros.children = [p[1]]

	p[0] = lista_parametros
	pass

def p_parametro(p):
	'''parametro : tipo DOIS_PONTOS ID
	| parametro ABRE_COLCHETES FECHA_COLCHETES'''

	parametro = Node('parametro')

	p[1].parent = parametro

	if p[2] == ':':
		DOIS_PONTOS = Node('DOIS_PONTOS', children=[Node(p[2])])

		ID = Node('ID', children=[Node(p[3])])

		parametro.children = [p[1], DOIS_PONTOS, ID]
	else:
		ABRE_COLCHETES = Node('ABRE_COLCHETES', children=[Node(p[2])])

		FECHA_COLCHETES = Node('FECHA_COLCHETES', children=[Node(p[3])])

		parametro.children = [p[1], ABRE_COLCHETES, FECHA_COLCHETES]

	p[0] = parametro
	pass

def p_corpo(p):
	'''corpo : corpo acao
	| vazio'''

	corpo = Node('corpo', children=[p[1]])
	if len(p) == 3:
		corpo.children = [p[1], p[2]]
	
	p[0] = corpo
	pass

def p_acao(p):
	'''acao : expressao
	| declaracao_variaveis
	| se
	| repita
	| leia
	| escreva
	| retorna'''

	acao = Node('acao', children=[p[1]])
	p[0] = acao
	pass

def p_se(p):
	'''se : SE expressao ENTAO corpo FIM
	| SE expressao ENTAO corpo SENAO corpo FIM'''

	se = Node('se')

	SE = Node('SE', children=[Node(p[1])])

	ENTAO = Node('ENTAO', children=[Node(p[3])])

	if len(p) == 6:
		FIM = Node('FIM', children=[Node(p[5])])
		se.children = [SE, p[2], ENTAO, p[4], FIM]

	
	elif len(p) == 8:
		SENAO = Node('SENAO', children=[Node(p[5])])
		FIM = Node('FIM', children=[Node(p[7])])

		se.children = [SE, p[2], ENTAO, p[4], SENAO, p[6], FIM]

	p[0] = se
	pass

def p_repita(p):
	'''repita : REPITA corpo ATE expressao'''

	REPITA = Node('REPITA', children=[Node(p[1])])

	ATE = Node('ATE', children=[Node(p[3])])

	repita = Node('repita', children=[REPITA, p[2], ATE, p[4]])
	p[0] = repita
	pass

def p_atribuicao(p):
	'''atribuicao : var ATRIBUICAO expressao'''

	ATRIBUICAO = Node('ATRIBUICAO', children=[Node(p[2])])

	atribuicao = Node('atribuicao', children=[p[1], ATRIBUICAO, p[3]])
	p[0] = atribuicao
	pass

def p_leia(p):
	'''leia : LEIA ABRE_PARENTES var FECHA_PARENTES'''

	LEIA = Node('LEIA', children=[Node(p[1])])

	ABRE_PARENTES = Node('ABRE_PARENTES', children=[Node(p[2])])

	FECHA_PARENTES = Node('FECHA_PARENTES', children=[Node(p[4])])

	leia = Node('leia', children=[LEIA, ABRE_PARENTES, p[3], FECHA_PARENTES])
	p[0] = leia
	pass

def p_escreva(p):
	'''escreva : ESCREVA ABRE_PARENTES expressao FECHA_PARENTES'''

	ESCREVA = Node('ESCREVA', children=[Node(p[1])])

	ABRE_PARENTES = Node('ABRE_PARENTES', children=[Node(p[2])])

	FECHA_PARENTES = Node('FECHA_PARENTES', children=[Node(p[4])])

	escreva = Node('escreva', children=[ESCREVA, ABRE_PARENTES, p[3], FECHA_PARENTES])
	p[0] = escreva
	pass

def p_retorna(p):
	'''retorna : RETORNA ABRE_PARENTES expressao FECHA_PARENTES'''

	RETORNA = Node('RETORNA', children=[Node(p[1])])

	ABRE_PARENTES = Node('ABRE_PARENTES', children=[Node(p[2])])

	FECHA_PARENTES = Node('FECHA_PARENTES', children=[Node(p[4])])

	retorna = Node('retorna', children=[RETORNA, ABRE_PARENTES, p[3], FECHA_PARENTES])
	p[0] = retorna
	pass

def p_expressao(p):
	'''expressao : expressao_logica
	| atribuicao'''

	expressao = Node('expressao', children=[p[1]])
	p[0] = expressao
	pass

def p_expressao_logica(p):
	'''expressao_logica : expressao_simples
	| expressao_logica operador_logico expressao_simples'''

	expressao_logica = Node('expressao_logica')

	if len(p) == 2:
		expressao_logica.children = [p[1]]
	elif len(p) == 4:
		expressao_logica.children = [p[1], p[2], p[3]]

	p[0] = expressao_logica
	pass

def p_expressao_simples(p):
	'''expressao_simples : expressao_aditiva
	| expressao_simples operador_relacional expressao_aditiva'''

	expressao_simples = Node('expressao_simples')

	if len(p) == 2:
		expressao_simples.children = [p[1]]
	elif len(p) == 4:
		expressao_simples.children = [p[1], p[2], p[3]]

	p[0] = expressao_simples
	pass

def p_expressao_aditiva(p):
	'''expressao_aditiva : expressao_multiplicativa
	| expressao_aditiva operador_soma expressao_multiplicativa'''

	expressao_aditiva = Node('expressao_aditiva')

	if len(p) == 2:
		expressao_aditiva.children = [p[1]]
	elif len(p) == 4:
		expressao_aditiva.children = [p[1], p[2], p[3]]

	p[0] = expressao_aditiva
	pass

def p_expressao_multiplicativa(p):
	'''expressao_multiplicativa : expressao_unaria
	| expressao_multiplicativa operador_multiplicacao expressao_unaria'''

	expressao_multiplicativa = Node('expressao_multiplicativa')

	if len(p) == 2:
		expressao_multiplicativa.children = [p[1]]
	elif len(p) == 4:
		expressao_multiplicativa.children = [p[1], p[2], p[3]]

	p[0] = expressao_multiplicativa
	pass

def p_expressao_unaria(p):
	'''expressao_unaria : fator
	| operador_soma fator
	| operador_negacao fator'''

	expressao_unaria = Node('expressao_unaria')

	if len(p) == 2:
		expressao_unaria.children = [p[1]]
	elif len(p) == 3:
		expressao_unaria.children = [p[1], p[2]]

	p[0] = expressao_unaria
	pass

def p_operador_relacional(p):
	'''operador_relacional : MENOR
	| MAIOR
	| IGUAL
	| DIFERENTE
	| MENOR_IGUAL
	| MAIOR_IGUAL'''

	OPERADOR = Node('RELACIONAL', children=[Node(p[1])])

	operador_relacional = Node('operador_relacional', children=[OPERADOR])
	p[0] = operador_relacional
	pass

def p_operador_soma(p):
	'''operador_soma : ADICAO
	| SUBTRACAO'''

	OPERADOR = Node('SOMA', children=[Node(p[1])])

	operador_soma = Node('operador_soma', children=[OPERADOR])
	p[0] = operador_soma
	pass

def p_operador_logico(p):
	'''operador_logico : E
	| OU'''

	OPERADOR = Node('LOGICO', children=[Node(p[1])])

	operador_logico = Node('operador_logico', children=[OPERADOR])
	p[0] = operador_logico
	pass

def p_operador_negacao(p):
	'''operador_negacao : NEGACAO'''

	OPERADOR = Node('NEGACAO', children=[Node(p[1])])

	operador_negacao = Node('operador_negacao', children=[OPERADOR])
	p[0] = operador_negacao
	pass

def p_operador_multiplicacao(p):
	'''operador_multiplicacao : MULTIPLICACAO
	| DIVISAO'''

	OPERADOR = Node('MULTIPLICACAO', children=[Node(p[1])])

	operador_multiplicacao = Node('operador_multiplicacao', children=[OPERADOR])
	p[0] = operador_multiplicacao
	pass

def p_fator(p):
	'''fator : ABRE_PARENTES expressao FECHA_PARENTES
	| chamada_funcao
	| var
	| numero'''

	fator = Node('fator')

	if len(p) == 2:
		fator.children = [p[1]]
	if len(p) == 4:
		ABRE_PARENTES = Node('ABRE_PARENTES', children=[Node(p[1])])

		FECHA_PARENTES = Node('FECHA_PARENTES', children=[Node(p[3])])

		fator.children = [ABRE_PARENTES, p[2], FECHA_PARENTES]

	p[0] = fator
	pass

def p_numero(p):
	'''numero : NUM_INTEIRO
	| NUM_FLUTUANTE
	| NUM_CIENTIFICO'''

	NUMERO = Node('NUMERO', children=[Node(p[1])])

	numero = Node('numero', children=[NUMERO])
	p[0] = numero
	pass

def p_chamada_funcao(p):
	'''chamada_funcao : ID ABRE_PARENTES lista_argumentos FECHA_PARENTES'''

	ID = Node('ID', children=[Node(p[1])])

	ABRE_PARENTES = Node('ABRE_PARENTES', children=[Node(p[2])])

	FECHA_PARENTES = Node('FECHA_PARENTES', children=[Node(p[4])])

	chamada_funcao = Node('chamada_funcao', children=[ID, ABRE_PARENTES, p[3], FECHA_PARENTES])
	p[0] = chamada_funcao
	pass

def p_lista_argumentos(p):
	'''lista_argumentos : lista_argumentos VIRGULA expressao
	| expressao
	| vazio'''

	lista_argumentos = Node('lista_argumentos')

	if len(p) == 2 and p[1]:
		lista_argumentos.children = [p[1]]
	if len(p) == 4:
		VIRGULA = Node('VIRGULA', children=[Node(p[2])])

		lista_argumentos.children = [p[1], VIRGULA, p[3]]
	p[0] = lista_argumentos
	pass

def p_vazio(p):
	'vazio :'

	p[0] = Node('vazio')
	pass
