import ply.yacc as yacc
from lexico import tokens

def p_funcion(p):
    'funcion : func nombre_funcion LPAREN RPAREN LLLAVE declaracion RLLAVE'

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