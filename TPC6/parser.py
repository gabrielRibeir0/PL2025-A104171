from analex import lexer

prox_simb = ('Erro', '', 0, 0)

def parserError(simb):
    raise Exception("Erro sintático, token inesperado: " + str(simb))

def rec_term(simb):
    global prox_simb
    if prox_simb.type == simb:
        prox_simb = lexer.token()
    else:
        parserError(prox_simb)

def rec_Expr():
    l = rec_Termo()
    r = rec_Expr2(l)
    print("Reconhecido: Exp --> Termo Exp2")
    return r

def rec_Expr2(l):
    global prox_simb
    if prox_simb is None:
        return l
    elif prox_simb.type == 'ADD':
        rec_term('ADD')
        t = rec_Termo()
        res = rec_Expr2(l + t)
        print("Reconhecido: Expr' --> '+' Termo Expr'")
        return res
    elif prox_simb.type == 'SUB':
        rec_term('SUB')
        t = rec_Termo()
        res = rec_Expr2(l - t)
        print("Reconhecido: Expr' --> '-' Termo Expr'")
        return res
    elif prox_simb.type == 'PF':
        print("Reconhecido: Expr' --> ε")
        return l
    else:
        parserError(prox_simb)
        return l

def rec_Termo():
    l = rec_Fator()
    r = rec_Termo2(l)
    print("Reconhecido: Termo --> Fator Termo'")
    return r

def rec_Termo2(l):
    global prox_simb
    if prox_simb is None:
        return l
    elif prox_simb.type == 'MUL':
        rec_term('MUL')
        f = rec_Fator()
        r = rec_Termo2(l * f)
        print("Reconhecido: Termo' --> '*' Fator Termo'")
        return r
    elif prox_simb.type == 'DIV':
        rec_term('DIV')
        f = rec_Fator()
        if f == 0:
            print("Erro: Divisão por zero")
            return float('inf')
        r = rec_Termo2(l / f)
        print("Reconhecido: Termo' --> '/' Fator Termo'")
        return r
    elif prox_simb.type in ('ADD', 'SUB', 'PF'):
        print("Reconhecido: Termo' --> ε")
        return l
    else:
        parserError(prox_simb)
        return l

def rec_Fator():
    global prox_simb
    if prox_simb is None:
        return 0
    elif prox_simb.type == 'PA':
        rec_term('PA')
        e = rec_Expr()
        rec_term('PF')
        print("Reconhecido: Fator --> '(' Expr ')'")
        return e
    elif prox_simb.type == 'NUM':
        n = int(prox_simb.value)
        rec_term('NUM')
        print("Reconhecido: Fator --> NUM")
        return n
    else:
        parserError(prox_simb)
        return 0


def rec_Parser(data):
    global prox_simb
    lexer.input(data)
    prox_simb = lexer.token()
    return rec_Expr()


if __name__ == "__main__":
    expressions = [
        "2+3",
        "67 - (2 + 3 * 4)",
        "(9 - 2) * (13 - 4)",
        "10 / 2 * 5",
        "2 + 3 * 4 - 8 / 2",
        "42",
        "(5)",
        "10 / 0",
        "3 + (4",
        "3 + * 4",
        "1 2 + 3",
        ""
    ]

    for expr in expressions:
        print(f"Expressão: \"{expr}\"")
        try:
            result = rec_Parser(expr)
            print(f"Resultado: {result}")
        except Exception as e:
            print(f"{e}")
        print("-" * 15)
