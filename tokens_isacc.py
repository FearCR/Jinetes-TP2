
                #AÚN NO ESTA COMPILADO, faltan cosas. 

tokens = {
    'SECURITY_RELATIONSHIP_OPEN', 'SECURITY_RELATIONSHIP_CLOSE', 'LINKED_NODE_OPEN', 'LINKED_NODE_CLOSE',  
    'RELATIONSHIP_TYPE_OPEN', 'RELATIONSHIP_TYPE_CLOSE', 'SECURITY_OBJECTIVES_OPEN',
    'SECURITY_OBJECTIVES_CLOSE', 'SECURITY_OBJECTIVE_OPEN', 'SECURITY_OBJECTIVE_CLOSE', 
    'SELF_OBJECTIVE_OPEN', 'SELF_OBJECTIVE_CLOSE', 'PEER_OBJECTIVE_OPEN', 'PEER_OBJECTIVE_CLOSE', 'END_OF_LINE'
}

#puede que existan algunos que se tengan que dividir en mas tokens, como la linea 14, 16, 22, etc, depende si nos interesa esa info
t_SECURITY_RELATIONSHIP_OPEN = r'<node:security-relationships>'
t_SECURITY_RELATIONSHIP_CLOSE = r'<\/node:security-relationships>'
t_LINKED_NODE_OPEN = r'<security-relationships:linked-node\snode-id="Cup2">'                             #falta expresion regular para el node-id 
t_LINKED_NODE_CLOSE = r'<\/security-relationships:linked-node>'
t_RELATIONSHIP_TYPE_OPEN = r'<linked-node:relationship-type\stype="Interaction"\sinteraction-id="Cu01">'  #falta expression regular para type e interacion-id
t_RELATIONSHIP_TYPE_CLOSE = r'<\/linked-node:relationship-type>'
t_SECURITY_OBJECTIVES_OPEN = r'<linked-node:security-objectives>'
t_SECURITY_OBJECTIVES_CLOSE = r'<\/linked-node:security-objectives>'
t_SECURITY_OBJECTIVE_OPEN = r'<security-objectives:security-objective>'
t_SECURITY_OBJECTIVE_CLOSE = r'<\/security-objectives:security-objective>'
t_SELF_OBJECTIVE_OPEN = r'<security-objective:self-objective\sobjective-id="DO[0][1]">'    #falta expresion regular para los D[J]
t_SELF_OBJECTIVE_CLOSE = r'<\/security-objective:self-objective>'
t_PEER_OBJECTIVE_OPEN = r'<security-objective:peer-objective\sobjective-id="DO[1][2]">'    #falta expresion regular para los D[J] 
t_PEER_OBJECTIVE_CLOSE = r'<\/security-objective:peer-objective>'
t_END_OF_LINE = r'\\n'


def p_expression_security_objective(t): #token adicional
    '''
    security-objective : SELF_OBJECTIVE_OPEN SELF_OBJECTIVE_CLOSE
                       | PEER_OBJECTIVE_OPEN PEER_OBJECTIVE_CLOSE
    '''
    return

def p_expression_security_objectives(t):    #token adicional
    '''
    security-objectives : security-objectives END_OF_LINE security-objectives
                        | SECURITY_OBJECTIVE_OPEN END_OF_LINE security-objective END_OF_LINE security-objective END_OF_LINE SECURITY_OBJECTIVE_CLOSE
    '''
    return

def p_expression_relationship_type(t):  #token adicional
    '''
    relationship-type : SECURITY_OBJECTIVES_OPEN END_OF_LINE security-objectives END_OF_LINE SECURITY_OBJECTIVES_CLOSE
    '''
    return

def p_expression_linked_node(t):    #token adicional
    '''
    linked-node : linked-node END_OF_LINE linked-node
                | RELATIONSHIP_TYPE_OPEN END_OF_LINE relationship-type END_OF_LINE RELATIONSHIP_TYPE_CLOSE
    '''
    return

def p_security_relationships(p): #token adicional.
    '''
    security-relationships : security-relationships END_OF_LINE security-relationships
                           | LINKED_NODE_OPEN END_OF_LINE linked-node END_OF_LINE LINKED_NODE_CLOSE
    '''
    return