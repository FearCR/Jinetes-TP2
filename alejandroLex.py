import ply.lex as lex
import ply.yacc as yacc
import sys
#xml start and Basic info
tokens=[
    'BASIC_INFORMATION_OPEN',
    'BASIC_INFORMATION_CLOSE',
    'COMPONENT_NAME_OPEN',
    'COMPONENT_NAME_CLOSE',
    'COMPONENT_OVERVIEW_OPEN',
    'COMPONENT_OVERVIEW_CLOSE',
    'COMPONENT_CATEGORIES_OPEN',
    'COMPONENT_CATEGORIES_CLOSE',
    'COMPONENT_CATEGORY_OPEN',
    'COMPONENT_CATEGORY_CLOSE',
    'INTRINSICAL_PROPERTIES_OPEN',
    'INTRINSICAL_PROPERTIES_CLOSE',
    'PROPERTIES_COLOR_OPEN',
    'PROPERTIES_COLOR_CLOSE',
    'PROPERTIES_MATERIAL_OPEN',
    'PROPERTIES_MATERIAL_CLOSE',
    'PROPERTIES_HEIGHT_OPEN',
    'PROPERTIES_HEIGHT_CLOSE',
    'PROPERTIES_WEIGHT_OPEN',
    'PROPERTIES_WEIGHT_CLOSE',
    'PROPERTIES_OTHER_OPEN',
    'PROPERTIES_OTHER_CLOSE',
    'STRING'

]

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
t_STRING=r'[a-zA-Z0-9_\s,./]+'
# Ignored characters
t_ignore = " \n\t"

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

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
