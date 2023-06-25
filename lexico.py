import ply.lex as lex

#Algoritmo Raul Leon

#func factorial(n int) int {
#    if n == 0 {
#        return 1
#    }
#    return n * factorial(n-1)
#}

#func main() {
#    number := 5
#    result := factorial(number)
#}

#Algortimo Pablo Herrera

#func Maximo() int {
# max:=nums[0]
# for i:=1;i<len(nums);i++{
#   if nums[i]>max{
#     max=nums[i]
#   }
# }
# return max
#}



#Algoritmo Xavier Cobos
#Realice mi aporte en Replit, así que lo pase directamente a este trabajo colaborativo c:
#https://replit.com/@XavierCobos/TurboLinedSpof#main.py

# package main
# import (
#     "fmt"
#     "math"
# )
# func calcularAreaCirculo(radio float64) float64 {
#     return math.Pi * math.Pow(radio, 2)
# }
# func main() {
#     radio := 5.0
#     area := calcularAreaCirculo(radio)
#     fmt.Printf("El área del círculo con radio %.2f es %.2f\n", radio, area)
# }


#Diccionario de palabras reservadas
reserved = {'while': 'WHILE','if': 'IF', 'func': 'FUNC', 'return': 'RETURN','for':'FOR','len':'LEN', 'package':'PACKAGE', 'main':'MAIN', 'printf':'PRINTF', 'switch':'SWITCH', 'case':'CASE',}

#Sequencia de tokens, puede ser lista o tupla
tokens = ('INT', 'FLOAT', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN',
          'RPAREN', 'ID', 'EQUALS', 'COMPARE', 'LLLAVE', 'RLLAVE', 'EQUALSVAR','LCORCHETE','RCORCHETE','PUNTOCOMA','MENORQUE','MAYORQUE','COMMA','PERIOD', 'STR', 'PALABRA', 'XCENTAJE', 'CADENA') + tuple(
            reserved.values())

#Exp Regulares para tokens de símbolos
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_INT = r'(-)?\d+'
t_FLOAT = r'(-)?\d+\.\d+'
t_EQUALS = r'='

#Raul Leon
t_COMPARE = r'=='
t_LLLAVE = r'\{'
t_RLLAVE = r'\}'
t_EQUALSVAR = r':='

#Pablo Herrera
t_LCORCHETE=r'\['
t_RCORCHETE=r'\]'
t_PUNTOCOMA=r'\;'
t_MENORQUE=r'\<'
t_MAYORQUE=r'\>'

#Xavier Cobos
t_COMMA      = r','
t_PERIOD     = r'\.'
t_STR        = r'"[^".]*"'
t_XCENTAJE   = r'\%'
t_CADENA     = r'\"[^\"]*\"'

#palabras con tilde
def t_PALABRA(t):
    r'[a-zA-ZáéíóúÁÉÍÓÚ]+'
    t.value = t.value.lower()
    return t

#Para contabilizar nro de líneas
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)


def t_ID(t):
  r'[a-zA-Z_]\w*'
  t.type = reserved.get(t.value, 'ID')
  return t


# Ignorar lo que no sea un token en mi LP
t_ignore = ' \t'


#Presentación de errores léxicos
def t_error(t):
  print("Componente léxico no reconocido '%s'" % t.value[0])
  t.lexer.skip(1)


def t_COMMENT(t):
  r'\/\/.*'
  pass


#Contruir analizador
lexer = lex.lex()

#Testeando
data = '''
        package main

import (
    "fmt"
    "math"
)

func calcularAreaCirculo(radio float64) float64 {
    return math.Pi * math.Pow(radio, 2)
}

func main() {
    radio := 5.0
    area := calcularAreaCirculo(radio)
    fmt.Printf("El área del círculo con radio %.2f es %.2f\n", radio, area)
}
      '''

#Datos de entrada
lexer.input(data)

# Tokenizador
while True:
  tok = lexer.token()
  if not tok:
    break  #Rompe
  print(tok)