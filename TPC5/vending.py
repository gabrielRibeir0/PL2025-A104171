import json
import ply.lex as lex
import sys

balance = 0
products = []
stock = None
selection_mode = False

tokens = ('LISTAR', 'MOEDA', 'SELECIONAR', 'SAIR', 'VALOR', 'PROD_ID')

def t_SELECIONAR(t):
    r'SELECIONAR'
    selection_mode = True
    return t

def t_SAIR(t):
    r'SAIR'
    print('maq: Até à próxima')
    sys.exit(0)

def t_PROD_ID(t):
    r'[A-Z]+[0-9]+'
    if selection_mode and t.value in stock:
        products.append(t.value)
        

t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

if __name__ == '__main__':
    with open('stock.json', 'r') as f:
        stock = json.load(f)
    while True:
        machine_input = input('-> ')
        lexer.input(machine_input)
        for tok in lexer:
            lexer.token()