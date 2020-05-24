# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables -- all in one file.
# -----------------------------------------------------------------------------

tokens = (
    'STRING',
    'VULN_NAME_OPEN','VULN_NAME_CLOSE',
    'REF_SECURITY_OPEN','REF_SECURITY_CLOSE','VULN_OVERVIEW_OPEN','VULN_OVERVIEW_CLOSE',
    'VULN_DESCRIPTION_OPEN','VULN_DESCRIPTION_CLOSE','VULN_IMPACT_OPEN','VULN_IMPACT_CLOSE',
    'VULN_SEVERITY_OPEN','VULN_SEVERITY_CLOSE',
    )

#TOKENS JULIAN
t_STRING                  = r'[a-zA-Z0-9_\s,./]+'
t_VULN_NAME_OPEN        = '<vulnerability:name>'
t_VULN_NAME_CLOSE       = '</vulnerability:name>'
#t_VULN_REFERENCE_OPEN   = '<vulnerability:reference-security-services>'
#t_VULN_REFERENCE_CLOSE  = '</vulnerability:reference-security-service>'
t_REF_SECURITY_OPEN     = '<reference-security-services:reference-security-service>'
t_REF_SECURITY_CLOSE    = '</reference-security-services:reference-security-service>'
t_VULN_OVERVIEW_OPEN    = '<vulnerability:overview>'
t_VULN_OVERVIEW_CLOSE   = '</vulnerability:overview>'
t_VULN_DESCRIPTION_OPEN = '<vulnerability:description>'
t_VULN_DESCRIPTION_CLOSE= '</vulnerability:description>'
t_VULN_IMPACT_OPEN      = '<vulnerability:impact>'
t_VULN_IMPACT_CLOSE     = '</vulnerability:impact>'
t_VULN_SEVERITY_OPEN    = '<vulnerability:severity>'
t_VULN_SEVERITY_CLOSE   = '</vulnerability:severity>'

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

# dictionary of names
names = { }

""" ESTAS SON FUNCIONES VIEJAS DE LA CALCULADORA 
def p_statement_expr(t):
    'statement : expression'
    print(t[1])
    
def p_expression_binop(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if t[2] == '+'  : t[0] = t[1] + t[3]
    elif t[2] == '-': t[0] = t[1] - t[3]
    elif t[2] == '*': t[0] = t[1] * t[3]
    elif t[2] == '/': t[0] = t[1] / t[3]
"""
    
#EXPRESIONES JULIAN          
def p_expression_vulnerability_name(t):
    'expression : VULN_NAME_OPEN STRING VULN_NAME_CLOSE'
    print("VULNERABILITY NAME")
"""
def p_expression_vulnerability_refSecurity(t):
    'expression : VULN_REFERENCE_OPEN expression VULN_REFERENCE_CLOSE'
    print("VULNERABILITY REFERENCE SECURITY")
"""
def p_expression_refSecurity(t):
    'expression : REF_SECURITY_OPEN STRING REF_SECURITY_CLOSE'
    print("REFERENC SECURITY")
def p_expression_vulnerability_overview(t):
    'expression : VULN_OVERVIEW_OPEN STRING VULN_OVERVIEW_CLOSE'
    print("VULNERABILITY OVERVIEW")
def p_expression_vulnerability_description(t):
    'expression : VULN_DESCRIPTION_OPEN STRING VULN_DESCRIPTION_CLOSE'
    print("VULNERABILITY DESCRIPTION")
def p_expression_vulnerability_impact(t):
    'expression : VULN_IMPACT_OPEN STRING VULN_IMPACT_CLOSE'
    print("VULNERABILITY IMPACT")
def p_expression_vulnerability_severity(t):
    'expression : VULN_SEVERITY_OPEN STRING VULN_SEVERITY_CLOSE'
    print("VULNERABILITY SEVERITY")
 
def p_error(t):
    print("Syntax error at '%s'" % t.value)


import ply.yacc as yacc
parser = yacc.yacc()
""" LEER POR INPUT CALCULADORA
while True:
    try:
        s = input('calc > ')   # Use raw_input on Python 2
    except EOFError:
        break
    parser.parse(s)
"""
#LEER ARCHIVO
file = open('prueba.xml','r')
count = 0
for line in file:
    try:
        parser.parse(line)
    except EOFError:
        break
file.close() 
