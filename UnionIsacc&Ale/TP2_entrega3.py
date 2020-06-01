import ply.lex as lex
import ply.yacc as yacc
import sys

tokens=[
#DOCUMENT START AND END
    'XML_VERSION','COMMENT_OPEN','GENERAL_CLOSE','OFFICE_DOCUMENT_OPEN','OFFICE_DOCUMENT_CLOSE',
    'OFFICE_MODEL_OPEN','OFFICE_MODEL_CLOSE','MODEL_NODES_OPEN','MODEL_NODES_CLOSE','MODEL_NODE_OPEN',
    'MODEL_NODE_CLOSE',
    #BASIC INFO
    'BASIC_INFORMATION_OPEN','BASIC_INFORMATION_CLOSE','COMPONENT_NAME_OPEN','COMPONENT_NAME_CLOSE',
    'COMPONENT_OVERVIEW_OPEN','COMPONENT_OVERVIEW_CLOSE','COMPONENT_CATEGORIES_OPEN','COMPONENT_CATEGORIES_CLOSE',
    'COMPONENT_CATEGORY_OPEN','COMPONENT_CATEGORY_CLOSE','INTRINSICAL_PROPERTIES_OPEN','INTRINSICAL_PROPERTIES_CLOSE',
    'PROPERTIES_COLOR_OPEN','PROPERTIES_COLOR_CLOSE','PROPERTIES_MATERIAL_OPEN','PROPERTIES_MATERIAL_CLOSE',
    'PROPERTIES_HEIGHT_OPEN','PROPERTIES_HEIGHT_CLOSE','PROPERTIES_WEIGHT_OPEN','PROPERTIES_WEIGHT_CLOSE',
    'PROPERTIES_OTHER_OPEN','PROPERTIES_OTHER_CLOSE',
    #THREATS
    'THREATS_OPEN','THREATS_CLOSE','THREAT_OPEN','THREAT_CLOSE','THREAT_NAME_OPEN','THREAT_NAME_CLOSE',
    'THREAT_DESCRIPTION_OPEN','THREAT_DESCRIPTION_CLOSE','THREAT_VULNERABILITIES_OPEN','THREAT_VULNERABILITIES_CLOSE',
    'VULNERABILITIES_VULNERABILITY_OPEN','VULNERABILITIES_VULNERABILITY_CLOSE',
    #STRING
    'STRING',
    #SECURITY  RELATIONSHIPS
	'SECURITY_RELATIONSHIP_OPEN', 'SECURITY_RELATIONSHIP_CLOSE', 'LINKED_NODE_OPEN', 'LINKED_NODE_CLOSE',
	'NODE_ID', 'RELATIONSHIP_TYPE_OPEN','INTERACTION_ID','RELATIONSHIP_TYPE_CLOSE',
	'SECURITY_OBJECTIVES_OPEN', 'SECURITY_OBJECTIVES_CLOSE', 'SECURITY_OBJECTIVE_OPEN', 'SECURITY_OBJECTIVE_CLOSE',
	'SELF_OBJECTIVE_OPEN', 'SELF_OBJECTIVE_CLOSE', 'PEER_OBJECTIVE_OPEN', 'PEER_OBJECTIVE_CLOSE',
	#SECURITY RELATIONSHIPS && SECURITY POLICIES
	'ID',
	#SECURITY POLICIES
	'SECURITY_POLICIES_OPEN', 'SECURITY_POLICIES_CLOSE', 'SECURITY_POLICY_OPEN', 'POLICY_ID',
	'SECURITY_POLICY_CLOSE', 'POLICY_NAME_OPEN', 'POLICY_NAME_CLOSE', 'POLICY_DESCRIPTION_OPEN', 'POLICY_DESCRIPTION_CLOSE',
	'SP_OBJECTIVES_OPEN', 'SP_OBJECTIVES_CLOSE', 'SP_OBJECTIVE_OPEN', 'SP_OBJECTIVE_CLOSE',
	'SP_ADDITIONAL_INFORMATION_OPEN', 'SP_ADDITIONAL_INFORMATION_CLOSE', 'SP_COMMENT_OPEN', 'SP_COMMENT_CLOSE', 'GENERAL_COMMENT'

]
#DOCUMENT START AND END
t_XML_VERSION=r'<\?xml\sversion=".+"\sencoding=".+"\?>'
t_COMMENT_OPEN=r'<!--'
t_GENERAL_CLOSE=r'-*>'
t_OFFICE_DOCUMENT_OPEN=r'<office:document-model\soffice:version=".+">'
t_OFFICE_DOCUMENT_CLOSE=r'</office:document-model>'
t_OFFICE_MODEL_OPEN=r'<office:model>'
t_OFFICE_MODEL_CLOSE=r'</office:model>'
t_MODEL_NODES_OPEN=r'<model:nodes>'
t_MODEL_NODES_CLOSE=r'</model:nodes>'
t_MODEL_NODE_OPEN=r'<model:node\snode-id=".+">'
t_MODEL_NODE_CLOSE=r'</model:node>'
#BASIC INFO
t_BASIC_INFORMATION_OPEN=r'<node:basic-information>'
t_BASIC_INFORMATION_CLOSE=r'</node:basic-information>'
t_COMPONENT_NAME_OPEN=r'<basic-information:component-name>'
t_COMPONENT_NAME_CLOSE=r'</basic-information:component-name>'
t_COMPONENT_OVERVIEW_OPEN=r'<basic-information:component-overview>'
t_COMPONENT_OVERVIEW_CLOSE=r'</basic-information:component-overview>'
t_COMPONENT_CATEGORIES_OPEN=r'<basic-information:component-categories>'
t_COMPONENT_CATEGORIES_CLOSE=r'</basic-information:component-categories>'
t_COMPONENT_CATEGORY_OPEN=r'<component-categories:component-category\scategory-id="[a-zA-Z0-9_\s,./]*">'
t_COMPONENT_CATEGORY_CLOSE=r'</component-categories:component-category>'
t_INTRINSICAL_PROPERTIES_OPEN=r'<basic-information:component-intrinsical-properties>'
t_INTRINSICAL_PROPERTIES_CLOSE=r'</basic-information:component-intrinsical-properties>'
t_PROPERTIES_COLOR_OPEN=r'<component-intrinsical-properties:color>'
t_PROPERTIES_COLOR_CLOSE=r'</component-intrinsical-properties:color>'
t_PROPERTIES_MATERIAL_OPEN=r'<component-intrinsical-properties:material>'
t_PROPERTIES_MATERIAL_CLOSE=r'</component-intrinsical-properties:material>'
t_PROPERTIES_HEIGHT_OPEN=r'<component-intrinsical-properties:height>'
t_PROPERTIES_HEIGHT_CLOSE=r'</component-intrinsical-properties:height>'
t_PROPERTIES_WEIGHT_OPEN=r'<component-intrinsical-properties:weight>'
t_PROPERTIES_WEIGHT_CLOSE=r'</component-intrinsical-properties:weight>'
t_PROPERTIES_OTHER_OPEN=r'<basic-information:other-details>'
t_PROPERTIES_OTHER_CLOSE=r'</basic-information:other-details>'
#THREATS
t_THREATS_OPEN=r'<node:threats>'
t_THREATS_CLOSE=r'</node:threats>'
t_THREAT_OPEN=r'<threats:threat\sthreat-id=".+">'
t_THREAT_CLOSE=r'</threats:threat>'
t_THREAT_NAME_OPEN=r'<threat:name>'
t_THREAT_NAME_CLOSE=r'</threat:name>'
t_THREAT_DESCRIPTION_OPEN=r'<threat:description>'
t_THREAT_DESCRIPTION_CLOSE=r'</threat:description>'
t_THREAT_VULNERABILITIES_OPEN=r'<threat:vulnerabilities>'
t_THREAT_VULNERABILITIES_CLOSE=r'</threat:vulnerabilities>'
t_VULNERABILITIES_VULNERABILITY_OPEN=r'<vulnerabilities:vulnerability-id>'
t_VULNERABILITIES_VULNERABILITY_CLOSE=r'</vulnerabilities:vulnerability-id>'


#SECURITY RELATIONSHIPS
t_SECURITY_RELATIONSHIP_OPEN = r'<node:security-relationships>'
t_SECURITY_RELATIONSHIP_CLOSE = r'</node:security-relationships>'
t_LINKED_NODE_OPEN = r'<security-relationships:linked-node\snode-id=' 
t_LINKED_NODE_CLOSE = r'</security-relationships:linked-node>'
t_RELATIONSHIP_TYPE_OPEN = r'<linked-node:relationship-type\stype="[a-zA-Z]+"\sinteraction-id='
t_RELATIONSHIP_TYPE_CLOSE = r'</linked-node:relationship-type>'
t_SECURITY_OBJECTIVES_OPEN = r'<linked-node:security-objectives>'
t_SECURITY_OBJECTIVES_CLOSE = r'</linked-node:security-objectives>'
#SECURITY RELATIONSHIPS Y SECURITY POLICIES
t_SECURITY_OBJECTIVE_OPEN = r'<security-objectives:security-objective>'
t_SECURITY_OBJECTIVE_CLOSE = r'</security-objectives:security-objective>'
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



#SECURITY RELATIONSHIPS Y SECURITY POLICIES. 
#funciona para NODE_ID - INTERACTION_ID - POLICY_ID
t_ID = r'"[a-zA-Z-0-9]+"'


#PARA TODO
t_STRING=r'[^<>"]+'


# Ignored characters
t_ignore = " \n\t"

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


#-------------------------------inicio del documento-------------------------------
def p_doc_model(p):
    '''
    doc_model : XML_VERSION  doc_model
              | doc_comment doc_model
              | OFFICE_DOCUMENT_OPEN office_model OFFICE_DOCUMENT_CLOSE
    '''
    return

def p_office_model(p):
    '''
    office_model : OFFICE_MODEL_OPEN model_nodes OFFICE_MODEL_CLOSE
    '''
    return
def p_model_nodes(p):
    '''
    model_nodes : MODEL_NODES_OPEN model_node model_nodes
                | model_node model_nodes
                | MODEL_NODES_CLOSE
    '''
    return
def p_model_node(p):
    '''
    model_node : MODEL_NODE_OPEN model_node
               | basic_info model_node
               | threats model_node
			   | structure_security_policies model_node
			   | structure_security_relationships model_node
               | MODEL_NODE_CLOSE
    '''
    print("cierra node",p[1])
    return
#-------------------------------inicio del documento-------------------------------

#-------------------------------Basic information-------------------------------
#adentro tiene todo basic information, nombre overvier categorias propiedades y otros detalles
def p_basic_information(p):
    '''
    basic_info : BASIC_INFORMATION_OPEN basic_info
               | component_name basic_info
               | component_overview basic_info
               | component_categories basic_info
               | intrinsical_properties basic_info
               | other_details basic_info
               | BASIC_INFORMATION_CLOSE
    '''
    return
# contiene string dentro
def p_component_name(p):
    '''
    component_name : COMPONENT_NAME_OPEN str COMPONENT_NAME_CLOSE
    '''
    return
#adentro tiene intrinsical properties
def p_intrinsical_properties(p):
    '''
    intrinsical_properties : INTRINSICAL_PROPERTIES_OPEN intrinsical_properties
                           | properties_color intrinsical_properties
                           | properties_material intrinsical_properties
                           | properties_height intrinsical_properties
                           | properties_weight intrinsical_properties
                           | INTRINSICAL_PROPERTIES_CLOSE
    '''
    return
#adentro tiene component_category
def p_component_categories(p):
    '''
    component_categories : COMPONENT_CATEGORIES_OPEN component_categories
                         | component_category component_categories
                         | COMPONENT_CATEGORIES_CLOSE
    '''
    return

#contiene str dentro
def p_component_overview(p):
    '''
    component_overview : COMPONENT_OVERVIEW_OPEN str COMPONENT_OVERVIEW_CLOSE
    '''
    return
#contiene string dentro
def p_other_details(p):
    '''
    other_details : PROPERTIES_OTHER_OPEN PROPERTIES_OTHER_CLOSE
    '''
    return
#contiene string dentro
def p_component_category(p):
    '''
    component_category : COMPONENT_CATEGORY_OPEN COMPONENT_CATEGORY_CLOSE
    '''
    return
#contiene string dentro
def p_properties_color(p):
    '''
    properties_color : PROPERTIES_COLOR_OPEN str PROPERTIES_COLOR_CLOSE
    '''
    return
#contiene string dentro
def p_properties_material(p):
    '''
    properties_material : PROPERTIES_MATERIAL_OPEN str PROPERTIES_MATERIAL_CLOSE
    '''
    return
#contiene str dentro
def p_properties_height(p):
    '''
    properties_height : PROPERTIES_HEIGHT_OPEN str PROPERTIES_HEIGHT_CLOSE
    '''
    return
#contiene string dentro
def p_properties_weight(p):
    '''
    properties_weight : PROPERTIES_WEIGHT_OPEN str PROPERTIES_WEIGHT_CLOSE
    '''
    return
#-------------------------------Basic information-------------------------------


#-------------------------------Threats-------------------------------
def p_threats(p):
    '''
    threats : THREATS_OPEN threats
            | threat threats
            | THREATS_CLOSE
    '''
    return
def p_threat(p):
    '''
    threat : THREAT_OPEN threat
            | threat_name threat
            | threat_description threat
            | threat_vulnerabilities threat
            | THREAT_CLOSE
    '''
    return
def p_threat_name(p):
    '''
    threat_name : THREAT_NAME_OPEN str THREAT_NAME_CLOSE
    '''
    return
def p_threat_description(p):
    '''
    threat_description : THREAT_DESCRIPTION_OPEN str THREAT_DESCRIPTION_CLOSE
    '''
    return
def p_threat_vulnerabilities(p):
    '''
    threat_vulnerabilities : THREAT_VULNERABILITIES_OPEN threat_vulnerabilities
                           | threat_vulnerability threat_vulnerabilities
                           | THREAT_VULNERABILITIES_CLOSE
    '''
    return
def p_threat_vulnerability(p):
    '''
    threat_vulnerability : VULNERABILITIES_VULNERABILITY_OPEN str VULNERABILITIES_VULNERABILITY_CLOSE
    '''
    return
#-------------------------------Threats-------------------------------




#------------------------------Security Policies------------------------------------
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
	security_policy : SECURITY_POLICY_OPEN ID GENERAL_CLOSE POLICY_NAME_OPEN STRING POLICY_NAME_CLOSE POLICY_DESCRIPTION_OPEN STRING POLICY_DESCRIPTION_CLOSE security_objectives_SP additional_info_SP SECURITY_POLICY_CLOSE
	'''
	print(3)
	return


def p_security_objectives_SP(t):
	'''
	security_objectives_SP : SP_OBJECTIVES_OPEN SECURITY_OBJECTIVE_OPEN STRING SECURITY_OBJECTIVE_CLOSE SP_OBJECTIVES_CLOSE
	'''
	print(4)
	return

def p_additional_info_SP(t):
	'''
	additional_info_SP : SP_ADDITIONAL_INFORMATION_OPEN SP_COMMENT_OPEN SP_COMMENT_CLOSE SP_ADDITIONAL_INFORMATION_CLOSE
	'''
	print(5)
	return
#-------------------------------Security Policies-----------------------------


#------------------------------Security Relationships------------------------------

def p_structure_security_relationships(t):
	'''
	structure_security_relationships : SECURITY_RELATIONSHIP_OPEN security-relationships SECURITY_RELATIONSHIP_CLOSE
	'''
	print("1")
	return

def p_security_relationships(t):
    '''
    security-relationships : security-relationships security-relationships
                           | LINKED_NODE_OPEN ID GENERAL_CLOSE linked-node LINKED_NODE_CLOSE
    '''
    print("2")
    return

def p_expression_linked_node(t):
    '''
    linked-node : linked-node linked-node
                | RELATIONSHIP_TYPE_OPEN ID GENERAL_CLOSE relationship-type RELATIONSHIP_TYPE_CLOSE
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

#----------------------------Security Relationships-------------------------------------






#-------------------------------Otros-------------------------------
def p_doc_comment(p):
    '''
    doc_comment : COMMENT_OPEN doc_comment
                | str doc_comment
                | GENERAL_CLOSE
    '''
def p_string(p):
    '''
    str : STRING str
              | STRING
              |
    '''
    print("se capturo correctamente el string",p[1])
    return
def p_error(p):
    print("Syntax error at '%s'" % p.value)
#-------------------------------Otros-------------------------------







print("------------------INICIO DE PRUEBA DE RECONOCIMIENTO DE TOKENS------------------")
file = open('prueba.xml','r')
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

print("\n\n\n")

print("------------------INICIO DE PRUEBA DE RECONOCIMIENTO DE GRAMATICA------------------")
with open('prueba.xml','r') as myfile:
    data=myfile.read()

parser=yacc.yacc()
parser.parse(data)
print("------------------FIN DE PRUEBA DE RECONOCIMIENTO DE GRAMATICA------------------")
