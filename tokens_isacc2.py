import ply.lex as lex
import ply.yacc as yacc
import sys

tokens = [
	'SECURITY_POLICIES_OPEN', 'SECURITY_POLICIES_CLOSE', 'SECURITY_POLICY_OPEN', 'POLICY_ID', 'END_OPEN',
	'SECURITY_POLICY_CLOSE', 'POLICY_NAME_OPEN', 'POLICY_NAME_CLOSE', 'POLICY_DESCRIPTION_OPEN', 'POLICY_DESCRIPTION_CLOSE',
	'SP_OBJECTIVES_OPEN', 'SP_OBJECTIVES_CLOSE', 'SP_OBJECTIVE_OPEN', 'SP_OBJECTIVE_CLOSE',
	'SP_ADDITIONAL_INFORMATION_OPEN', 'SP_ADDITIONAL_INFORMATION_CLOSE', 'SP_COMMENT_OPEN', 'SP_COMMENT_CLOSE', 'GENERAL_COMMENT'
]
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
t_SP_OBJECTIVE_OPEN = r'<security-objectives:security-objective>'
t_SP_OBJECTIVE_CLOSE = r'</security-objectives:security-objective>'
t_SP_ADDITIONAL_INFORMATION_OPEN = r'<security-policy:additional-information>'
t_SP_ADDITIONAL_INFORMATION_CLOSE = r'</security-policy:additional-information>'
t_SP_COMMENT_OPEN = r'<additional-information:comment>'
t_SP_COMMENT_CLOSE = r'</additional-information:comment>'
t_GENERAL_COMMENT = r'(\w|\s|\(|\)|,|-|/|\[|\])+'
t_POLICY_ID = r'"(\w |-)+"'
t_END_OPEN = r'>'
t_ignore = " \n\t"


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    return

file = open('pruebaIsacc2.xml','r')
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
