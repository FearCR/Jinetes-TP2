# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables -- all in one file.
# -----------------------------------------------------------------------------

tokens = (
    #GENERALES 
    'STRING','ADDITIONALINFO_COMMENT_OPEN','ADDITIONALINFO_COMMENT_CLOSE',
    #VULNERABILITY
    'NODE_VULNERABILITIES_OPEN','NODE_VULNERABILITIES_CLOSE',
    'VULNERABILITY_OPEN','VULNERABILITY_CLOSE','VULN_NAME_OPEN','VULN_NAME_CLOSE',
    'REF_SECURITY_OPEN','REF_SECURITY_CLOSE','VULN_OVERVIEW_OPEN','VULN_OVERVIEW_CLOSE',
    'VULN_DESCRIPTION_OPEN','VULN_DESCRIPTION_CLOSE','VULN_IMPACT_OPEN','VULN_IMPACT_CLOSE',
    'VULN_SEVERITY_OPEN','VULN_SEVERITY_CLOSE', 'VULN_ADDITIONAL_INFO_OPEN','VULN_ADDITIONAL_INFO_CLOSE',
    #SECURITY CONTROL
    'NODE_SECURITY_CONTROLS_OPEN','NODE_SECURITY_CONTROLS_CLOSE', 'SECURITY_CONTROL_OPEN','SECURITY_CONTROL_CLOSE',
    'SECCONT_NAME_OPEN','SECCONT_NAME_CLOSE','SECCONT_DESCRIPTION_OPEN','SECCONT_DESCRIPTION_CLOSE',
    'SECCONT_SECURITY_POLICIES_OPEN','SECCONT_SECURITY_POLICIES_CLOSE','SECPOLICY_ID_OPEN','SECPOLICY_ID_CLOSE',
    'SECCONT_ADDITIONAL_INFO_OPEN','SECCONT_ADDITIONAL_INFO_CLOSE',
    )

#TOKENS JULIAN
#GENERALES
t_STRING                = r'[a-zA-Z0-9_\s,./\[\]]+'
t_ADDITIONALINFO_COMMENT_OPEN  = '<additional-information:comment>'
t_ADDITIONALINFO_COMMENT_CLOSE = '</additional-information:comment>'
#VULNERABILITY
t_NODE_VULNERABILITIES_OPEN  = '<node:vulnerabilities>'
t_NODE_VULNERABILITIES_CLOSE = '</node:vulnerabilities>'
##OJO CON ESTE QUE TIENE STRING ADENTRO, TALVEZ SE TENGA QUE MODIFICAR
#t_VULNERABILITY_OPEN    = r'<vulnerabilities:vulnerability[a-zA-Z0-9_\s,./]+>'
#t_VULNERABILITY_CLOSE   = '</vulnerabilities:vulnerability>'
####################################
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
t_VULN_ADDITIONAL_INFO_OPEN  = '<vulnerability:additional-information>'
t_VULN_ADDITIONAL_INFO_CLOSE = '</vulnerability:additional-information>'
#SECURITY CONTROL
#IGUAL QUE EL DE ARRIBA PUEDE QUE HAYA QUE CAMBIARLO
##t_NODE_SECURITY_CONTROLS_OPEN     = '<node:security-controls>'
##t_NODE_SECURITY_CONTROLS_CLOSE    = '</node:security-controls>'
t_SECURITY_CONTROL_OPEN          = r'<security-controls:security-control[a-zA-Z0-9_\s,./]+>'
t_SECURITY_CONTROL_CLOSE         = ' </security-controls:security-control>'
#########################################
t_SECCONT_NAME_OPEN                 = '<security-control:name>'
t_SECCONT_NAME_CLOSE                = '</security-control:name>'
t_SECCONT_DESCRIPTION_OPEN          = '<security-control:description>'
t_SECCONT_DESCRIPTION_CLOSE         = '</security-control:description>'
t_SECCONT_SECURITY_POLICIES_OPEN    = '<security-control:security-policies>'
t_SECCONT_SECURITY_POLICIES_CLOSE   = '</security-control:security-policies>'
t_SECPOLICY_ID_OPEN                 = '<security-policies:security-policy-id>'
t_SECPOLICY_ID_CLOSE                = '</security-policies:security-policy-id>'
t_SECCONT_ADDITIONAL_INFO_OPEN      = '<security-control:additional-information>'
t_SECCONT_ADDITIONAL_INFO_CLOSE     = '</security-control:additional-information>'
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

#GENERALES
def p_expression_additionalInfo(t):
    'expression : ADDITIONALINFO_COMMENT_OPEN ADDITIONALINFO_COMMENT_CLOSE'
    print("ADDITIONAL INFO")
#VULNERABILITIES
#ESTAS HAY QUE CAMBIARLAS A FUTURO####################################
"""
def p_expression_vulnerabilities(t):
    'expression : NODE_VULNERABILITIES_OPEN NODE_VULNERABILITIES_CLOSE'
    print("VULNERABILITIES")   

def p_expression_vulnerability(t):
    'expression : VULNERABILITY_OPEN VULNERABILITY_CLOSE'
    print("VULNERABILITY")
""" 
####################################

def p_expression_vulnerability_name(t):
    'expression : VULN_NAME_OPEN STRING VULN_NAME_CLOSE'
    print("VULNERABILITY NAME")
#ESTAS HAY QUE CAMBIARLAS A FUTURO####################################
"""
def p_expression_vulnerability_refSecurity(t):
    'expression : VULN_REFERENCE_OPEN expression VULN_REFERENCE_CLOSE'
    print("VULNERABILITY REFERENCE SECURITY")
"""
#####################################
def p_expression_refSecurity(t):
    'expression : REF_SECURITY_OPEN STRING REF_SECURITY_CLOSE'
    print("REFERENCE SECURITY")
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
#HAY QUE CAMBIARLO A FUTURO###################
"""
def p_expression_vulnerability_additionalInfo(t):
    'expression : VULN_ADDITIONAL_INFO_OPEN VULN_ADDITIONAL_INFO_CLOSE'
    print("VULNERABILITY ADDITIONAL INFO") 
"""
######################################

#Security
#ESTAS HAY QUE CAMBIARLAS A FUTURO####################################
"""
def p_expression_security_controls(t):
    'expression : NODE_SECURITY_CONTROLS_OPEN NODE_SECURITY_CONTROLS_CLOSE'
    print("SECURITY CONTROLS")
def p_expression_security_control(t):
    'expression : SECURITY_CONTROLS_OPEN SECURITY_CONTROLS_CLOSE'
    print("SECURITY CONTROLS")
"""
##########
def p_expression_security_control_name(t):
    'expression : SECCONT_NAME_OPEN  STRING SECCONT_NAME_CLOSE'
    print("SECURITY CONTROL NAME")
def p_expression_security_control_description(t):
    'expression : SECCONT_DESCRIPTION_OPEN  STRING SECCONT_DESCRIPTION_CLOSE'
    print("SECURITY CONTROL DESCRIPTION")
####HAY QUE CAMBIARLAS######
"""
def p_expression_security_policies(t):
    'expression : SECCONT_SECURITY_POLICIES_OPEN  STRING SECCONT_SECURITY_POLICIES_CLOSE'
    print("SECURITY CONTROL POLICIES")
"""
#######
def p_expression_security_policyID(t):
    'expression : SECPOLICY_ID_OPEN  STRING SECPOLICY_ID_CLOSE'
    print("SECURITY POLICY ID")
#HAY QUE CAMBIARLO A FUTURO###################
"""
def p_expression_securityPolicy_additionalInfo(t):
    'expression : SECCONT_ADDITIONAL_INFO_OPEN SECCONT_ADDITIONAL_INFO_CLOSE'
    print("Security Policy Additonal Info") 
"""
######################################
    
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
