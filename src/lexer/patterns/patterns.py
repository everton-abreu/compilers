# patterns/patterns.py

t_ATRIBUICAO = r'\:\='

t_ADICAO = r'\+'
t_SUBTRACAO = r'-'
t_MULTIPLICACAO = r'\*'
t_DIVISAO = r'\/'

t_MAIOR_IGUAL = r'\>\='
t_MENOR_IGUAL = r'\<\='
t_DIFERENTE = r'\<\>'
t_IGUAL = r'\='
t_MAIOR = r'\>'
t_MENOR = r'\<'

t_E = r'\&\&'
t_OU = r'\|\|'

t_NEGACAO = r'\!'

t_ABRE_PARENTES = r'\('
t_FECHA_PARENTES = r'\)'
t_ABRE_COLCHETES = r'\['
t_FECHA_COLCHETES = r'\]'
t_DOIS_PONTOS = r'\:'
t_VIRGULA = r'\,'

t_ignore = ' \t'

def t_NUM_FLUTUANTE(t):
	r'(\d+)\.(\d+)?'
	t.value = float(t.value)
	return t

def t_NUM_INTEIRO(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)
	pass

def t_COMENTARIO(t):
	r'\{(.|\n)*?\}'

def t_error(t):
	print("Caracter invalido '%s'" % t.value[0])
	t.lexer.skip(1)
