import ply.lex as lex
import ply.yacc as yacc
import sys

tokens = [
	'SECURITY_RELATIONSHIP_OPEN', 'SECURITY_RELATIONSHIP_CLOSE', 'LINKED_NODE_OPEN', 'LINKED_NODE_CLOSE',
	'NODE_ID', 'END_OPEN', 'RELATIONSHIP_TYPE_OPEN','INTERACTION_ID','RELATIONSHIP_TYPE_CLOSE',
	'SECURITY_OBJECTIVES_OPEN', 'SECURITY_OBJECTIVES_CLOSE', 'SECURITY_OBJECTIVE_OPEN', 'SECURITY_OBJECTIVE_CLOSE',
	'SELF_OBJECTIVE_OPEN', 'SELF_OBJECTIVE_CLOSE', 'PEER_OBJECTIVE_OPEN', 'PEER_OBJECTIVE_CLOSE',
	'END_OF_LINE', 'TAB'
]

t_SECURITY_RELATIONSHIP_OPEN = r'<node:security-relationships>'
t_SECURITY_RELATIONSHIP_CLOSE = r'</node:security-relationships>'			#aun no la pruebo. 
t_LINKED_NODE_OPEN = r'<security-relationships:linked-node\snode-id=' 
t_LINKED_NODE_CLOSE = r'</security-relationships:linked-node>'
t_RELATIONSHIP_TYPE_OPEN = r'<linked-node:relationship-type\stype="[a-zA-Z]+"\sinteraction-id='
t_RELATIONSHIP_TYPE_CLOSE = r'</linked-node:relationship-type>'				#aun no la pruebo. 
t_SECURITY_OBJECTIVES_OPEN = r'<linked-node:security-objectives>'
t_SECURITY_OBJECTIVES_CLOSE = r'</linked-node:security-objectives>'
t_SECURITY_OBJECTIVE_OPEN = r'<security-objectives:security-objective>'
t_SECURITY_OBJECTIVE_CLOSE = r'</security-objectives:security-objective>'
t_SELF_OBJECTIVE_OPEN = r'<security-objective:self-objective\sobjective-id="DO\[\d\]\[\d\]">'
t_SELF_OBJECTIVE_CLOSE = r'</security-objective:self-objective>'
t_PEER_OBJECTIVE_OPEN = r'<security-objective:peer-objective\speer-objective-id="IO\[\d\]\[\d\]">'
t_PEER_OBJECTIVE_CLOSE = r'</security-objective:peer-objective>'

t_INTERACTION_ID = r'"\w+\d+"'
t_NODE_ID = r'"[a-zA-Z-]+"'
t_END_OPEN = r'>'
t_END_OF_LINE = r'\n'
t_TAB = r'\t+'
#t_ESPACE = r'\s+'


def p_expression_security_objective(t):
    '''
    security-objective : SELF_OBJECTIVE_OPEN SELF_OBJECTIVE_CLOSE
                       | PEER_OBJECTIVE_OPEN PEER_OBJECTIVE_CLOSE
    '''
    return

def p_expression_security_objectives(t):
    '''
    security-objectives : security-objectives END_OF_LINE security-objectives
                        | SECURITY_OBJECTIVE_OPEN END_OF_LINE security-objective END_OF_LINE security-objective END_OF_LINE SECURITY_OBJECTIVE_CLOSE
    '''
    return

def p_expression_relationship_type(t):
    '''
    relationship-type : SECURITY_OBJECTIVES_OPEN END_OF_LINE security-objectives END_OF_LINE SECURITY_OBJECTIVES_CLOSE
    '''
    return

def p_expression_linked_node(t):
    '''
    linked-node : linked-node END_OF_LINE linked-node
                | RELATIONSHIP_TYPE_OPEN INTERACTION_ID END_OPEN END_OF_LINE relationship-type END_OF_LINE RELATIONSHIP_TYPE_CLOSE
    '''
    return

def p_security_relationships(p):
    '''
    security-relationships : security-relationships END_OF_LINE security-relationships
                           | LINKED_NODE_OPEN NODE_ID END_OPEN END_OF_LINE linked-node END_OF_LINE LINKED_NODE_CLOSE
    '''
    return


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    return


file = open('pruebaIsacc.xml','r')
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
