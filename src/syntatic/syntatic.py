# src/syntatic/syntatic.py

import ply.yacc as yacc

from lexer import tokens
# pylint: disable=unused-wildcard-import
from syntatic.rules import *

def syntatic():
	print('ola')

parser = yacc.yacc(start='programa', optimize=False)

def parse(data, debug = 0):
	parser.error = 0
	p = parser.parse(data, debug=debug)
	if parser.error:
		return None

	return p
