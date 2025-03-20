import ply.lex as lex

tokens = (
    'REAL',
    'INTEGER',
    'COMMA',
    'BOOL',
    'OPEN_BRACKET',
    'CLOSE_BRACKET',
    'STRING',
)

def t_REAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_COMMA = ','
t_BOOL = r'([Ff][Aa][Ll][Ss][Ee])|([Tt][Rr][Uu][Ee])'
t_OPEN_BRACKET = r'\['
t_CLOSE_BRACKET = r'\]'
t_STRING = r'(\w+-)*\w+'

t_ignore = r' \t'

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

list = '[ 1,5, palavra, False ,3.14, 0, fim]'

lexer.input(list)

while tok := lexer.token():
    print(tok)