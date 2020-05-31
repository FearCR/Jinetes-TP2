import sys
import ply.lex as lex
import ply.yacc as yacc


tokens = (
    'DATA',
    'DATASP',
    'NODE_RISKS_OPEN',
    'NODE_RISKS_CLOSE',
    'RISKS_RISK_OPEN',
    'RISKS_RISK_CLOSE',
    'RISK_NAME_OPEN',
    'RISK_NAME_CLOSE',
    'RISK_OBJ_OPEN',
    'RISK_OBJ_CLOSE',
    'RISK_VUL_OPEN',
    'RISK_VUL_CLOSE',
    'RISK_THREAT_OPEN',
    'RISK_THREAT_CLOSE',
    'RISK_DESCRIPTION_OPEN',
    'RISK_DESCRIPTION_CLOSE',
    'RISK_LIKHD_OPEN',
    'RISK_LIKHD_CLOSE',
    'RISK_IMPACT_OPEN',
    'RISK_IMPACT_CLOSE',
    'RISK_TEMP_OPEN',
    'RISK_TEMP_CLOSE',
    'RISK_ADDINFO_OPEN',
    'RISK_ADDINFO_CLOSE',
    'RISK_ADDINFOCOMM_OPEN',
    'RISK_ADDINFOCOMM_CLOSE',
)

# TOKENS RONNY
#t_DATA = r'''[a-zA-Z0-9_\s,.:,ó\[\]]+\s?-?\s?[a-zA-Z0-9_\s,.:,ó\/]*-?\s?[a-zA-Z0-9_\s,.:,ó]*'''
t_DATA = r'[^<>]+'

t_NODE_RISKS_OPEN=r'<node:risks>'
t_NODE_RISKS_CLOSE=r'</node:risks>'
t_RISKS_RISK_OPEN=r'<risks:risk\srisk-id=".*">'
t_RISKS_RISK_CLOSE=r'</risks:risk>'
t_RISK_NAME_OPEN=r'<risk:name>'
t_RISK_NAME_CLOSE=r'</risk:name>'
t_RISK_OBJ_OPEN=r'<risk:objective-id>'
t_RISK_OBJ_CLOSE=r'</risk:objective-id>'
t_RISK_VUL_OPEN=r'<risk:vulnerability-id>'
t_RISK_VUL_CLOSE=r'</risk:vulnerability-id>'
t_RISK_THREAT_OPEN=r'<risk:threat-id>'
t_RISK_THREAT_CLOSE=r'</risk:threat-id>'
t_RISK_DESCRIPTION_OPEN=r'<risk:description>'
t_RISK_DESCRIPTION_CLOSE=r'</risk:description>'
t_RISK_LIKHD_OPEN=r'<risk:likelihood>'
t_RISK_LIKHD_CLOSE=r'</risk:likelihood>'
t_RISK_IMPACT_OPEN=r'<risk:impact>'
t_RISK_IMPACT_CLOSE=r'</risk:impact>'
t_RISK_TEMP_OPEN=r'<risk:temporality>'
t_RISK_TEMP_CLOSE=r'</risk:temporality>'

t_RISK_ADDINFO_OPEN=r'<risk:additional-information>'
t_RISK_ADDINFO_CLOSE=r'</risk:additional-information>'
t_RISK_ADDINFOCOMM_OPEN=r'<additional-information:comment>'
t_RISK_ADDINFOCOMM_CLOSE=r'</additional-information:comment>'



t_ignore = " \n\t"



def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
import ply.lex as lex

lexer = lex.lex()


def p_node_risks(t):
    '''
    node_risks : NODE_RISKS_OPEN node_risks
                  | risks_risk node_risks
                  | NODE_RISKS_CLOSE
                  '''


def p_risks_risk(t):
    '''
    risks_risk : RISKS_RISK_OPEN risks_risk
                  |  risk_name
                  |  risk_objective
                  |  risk_vulnerability
                  |  risk_threat
                  |  risk_description
                  |  risk_likelihood
                  |  risk_impact
                  |  risk_temporality
                  |  risk_additional_information
                  | RISKS_RISK_CLOSE
                  '''


def p_risk_name(t):
    '''
    risk_name : RISK_NAME_OPEN DATA RISK_NAME_CLOSE
    '''
    print("Risk name: ",t[2])


def p_risk_objective(t):
    '''
    risk_objective : RISK_OBJ_OPEN DATA RISK_OBJ_CLOSE
    '''
    print("Risk objective: ", t[2])

def p_risk_vulnerability(t):
    '''
    risk_vulnerability : RISK_VUL_OPEN DATA RISK_VUL_CLOSE
    '''
    print("Risk vulnerability: ", t[2])


def p_risk_threat(t):
    '''
    risk_threat : RISK_THREAT_OPEN DATA RISK_THREAT_CLOSE
    '''
    print("Risk threat: ", t[2])


def p_risk_description(t):
    '''
    risk_description : RISK_DESCRIPTION_OPEN DATA RISK_DESCRIPTION_CLOSE
    '''
    print("Risk description: ", t[2])

def p_risk_likelihood(t):
    '''
    risk_likelihood : RISK_LIKHD_OPEN DATA RISK_LIKHD_CLOSE
    '''
    print("Risk likelihood: ", t[2])


def p_risk_impact(t):
    '''
    risk_impact : RISK_IMPACT_OPEN DATA RISK_IMPACT_CLOSE
    '''
    print("Risk impact: ", t[2])

def p_risk_temporality(t):
    '''
    risk_temporality : RISK_TEMP_OPEN DATA RISK_TEMP_CLOSE
    '''
    print("Risk temporality: ", t[2])

def p_risk_additional_information(t):
    '''
    risk_additional_information : RISK_ADDINFO_OPEN additional_information_comment RISK_ADDINFO_CLOSE
    '''


def p_additional_information_comment(t):
    '''
    additional_information_comment : RISK_ADDINFOCOMM_OPEN RISK_ADDINFOCOMM_CLOSE
    '''


def p_error(t):
    print("Syntax error at '%s'" % t.value)


print("------------------RECONOCIMIENTO DE TOKENS------------------")
file = open('pruebaRisk.xml','r')
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


import ply.yacc as yacc
parser = yacc.yacc()

with open('pruebaRisk.xml', 'r') as myfile:
    data=myfile.read()

parser=yacc.yacc()
parser.parse(data)



