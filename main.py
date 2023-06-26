import ply.yacc as yacc
from lexico import tokens

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