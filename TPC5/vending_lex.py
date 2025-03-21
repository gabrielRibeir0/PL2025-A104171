import ply.lex as lex

tokens = ('LISTAR', 'MOEDA', 'SELECIONAR', 'SAIR', 'VALOR', 'PROD_ID', 'VIRG')

t_LISTAR = r'LISTAR'
t_MOEDA = r'MOEDA'
t_SELECIONAR = r'SELECIONAR'
t_SAIR = r'SAIR'
t_VALOR = r'1c|2c|5c|10c|20c|50c|1e|2e'
t_PROD_ID = r'[A-Z]+[0-9]+'
t_VIRG = r','

t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()