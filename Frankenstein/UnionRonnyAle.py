import ply.lex as lex
import ply.yacc as yacc
import sys

tokens = [
    # DOCUMENT START AND END
    'XML_VERSION', 'COMMENT_OPEN', 'COMMENT_CLOSE', 'OFFICE_DOCUMENT_OPEN', 'OFFICE_DOCUMENT_CLOSE',
    'OFFICE_MODEL_OPEN', 'OFFICE_MODEL_CLOSE', 'MODEL_NODES_OPEN', 'MODEL_NODES_CLOSE', 'MODEL_NODE_OPEN',
    'MODEL_NODE_CLOSE',
    # BASIC INFO
    'BASIC_INFORMATION_OPEN', 'BASIC_INFORMATION_CLOSE', 'COMPONENT_NAME_OPEN', 'COMPONENT_NAME_CLOSE',
    'COMPONENT_OVERVIEW_OPEN', 'COMPONENT_OVERVIEW_CLOSE', 'COMPONENT_CATEGORIES_OPEN', 'COMPONENT_CATEGORIES_CLOSE',
    'COMPONENT_CATEGORY_OPEN', 'COMPONENT_CATEGORY_CLOSE', 'INTRINSICAL_PROPERTIES_OPEN',
    'INTRINSICAL_PROPERTIES_CLOSE',
    'PROPERTIES_COLOR_OPEN', 'PROPERTIES_COLOR_CLOSE', 'PROPERTIES_MATERIAL_OPEN', 'PROPERTIES_MATERIAL_CLOSE',
    'PROPERTIES_HEIGHT_OPEN', 'PROPERTIES_HEIGHT_CLOSE', 'PROPERTIES_WEIGHT_OPEN', 'PROPERTIES_WEIGHT_CLOSE',
    'PROPERTIES_OTHER_OPEN', 'PROPERTIES_OTHER_CLOSE',
    # SECURITY OBJECTIVES
    'NODE_SECUOBJ_OPEN', 'NODE_SECUOBJ_CLOSE', 'SECUOBJ_OBJ_OPEN', 'SECUOBJ_OBJ_CLOSE',
    'SECUOBJ_NAME_OPEN', 'SECUOBJ_NAME_CLOSE', 'SECUOBJ_DESCRIP_OPEN', 'SECUOBJ_DESCRIP_CLOSE',
    'SECUOBJ_OBJTYPE_OPEN', 'SECUOBJ_OBJTYPE_CLOSE', 'SECUOBJ_SECUSERV_OPEN', 'SECUOBJ_SECUSERV_CLOSE',
    'SECUOBJ_TEMP_OPEN', 'SECUOBJ_TEMP_CLOSE', 'SECUOBJ_ADDINFO_OPEN',
    'SECUOBJ_ADDINFO_CLOSE', 'SECUOBJ_OBJSOUR_OPEN', 'SECUOBJ_OBJSOUR_CLOSE',
    # THREATS
    'THREATS_OPEN', 'THREATS_CLOSE', 'THREAT_OPEN', 'THREAT_CLOSE', 'THREAT_NAME_OPEN', 'THREAT_NAME_CLOSE',
    'THREAT_DESCRIPTION_OPEN', 'THREAT_DESCRIPTION_CLOSE', 'THREAT_VULNERABILITIES_OPEN',
    'THREAT_VULNERABILITIES_CLOSE',
    'VULNERABILITIES_VULNERABILITY_OPEN', 'VULNERABILITIES_VULNERABILITY_CLOSE',
    # STRING
    'STRING',
    #RISK 
    'NODE_RISKS_OPEN', 'NODE_RISKS_CLOSE', 'RISKS_RISK_OPEN', 'RISKS_RISK_CLOSE', 'RISK_NAME_OPEN',
    'RISK_NAME_CLOSE', 'RISK_OBJ_OPEN', 'RISK_OBJ_CLOSE', 'RISK_VUL_OPEN', 'RISK_VUL_CLOSE',
    'RISK_THREAT_OPEN', 'RISK_THREAT_CLOSE', 'RISK_DESCRIPTION_OPEN', 'RISK_DESCRIPTION_CLOSE',
    'RISK_LIKHD_OPEN', 'RISK_LIKHD_CLOSE', 'RISK_IMPACT_OPEN', 'RISK_IMPACT_CLOSE',
    'RISK_TEMP_OPEN', 'RISK_TEMP_CLOSE', 'RISK_ADDINFO_OPEN', 'RISK_ADDINFO_CLOSE',

    'ADDINFOCOMM_OPEN','ADDINFOCOMM_CLOSE'


]
# DOCUMENT START AND END
t_XML_VERSION = r'<\?xml\sversion=".+"\sencoding=".+"\?>'
t_COMMENT_OPEN = r'<!--'
t_COMMENT_CLOSE = r'-*>'
t_OFFICE_DOCUMENT_OPEN = r'<office:document-model\soffice:version=".+">'
t_OFFICE_DOCUMENT_CLOSE = r'</office:document-model>'
t_OFFICE_MODEL_OPEN = r'<office:model>'
t_OFFICE_MODEL_CLOSE = r'</office:model>'
t_MODEL_NODES_OPEN = r'<model:nodes>'
t_MODEL_NODES_CLOSE = r'</model:nodes>'
t_MODEL_NODE_OPEN = r'<model:node\snode-id=".+">'
t_MODEL_NODE_CLOSE = r'</model:node>'
# BASIC INFO
t_BASIC_INFORMATION_OPEN = r'<node:basic-information>'
t_BASIC_INFORMATION_CLOSE = r'</node:basic-information>'
t_COMPONENT_NAME_OPEN = r'<basic-information:component-name>'
t_COMPONENT_NAME_CLOSE = r'</basic-information:component-name>'
t_COMPONENT_OVERVIEW_OPEN = r'<basic-information:component-overview>'
t_COMPONENT_OVERVIEW_CLOSE = r'</basic-information:component-overview>'
t_COMPONENT_CATEGORIES_OPEN = r'<basic-information:component-categories>'
t_COMPONENT_CATEGORIES_CLOSE = r'</basic-information:component-categories>'
t_COMPONENT_CATEGORY_OPEN = r'<component-categories:component-category\scategory-id="[a-zA-Z0-9_\s,./]*">'
t_COMPONENT_CATEGORY_CLOSE = r'</component-categories:component-category>'
t_INTRINSICAL_PROPERTIES_OPEN = r'<basic-information:component-intrinsical-properties>'
t_INTRINSICAL_PROPERTIES_CLOSE = r'</basic-information:component-intrinsical-properties>'
t_PROPERTIES_COLOR_OPEN = r'<component-intrinsical-properties:color>'
t_PROPERTIES_COLOR_CLOSE = r'</component-intrinsical-properties:color>'
t_PROPERTIES_MATERIAL_OPEN = r'<component-intrinsical-properties:material>'
t_PROPERTIES_MATERIAL_CLOSE = r'</component-intrinsical-properties:material>'
t_PROPERTIES_HEIGHT_OPEN = r'<component-intrinsical-properties:height>'
t_PROPERTIES_HEIGHT_CLOSE = r'</component-intrinsical-properties:height>'
t_PROPERTIES_WEIGHT_OPEN = r'<component-intrinsical-properties:weight>'
t_PROPERTIES_WEIGHT_CLOSE = r'</component-intrinsical-properties:weight>'
t_PROPERTIES_OTHER_OPEN = r'<basic-information:other-details>'
t_PROPERTIES_OTHER_CLOSE = r'</basic-information:other-details>'
# THREATS
t_THREATS_OPEN = r'<node:threats>'
t_THREATS_CLOSE = r'</node:threats>'
t_THREAT_OPEN = r'<threats:threat\sthreat-id=".+">'
t_THREAT_CLOSE = r'</threats:threat>'
t_THREAT_NAME_OPEN = r'<threat:name>'
t_THREAT_NAME_CLOSE = r'</threat:name>'
t_THREAT_DESCRIPTION_OPEN = r'<threat:description>'
t_THREAT_DESCRIPTION_CLOSE = r'</threat:description>'
t_THREAT_VULNERABILITIES_OPEN = r'<threat:vulnerabilities>'
t_THREAT_VULNERABILITIES_CLOSE = r'</threat:vulnerabilities>'
t_VULNERABILITIES_VULNERABILITY_OPEN = r'<vulnerabilities:vulnerability-id>'
t_VULNERABILITIES_VULNERABILITY_CLOSE = r'</vulnerabilities:vulnerability-id>'
#RISK
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

#SECURITY OBJECTIVES
t_NODE_SECUOBJ_OPEN=r'<node:security-objectives>'
t_NODE_SECUOBJ_CLOSE=r'</node:security-objectives>'
t_SECUOBJ_OBJ_OPEN=r'<security-objectives:security-objective\sobjective-id="\w\w\[\d]\[\d]">'
t_SECUOBJ_OBJ_CLOSE=r'</security-objectives:security-objective>'
t_SECUOBJ_NAME_OPEN = r'<security-objective:name>'
t_SECUOBJ_NAME_CLOSE = r'</security-objective:name>'
t_SECUOBJ_DESCRIP_OPEN=r'<security-objective:description>'
t_SECUOBJ_DESCRIP_CLOSE=r'</security-objective:description>'
t_SECUOBJ_OBJTYPE_OPEN=r'<security-objective:objective-type>'
t_SECUOBJ_OBJTYPE_CLOSE=r'</security-objective:objective-type>'
t_SECUOBJ_SECUSERV_OPEN=r'<security-objective:security-service>'
t_SECUOBJ_SECUSERV_CLOSE=r'</security-objective:security-service>'
t_SECUOBJ_TEMP_OPEN=r'<security-objective:temporality>'
t_SECUOBJ_TEMP_CLOSE=r'</security-objective:temporality>'
t_SECUOBJ_ADDINFO_OPEN=r'<security-objective:additional-information>'
t_SECUOBJ_ADDINFO_CLOSE=r'</security-objective:additional-information>'
t_SECUOBJ_OBJSOUR_OPEN=r'<security-objective:objective-source>'
t_SECUOBJ_OBJSOUR_CLOSE=r'</security-objective:objective-source>'


t_ADDINFOCOMM_OPEN=r'<additional-information:comment>'
t_ADDINFOCOMM_CLOSE=r'</additional-information:comment>'


t_STRING = r'[^<>]+'

# Ignored characters
t_ignore = " \n\t"


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# -------------------------------inicio del documento-------------------------------
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
               | node_security_objective model_node
               | threats model_node
               | node_risks model_node
               | MODEL_NODE_CLOSE
    '''
    print("cierra node", p[1])
    return


# -------------------------------inicio del documento-------------------------------

# -------------------------------Basic information-------------------------------
# adentro tiene todo basic information, nombre overvier categorias propiedades y otros detalles
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


# adentro tiene intrinsical properties
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


# adentro tiene component_category
def p_component_categories(p):
    '''
    component_categories : COMPONENT_CATEGORIES_OPEN component_categories
                         | component_category component_categories
                         | COMPONENT_CATEGORIES_CLOSE
    '''
    return


# contiene str dentro
def p_component_overview(p):
    '''
    component_overview : COMPONENT_OVERVIEW_OPEN str COMPONENT_OVERVIEW_CLOSE
    '''
    p[0] = p[2]
    return


# contiene string dentro
def p_other_details(p):
    '''
    other_details : PROPERTIES_OTHER_OPEN PROPERTIES_OTHER_CLOSE
    '''
    return


# contiene string dentro
def p_component_category(p):
    '''
    component_category : COMPONENT_CATEGORY_OPEN COMPONENT_CATEGORY_CLOSE
    '''

    return


# contiene string dentro
def p_properties_color(p):
    '''
    properties_color : PROPERTIES_COLOR_OPEN str PROPERTIES_COLOR_CLOSE
    '''
    p[0] = p[2]
    return


# contiene string dentro
def p_properties_material(p):
    '''
    properties_material : PROPERTIES_MATERIAL_OPEN str PROPERTIES_MATERIAL_CLOSE
    '''
    p[0] = p[2]
    return


# contiene str dentro
def p_properties_height(p):
    '''
    properties_height : PROPERTIES_HEIGHT_OPEN str PROPERTIES_HEIGHT_CLOSE
    '''
    p[0] = p[2]
    return


# contiene string dentro
def p_properties_weight(p):
    '''
    properties_weight : PROPERTIES_WEIGHT_OPEN str PROPERTIES_WEIGHT_CLOSE
    '''
    p[0] = p[2]
    return


# -------------------------------Basic information-------------------------------
#-------------------------------SECURITY OBJECTIVES-------------------------------
def p_node_security_objective(t):
    '''node_security_objective : NODE_SECUOBJ_OPEN node_security_objective
                                   | security_objective_obj node_security_objective
                                   | NODE_SECUOBJ_CLOSE '''

def p_security_objective_obj(t):
    #'security_objective_obj : SECUOBJ_OBJ_OPEN security_objective_name security_objective_description SECUOBJ_OBJ_CLOSE'

    '''security_objective_obj : SECUOBJ_OBJ_OPEN security_objective_obj
                              | security_objective_name security_objective_obj
                              | security_objective_description security_objective_obj
                              | security_objective_objective_type security_objective_obj
                              | security_objective_security_service security_objective_obj
                              | security_objective_temporality security_objective_obj
                              | security_objective_additional_information security_objective_obj
                              | security_objective_source security_objective_obj
                              | SECUOBJ_OBJ_CLOSE'''

def p_security_objective_name(t):
    'security_objective_name : SECUOBJ_NAME_OPEN str SECUOBJ_NAME_CLOSE'



def p_security_objective_description(t):
    'security_objective_description : SECUOBJ_DESCRIP_OPEN str SECUOBJ_DESCRIP_CLOSE'




def p_security_objective_objective_type(t):
    'security_objective_objective_type : SECUOBJ_OBJTYPE_OPEN str SECUOBJ_OBJTYPE_CLOSE'



def p_security_objective_security_service(t):
    'security_objective_security_service : SECUOBJ_SECUSERV_OPEN str SECUOBJ_SECUSERV_CLOSE'



def p_security_objective_temporality(t):
    'security_objective_temporality : SECUOBJ_TEMP_OPEN str SECUOBJ_TEMP_CLOSE'



def p_security_objective_additional_information(t):
    'security_objective_additional_information : SECUOBJ_ADDINFO_OPEN additional_information_Comment SECUOBJ_ADDINFO_CLOSE'


def p_security_objective_source(t):
    'security_objective_source : SECUOBJ_OBJSOUR_OPEN str SECUOBJ_OBJSOUR_CLOSE'


#-------------------------------SECURITY OBJECTIVES-------------------------------

# -------------------------------Threats-------------------------------
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


# -------------------------------Threats-------------------------------

# -------------------------------RISK-------------------------------
def p_node_risks(t):
    '''
    node_risks : NODE_RISKS_OPEN node_risks
               | risks_risk node_risks
               | NODE_RISKS_CLOSE
                  '''


def p_risks_risk(t):
    '''
    risks_risk : RISKS_RISK_OPEN risks_risk
                | risk_name risks_risk
                | risk_objective risks_risk
                | risk_vulnerability risks_risk
                | risk_threat risks_risk
                | risk_description risks_risk
                | risk_likelihood risks_risk
                | risk_impact risks_risk
                | risk_temporality risks_risk
                | risk_additional_information risks_risk
                | RISKS_RISK_CLOSE
                  '''


def p_risk_name(t):
    '''
    risk_name : RISK_NAME_OPEN risk_name
              | str risk_name
              | RISK_NAME_CLOSE
    '''



def p_risk_objective(t):
    '''
    risk_objective : RISK_OBJ_OPEN str RISK_OBJ_CLOSE
    '''


def p_risk_vulnerability(t):
    '''
    risk_vulnerability : RISK_VUL_OPEN str RISK_VUL_CLOSE
    '''



def p_risk_threat(t):
    '''
    risk_threat : RISK_THREAT_OPEN str RISK_THREAT_CLOSE
    '''



def p_risk_description(t):
    '''
    risk_description : RISK_DESCRIPTION_OPEN str RISK_DESCRIPTION_CLOSE
    '''


def p_risk_likelihood(t):
    '''
    risk_likelihood : RISK_LIKHD_OPEN str RISK_LIKHD_CLOSE
    '''



def p_risk_impact(t):
    '''
    risk_impact : RISK_IMPACT_OPEN str RISK_IMPACT_CLOSE
    '''


def p_risk_temporality(t):
    '''
    risk_temporality : RISK_TEMP_OPEN str RISK_TEMP_CLOSE
    '''


def p_risk_additional_information(t):
    '''
    risk_additional_information : RISK_ADDINFO_OPEN additional_information_Comment RISK_ADDINFO_CLOSE
    '''


# -------------------------------RISK-------------------------------
def p_additional_information_Comment(t):
    'additional_information_Comment : ADDINFOCOMM_OPEN ADDINFOCOMM_CLOSE'
# -------------------------------Otros-------------------------------
def p_doc_comment(p):
    '''
    doc_comment : COMMENT_OPEN doc_comment
                | str doc_comment
                | COMMENT_CLOSE
    '''


def p_string(p):
    '''
    str : STRING str
              | STRING
    '''
    p[0] = p[1]
    print("se capturo correctamente el string", p[0])
    return


def p_error(p):
    print("Syntax error at '%s'" % p.value)


# -------------------------------Otros-------------------------------


print("------------------INICIO DE PRUEBA DE RECONOCIMIENTO DE TOKENS------------------")
file = open('pruebaRonnyAle.xml', 'r')
count = 0
for line in file:
    try:
        lexer = lex.lex()
        lexer.input(line)
        while True:
            tok = lexer.token()
            if not tok:
                break
            print(tok)
    except EOFError:
        break
file.close()
print("------------------FIN DE PRUEBA DE RECONOCIMIENTO DE TOKENS------------------")

print("\n\n\n")

print("------------------INICIO DE PRUEBA DE RECONOCIMIENTO DE GRAMATICA------------------")
with open('pruebaRonnyAle.xml', 'r') as myfile:
    data = myfile.read()

parser = yacc.yacc()
parser.parse(data)
print("------------------FIN DE PRUEBA DE RECONOCIMIENTO DE GRAMATICA------------------")