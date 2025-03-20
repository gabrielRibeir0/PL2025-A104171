import ply.lex as lex

tokens = (
    'NUMBER',
    'THREE_DOTS',
    'DOT',
    'COMMA',
    'SEMI_COLLON',
    'QUESTION_MARK',
    'EXCLAMATION_MARK',
    'QUOTE',
    'SINGLE_QUOTE',
    'OPEN_QUOTE',
    'CLOSE_QUOTE',
    'OPEN_BRACKET',
    'CLOSE_BRACKET',
    'WORD',
    'HYPHEN',
)

t_NUMBER = r'-?\d+([.,]\d+)?'
t_THREE_DOTS = r'\.\.\.'
t_DOT = r'\.'
t_COMMA = r','
t_SEMI_COLLON = r';'
t_QUESTION_MARK = r'\?'
t_EXCLAMATION_MARK = r'!'
t_QUOTE = r'"'
t_SINGLE_QUOTE = r'\''
t_OPEN_QUOTE = r'«'
t_CLOSE_QUOTE = r'»'
t_OPEN_BRACKET = r'\('
t_CLOSE_BRACKET = r'\)'
t_WORD = r'(\w+-)*\w+'
t_HYPHEN = r'-'

t_ignore = r' \t'

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

sentence = "Olá! Como está? Você viu o jogo no fim-de-semana, 3-2? Foi incrível... não achas? O jogador número 10, o 'craque', fez um golo aos 90,5 minutos! Ele disse: «Vamos ganhar o próximo!» (Espero que sim.) "

lexer.input(sentence)

while tok := lexer.token():
    print(tok)