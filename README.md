# XML pseudo compilador o analizador utilizando la herramienta PLY

- SingleNodeAnalizer --> Contiene una version final incompleta pero funcional(respaldo)  
- MultiNodeAnalizer --> Contiene una version final completa capaz de analizar lexica y gramaticamente el archivo XML dado o cualquier otro con la misma estructura y tags(Security tree del profesor Villalon)
  
  
**Overview:** Programa que recibe como entrada un archivo XML con una estructura especifica(en este caso un proyecto de seguridad de un profesor) y lo analiza lexica y gramaticamente usando la libreria de python PLY(Lex & yacc), por ultimo con esta misma herramienta forma un arbol recursivo con el que recoge toda la informacion del documento y la despliega al usuario
