import ply.lex as lex

states = (
    ('somadoron', 'inclusive'),
)

tokens = (
    'NUMBER',
    'ON',
    'OFF',
    'EQUALS',
)

def t_somadoron_NUMBER(t):
    r'-?\d+'
    t.value = int(t.value)
    t.somador += t.value
    return t

def t_NUMBER(t):
    r'-?\d+'
    t.value = int(t.value)
    return t

def t_ON(t):
    r'(?i:on)'
    t.lexer.begin('somadoron')
    return t

def t_OFF(t):
    r'(?i:off)'
    return t

def t_EQUALS(t):
    r'='
    print(t.lexer.somador)
    return t

t_ignore = r' \t'

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()
lexer.somador = 0

text = 'sjkahdg45  asldkjh siadohj2025-02-07=OFfasd789 43oN2jkshad5='
text2 = 'ON 3 5 OFF 2 ='

lexer.input(text2)

while tok := lexer.token():
    print(tok)