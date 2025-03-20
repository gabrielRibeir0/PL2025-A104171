import ply.yacc as yacc
from calc_lex import tokens

def p_op_1(p):
    'op : calc'
    p[0] = p[1]

def p_op_2(p):
    'op : op PLUS calc'
    p[0] = p[1] + p[3]

def p_op_3(p):
    'op : op MINUS calc'
    p[0] = p[1] - p[3]

# operação para divisão e multiplicação, que têm prioridade
# o parser verifica primeiro match à direita (LR1)
def p_calc_1(p):
    'calc : expr'
    p[0] = p[1]

def p_calc_2(p):
    'calc : calc TIMES expr'
    p[0] = p[1] * p[3]

def p_calc_3(p):
    'calc : calc DIVIDE expr'
    p[0] = p[1] / p[3]

# operação para parentesis
def p_expr_1(p):
    'expr : NUMBER'
    p[0] = p[1]

def p_expr_2(p):
    'expr : LPAREN op RPAREN'
    p[0] = p[2]

def p_error(p):
    print('Erro de sintaxe')

parser = yacc.yacc()
r = parser.parse('3 + 2 + 1+4')
print('Resultado:', r)
print(f'Resultado: {parser.parse('3 - 2 - 1')}')
print(f'Resultado: {parser.parse('3 + 2 - 4')}')
print(f'Resultado: {parser.parse('3 + 2 * 4')}')
print(f'Resultado: {parser.parse('3 / 3 - 4')}')
print(f'Resultado: {parser.parse('(3 + 2) * 4')}')
print(f'Resultado: {parser.parse('3 / (2 * 4)')}')
print(f'Resultado: {parser.parse('(3 + 2) / 4')}')
print(f'Resultado: {parser.parse('3 + (* * 4)')}')