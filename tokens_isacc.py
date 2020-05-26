import ply.lex as lex
import ply.yacc as yacc
import sys

tokens = [
	'SECURITY_RELATIONSHIP_OPEN', 'SECURITY_RELATIONSHIP_CLOSE', 'LINKED_NODE_OPEN', 'LINKED_NODE_CLOSE',
	'NODE_ID', 'END_OPEN', 'RELATIONSHIP_TYPE_OPEN','INTERACTION_ID','RELATIONSHIP_TYPE_CLOSE',
	'SECURITY_OBJECTIVES_OPEN', 'SECURITY_OBJECTIVES_CLOSE', 'SECURITY_OBJECTIVE_OPEN', 'SECURITY_OBJECTIVE_CLOSE',
	'SELF_OBJECTIVE_OPEN', 'SELF_OBJECTIVE_CLOSE', 'PEER_OBJECTIVE_OPEN', 'PEER_OBJECTIVE_CLOSE'
]

t_SECURITY_RELATIONSHIP_OPEN = r'<node:security-relationships>'
t_SECURITY_RELATIONSHIP_CLOSE = r'</node:security-relationships>'
t_LINKED_NODE_OPEN = r'<security-relationships:linked-node\snode-id=' 
t_LINKED_NODE_CLOSE = r'</security-relationships:linked-node>'
t_RELATIONSHIP_TYPE_OPEN = r'<linked-node:relationship-type\stype="[a-zA-Z]+"\sinteraction-id='
t_RELATIONSHIP_TYPE_CLOSE = r'</linked-node:relationship-type>'
t_SECURITY_OBJECTIVES_OPEN = r'<linked-node:security-objectives>'
t_SECURITY_OBJECTIVES_CLOSE = r'</linked-node:security-objectives>'
t_SECURITY_OBJECTIVE_OPEN = r'<security-objectives:security-objective>'
t_SECURITY_OBJECTIVE_CLOSE = r'</security-objectives:security-objective>'
t_SELF_OBJECTIVE_OPEN = r'<security-objective:self-objective\sobjective-id="DO\[\d\]\[\d\]">'
t_SELF_OBJECTIVE_CLOSE = r'</security-objective:self-objective>'
t_PEER_OBJECTIVE_OPEN = r'(<security-objective:peer-objective\speer-objective-id="[DI]O\[\d\]\[\d\]"> | <security-objective:peer-objective\sobjective-id="[DI]O\[\d\]\[\d\]">)'
t_PEER_OBJECTIVE_CLOSE = r'</security-objective:peer-objective>'

t_INTERACTION_ID = r'"\w+\d+"'
t_NODE_ID = r'"[a-zA-Z-]+"'
t_END_OPEN = r'>'
t_ignore = " \n\t"


def p_structure_security_relationships(t):
	'''
	structure_security_relationships : SECURITY_RELATIONSHIP_OPEN security-relationships SECURITY_RELATIONSHIP_CLOSE
	'''
	print("1")
	return

def p_security_relationships(t):
    '''
    security-relationships : security-relationships security-relationships
                           | LINKED_NODE_OPEN NODE_ID END_OPEN  linked-node LINKED_NODE_CLOSE
    '''
    print("2")
    return

def p_expression_linked_node(t):
    '''
    linked-node : linked-node linked-node
                | RELATIONSHIP_TYPE_OPEN INTERACTION_ID END_OPEN relationship-type RELATIONSHIP_TYPE_CLOSE
    '''
    print("3")
    return


def p_expression_relationship_type(t):
    '''
    relationship-type : SECURITY_OBJECTIVES_OPEN security-objectives SECURITY_OBJECTIVES_CLOSE
    '''
    print("4")
    return


def p_expression_security_objectives(t):
    '''
    security-objectives : security-objectives security-objectives
                        | SECURITY_OBJECTIVE_OPEN security-objective security-objective SECURITY_OBJECTIVE_CLOSE
    '''
    print("5")
    return

def p_expression_security_objective(t):
    '''
    security-objective : SELF_OBJECTIVE_OPEN SELF_OBJECTIVE_CLOSE
                       | PEER_OBJECTIVE_OPEN PEER_OBJECTIVE_CLOSE
    '''
    print("6")
    return

def p_error(p):
	print("Syntax error")
	return

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    return


file = open('pruebaIsacc.xml','r')
count = 0
print("------------------INICIO DE PRUEBA DE RECONOCIMIENTO DE TOKENS------------------")
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

print("------------------INICIO DE PRUEBA DE RECONOCIMIENTO DE GRAMATICA------------------")
with open('pruebaIsacc.xml','r') as myfile:
    data=myfile.read()
    #print(data)
parser=yacc.yacc()
parser.parse(data)
print("------------------FIN DE PRUEBA DE RECONOCIMIENTO DE GRAMATICA------------------")
