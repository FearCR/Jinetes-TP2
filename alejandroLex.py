import ply.lex as lex
import ply.yacc as yacc
import sys

tokens=[
#DOCUMENT START AND END
    'XML_VERSION','COMMENT_OPEN','COMMENT_CLOSE','OFFICE_DOCUMENT_OPEN','OFFICE_DOCUMENT_CLOSE',
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
    'STRING'

]
#DOCUMENT START AND END
#t_XML_VERSION=r'<\?xml\sversion=".+"\sencoding=".+"\?>'
#t_COMMENT_OPEN=r'<!--'
#t_COMMENT_CLOSE=r'--*>'
#t_OFFICE_DOCUMENT_OPEN=r'<office:document-model\soffice:version=".+">'
#t_OFFICE_DOCUMENT_CLOSE=r'</office:document-model>'
#t_OFFICE_MODEL_OPEN=r'<office:model>'
#t_OFFICE_MODEL_CLOSE=r'</office:model>'
#t_MODEL_NODES_OPEN=r'<model:nodes>'
#t_MODEL_NODES_CLOSE=r'</model:nodes>'
#t_MODEL_NODE_OPEN=r'<model:node\snode-id=".+">'
#t_MODEL_NODE_CLOSE=r'</model:node>'
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
#t_THREATS_OPEN=r'<node:threats>'
#t_THREATS_CLOSE=r'</node:threats>'
#t_THREAT_OPEN=r'<threats:threat\sthreat-id=".+">'
#t_THREAT_CLOSE=r'</threats:threat>'
#t_THREAT_NAME_OPEN=r'<threat:name>'
#t_THREAT_NAME_CLOSE=r'</threat:name>'
#t_THREAT_DESCRIPTION_OPEN=r'<threat:description>'
#t_THREAT_DESCRIPTION_CLOSE=r'</threat:description>'
#t_THREAT_VULNERABILITIES_OPEN=r'<threat:vulnerabilities>'
#t_THREAT_VULNERABILITIES_CLOSE=r'</threat:vulnerabilities>'
#t_VULNERABILITIES_VULNERABILITY_OPEN=r'<vulnerabilities:vulnerability-id>'
#t_VULNERABILITIES_VULNERABILITY_CLOSE=r'</vulnerabilities:vulnerability-id>'

t_STRING=r'[a-zA-Z0-9_\s,./:,ó]+\s?-?\s?[a-zA-Z0-9_\s,./:,ó]*'
# Ignored characters
t_ignore = " \n\t"
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


#adentro tiene todo basic information
def p_basic_information(t):
    'basic_info : BASIC_INFORMATION_OPEN component_name component_overview component_categories intrinsical_properties other_details BASIC_INFORMATION_CLOSE'
    print("se cerro correctamente informacion basica")
    return
#no contiene nada dentro
def p_component_name(p):
    'component_name : COMPONENT_NAME_OPEN str COMPONENT_NAME_CLOSE'
    print("se cerro correctamente el nompre del componente")
    return
#adentro tiene intrinsical properties
def p_intrinsical_properties(t):
    'intrinsical_properties : INTRINSICAL_PROPERTIES_OPEN properties_color properties_material properties_height properties_weight INTRINSICAL_PROPERTIES_CLOSE'
    print("se cerro correctamente propiedades intrinsicas")
    return
#adentro tiene component_category
def p_component_categories(t):
    'component_categories : COMPONENT_CATEGORIES_OPEN component_category COMPONENT_CATEGORIES_CLOSE'
    print("se cerro correctamente categorias del componente")
    return

#no contiene nada dentro
def p_component_overview(t):
    'component_overview : COMPONENT_OVERVIEW_OPEN str COMPONENT_OVERVIEW_CLOSE'
    print("se cerro correctamente overview")
    return
#no contiene nada dentro
def p_other_details(t):
    'other_details : PROPERTIES_OTHER_OPEN str PROPERTIES_OTHER_CLOSE'
    print("se cerro correctamente otros detalles")
    return
#no contiene nada dentro
def p_component_category(t):
    'component_category : COMPONENT_CATEGORY_OPEN COMPONENT_CATEGORY_CLOSE'
    print("se cerro correctamente categoria del componente")
    return
#no contiene nada dentro
def p_properties_color(t):
    'properties_color : PROPERTIES_COLOR_OPEN str PROPERTIES_COLOR_CLOSE'
    print("se cerro correctamente color")
    return
#no contiene nada dentro
def p_properties_material(t):
    'properties_material : PROPERTIES_MATERIAL_OPEN str PROPERTIES_MATERIAL_CLOSE'
    print("se cerro correctamente material")
    return
#no contiene nada dentro
def p_properties_height(t):
    'properties_height : PROPERTIES_HEIGHT_OPEN str PROPERTIES_HEIGHT_CLOSE'
    print("se cerro correctamente altura")
    return
#no contiene nada dentro
def p_properties_weight(t):
    'properties_weight : PROPERTIES_WEIGHT_OPEN str PROPERTIES_WEIGHT_CLOSE'
    print("se cerro correctamente peso")
    return

def p_string(t):
    '''
    str : STRING str
              | STRING
              | empty
    '''
    print("se capturo correctamente el string",t[1])
    return
def p_empty(p):
    'empty : '
def p_error(p):
    print("Syntax error found in",p)

print("------------------INICIO DE PRUEBA DE RECONOCIMIENTO DE TOKENS------------------")
file = open('pruebaALex.xml','r')
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
with open('pruebaALex.xml','r') as myfile:
    data=myfile.read()

parser=yacc.yacc()
parser.parse(data)
print("------------------FIN DE PRUEBA DE RECONOCIMIENTO DE GRAMATICA------------------")
