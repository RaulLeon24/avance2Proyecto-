import ply.yacc as yacc
from lexer import tokens

# Regla de inicio para el analizador sintáctico
def p_program(p):
    '''program : package_decl import_decl func_decl'''
    p[0] = p[1], p[2], p[3]  # Retorna los resultados de las subreglas

# Reglas gramaticales adicionales para package_decl, import_decl y func_decl

# Regla para package_decl
def p_package_decl(p):
    '''package_decl : PACKAGE IDENTIFIER SEMICOLON'''
    p[0] = p[2]  # Retorna el nombre del paquete

# Regla para import_decl
def p_import_decl(p):
    '''import_decl : IMPORT import_spec'''
    p[0] = p[2]  # Retorna las especificaciones de importación

# Reglas adicionales para import_spec y func_decl

# Error handling (opcional)
def p_error(p):
    if p:
        print(f"Error de sintaxis en el token '{p.value}'")
    else:
        print("Error de sintaxis en la entrada")

# Construir el analizador sintáctico
parser = yacc.yacc()

# Ejemplo de uso
code = '''
package main;

import "fmt";

func main() {
    fmt.Println("Hola, mundo!");
}
'''

result = parser.parse(code)
print(result)
