# src/syntatic/rules/errors.py
from anytree import Node
from ply import yacc

def error_msg(error, msg="", but=""):
	msg_error = "Espera-se " + msg + " na linha " + str(error.lineno)
	if len(but):
		msg_error = msg_error + ", mas encontrou " + but
	return msg_error

def p_se_error(p):
	'''se : SE expressao ENTAO corpo error
	| SE expressao error corpo FIM
	| SE error'''

	se = Node('se com erro')
	p[0] = se

	if p.slice[2].type == 'error' and len(p) == 3:
		SE = Node(p[1])
		p[0].children = [SE]

		print(error_msg(p.slice[2], msg="bolinha"))
	if p.slice[3].type == 'error' and len(p) == 6:
		SE = Node(p[1])
		p[0].children = [SE]

		print(error_msg(p.slice[3], msg="'entao' após 'expressão'", but=("'%s'" % (p[3].value))))
	elif p.slice[5].type == 'error' and len(p) == 6:
		SE = Node(p[1])
		p[0].children = [SE]

		print(error_msg(p.slice[5], msg="faltou o fim"))

	pass

def p_se_error_2(p):
	'''se : SE expressao ENTAO corpo SENAO corpo error'''

	pass

def p_indice_error(p):
	'''indice : indice ABRE_COLCHETES expressao error
	| indice ABRE_COLCHETES error FECHA_COLCHETES
	| indice ABRE_COLCHETES error
	| indice error'''

	indice = Node('indice com erro')
	p[0] = indice

	if p.slice[2].type == 'error' and len(p) == 3:
		p[0].children = [p[1]]

		print(error_msg(p.slice[2], msg="'['1"))
	if p.slice[3].type == 'error' and len(p) == 4:
		ABRE_COLCHETES = Node('ABRE_COLCHETES')

		p[0].children = [p[1], ABRE_COLCHETES]

		print(error_msg(p.slice[3], msg="\"numero\" após '['"))
	elif p.slice[3].type == 'error' and len(p) == 5:
		ABRE_COLCHETES = Node('ABRE_COLCHETES')
		FECHA_COLCHETES = Node('FECHA_COLCHETES')

		p[0].children = [p[1], ABRE_COLCHETES, FECHA_COLCHETES]

		print(error_msg(p.slice[3], msg="\"numero\" entre '[' e ']'"))
	elif p.slice[4].type == 'error':
		ABRE_COLCHETES = Node('ABRE_COLCHETES')

		p[0].children = [p[1], ABRE_COLCHETES, p[4]]

		print(error_msg(p.slice[4], msg="erro de indice funcao indice_error"))
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

	indice = Node('indice com erro')
	p[0] = indice
	pass

def p_numero_error(p):
	'''numero : error'''

	if p.slice[1].type == 'error':
		print("Erro de declaracao na linha %s, espera-se um numero" % (p.slice[1].lineno))

	numero = Node('numero com erro')
	p[0] = numero
	pass


def p_error(p):
	if p:
		print("erro sintático: não foi possível reconhecer '%s' na linha %d" % (p.value, p.lineno))
	else:
		print("erro sintático: definições incompletas!")
		exit(0)
	pass

