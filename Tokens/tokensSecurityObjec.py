# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables -- all in one file.
# -----------------------------------------------------------------------------

tokens = (
    'DATA',
    'SECUOBJ_NAME_OPEN', 'SECUOBJ_NAME_CLOSE','SECUOBJ_DESCRIP_OPEN','SECUOBJ_DESCRIP_CLOSE',
    'SECUOBJ_OBJTYPE_OPEN','SECUOBJ_OBJTYPE_CLOSE','SECUOBJ_SECUSERV_OPEN','SECUOBJ_SECUSERV_CLOSE',
    'SECUOBJ_TEMP_OPEN','SECUOBJ_TEMP_CLOSE','SECUOBJ_OBJSOUR_OPEN','SECUOBJ_OBJSOUR_CLOSE'

)

# TOKENS RONNY
t_DATA = r'[a-zA-Z0-9_\s,./]+'
t_SECUOBJ_NAME_OPEN = '<security-objective:name>'
t_SECUOBJ_NAME_CLOSE = '</security-objective:name>'
t_SECUOBJ_DESCRIP_OPEN='<security-objective:description>'
t_SECUOBJ_DESCRIP_CLOSE='</security-objective:description>'
t_SECUOBJ_OBJTYPE_OPEN='<security-objective:objective-type>'
t_SECUOBJ_OBJTYPE_CLOSE='</security-objectives:objective-type>'
t_SECUOBJ_SECUSERV_OPEN='<security-objective:security-service>'
t_SECUOBJ_SECUSERV_CLOSE='</security-objective:security-service>'
t_SECUOBJ_TEMP_OPEN="<security-objective:temporality>"
t_SECUOBJ_TEMP_CLOSE="</security-objective:temporality>"
t_SECUOBJ_OBJSOUR_OPEN="<security-objectives:objective-source>"
t_SECUOBJ_OBJSOUR_CLOSE="</security-objectives:objective-source>"
def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


# Ignored characters
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
import ply.lex as lex

lexer = lex.lex()

# Parsing rules

precedence = (

)


def p_expression_security_objective_name(t):
    'expression : SECUOBJ_NAME_OPEN DATA SECUOBJ_NAME_CLOSE'
    print("SECUOBJ_NAME")


def p_expression_security_objective_description(t):
    'expression : SECUOBJ_DESCRIP_OPEN DATA SECUOBJ_DESCRIP_CLOSE'
    print("SECUOBJ_DESCRIP")

def p_expression_security_objective_objective_type(t):
    'expression : SECUOBJ_OBJTYPE_OPEN DATA SECUOBJ_OBJTYPE_CLOSE'
    print("SECUOBJ_OBJTYPE")


def p_expression_security_objective_security_service(t):
    'expression : SECUOBJ_SECUSERV_OPEN DATA SECUOBJ_SECUSERV_CLOSE'
    print("SECUOBJ_SECUSERV")


def p_expression_security_objective_temporality(t):
    'expression : SECUOBJ_TEMP_OPEN DATA SECUOBJ_TEMP_CLOSE'
    print("SECUOBJ_TEMP")


def p_expression_security_objective_source(t):
    'expression : SECUOBJ_OBJSOUR_OPEN DATA SECUOBJ_OBJSOUR_CLOSE'
    print("SECUOBJ_SOURCE")





def p_error(t):
    print("Syntax error at '%s'" % t.value)


import ply.yacc as yacc
parser = yacc.yacc()

file = open('securityObjec.xml', 'r')
count = 0
for line in file:
    try:
        parser.parse(line)
    except EOFError:
        break
file.close()