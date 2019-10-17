from ply import lex

from lexer.tokens import tokens
from lexer.reserved import reserved
from lexer.patterns import *

tokens += tuple(reserved.values())

def t_ID(t):
	r'[a-zA-Z_à-ú][a-zA-Z_0-9à-ú]*'
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
