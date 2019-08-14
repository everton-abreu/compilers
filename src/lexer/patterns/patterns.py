# patterns/patterns.py

t_MAIS = r'\+'
t_MENOS = r'-'
t_VEZES = r'\*'
t_DIVIDIR = r'/'
t_ABRE_PARENTES = r'\('
t_FECHA_PARENTES = r'\)'
t_DOIS_PONTOS = r'\:'
t_RECEBE = r'\:\='
t_IGUAL = r'\='
t_MAIOR = r'\>'
t_MENOR = r'\<'

t_ignore = ' \t'

def t_NUMERO(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)
	pass

def t_COMENTARIO(t):
	r'\{.*\}'

def t_error(t):
	print("Caracter invalido '%s'" % t.value[0])
	t.lexer.skip(1)
