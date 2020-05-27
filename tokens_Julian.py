import ply.lex as lex
import ply.yacc as yacc
import sys

tokens = (
    #GENERALES 
    'STRING','ADDITIONALINFO_COMMENT_OPEN','ADDITIONALINFO_COMMENT_CLOSE',
    #VULNERABILITY
    'NODE_VULNERABILITIES_OPEN','NODE_VULNERABILITIES_CLOSE',
    'VULNERABILITY_OPEN','VULNERABILITY_CLOSE','VULN_NAME_OPEN','VULN_NAME_CLOSE',
    'VULN_REFERENCE_OPEN','VULN_REFERENCE_CLOSE',
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
t_ADDITIONALINFO_COMMENT_OPEN  = r'<additional-information:comment>'
t_ADDITIONALINFO_COMMENT_CLOSE = r'</additional-information:comment>'
#VULNERABILITY
t_NODE_VULNERABILITIES_OPEN  = r'<node:vulnerabilities>'
t_NODE_VULNERABILITIES_CLOSE = r'</node:vulnerabilities>'
##OJO CON ESTE QUE TIENE STRING ADENTRO, TALVEZ SE TENGA QUE MODIFICAR
t_VULNERABILITY_OPEN    = r'<vulnerabilities:vulnerability\svunerability-id=\"[a-zA-Z0-9_\s,./-]+\">'
t_VULNERABILITY_CLOSE   = r'</vulnerabilities:vulnerability>'
####################################
t_VULN_NAME_OPEN        = r'<vulnerability:name>'
t_VULN_NAME_CLOSE       = r'</vulnerability:name>'
t_VULN_REFERENCE_OPEN   = r'<vulnerability:reference-security-services>'
t_VULN_REFERENCE_CLOSE  = r'</vulnerability:reference-security-services>'
t_REF_SECURITY_OPEN     = r'<reference-security-services:reference-security-service>'
t_REF_SECURITY_CLOSE    = r'</reference-security-services:reference-security-service>'
t_VULN_OVERVIEW_OPEN    = r'<vulnerability:overview>'
t_VULN_OVERVIEW_CLOSE   = r'</vulnerability:overview>'
t_VULN_DESCRIPTION_OPEN = r'<vulnerability:description>'
t_VULN_DESCRIPTION_CLOSE= r'</vulnerability:description>'
t_VULN_IMPACT_OPEN      = r'<vulnerability:impact>'
t_VULN_IMPACT_CLOSE     = r'</vulnerability:impact>'
t_VULN_SEVERITY_OPEN    = r'<vulnerability:severity>'
t_VULN_SEVERITY_CLOSE   = r'</vulnerability:severity>'
t_VULN_ADDITIONAL_INFO_OPEN  = r'<vulnerability:additional-information>'
t_VULN_ADDITIONAL_INFO_CLOSE = r'</vulnerability:additional-information>'
#SECURITY CONTROL
#IGUAL QUE EL DE ARRIBA PUEDE QUE HAYA QUE CAMBIARLO
t_NODE_SECURITY_CONTROLS_OPEN     = '<node:security-controls>'
t_NODE_SECURITY_CONTROLS_CLOSE    = '</node:security-controls>'
t_SECURITY_CONTROL_OPEN          = r'<security-controls:security-control\scontrol-id=\"[a-zA-Z0-9_\s,./-]+\">'
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
t_ignore = " \t\n"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Build the lexer
lexer = lex.lex()

# Parsing rules

precedence = (
    )

# dictionary of names
names = { }
    
#EXPRESIONES JULIAN 
#VULNERABILITIES
def p_expression(t):
    '''expression : node_vulnerabilities
                  | node_security_controls'''

def p_node_vulnerabilities(t):
    '''node_vulnerabilities : NODE_VULNERABILITIES_OPEN node_vulnerabilities
                            | vulnerability node_vulnerabilities
                            | NODE_VULNERABILITIES_CLOSE'''

def p_vulnerability(t):
    '''vulnerability : VULNERABILITY_OPEN vulnerability
                     | vulnerability_name vulnerability
                     | vulnerability_refSecurity vulnerability
                     | refSecurity vulnerability
                     | vulnerability_overview vulnerability
                     | vulnerability_description vulnerability
                     | vulnerability_impact vulnerability
                     | vulnerability_severity vulnerability
                     | vulnerability_additionalInfo vulnerability
                     | VULNERABILITY_CLOSE'''
          
def p_vulnerability_refSecurity(t):
    '''vulnerability_refSecurity : VULN_REFERENCE_OPEN vulnerability_refSecurity
                                 | refSecurity
                                 | VULN_REFERENCE_CLOSE'''
                                 
def p_vulnerability_additionalInfo(t):
    '''vulnerability_additionalInfo : VULN_ADDITIONAL_INFO_OPEN vulnerability_additionalInfo
                                    | additionalInfo
                                    | VULN_ADDITIONAL_INFO_CLOSE''' 
               
def p_vulnerability_name(t):
    'vulnerability_name : VULN_NAME_OPEN STRING VULN_NAME_CLOSE'
    print("Nombre del objetivo", t[2])
def p_refSecurity(t):
    'refSecurity : REF_SECURITY_OPEN STRING REF_SECURITY_CLOSE'
    print("Descripcion: ", t[2])
def p_vulnerability_overview(t):
    'vulnerability_overview : VULN_OVERVIEW_OPEN STRING VULN_OVERVIEW_CLOSE'
    print("Overiew Vulnerabilidad: ",t[2])
def p_vulnerability_description(t):
    'vulnerability_description : VULN_DESCRIPTION_OPEN STRING VULN_DESCRIPTION_CLOSE'
    print("Descripcion detallada: ",t[2])
def p_vulnerability_impact(t):
    'vulnerability_impact : VULN_IMPACT_OPEN STRING VULN_IMPACT_CLOSE'
    print("Impacto: ",t[2])
def p_vulnerability_severity(t):
    'vulnerability_severity : VULN_SEVERITY_OPEN STRING VULN_SEVERITY_CLOSE'
    print("Severidad: ",t[2])


#Security
def p_node_security_controls(t):
    '''node_security_controls : NODE_SECURITY_CONTROLS_OPEN node_security_controls
                              | security_control node_security_controls
                              | NODE_SECURITY_CONTROLS_CLOSE'''

def p_security_control(t):
    '''security_control : SECURITY_CONTROL_OPEN security_control
                        | security_control_name security_control
                        | security_control_description security_control
                        | security_policies security_control
                        | securityControl_additionalInfo security_control
                        | SECURITY_CONTROL_CLOSE'''
          
def p_security_policies(t):
    '''security_policies : SECCONT_SECURITY_POLICIES_OPEN security_policies
                         | security_policyID
                         | SECCONT_SECURITY_POLICIES_CLOSE'''
                                 
def p_securityControl_additionalInfo(t):
    '''securityControl_additionalInfo : SECCONT_ADDITIONAL_INFO_OPEN securityControl_additionalInfo
                                      | additionalInfo
                                      | SECCONT_ADDITIONAL_INFO_CLOSE''' 
                                    
def p_security_control_name(t):
    'security_control_name : SECCONT_NAME_OPEN STRING SECCONT_NAME_CLOSE'
    print("SECURITY CONTROL NAME")
def p_security_control_description(t):
    'security_control_description : SECCONT_DESCRIPTION_OPEN STRING SECCONT_DESCRIPTION_CLOSE'
    print("SECURITY CONTROL DESCRIPTION")

def p_security_policyID(t):
    'security_policyID : SECPOLICY_ID_OPEN STRING SECPOLICY_ID_CLOSE'
    print("SECURITY POLICY ID")
#GENERALES
def p_additionalInfo(t):
    'additionalInfo : ADDITIONALINFO_COMMENT_OPEN ADDITIONALINFO_COMMENT_CLOSE'
    print("ADDITIONAL INFO")

#ERROR    
def p_error(t):
    print("Syntax error at '%s'" % t.value)



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
print("------------------RECONOCIMIENTO DE TOKENS------------------")
file = open('pruebaJulian.xml','r')
count = 0
for line in file:
    try:
        lexer=lex.lex()
        lexer.input(line)
        while True:
            tok=lexer.token()
            if not tok:
                break
            print(tok)
    except EOFError:
        break
file.close() 
print("------------------FIN DE PRUEBA DE RECONOCIMIENTO DE TOKENS------------------")
