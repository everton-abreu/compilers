# src/syntatic/rules/rules.py
from anytree import Node
from lexer import tokens


precendence = (
	('left', 'PLUS', 'MINUS'),
	('left', 'TIMES', 'DIVIDE'),
)

def p_programa(p):
	'programa : lista_declaracoes'

	programa = Node('programa')
	p[0] = programa
	p[1].parent = programa
	pass

def p_lista_declaracoes(p):
	'''lista_declaracoes : lista_declaracoes declaracao
	| declaracao'''

	lista_declaracoes = Node('lista_declaracoes')
	p[0] = lista_declaracoes
	p[1].parent = lista_declaracoes

	if (len(p) > 2):
		p[2].parent = lista_declaracoes
	pass

def p_declaracao(p):
	'''declaracao : declaracao_variaveis
	| inicializacao_variaveis
	| declaracao_funcao'''

	declaracao = Node('declaracao')
	p[0] = declaracao

	p[1].parent = declaracao
	pass

def p_declaracao_variaveis(p):
	'declaracao_variaveis : tipo DOIS_PONTOS lista_variaveis'

	declaracao_variaveis = Node('declaracao_variaveis')
	p[0] = declaracao_variaveis

	p[1].parent = declaracao_variaveis

	dois_pontos = Node('dois_pontos')
	p[2] = dois_pontos
	p[2].parent = declaracao_variaveis

	p[3].parent = declaracao_variaveis
	pass

def p_inicializacao_variaveis(p):
	'inicializacao_variaveis : atribuicao'

	inicializacao_variaveis = Node('inicializacao_variaveis')
	p[0] = inicializacao_variaveis

	p[1] = inicializacao_variaveis
	pass

def p_lista_variaveis(p):
	'''lista_variaveis : lista_variaveis VIRGULA var
	| var'''

	lista_variaveis = Node('lista_variaveis')
	p[0] = lista_variaveis

	p[1].parent = lista_variaveis

	if (len(p) > 2):
		virgula = Node('virgula')
		p[2] = virgula
		p[2].parent = lista_variaveis

		p[3].parent = lista_variaveis
	pass

def p_var(p):
	'''var : ID
	| ID indice'''

	var = Node('var')
	p[0] = var

	id = Node('id')
	p[1] = id
	p[1].parent = var

	if (len(p) > 2):
		p[2].parent = var
	pass

def p_indice(p):
	'''indice : indice ABRE_COLCHETES expressao FECHA_COLCHETES
	| ABRE_COLCHETES expressao FECHA_COLCHETES'''

	indice = Node('indice')
	p[0] = indice

	abre_colchetes = Node('abre_colchetes')
	fecha_colchetes = Node('fecha_colchetes')

	if (len(p) > 4):
		p[1].parent = indice

		p[2] = abre_colchetes
		p[2].parent = indice

		p[3].parent = indice

		p[4] = fecha_colchetes
		p[4].parent = indice
	else:
		p[1] = abre_colchetes
		p[1].parent = indice

		p[2].parent = indice

		p[3] = fecha_colchetes
		p[3].parent = indice
	pass

def p_tipo(p):
	'''tipo : INTEIRO
	| FLUTUANTE'''

	tipo = Node('tipo')
	p[0] = tipo
# terminar
	print(p[1])
	pass

def p_declaracao_funcao(p):
	'''declaracao_funcao : tipo cabecalho
	| cabecalho'''

	pass

def p_cabecalho(p):
	'''cabecalho : '''

	pass

def p_lista_parametros(p):
	'''lista_parametros : '''

	pass

def p_parametro(p):
	'''parametro : '''

	pass

def p_corpo(p):
	'''corpo : '''

	pass

def p_acao(p):
	'''acao : '''

	pass

def p_se(p):
	'''se : '''

	pass

def p_repita(p):
	'''repita : '''

	pass

def p_atribuicao(p):
	'''atribuicao : '''

	pass

def p_leia(p):
	'''leia : '''

	pass

def p_escreva(p):
	'''escreva : '''

	pass

def p_retorna(p):
	'''retorna : '''

	pass

def p_expressao(p):
	'''expressao : '''

	pass

def p_expressao_logica(p):
	'''expressao_logica : '''

	pass

def p_expressao_simples(p):
	'''expressao_simples : '''

	pass

def p_expressao_aditiva(p):
	'''expressao_aditiva : '''

	pass

def p_expressao_multiplicativa(p):
	'''expressao_multiplicativa : '''

	pass

def p_expressao_unaria(p):
	'''expressao_unaria : '''

	pass

def p_operador_relacional(p):
	'''operador_relacional : '''

	pass

def p_operador_soma(p):
	'''operador_soma : '''

	pass

def p_operador_logico(p):
	'''operador_logico : '''

	pass

def p_operador_negacao(p):
	'''operador_negacao : '''

	pass

def p_operador_multiplicacao(p):
	'''operador_multiplicacao : '''

	pass

def p_fator(p):
	'''fator : '''

	pass

def p_numero(p):
	'''numero : '''

	pass

def p_chamada_funcao(p):
	'''chamada_funcao : '''

	pass

def p_lista_argumentos(p):
	'''lista_argumentos : '''

	pass

def p_error(p):
	print('syntax error')
	pass
