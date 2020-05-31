
import sys
import ply.lex as lex
import ply.yacc as yacc
tokens = (
    'DATA',
    'NODE_SECUOBJ_OPEN',
    'NODE_SECUOBJ_CLOSE',
    'SECUOBJ_OBJ_OPEN',
    'SECUOBJ_OBJ_CLOSE',
    'SECUOBJ_NAME_OPEN',
    'SECUOBJ_NAME_CLOSE',
    'SECUOBJ_DESCRIP_OPEN',
    'SECUOBJ_DESCRIP_CLOSE',
    'SECUOBJ_OBJTYPE_OPEN',
    'SECUOBJ_OBJTYPE_CLOSE',
    'SECUOBJ_SECUSERV_OPEN',
    'SECUOBJ_SECUSERV_CLOSE',
    'SECUOBJ_TEMP_OPEN',
    'SECUOBJ_TEMP_CLOSE',
    'SECUOBJ_ADDINFO_OPEN',
    'SECUOBJ_ADDINFO_CLOSE',
    'SECUOBJ_ADDINFOCOMM_OPEN',
    'SECUOBJ_ADDINFOCOMM_CLOSE',
    'SECUOBJ_OBJSOUR_OPEN',
    'SECUOBJ_OBJSOUR_CLOSE',

)

# TOKENS RONNY
t_DATA = r'[a-zA-Z0-9_\s,./:,ó]+\s?-?\s?[a-zA-Z0-9_\s,./:,ó]*'
t_NODE_SECUOBJ_OPEN=r'<node:security-objectives>'
t_NODE_SECUOBJ_CLOSE=r'</node:security-objectives>'
t_SECUOBJ_OBJ_OPEN=r'<security-objectives:security-objective\sobjective-id="\w\w\[\d]\[\d]">'
t_SECUOBJ_OBJ_CLOSE=r'</security-objectives:security-objective>'
t_SECUOBJ_NAME_OPEN = r'<security-objective:name>'
t_SECUOBJ_NAME_CLOSE = r'</security-objective:name>'
t_SECUOBJ_DESCRIP_OPEN=r'<security-objective:description>'
t_SECUOBJ_DESCRIP_CLOSE=r'</security-objective:description>'
t_SECUOBJ_OBJTYPE_OPEN=r'<security-objective:objective-type>'
t_SECUOBJ_OBJTYPE_CLOSE=r'</security-objectives:objective-type>'
t_SECUOBJ_SECUSERV_OPEN=r'<security-objective:security-service>'
t_SECUOBJ_SECUSERV_CLOSE=r'</security-objective:security-service>'
t_SECUOBJ_TEMP_OPEN=r'<security-objective:temporality>'
t_SECUOBJ_TEMP_CLOSE=r'</security-objective:temporality>'
t_SECUOBJ_ADDINFO_OPEN=r'<security-objective:additional-information>'
t_SECUOBJ_ADDINFO_CLOSE=r'</security-objective:additional-information>'
t_SECUOBJ_ADDINFOCOMM_OPEN=r'<additional-information:comment>'
t_SECUOBJ_ADDINFOCOMM_CLOSE=r'</additional-information:comment>'
t_SECUOBJ_OBJSOUR_OPEN=r'<security-objective:objective-source>'
t_SECUOBJ_OBJSOUR_CLOSE=r'</security-objectives:objective-source>'
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
                              | security_additional_information security_objective_obj
                              | security_objective_source security_objective_obj
                              | SECUOBJ_OBJ_CLOSE'''

def p_security_objective_name(t):
    'security_objective_name : SECUOBJ_NAME_OPEN DATA SECUOBJ_NAME_CLOSE'
    print("Nombre del objetivo", t[2])


def p_security_objective_description(t):
    'security_objective_description : SECUOBJ_DESCRIP_OPEN DATA SECUOBJ_DESCRIP_CLOSE'
    print("Descripcion: ", t[2])



def p_security_objective_objective_type(t):
    'security_objective_objective_type : SECUOBJ_OBJTYPE_OPEN DATA SECUOBJ_OBJTYPE_CLOSE'
    print("Tipo de objetivo: ",t[2])


def p_security_objective_security_service(t):
    'security_objective_security_service : SECUOBJ_SECUSERV_OPEN DATA SECUOBJ_SECUSERV_CLOSE'
    print("security-service: ",t[2])


def p_security_objective_temporality(t):
    'security_objective_temporality : SECUOBJ_TEMP_OPEN DATA SECUOBJ_TEMP_CLOSE'
    print("temporality: ", t[2])



def p_security_additional_information(t):
    'security_additional_information : SECUOBJ_ADDINFO_OPEN security_additional_information_Comment SECUOBJ_ADDINFO_CLOSE'



def p_security_additional_information_Comment(t):
    'security_additional_information_Comment : SECUOBJ_ADDINFOCOMM_OPEN SECUOBJ_ADDINFOCOMM_CLOSE'


def p_security_objective_source(t):
    'security_objective_source : SECUOBJ_OBJSOUR_OPEN DATA SECUOBJ_OBJSOUR_CLOSE'
    print("objective-source: ",t[2])


def p_error(t):
    print("Syntax error at '%s'" % t.value)


print("------------------RECONOCIMIENTO DE TOKENS------------------")
file = open('PruebasecurityObjec.xml','r')
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
with open('PruebasecurityObjec.xml', 'r') as myfile:
    data=myfile.read()

parser=yacc.yacc()
parser.parse(data)