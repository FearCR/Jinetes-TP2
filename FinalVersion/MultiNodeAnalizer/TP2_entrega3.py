import ply.lex as lex
import ply.yacc as yacc
import container
import sys
import re
import os

nodeDictionary={}
tokens=[
#DOCUMENT START AND END
    'XML_VERSION','COMMENT_OPEN','GENERAL_CLOSE','OFFICE_DOCUMENT_OPEN','OFFICE_DOCUMENT_CLOSE',
    'OFFICE_MODEL_OPEN','OFFICE_MODEL_CLOSE','MODEL_NODES_OPEN','MODEL_NODES_CLOSE','MODEL_NODE_OPEN',
    'MODEL_NODE_CLOSE',
    #BASIC INFO
    'BASIC_INFORMATION_OPEN','BASIC_INFORMATION_CLOSE','COMPONENT_NAME_OPEN','COMPONENT_NAME_CLOSE',
    'COMPONENT_OVERVIEW_OPEN','COMPONENT_OVERVIEW_CLOSE','INTRINSICAL_PROPERTIES_OPEN','INTRINSICAL_PROPERTIES_CLOSE',
    'PROPERTIES_COLOR_OPEN','PROPERTIES_COLOR_CLOSE','PROPERTIES_MATERIAL_OPEN','PROPERTIES_MATERIAL_CLOSE',
    'PROPERTIES_HEIGHT_OPEN','PROPERTIES_HEIGHT_CLOSE','PROPERTIES_WEIGHT_OPEN','PROPERTIES_WEIGHT_CLOSE',
    'PROPERTIES_COUNT_OPEN','PROPERTIES_COUNT_CLOSE','PROPERTIES_FRAGILITY_OPEN','PROPERTIES_FRAGILITY_CLOSE',
    'PROPERTIES_PROPERTY_OPEN','PROPERTIES_PROPERTY_CLOSE',
    #THREATS
    'THREATS_OPEN','THREATS_CLOSE','THREAT_OPEN','THREAT_CLOSE','THREAT_NAME_OPEN','THREAT_NAME_CLOSE',
    'THREAT_DESCRIPTION_OPEN','THREAT_DESCRIPTION_CLOSE','THREAT_VULNERABILITIES_OPEN','THREAT_VULNERABILITIES_CLOSE',
    'VULNERABILITIES_VULNERABILITY_OPEN','VULNERABILITIES_VULNERABILITY_CLOSE',
    #STRING
    'STRING',
    #SECURITY  RELATIONSHIPS
	'SECURITY_RELATIONSHIP_OPEN', 'SECURITY_RELATIONSHIP_CLOSE', 'LINKED_NODE_OPEN', 'LINKED_NODE_CLOSE',
	'RELATIONSHIP_TYPE_OPEN', 'RELATIONSHIP_TYPE_CLOSE',
	'SECURITY_OBJECTIVES_OPEN', 'SECURITY_OBJECTIVES_CLOSE', 'SECURITY_OBJECTIVE_OPEN',
	'SELF_OBJECTIVE_OPEN', 'SELF_OBJECTIVE_CLOSE', 'PEER_OBJECTIVE_OPEN', 'PEER_OBJECTIVE_CLOSE',
	#SECURITY RELATIONSHIPS && SECURITY POLICIES
	'ID',
	#SECURITY POLICIES
	'SECURITY_POLICIES_OPEN', 'SECURITY_POLICIES_CLOSE', 'SECURITY_POLICY_OPEN',
	'SECURITY_POLICY_CLOSE', 'POLICY_NAME_OPEN', 'POLICY_NAME_CLOSE', 'POLICY_DESCRIPTION_OPEN', 'POLICY_DESCRIPTION_CLOSE',
	'SP_OBJECTIVES_OPEN', 'SP_OBJECTIVES_CLOSE',
	'ADDITIONAL_INFO_OPEN', 'ADDITIONAL_INFO_CLOSE',
    #VULNERABILITY
    'VULNERABILITIES_OPEN','VULNERABILITIES_CLOSE',
    'VULNERABILITY_OPEN','VULNERABILITY_CLOSE','VULN_NAME_OPEN','VULN_NAME_CLOSE',
    'VULN_REFERENCE_OPEN','VULN_REFERENCE_CLOSE',
    'REF_SECURITY_OPEN','REF_SECURITY_CLOSE','VULN_OVERVIEW_OPEN','VULN_OVERVIEW_CLOSE',
    'VULN_DESCRIPTION_OPEN','VULN_DESCRIPTION_CLOSE','VULN_IMPACT_OPEN','VULN_IMPACT_CLOSE',
    'VULN_SEVERITY_OPEN','VULN_SEVERITY_CLOSE', 'VULN_ADDITIONAL_INFO_OPEN','VULN_ADDITIONAL_INFO_CLOSE',
    #SECURITY CONTROL
    'SECURITY_CONTROLS_OPEN','SECURITY_CONTROLS_CLOSE', 'SECURITY_CONTROL_OPEN','SECURITY_CONTROL_CLOSE',
    'SECCONT_NAME_OPEN','SECCONT_NAME_CLOSE','SECCONT_DESCRIPTION_OPEN','SECCONT_DESCRIPTION_CLOSE',
    'SECCONT_SECURITY_POLICIES_OPEN','SECCONT_SECURITY_POLICIES_CLOSE','SECPOLICY_ID_OPEN','SECPOLICY_ID_CLOSE',
    'SECCONT_ADDITIONAL_INFO_OPEN','SECCONT_ADDITIONAL_INFO_CLOSE',
    #RISK
    'NODE_RISKS_OPEN', 'NODE_RISKS_CLOSE', 'RISKS_RISK_OPEN', 'RISKS_RISK_CLOSE', 'RISK_NAME_OPEN',
    'RISK_NAME_CLOSE', 'RISK_OBJ_OPEN', 'RISK_OBJ_CLOSE', 'RISK_VUL_OPEN', 'RISK_VUL_CLOSE',
    'RISK_THREAT_OPEN', 'RISK_THREAT_CLOSE', 'RISK_DESCRIPTION_OPEN', 'RISK_DESCRIPTION_CLOSE',
    'RISK_LIKHD_OPEN', 'RISK_LIKHD_CLOSE', 'RISK_IMPACT_OPEN', 'RISK_IMPACT_CLOSE',
    'RISK_TEMP_OPEN', 'RISK_TEMP_CLOSE',
     # SECURITY OBJECTIVES
    'NODE_SECUOBJ_OPEN', 'NODE_SECUOBJ_CLOSE', 'SECUOBJ_OBJ_OPEN',
    'SECUOBJ_NAME_OPEN', 'SECUOBJ_NAME_CLOSE', 'SECUOBJ_DESCRIP_OPEN', 'SECUOBJ_DESCRIP_CLOSE',
    'SECUOBJ_OBJTYPE_OPEN', 'SECUOBJ_OBJTYPE_CLOSE', 'SECUOBJ_SECUSERV_OPEN', 'SECUOBJ_SECUSERV_CLOSE',
    'SECUOBJ_TEMP_OPEN', 'SECUOBJ_TEMP_CLOSE', 'SECUOBJ_OBJSOUR_OPEN', 'SECUOBJ_OBJSOUR_CLOSE',
    #TOKEN QUE COMPARTO CON RONNY
    'SECUOBJ_OBJ_CLOSE'


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
t_PROPERTIES_COUNT_OPEN=r'<component-intrinsical-properties:count>'
t_PROPERTIES_COUNT_CLOSE=r'</component-intrinsical-properties:count>'
t_PROPERTIES_FRAGILITY_OPEN=r'<component-intrinsical-properties:fragility>'
t_PROPERTIES_FRAGILITY_CLOSE=r'</component-intrinsical-properties:fragility>'
t_PROPERTIES_PROPERTY_OPEN=r'<component-intrinsical-properties:property>'
t_PROPERTIES_PROPERTY_CLOSE=r'</component-intrinsical-properties:property>'

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
#t_SECURITY_OBJECTIVE_CLOSE = r'</security-objectives:security-objective>'
#SECURITY RELATIONSHIPS
t_SELF_OBJECTIVE_OPEN = r'<security-objective:self-objective\sobjective-id="DO\[\d\]\[\d\]">'
t_SELF_OBJECTIVE_CLOSE = r'</security-objective:self-objective>'
t_PEER_OBJECTIVE_OPEN = r'(<security-objective:peer-objective\speer-objective-id="[DI]O\[\d\]\[\d\]"> | <security-objective:peer-objective\sobjective-id="[DI]O\[\d\]\[\d\]">)'
t_PEER_OBJECTIVE_CLOSE = r'</security-objective:peer-objective>'

#TOKEN QUE TENGO QUE COMPARTIR CON RONNY
t_SECUOBJ_OBJ_CLOSE=r'</security-objectives:security-objective>'

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


#VULNERABILITY
t_VULNERABILITIES_OPEN       = r'<node:vulnerabilities>'
t_VULNERABILITIES_CLOSE      = r'</node:vulnerabilities>'
t_VULNERABILITY_OPEN         = r'<vulnerabilities:vulnerability\svunerability-id=\"[a-zA-Z0-9_\s,./-]+\"(\ssource-database=\"[a-zA-Z0-9_\s,./-]+\")*>'
t_VULNERABILITY_CLOSE        = r'</vulnerabilities:vulnerability>'
t_VULN_NAME_OPEN             = r'<vulnerability:name>'
t_VULN_NAME_CLOSE            = r'</vulnerability:name>'
t_VULN_REFERENCE_OPEN        = r'<vulnerability:reference-security-services>'
t_VULN_REFERENCE_CLOSE       = r'</vulnerability:reference-security-services>'
t_REF_SECURITY_OPEN          = r'<reference-security-services:reference-security-service>'
t_REF_SECURITY_CLOSE         = r'</reference-security-services:reference-security-service>'
t_VULN_OVERVIEW_OPEN         = r'<vulnerability:overview>'
t_VULN_OVERVIEW_CLOSE        = r'</vulnerability:overview>'
t_VULN_DESCRIPTION_OPEN      = r'<vulnerability:description>'
t_VULN_DESCRIPTION_CLOSE     = r'</vulnerability:description>'
t_VULN_IMPACT_OPEN           = r'<vulnerability:impact>'
t_VULN_IMPACT_CLOSE          = r'</vulnerability:impact>'
t_VULN_SEVERITY_OPEN         = r'<vulnerability:severity>'
t_VULN_SEVERITY_CLOSE        = r'</vulnerability:severity>'
#SECURITY CONTROLS
t_SECURITY_CONTROLS_OPEN         = r'<node:security-controls>'
t_SECURITY_CONTROLS_CLOSE        = r'</node:security-controls>'
t_SECURITY_CONTROL_OPEN          = r'<security-controls:security-control\scontrol-id=\"[a-zA-Z0-9_\s,./-]+\">'
t_SECURITY_CONTROL_CLOSE         = r'</security-controls:security-control>'
t_SECCONT_NAME_OPEN                 = r'<security-control:name>'
t_SECCONT_NAME_CLOSE                = r'</security-control:name>'
t_SECCONT_DESCRIPTION_OPEN          = r'<security-control:description>'
t_SECCONT_DESCRIPTION_CLOSE         = r'</security-control:description>'
t_SECCONT_SECURITY_POLICIES_OPEN    = r'<security-control:security-policies>'
t_SECCONT_SECURITY_POLICIES_CLOSE   = r'</security-control:security-policies>'
t_SECPOLICY_ID_OPEN                 = r'<security-policies:security-policy-id>'
t_SECPOLICY_ID_CLOSE                = r'</security-policies:security-policy-id>'
t_SECCONT_ADDITIONAL_INFO_OPEN      = r'<security-control:additional-information>'
t_SECCONT_ADDITIONAL_INFO_CLOSE     = r'</security-control:additional-information>'
#SECURITY OBJECTIVES
t_NODE_SECUOBJ_OPEN=r'<node:security-objectives>'
t_NODE_SECUOBJ_CLOSE=r'</node:security-objectives>'
t_SECUOBJ_OBJ_OPEN=r'<security-objectives:security-objective\sobjective-id=".*">'
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
t_SECUOBJ_OBJSOUR_OPEN=r'<security-objective:objective-source>'
t_SECUOBJ_OBJSOUR_CLOSE=r'</security-objective:objective-source>'
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
               | vulnerabilities model_node
               | node_risks model_node
               | security_controls model_node
               | node_security_objective model_node
               | MODEL_NODE_CLOSE
    '''
    #Si se llega a cierre, se crea un nuevo nodo
    if p[1] == "</model:node>":
        nuevoNodo = container.Node()
        p[0]=nuevoNodo
    #Si se encunetra igual, se hace split para obtener el Id de nodo
    elif "=" in p[1]:
        array = p[1].split("\"")
        p[2].setId(array[1])
        p[0]=p[2]
        nodeDictionary[p[0].id]=p[0]
    elif p[1][0]=="listaSControls":
        p[2].setSecurity_Controls(p[1][1])
        p[0]=p[2]
    #Si no, se verifica si se tiene una lista de Threats y se actualiza la instancia de Nodo
    elif p[1][0]=="listaThreats":
        p[2].setThreats(p[1][1])
        p[0]=p[2]
    elif p[1][0]=="listaVuln":
        p[2].setVulnerabilities(p[1][1])
        p[0]=p[2]
    elif p[1][0]=="listaBasic":
        p[2].setBasic_Information(p[1][1])
        p[0]=p[2]
    elif p[1][0]=="listaSPolicies":
        p[2].setSecurity_Policies(p[1][1])
        p[0]=p[2]
    elif p[1][0]=="listaSRelationships":
        p[2].setSecurity_Relationships(p[1][1])
        p[0]=p[2]
    elif p[1][0]=="objs":
        p[2].setListObj(p[1][1])
        p[0]=p[2]
    elif p[1][0]=="risks":
        p[2].setRiks(p[1][1])
        p[0]=p[2]
    return
#-------------------------------inicio del documento-------------------------------

#-------------------------------SECURITY OBJECTIVES-------------------------------
def p_node_security_objective(p):
    '''
    node_security_objective : NODE_SECUOBJ_OPEN node_security_objective
                               | security_objective_obj node_security_objective
                               | NODE_SECUOBJ_CLOSE
    '''
    if p[1] == "</node:security-objectives>":
        security_objectives=container.Security_objectives()
        p[0]=security_objectives
    elif p[1][0]=="obj":
        p[2].addSecurity_objective(p[1][1])
        p[0] = p[2]
    elif p[1]=="<node:security-objectives>":
        p[0] = ("objs", p[2])
        #p[0][1].printObjectives()
    return


def p_security_objective_obj(p):
    #'security_objective_obj : SECUOBJ_OBJ_OPEN security_objective_name security_objective_description SECUOBJ_OBJ_CLOSE'

    '''
    security_objective_obj : SECUOBJ_OBJ_OPEN security_objective_obj
                              | security_objective_name security_objective_obj
                              | security_objective_description security_objective_obj
                              | security_objective_objective_type security_objective_obj
                              | security_objective_security_service security_objective_obj
                              | security_objective_temporality security_objective_obj
                              | security_objective_source security_objective_obj
                              | SECUOBJ_OBJ_CLOSE
    '''

    if p[1]=="</security-objectives:security-objective>":
        objective=container.Security_objective()
        p[0]=objective
    elif p[1][0]=="source":
        p[2].setSource(p[1][1])
        p[0] = p[2]
    elif p[1][0]=="temp":
        p[2].setTemp(p[1][1])
        p[0] = p[2]
    elif p[1][0] == "service":
        p[2].setService(p[1][1])
        p[0] = p[2]
    elif p[1][0] == "type":
        p[2].setObjType(p[1][1])
        p[0] = p[2]
    elif p[1][0] == "descri":
        p[2].setDescrip(p[1][1])
        p[0] = p[2]
    elif p[1][0] == "name":
        p[2].setName(p[1][1])
        p[0] = p[2]
    elif "=" in p[1]:
        array = p[1].split("\"")
        p[2].setId(array[1])
        p[0] = ("obj", p[2])
    return






def p_security_objective_name(p):
    'security_objective_name : SECUOBJ_NAME_OPEN STRING SECUOBJ_NAME_CLOSE'
    p[0] = ("name", p[2])
    return


def p_security_objective_description(p):
    'security_objective_description : SECUOBJ_DESCRIP_OPEN STRING SECUOBJ_DESCRIP_CLOSE'
    p[0] = ("descri", p[2])
    return


def p_security_objective_objective_type(p):
    'security_objective_objective_type : SECUOBJ_OBJTYPE_OPEN STRING SECUOBJ_OBJTYPE_CLOSE'
    p[0] = ("type", p[2])
    return

def p_security_objective_security_service(p):
    'security_objective_security_service : SECUOBJ_SECUSERV_OPEN STRING SECUOBJ_SECUSERV_CLOSE'
    p[0] = ("service", p[2])
    return

def p_security_objective_temporality(p):
    'security_objective_temporality : SECUOBJ_TEMP_OPEN STRING SECUOBJ_TEMP_CLOSE'
    p[0] = ("temp", p[2])
    return
def p_security_objective_source(p):
    'security_objective_source : SECUOBJ_OBJSOUR_OPEN STRING SECUOBJ_OBJSOUR_CLOSE'
    p[0] = ("source", p[2])
    return
#-------------------------------SECURITY OBJECTIVES-------------------------------

# -------------------------------RISK-------------------------------
def p_node_risks(p):
    '''
    node_risks : NODE_RISKS_OPEN node_risks
               | risks_risk node_risks
               | NODE_RISKS_CLOSE
    '''
    if p[1] == "</node:risks>":
        risks=container.Risks()
        p[0]=risks
    elif p[1][0] == "risk":
        p[2].addRisk(p[1][1])
        p[0] = p[2]
    elif p[1] == "<node:risks>":
        p[0] = ("risks", p[2])
        #p[0][1].printRisks()
    return

def p_risks_risk(p):
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
                | RISKS_RISK_CLOSE
    '''

    if p[1]=="</risks:risk>":
        risk=container.Risk()
        p[0]=risk
    elif p[1][0] == "temp":
        p[2].setTemporality(p[1][1])
        p[0] = p[2]
    elif p[1][0] == "imp":
        p[2].setImpact(p[1][1])
        p[0] = p[2]
    elif p[1][0] == "like":
        p[2].setLikelihood(p[1][1])
        p[0] = p[2]
    elif p[1][0] == "descrip":
        p[2].setDescrip(p[1][1])
        p[0] = p[2]
    elif p[1][0] == "thr":
        p[2].setThreatId(p[1][1])
        p[0] = p[2]
    elif p[1][0] == "vul":
        p[2].setVulne(p[1][1])
        p[0] = p[2]
    elif p[1][0] == "obj":
        p[2].setObjId(p[1][1])
        p[0] = p[2]
    elif p[1][0] == "name":
        p[2].setName(p[1][1])
        p[0] = p[2]
    elif "=" in p[1]:
        array = p[1].split("\"")
        p[2].setId(array[1])
        p[0] = ("risk", p[2])
    return

def p_risk_name(p):
    '''
    risk_name : RISK_NAME_OPEN risk_name
              | STRING risk_name
              | RISK_NAME_CLOSE
    '''

    if p[1] == "</risk:name>":
        name=""
        p[0]=name
    elif p[1] != "</risk:name>"  and    p[1] != "<risk:name>":
        p[2]=p[1]
        p[0]=p[2]
    elif p[1] == "<risk:name>":
        p[0] = ("name", p[2])
    return

def p_risk_objective(p):
    '''
    risk_objective : RISK_OBJ_OPEN STRING RISK_OBJ_CLOSE
    '''
    p[0] = ("obj", p[2])
    return
def p_risk_vulnerability(p):
    '''
    risk_vulnerability : RISK_VUL_OPEN STRING RISK_VUL_CLOSE
    '''
    p[0] = ("vul", p[2])
    return

def p_risk_threat(p):
    '''
    risk_threat : RISK_THREAT_OPEN STRING RISK_THREAT_CLOSE
    '''
    p[0] = ("thr", p[2])
    return

def p_risk_description(p):
    '''
    risk_description : RISK_DESCRIPTION_OPEN STRING RISK_DESCRIPTION_CLOSE
    '''
    p[0] = ("descrip", p[2])
    return
def p_risk_likelihood(p):
    '''
    risk_likelihood : RISK_LIKHD_OPEN STRING RISK_LIKHD_CLOSE
    '''
    p[0] = ("like", p[2])
    return

def p_risk_impact(p):
    '''
    risk_impact : RISK_IMPACT_OPEN STRING RISK_IMPACT_CLOSE
    '''
    p[0] = ("imp", p[2])
    return
def p_risk_temporality(p):
    '''
    risk_temporality : RISK_TEMP_OPEN STRING RISK_TEMP_CLOSE
    '''
    p[0] = ("temp", p[2])
    return
# -------------------------------RISK-------------------------------

#-------------------------------Basic information-------------------------------
#adentro tiene todo basic information, nombre overview categorias propiedades y otros detalles
def p_basic_information(p):
    '''
    basic_info : BASIC_INFORMATION_OPEN basic_info
               | component_name basic_info
               | component_overview basic_info
               | intrinsical_properties basic_info
               | BASIC_INFORMATION_CLOSE
    '''
    #print(p[1])
    if p[1] == "</node:basic-information>":
        newsBasic=container.Basic_Information()
        p[0]=newsBasic
    elif p[1][0] == "name":
        p[2].setName(p[1][1])
        p[0]=p[2]
    elif p[1][0] == "overview":
        p[2].setOverview(p[1][1])
        p[0]=p[2]
    elif p[1][0] == "properties":
        p[2].setProperties(p[1])
        p[0]=p[2]
        #Si se llega al final, se pasa la Lista al nivel superior.
    elif p[1] == "<node:basic-information>":
        p[0]=("listaBasic",p[2])
        #print("AGREGANDO NUEVO BASIC INFOTMATION")
    return
# contiene string dentro
def p_component_name(p):
    '''
    component_name : COMPONENT_NAME_OPEN str COMPONENT_NAME_CLOSE
    '''
    p[0]=("name",p[2])
    return
#adentro tiene intrinsical properties
def p_intrinsical_properties(p):
    '''
    intrinsical_properties : INTRINSICAL_PROPERTIES_OPEN intrinsical_properties
                           | properties_color intrinsical_properties
                           | properties_material intrinsical_properties
                           | properties_height intrinsical_properties
                           | properties_weight intrinsical_properties
                           | properties_count intrinsical_properties
                           | properties_fragility intrinsical_properties
                           | properties_property intrinsical_properties
                           | INTRINSICAL_PROPERTIES_CLOSE
    '''
    if p[1] == "</basic-information:component-intrinsical-properties>":
        p[0]=[]
        p[0].append("properties")
    elif p[1][0] == "color":
        p[2].append(p[1])
        p[0]=p[2]
    elif p[1][0] == "material":
        p[2].append(p[1])
        p[0]=p[2]
    elif p[1][0] == "height":
        p[2].append(p[1])
        p[0]=p[2]
    elif p[1][0] == "weight":
        p[2].append(p[1])
        p[0]=p[2]
    elif p[1][0] == "count":
        p[2].append(p[1])
        p[0]=p[2]
    elif p[1][0] == "fragility":
        p[2].append(p[1])
        p[0]=p[2]
    elif p[1][0] == "property":
        p[2].append(p[1])
        p[0]=p[2]
    elif p[1] == "<basic-information:component-intrinsical-properties>":
        p[0]=p[2]
        #print("Enviando propiedades")
    return


#contiene str dentro
def p_component_overview(p):
    '''
    component_overview : COMPONENT_OVERVIEW_OPEN str COMPONENT_OVERVIEW_CLOSE
    '''
    p[0]=("overview",p[2])
    return


#contiene string dentro
def p_properties_color(p):
    '''
    properties_color : PROPERTIES_COLOR_OPEN str PROPERTIES_COLOR_CLOSE
    '''
    p[0]=("color",p[2])
    return
#contiene string dentro
def p_properties_material(p):
    '''
    properties_material : PROPERTIES_MATERIAL_OPEN str PROPERTIES_MATERIAL_CLOSE
    '''
    p[0]=("material",p[2])
    return
#contiene str dentro
def p_properties_height(p):
    '''
    properties_height : PROPERTIES_HEIGHT_OPEN str PROPERTIES_HEIGHT_CLOSE
    '''
    p[0]=("height",p[2])
    return
#contiene string dentro
def p_properties_weight(p):
    '''
    properties_weight : PROPERTIES_WEIGHT_OPEN str PROPERTIES_WEIGHT_CLOSE
    '''
    p[0]=("weight",p[2])
    return
#contiene string dentro
def p_properties_count(p):
    '''
    properties_count : PROPERTIES_COUNT_OPEN str PROPERTIES_COUNT_CLOSE
    '''
    p[0]=("count",p[2])
    return
#contiene string dentro
def p_properties_fragility(p):
    '''
    properties_fragility : PROPERTIES_FRAGILITY_OPEN str PROPERTIES_FRAGILITY_CLOSE
    '''
    p[0]=("fragility",p[2])
    return
#contiene string dentro
def p_properties_property(p):
    '''
    properties_property : PROPERTIES_PROPERTY_OPEN str PROPERTIES_PROPERTY_CLOSE
    '''
    p[0]=("property",p[2])
    return
#-------------------------------Basic information-------------------------------


#-------------------------------Threats-------------------------------
def p_threats(p):
    '''
    threats : THREATS_OPEN threats
            | threat threats
            | THREATS_CLOSE
    '''
    #Si se llega al final de Threats, se crea una nueva Lista de Threats
    if p[1] == "</node:threats>":
        newThreats=container.Threats()
        p[0]=newThreats
    #Si se encuentra un Threat, se agrega a la lista
    elif p[1][0]=="threat":
         p[2].addThreat(p[1][1])
         p[0]=p[2]
    #Si se llega al final, se pasa la Lista al nivel superior.
    elif p[1] == "<node:threats>":
        p[0]=("listaThreats",p[2])
        #print("AGREGANDO NUEVA LISTA THREATS")
        #p[0][1].printThreats()



    return
def p_threat(p):
    '''
    threat  : THREAT_OPEN threat
            | threat_name threat
            | threat_description threat
            | threat_vulnerabilities threat
            | THREAT_CLOSE
    '''
    #Se empieza en vulnerability y termina en THREAT OPEN
    if p[1][0]=="vuln":
    #Aqui llega a fondo y se inicia el nuevo Threat
        newThreat= container.Threat()
        newThreat.setVulnerability(p[1][1])
        p[0]=newThreat
    #Para los siguientes metodos se actualiza el objeto y se manda arriba
    elif p[1][0]=="desc":
        p[2].setDescription(p[1][1])
        p[0]=p[2]
    elif p[1][0]=="name":
        p[2].setName(p[1][1])
        p[0]=p[2]
    #Cuando ve un = se le hace split para obtener el ID
    elif "=" in p[1]:
        array = p[1].split("\"")
        p[2].setId(array[1])
        p[0]=("threat",p[2])
        #print("AGREGANDO NUEVO THREAT")
        #p[0][1].printThreat()
    return


def p_threat_name(p):
    '''
    threat_name : THREAT_NAME_OPEN str THREAT_NAME_CLOSE
    '''
    #Se hace una tupla para identificar que variable es y se pasa el dato arriba
    p[0]=("name",p[2])
    return p
def p_threat_description(p):
    '''
    threat_description : THREAT_DESCRIPTION_OPEN str THREAT_DESCRIPTION_CLOSE
    '''
    #Se hace una tupla para identificar que variable es y se pasa el dato arriba
    p[0]=("desc",p[2])
    return
def p_threat_vulnerabilities(p):
    '''
    threat_vulnerabilities : THREAT_VULNERABILITIES_OPEN threat_vulnerabilities
                           | threat_vulnerability threat_vulnerabilities
                           | THREAT_VULNERABILITIES_CLOSE
    '''
    #Si se pasa la tupla segun corresponda a niveles superiores
    if p[1][0] == "vuln":
        p[0]=p[1]
    elif p[1] == "<threat:vulnerabilities>":
        p[0]=p[2]
    return
def p_threat_vulnerability(p):
    '''
    threat_vulnerability : VULNERABILITIES_VULNERABILITY_OPEN str VULNERABILITIES_VULNERABILITY_CLOSE
    '''
    #Se hace una tupla para identificar que variable es y se pasa el dato arriba
    p[0]= ("vuln",p[2])
    return p
#-------------------------------Threats-------------------------------



#------------------------------Security Policies------------------------------------
def p_structure_security_policies(t):
	'''
	structure_security_policies : security_policies
	'''
	#t[1].print_security_policies()
	t[0] = ("listaSPolicies", t[1])
	return

def p_security_policies(t):
	'''
	security_policies : SECURITY_POLICIES_OPEN security_policies
					  | security_policy security_policies
					  | SECURITY_POLICIES_CLOSE
	'''
	if t[1] == "</node:security-policies>":
		security_policies_list = container.security_policies()
		t[0] = security_policies_list
	else:
		if t[1] != "<node:security-policies>":
			t[2].add_security_policie(t[1])
			t[0] = t[2]
		else:
			t[0] = t[2]
	return

def p_security_policy(t):
	'''
	security_policy : SECURITY_POLICY_OPEN ID GENERAL_CLOSE POLICY_NAME_OPEN STRING POLICY_NAME_CLOSE POLICY_DESCRIPTION_OPEN STRING POLICY_DESCRIPTION_CLOSE security_objectives_SP SECURITY_POLICY_CLOSE
	'''
	security_policy = container.security_policy()
	t[0] = security_policy
	t[0].set_id(t[2])
	t[0].set_name(t[5])
	t[0].set_description(t[8])
	t[0].set_objective(t[10])
	return


def p_security_objectives_SP(t):
	'''
	security_objectives_SP : SP_OBJECTIVES_OPEN SECURITY_OBJECTIVE_OPEN STRING SECUOBJ_OBJ_CLOSE SP_OBJECTIVES_CLOSE
	'''
	t[0] = t[3]
	return

#-------------------------------Security Policies-----------------------------

#------------------------------Security Relationships------------------------------


def p_structure_security_relationships(t):
	'''
	structure_security_relationships : security-relationships
	'''
	#t[1].print_security_relationships()
	t[0] = ("listaSRelationships", t[1])
	return


def p_security_relationships(t):
    '''
    security-relationships : SECURITY_RELATIONSHIP_OPEN security-relationships
                           | linked-node security-relationships
                           | SECURITY_RELATIONSHIP_CLOSE
    '''
    if t[1] == "</node:security-relationships>":
        list_security_relationships = container.security_relationships()
        t[0] = list_security_relationships
    else:
        if t[1][0] == "nodo":
            t[2].add_security_relationship(t[1][1])
            t[0] = t[2]
        else:
            t[0] = t[2]
    return


def p_expression_linked_node(t):
    '''
    linked-node : linked_node_open linked-node
                | relationship-type linked-node
				| LINKED_NODE_CLOSE
    '''
    if t[1] == "</security-relationships:linked-node>":
        node_security_relationship = container.security_relationship()
        t[0] = node_security_relationship
    else:
        if t[1][0] == "interaction_id":
            t[2].add_interaction_id(t[1][1])
            t[0] = t[2]
        else:
            if t[1][0] == "node_id":
                t[2].set_id(t[1][1])
                t[0] = ("nodo",t[2])
    return


def p_linked_node_open(t):
	'''
	linked_node_open : LINKED_NODE_OPEN ID GENERAL_CLOSE
	'''
	t[0] = ("node_id", t[2])
	return

def p_expression_relationship_type(t):
    '''
    relationship-type : RELATIONSHIP_TYPE_OPEN ID GENERAL_CLOSE relationship-type
					  | security-objectives_SR relationship-type
					  | security-objectives_SR RELATIONSHIP_TYPE_CLOSE
    '''
    match = re.search('<linked-node:relationship-type\stype="[a-zA-Z]+"\sinteraction-id=', str(t[1]))
    if match:
        t[0] = ("interaction_id",t[2])
    return


def p_expression_security_objectives_SR(t):
    '''
    security-objectives_SR : SECURITY_OBJECTIVES_OPEN security-objectives_SR
						   | security-objective_SR security-objectives_SR
						   | security-objective_SR SECURITY_OBJECTIVES_CLOSE
    '''
    return

def p_expression_security_objective_SR(t):
    '''
    security-objective_SR : SECURITY_OBJECTIVE_OPEN SELF_OBJECTIVE_OPEN SELF_OBJECTIVE_CLOSE PEER_OBJECTIVE_OPEN PEER_OBJECTIVE_CLOSE SECUOBJ_OBJ_CLOSE
    '''
    return
#----------------------------Security Relationships-------------------------------------


#------------------------------------------Vulnerabilities------------------------------
def p_vulnerabilities(p):
    '''
    vulnerabilities : VULNERABILITIES_OPEN vulnerabilities
                    | vulnerability vulnerabilities
                    | VULNERABILITIES_CLOSE
    '''
    #Si se llega al final de Threats, se crea una nueva Lista de Threats
    if p[1] == "</node:vulnerabilities>":
        newVulnerabilities=container.Vulnerabilities()
        p[0]=newVulnerabilities
    #Si se encuentra un Threat, se agrega a la lista
    elif p[1][0]=="vulnerability":
         p[2].addVulnerability(p[1][1])
         p[0]=p[2]
    #Si se llega al final, se pasa la Lista al nivel superior.
    elif p[1] == "<node:vulnerabilities>":
        p[0]=("listaVuln",p[2])
        #print("AGREGANDO NUEVA LISTA VULNERABILITIES")
        #p[0][1].printVulnerabilities()
    return
def p_vulnerability(p):
    '''
    vulnerability : VULNERABILITY_OPEN vulnerability
                  | vulnerability_name vulnerability
                  | vulnerability_refSecurity vulnerability
                  | vulnerability_overview vulnerability
                  | vulnerability_description vulnerability
                  | vulnerability_impact vulnerability
                  | vulnerability_severity vulnerability
                  | vulnerability_additionalInfo vulnerability
                  | VULNERABILITY_CLOSE
    '''
    if p[1]=="</vulnerabilities:vulnerability>":
        newVulnerability = container.Vulnerability()
        p[0]= newVulnerability
        #print("CREA VUL")
    elif p[1][0]=="vulSeveriy":
        p[2].setSeverity(p[1][1])
        p[0]=p[2]
    elif p[1][0]=="vulImpact":
        p[2].setImpact(p[1][1])
        p[0]=p[2]
    elif p[1][0]=="vulDesc":
        p[2].setDescription(p[1][1])
        p[0]=p[2]
    elif p[1][0]=="vulOverview":
        p[2].setOverview(p[1][1])
        p[0]=p[2]
    elif p[1][0]=="refSecurity":
        p[2].setReferenceSecurity(p[1][1])
        p[0]=p[2]
    elif p[1][0]=="vulName":
        p[2].setName(p[1][1])
        p[0]=p[2]
    elif "=" in p[1]:
        array = p[1].split("\"")
        #print(array)
        #print(len(array))
        p[2].setId(array[1])
        if len(array)== 5:
            p[2].setSourceDB(array[3])
        else:
            p[2].setSourceDB("Not Provided")
        p[0]=("vulnerability",p[2])
        #print("AGREGANDO NUEVA VULNERABILITY")
        #p[0][1].printVulnerability()
    else:
        p[0]=p[2]
    return
def p_vulnerability_refSecurity(p):
    '''
    vulnerability_refSecurity : VULN_REFERENCE_OPEN vulnerability_refSecurity
                              | refSecurity vulnerability_refSecurity
                              | VULN_REFERENCE_CLOSE
    '''
    if p[1][0] == "refSecurity":
        p[0]=p[1]
    if p[1] == "<vulnerability:reference-security-services>":
        p[0]=p[2]
    return
def p_vulnerability_additionalInfo(p):
    '''
    vulnerability_additionalInfo : VULN_ADDITIONAL_INFO_OPEN ADDITIONAL_INFO_OPEN  ADDITIONAL_INFO_CLOSE VULN_ADDITIONAL_INFO_CLOSE
    '''
    return

def p_vulnerability_name(p):
    '''
    vulnerability_name : VULN_NAME_OPEN str VULN_NAME_CLOSE
    '''
    p[0]=("vulName",p[2])
    return

def p_refSecurity(p):
    '''
    refSecurity : REF_SECURITY_OPEN str REF_SECURITY_CLOSE
    '''
    p[0]=("refSecurity",p[2])
    return

def p_vulnerability_overview(p):
    '''
    vulnerability_overview : VULN_OVERVIEW_OPEN str VULN_OVERVIEW_CLOSE
    '''
    p[0]=("vulOverview",p[2])
    return

def p_vulnerability_description(p):
    '''
    vulnerability_description : VULN_DESCRIPTION_OPEN str VULN_DESCRIPTION_CLOSE
    '''
    p[0]=("vulDesc",p[2])
    return

def p_vulnerability_impact(p):
    '''
    vulnerability_impact : VULN_IMPACT_OPEN str VULN_IMPACT_CLOSE
    '''
    p[0]=("vulImpact",p[2])
    return

def p_vulnerability_severity(p):
    '''
    vulnerability_severity : VULN_SEVERITY_OPEN str VULN_SEVERITY_CLOSE
    '''
    #print("LLEGA FONDO SEVERITY")
    p[0]=("vulSeveriy",p[2])
    return
#------------------------------------------Vulnerabilities------------------------------

#------------------------------------------Security Controls------------------------------
def p_security_controls(p):
    '''
    security_controls : SECURITY_CONTROLS_OPEN security_controls
                      | security_control security_controls
                      | SECURITY_CONTROLS_CLOSE
    '''
    #Si se llega al final de Threats, se crea una nueva Lista de Threats
    if p[1] == "</node:security-controls>":
        newsControls=container.Security_Controls()
        p[0]=newsControls
    #Si se encuentra un Threat, se agrega a la lista
    elif p[1][0]=="sControl":
         p[2].addSecurity_Control(p[1][1])
         p[0]=p[2]
    #Si se llega al final, se pasa la Lista al nivel superior.
    elif p[1] == "<node:security-controls>":
        p[0]=("listaSControls",p[2])
        #print("AGREGANDO NUEVA LISTA SECURITY CONTROLS")
        #p[0][1].printSecurity_Controls()
    return
def p_security_control(p):
    '''
    security_control : SECURITY_CONTROL_OPEN security_control
                     | security_control_name security_control
                     | security_control_description security_control
                     | sec_policies security_control
                     | securityControl_additionalInfo security_control
                     | SECURITY_CONTROL_CLOSE
    '''
    if p[1]=="</security-controls:security-control>":
        newSControl = container.Security_Control()
        p[0]= newSControl
    elif p[1][0]=="polID":
        p[2].setSecurityPolicyID(p[1][1])
        p[0]=p[2]
    elif p[1][0]=="polDesc":
        p[2].setDescription(p[1][1])
        p[0]=p[2]
    elif p[1][0]=="polName":
        p[2].setName(p[1][1])
        p[0]=p[2]
    elif "=" in p[1]:
        array = p[1].split("\"")
        p[2].setId(array[1])
        p[0]=("sControl",p[2])
        #print("AGREGANDO NUEVO SECURITY CONTROL")
        #p[0][1].printSecurity_Control()
    else:
        p[0]=p[2]
    return
def p_sec_policies(p):
    '''
    sec_policies : SECCONT_SECURITY_POLICIES_OPEN sec_policies
                 | security_policyID sec_policies
                 | SECCONT_SECURITY_POLICIES_CLOSE
    '''
    if p[1][0] == "polID":
        p[0]=p[1]
    if p[1] == "<security-control:security-policies>":
        p[0]=p[2]
    return
def p_securityControl_additionalInfo(p):
    '''
    securityControl_additionalInfo : SECCONT_ADDITIONAL_INFO_OPEN ADDITIONAL_INFO_OPEN ADDITIONAL_INFO_CLOSE SECCONT_ADDITIONAL_INFO_CLOSE
    '''
    return
def p_security_control_name(p):
    '''
    security_control_name : SECCONT_NAME_OPEN str SECCONT_NAME_CLOSE
    '''
    p[0]=("polName",p[2])
    return
def p_security_control_description(p):
    '''
    security_control_description : SECCONT_DESCRIPTION_OPEN str SECCONT_DESCRIPTION_CLOSE
    '''
    p[0]=("polDesc",p[2])
    return
def p_security_policyID(p):
    '''
    security_policyID : SECPOLICY_ID_OPEN str SECPOLICY_ID_CLOSE
    '''
    p[0]=("polID",p[2])
    return
#------------------------------------------Security Controls------------------------------



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
    '''
    p[0]=p[1]
    return p
def p_error(p):
    print("Syntax error at '%s'" % p.value)
#-------------------------------Otros------------------------------
"""
#Prueba Contenedor
test = container.Vulnerability()
testB = container.Vulnerability()
test.setAll("newID","newDB","newName","newReferenceSecurity","newOverview","newDescription","newImpact","newSeverity")
testB.setAll("2newID","2newDB","2newName","2newReferenceSecurity","2newOverview","2newDescription","2newImpact","2newSeverity")
testVulns = container.Vulnerabilities()
testVulns.addVulnerability(test)
testVulns.addVulnerability(testB)

testTA = container.Threat()
testTB = container.Threat()
testTA.setAll("A1","NameA1","HereGoesDescription","Vulnerability")
testTB.setAll("B2","NameB2","B2HereGoesDescription","B2Vulnerability")
testThreats = container.Threats()
testThreats.addThreat(testTA)
testThreats.addThreat(testTB)

testSC = container.Security_Control()
testSCB = container.Security_Control()
testSC.setAll("newID","newName","newDescription","newSecurityPolicyID")
testSCB.setAll("2newID","2newName","2newDescription","2newSecurityPolicyID")
testSCS = container.Security_Controls()
testSCS.addSecurity_Control(testSC)
testSCS.addSecurity_Control(testSCB)

nodeTest = container.Node()
nodeTest.setId("NODO A")
nodeTest.setThreats(testThreats)
nodeTest.setVulnerabilities(testVulns)
nodeTest.setSecurity_Controls(testSCS)
nodeTest.printAll()
"""
lexer=lex.lex()

"""
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
"""
#print("------------------INICIO DE PRUEBA DE RECONOCIMIENTO DE GRAMATICA------------------")

with open('prueba.xml','r') as myfile:
    data=myfile.read()

parser=yacc.yacc()
parser.parse(data)
#print("------------------FIN DE PRUEBA DE RECONOCIMIENTO DE GRAMATICA------------------")
print("Equipo:Los 4 Jinetes del Apocalipsis")
print("Funciona con el archivo xml modificado prueba.xml")
user_input=""
while user_input!= "exit":

    print("\n\n\n\033[92mMenu de usuario:\033[0m")
    print("\033[4mEscriba un \033[92mnumero\033[0m\033[4m correspondiente a la accion deseada\033[0m")
    print("\n1- imprimir todos los nodos y toda su informacion")
    print("\n2- imprimir informacion de un nodo especifico")
    print("\n\n\nEscriba \033[93mexit\033[0m para salir del programa\n")
    user_input=input()
    os.system('cls' if os.name=='nt' else 'clear')
    if user_input=="1":
        for key,value in nodeDictionary.items():
            value.printAll()
            print("\n\n\n")
    elif user_input=="2":
        print("Nodos disponibles:")
        for key,value in nodeDictionary.items():
            print(key)
        print("escriba el \033[92mnombre\033[0m del nodo que desea desplegar:")
        nodeKey=input()
        if nodeKey in nodeDictionary:
            while user_input!="10":
                print("\033[0m\n\n\033[4mEscriba el \033[92mnumero\033[0m\033[4m correspondiente accion que desea realizar\033[0m")
                print("\n1- imprimir toda su informacion")
                print("\n2- imprimir informacion basica")
                print("\n3- imprimir Amenazas")
                print("\n4- imprimir Riesgos")
                print("\n5- imprimir Controles de seguridad")
                print("\n6- imprimir Politicas de seguridad")
                print("\n7- imprimir Relaciondes de seguridad")
                print("\n8- imprimir Objetivos de seguridad")
                print("\n9- imprimir Vulnerabilidades")
                print("\n10- Salir de este menu")
                user_input=input()
                os.system('cls' if os.name=='nt' else 'clear')
                if user_input=="1":
                    nodeDictionary.get(nodeKey).printAll()
                elif user_input=="2":
                    nodeDictionary.get(nodeKey).basic_Information.printBasic_Information()
                elif user_input=="3":
                    nodeDictionary.get(nodeKey).threats.printThreats()
                elif user_input=="4":
                    nodeDictionary.get(nodeKey).risks.printRisks()
                elif user_input=="5":
                    nodeDictionary.get(nodeKey).security_Controls.printSecurity_Controls()
                elif user_input=="6":
                    nodeDictionary.get(nodeKey).security_policies.print_security_policies()
                elif user_input=="7":
                    nodeDictionary.get(nodeKey).security_relationships.print_security_relationships()
                elif user_input=="8":
                    nodeDictionary.get(nodeKey).security_objectives.printObjectives()
                elif user_input=="9":
                    nodeDictionary.get(nodeKey).vulnerabilities.printVulnerabilities()
                elif user_input=="10":
                    print("\033[93m\nvolviendo al menu principal\n\033[0m")

                else:
                    print("\033[93m\ninput invalido\n\033[0m")
        else:
            print("\033[93m\nla llave ingresada no existe, intentelo de nuevo\n\033[0m")
    elif user_input=="exit":
        print("")
    else:
        print("\033[93m\nInput invalido\033[0m\n")
