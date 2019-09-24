from ply import lex

from tokens.tokens import tokens
from reserved.words import reserved
from patterns.patterns import *

tokens += list(reserved.values())

def t_ID(t):
	r'[a-zãéA-Z_][a-zãéA-Z_0-9]*'
	t.type = reserved.get(t.value, 'ID')
	return t

lexer = lex.lex()

def tokenize(data = None):
	if data == None: return None
	
	lexer.input(data)
	tokens = []

	while True:
		tok = lexer.token()
		if not tok: break
		
		tokens.append(tok)
	return tokens
