import sys
import ply.lex as lex
import ply.yacc as yacc


tokens = (
    'DATA',
    'NODE_RISKS_OPEN',
    'NODE_RISKS_CLOSE',
    'RISKS_RISK_OPEN',
    'RISKS_RISK_CLOSE',
    'RISK_NAME_OPEN',
    'RISK_NAME_CLOSE',
    'RISK_OBJ_OPEN',
    'RISK_OBJ_CLOSE',
)

# TOKENS RONNY
t_DATA = r'([a-zA-Z0-9_\s,./:,ó]+\s?-?\s?[a-zA-Z0-9_\s,./:,ó]*(\[\d\])+) | ([a-zA-Z0-9_\s,./:,ó]+\s?-?\s?[a-zA-Z0-9_\s,./:,ó]*)'
t_NODE_RISKS_OPEN=r'<node:risks>'
t_NODE_RISKS_CLOSE=r'</node:risks>'
t_RISKS_RISK_OPEN=r'<risks:risk\srisk-id="((\w+-)+)\w+">'
t_RISKS_RISK_CLOSE=r'</risks:risk>'
t_RISK_NAME_OPEN=r'<risk:name>'
t_RISK_NAME_CLOSE=r'</risk:name>'
t_RISK_OBJ_OPEN=r'<risk:objective-id>'
t_RISK_OBJ_CLOSE=r'</risk:objective-id>'
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
    '''node_risks : NODE_RISKS_OPEN node_risks
                  | risks_risk node_risks
                  | NODE_RISKS_CLOSE'''


def p_risks_risk(t):
    '''risks_risk : RISKS_RISK_OPEN risks_risk
                  |  risk_name risks_risk
                  |  risk_name risk_objective
                  | RISKS_RISK_CLOSE'''


def p_risk_name(t):
    '''risk_name : RISK_NAME_OPEN DATA RISK_NAME_CLOSE'''
    print("Risk name: ",t[2])


def p_risk_objective(t):
    '''risk_objective : RISK_OBJ_OPEN DATA RISK_OBJ_CLOSE'''
    print("Risk objective: ", t[2])


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



