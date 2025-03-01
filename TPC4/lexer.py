import ply.lex as lex

tokens = (
    'SELECT',
    'WHERE',
    'LIMIT',
    'DOT',
    'LCB', #Left Curly Bracket
    'RCB', #Right Curly Bracket
    'VAR',
    'LANG',
    'URI',
    'A',
    'NUMBER',
    'COMMENT',
    'STRING',
)

t_SELECT = r'[sS][eE][lL][eE][cC][tT]'
t_WHERE = r'[wW][hH][eE][rR][eE]'
t_LIMIT = r'[lL][iI][mM][iI][tT]'
t_DOT = r'\.'
t_LCB = r'\{'
t_RCB = r'\}'

def t_VAR(t):
    r'\?[a-z]+'
    t.value = t.value.strip('?')
    return t

t_LANG = r'@[a-z\-]+'
t_URI = r'[a-z]+:[a-zA-Z0-9]+'
t_A = r'a'
t_COMMENT = r'\#.*'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\"[\w\s]*\"'
    t.value = t.value.strip('\"')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

data = '''
# DBPedia: obras de Chuck Berry

select ?nome ?desc where {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en .
    ?w dbo:artist ?s.
    ?w foaf:name ?nome.
    ?w dbo:abstract ?desc
} LIMIT 1000 # Limite de 1000 resultados
<
'''

lexer.input(data)

for tok in lexer:
    print(tok)