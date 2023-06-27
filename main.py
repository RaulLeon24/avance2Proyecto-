import ply.yacc as yacc
from lexico import tokens



#Xavi
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



#Avance Gabriel Herrera

# Regla declaracion de funciones sin parametros
def p_funcionSinPar(p):
    '''funcion : 
    FUNC campo LPAREN RPAREN tipoDato LLLAVE cuerpo RLLAVE
      '''
    
# Definicio de campo y valor de retorno
def p_campo(p):
    '''campo : ID
    '''

def p_tipoDato(p):
    '''tipoDato : "int"
                   | "float"
                   | "string"
    '''

# Regla para cuerpo de la funcion
def p_cuerpo(p):
    '''cuerpo : 
    repetirLineas
    RETURN ID  
    '''
#Linea y su regla de produccion
def repetirLineas(p):
    '''repetirLineas : linea
                     | linea repetirLineas
    '''

def p_linea(p):
    '''
    linea : ID EQUALS expresion | ID EQUALS ID | FOR 
    
    '''

#Definicion estructura control FOR
def p_for(p):
    '''FOR : 
    FOR ID EQUALS INT PUNTOCOMA ID MENORQUE LEN LPAREN ID RPAREN PUNTOCOMA ID PLUS PLUS LLLAVE
    cuerpo
    RLLAVE
    '''

#Definicion arreglos
def p_arreglo(p):
    '''arreglo : ID LCORCHETE INT RCORCHETE tipoDato LLAVE elemArray RLLAVE
    '''
def p_elemArray(p):
    '''elemArray : numero 
                 | numero COMMA elemArray
    '''

def p_numero(p):
    '''numero : INT
                | FLOAT
        '''


#Avance Raul Leon

def p_statement_if(p):
    'statement : IF  expression  LLLAVE statements RLLAVE'
    

def p_statement_if_else(p):
    'statement : IF  expression  LLLAVE statements RLLAVE ELSE LLLAVE statements RLLAVE'

def p_expression(p):
    '''expression : expression EQUALS expression
                  | NUMBER'''

def p_statements(p):
    'statements : statements statement'


def p_statements_single(p):
    'statements : statement'


# Definición de Estructura de Datos Slices
def p_slice(p):
    'p_slice : ID LCORCHETE RCORCHETE ID'


def p_error(p):
    if p:
         print("Error de sintaxis en token:", p.type)
         #sintactico.errok()
    else:
         print("Syntax error at EOF")

# Build the parser
sintactico = yacc.yacc()

while True:
   try:
       s = input('golang > ')
   except EOFError:
       break
   if not s: continue
   result = sintactico.parse(s)
   if result!=None: print(result)


