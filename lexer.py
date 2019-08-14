import ply.lex as lex

from tokens.tokens import tokens
from reserved.words import reserved
from patterns.patterns import *

def t_ID(t):
	r'[a-zãéA-Z_][a-zãéA-Z_0-9]*'
	t.type = reserved.get(t.value, 'ID')
	return t

lexer = lex.lex()

data = '''
inteiro: n
inteiro fatorial(inteiro: n)
	inteiro: fat
	se n > 0 então {não calcula se n > 0}
		fat := 1
		repita
			fat := fat * n
			n := n - 1
		até n = 0
		retorna(fat) {retorna o valor do fatorial de n}
	senão
		retorna(0)
	fim
fim

inteiro principal()
	leia(n)
	escreva(fatorial(n))
	retorna(0)
fim
'''

lexer.input(data)

while True:
	tok = lexer.token()
	if not tok:
		break
	print(tok)
