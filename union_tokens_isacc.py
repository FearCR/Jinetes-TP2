import ply.lex as lex
import ply.yacc as yacc
import sys

tokens = [
	#SECURITY  RELATIONSHIPS
	'SECURITY_RELATIONSHIP_OPEN', 'SECURITY_RELATIONSHIP_CLOSE', 'LINKED_NODE_OPEN', 'LINKED_NODE_CLOSE',
	'NODE_ID', 'RELATIONSHIP_TYPE_OPEN','INTERACTION_ID','RELATIONSHIP_TYPE_CLOSE',
	'SECURITY_OBJECTIVES_OPEN', 'SECURITY_OBJECTIVES_CLOSE', 'SECURITY_OBJECTIVE_OPEN', 'SECURITY_OBJECTIVE_CLOSE',
	'SELF_OBJECTIVE_OPEN', 'SELF_OBJECTIVE_CLOSE', 'PEER_OBJECTIVE_OPEN', 'PEER_OBJECTIVE_CLOSE',
	#AMBOS
	'END_OPEN', 'ID',
	#SECURITY POLICIES
	'SECURITY_POLICIES_OPEN', 'SECURITY_POLICIES_CLOSE', 'SECURITY_POLICY_OPEN', 'POLICY_ID',
	'SECURITY_POLICY_CLOSE', 'POLICY_NAME_OPEN', 'POLICY_NAME_CLOSE', 'POLICY_DESCRIPTION_OPEN', 'POLICY_DESCRIPTION_CLOSE',
	'SP_OBJECTIVES_OPEN', 'SP_OBJECTIVES_CLOSE', 'SP_OBJECTIVE_OPEN', 'SP_OBJECTIVE_CLOSE',
	'SP_ADDITIONAL_INFORMATION_OPEN', 'SP_ADDITIONAL_INFORMATION_CLOSE', 'SP_COMMENT_OPEN', 'SP_COMMENT_CLOSE', 'GENERAL_COMMENT'
	
]
#SECURITY RELATIONSHIPS
t_SECURITY_RELATIONSHIP_OPEN = r'<node:security-relationships>'
t_SECURITY_RELATIONSHIP_CLOSE = r'</node:security-relationships>'
t_LINKED_NODE_OPEN = r'<security-relationships:linked-node\snode-id=' 
t_LINKED_NODE_CLOSE = r'</security-relationships:linked-node>'
t_RELATIONSHIP_TYPE_OPEN = r'<linked-node:relationship-type\stype="[a-zA-Z]+"\sinteraction-id='
t_RELATIONSHIP_TYPE_CLOSE = r'</linked-node:relationship-type>'
t_SECURITY_OBJECTIVES_OPEN = r'<linked-node:security-objectives>'
t_SECURITY_OBJECTIVES_CLOSE = r'</linked-node:security-objectives>'
#AMBOS
t_SECURITY_OBJECTIVE_OPEN = r'<security-objectives:security-objective>'
t_SECURITY_OBJECTIVE_CLOSE = r'</security-objectives:security-objective>'
#
#SECURITY RELATIONSHIPS
t_SELF_OBJECTIVE_OPEN = r'<security-objective:self-objective\sobjective-id="DO\[\d\]\[\d\]">'
t_SELF_OBJECTIVE_CLOSE = r'</security-objective:self-objective>'
t_PEER_OBJECTIVE_OPEN = r'(<security-objective:peer-objective\speer-objective-id="[DI]O\[\d\]\[\d\]"> | <security-objective:peer-objective\sobjective-id="[DI]O\[\d\]\[\d\]">)'
t_PEER_OBJECTIVE_CLOSE = r'</security-objective:peer-objective>'


#SECURITY POLICIES
t_SECURITY_POLICIES_OPEN = r'<node:security-policies>'
t_SECURITY_POLICIES_CLOSE = r'</node:security-policies>'
t_SECURITY_POLICY_OPEN = r'<security-policies:security-policy\spolicy-id='
t_SECURITY_POLICY_CLOSE = r'</security-policies:security-policy>'
t_POLICY_NAME_OPEN = r'<security-policy:name>'
t_POLICY_NAME_CLOSE = r'</security-policy:name>'
t_POLICY_DESCRIPTION_OPEN = r'<security-policy:description>'
t_POLICY_DESCRIPTION_CLOSE = r'</security-policy:description>'
t_SP_OBJECTIVES_OPEN = r'(<security-policy:security-objectives>|<security-policies:security-objectives>)'
t_SP_OBJECTIVES_CLOSE = r'(</security-policy:security-objectives>|</security-policies:security-objectives>)'
t_SP_ADDITIONAL_INFORMATION_OPEN = r'<security-policy:additional-information>'
t_SP_ADDITIONAL_INFORMATION_CLOSE = r'</security-policy:additional-information>'
t_SP_COMMENT_OPEN = r'<additional-information:comment>'
t_SP_COMMENT_CLOSE = r'</additional-information:comment>'

#AMBOS
t_END_OPEN = r'>'
#AMBOS, funciona para NODE_ID - INTERACTION_ID - POLICY_ID  #t_NODE_ID = r'"[a-zA-Z-1-9]+"'  #t_INTERACTION_ID = r'"\w+\d+"'  #t_POLICY_ID = r'"(\w |-)+"'
t_ID = r'"[a-zA-Z-0-9]+"'
#SECURITY POLICIES
t_GENERAL_COMMENT = r'(\w|\s|\(|\)|,|-|/|\[|\])+'		
#AMBOS
t_ignore = " \n\t"



#PARA QUE RECONOZCA AMBAS GRAMATICAS, de momento una o la otra, aunque al final son todas. 
def p_all_structure(t):
	'''
	all_structures : structure_security_relationships
				   | structure_security_policies
	'''
	print(9)
	return


#GRAMATICA SECURITY POLICIES. 
def p_structure_security_policies(t):
	'''
	structure_security_policies : SECURITY_POLICIES_OPEN security_policies SECURITY_POLICIES_CLOSE
	'''
	print(1)
	return

def p_security_policies(t):
	'''
	security_policies : security_policies security_policies
					  | security_policy
	'''
	print(2)
	return

def p_security_policy(t):
	'''
	security_policy : SECURITY_POLICY_OPEN ID END_OPEN POLICY_NAME_OPEN GENERAL_COMMENT POLICY_NAME_CLOSE POLICY_DESCRIPTION_OPEN GENERAL_COMMENT POLICY_DESCRIPTION_CLOSE security_objectives_SP additional_info_SP SECURITY_POLICY_CLOSE
	'''
	print(3)
	return


def p_security_objectives_SP(t):
	'''
	security_objectives_SP : SP_OBJECTIVES_OPEN SECURITY_OBJECTIVE_OPEN GENERAL_COMMENT SECURITY_OBJECTIVE_CLOSE SP_OBJECTIVES_CLOSE
	'''
	print(4)
	return

def p_additional_info_SP(t):
	'''
	additional_info_SP : SP_ADDITIONAL_INFORMATION_OPEN SP_COMMENT_OPEN SP_COMMENT_CLOSE SP_ADDITIONAL_INFORMATION_CLOSE
	'''
	print(5)
	return


#GRAMATICA SECURITY RELATIONSHIPS. 

def p_structure_security_relationships(t):
	'''
	structure_security_relationships : SECURITY_RELATIONSHIP_OPEN security-relationships SECURITY_RELATIONSHIP_CLOSE
	'''
	print("1")
	return

def p_security_relationships(t):
    '''
    security-relationships : security-relationships security-relationships
                           | LINKED_NODE_OPEN ID END_OPEN linked-node LINKED_NODE_CLOSE
    '''
    print("2")
    return

def p_expression_linked_node(t):
    '''
    linked-node : linked-node linked-node
                | RELATIONSHIP_TYPE_OPEN ID END_OPEN relationship-type RELATIONSHIP_TYPE_CLOSE
    '''
    print("3")
    return


def p_expression_relationship_type(t):
    '''
    relationship-type : SECURITY_OBJECTIVES_OPEN security-objectives_SR SECURITY_OBJECTIVES_CLOSE
    '''
    print("4")
    return


def p_expression_security_objectives_SR(t):
    '''
    security-objectives_SR : security-objectives_SR security-objectives_SR
						   | SECURITY_OBJECTIVE_OPEN security-objective_SR security-objective_SR SECURITY_OBJECTIVE_CLOSE
    '''
    print("5")
    return

def p_expression_security_objective_SR(t):
    '''
    security-objective_SR : SELF_OBJECTIVE_OPEN SELF_OBJECTIVE_CLOSE
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
#file = open('pruebaIsacc2.xml','r')
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
#with open('pruebaIsacc2.xml','r') as myfile:	
    data=myfile.read()
    #print(data)
parser=yacc.yacc()
parser.parse(data)
print("------------------FIN DE PRUEBA DE RECONOCIMIENTO DE GRAMATICA------------------")

