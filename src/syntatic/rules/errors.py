# src/syntatic/rules/errors.py
from anytree import Node
from ply import yacc

def error_msg(error, msg="", but=""):
	msg_error = "Espera-se " + msg + " na linha " + str(error.lineno)
	if len(but):
		msg_error = msg_error + ", mas encontrou "
	return msg_error

def p_indice_error(p):
	'''indice : indice ABRE_COLCHETES expressao error
	| indice ABRE_COLCHETES error FECHA_COLCHETES
	| indice ABRE_COLCHETES error
	| indice error'''

	if p.slice[2].type == 'error' and len(p) == 3:
		print(error_msg(p.slice[2], msg="'['"))
	if p.slice[3].type == 'error' and len(p) == 4:
		print(error_msg(p.slice[3], msg="\"numero\" após '['"))
	elif p.slice[3].type == 'error' and len(p) == 5:
		print(error_msg(p.slice[3], msg="']'"))
	elif p.slice[4].type == 'error':
		print("Espera-se \"]\" 4")

	indice = Node('indice')
	p[0] = indice
	pass

def p_indice_error_2(p):
	'''indice : ABRE_COLCHETES expressao error
	| ABRE_COLCHETES error FECHA_COLCHETES
	| ABRE_COLCHETES error'''

	if p.slice[2].type == 'error' and len(p) == 3:
		print("Espera-se '[\"numero\"]' 1 1")
	elif p.slice[2].type == 'error' and len(p) == 4:
		print("Espera-se \"numero\" entre '[' e ']' na linha %d" % (p[2].lineno))
	elif p.slice[3].type == 'error':
		print("Espera-se \"]\" 3 1")

	indice = Node('indice')
	p[0] = indice
	pass

def p_numero_error(p):
	'''numero : error'''

	if p.slice[1].type == 'error':
		print("Erro de declaracao na linha %s, espera-se um numero" % (str(p.slice[1].lineno)))

	numero = Node('numero')
	p[0] = numero
	pass


def p_error(p):
	if p:
		# print("erro sintático: não foi possível reconhecer '%s' na linha %d" % (p.value, p.lineno))
		p = p
	else:
		print("erro sintático: definições incompletas!")
		exit(0)
	pass

