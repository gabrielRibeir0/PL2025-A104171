from analex import lexer, tokens

tokens_list = []
next_token = None

def advance():
    global next_token
    current_token_index += 1
    if current_token_index < len(tokens_list):
        current_token = tokens_list[current_token_index]
    else:
        current_token = None

def match(expected_token_type):
    global current_token
    if current_token and current_token.type == expected_token_type:
        token_value = current_token.value
        advance()
        return token_value
    else:
        expected = expected_token_type
        found = current_token.type if current_token else 'FIM'
        line = current_token.lineno if current_token else 'desconhecida'
        raise Exception(f"Erro de sintaxe na linha {line}: Esperado '{expected}', encontrado '{found}'")

def p_expr_1():
    """Expr -> Termo Expr'"""
    left_value = p_termo_1()
    return p_expr_2(left_value)

def p_expr_2(left_value):
    """Expr' -> ADD Termo Expr' | SUB Termo Expr' | epsilon"""
    global current_token
    if current_token and current_token.type == 'ADD':
        match('ADD')
        right_value = p_termo_1()
        result = left_value + right_value
        return p_expr_2(result)
    elif current_token and current_token.type == 'SUB':
        match('SUB')
        right_value = p_termo_1()
        result = left_value - right_value
        return p_expr_2(result)
    else:
        return left_value

def p_termo_1():
    """Termo -> Fator Termo'"""
    left_value = p_fator()
    return p_termo_2(left_value)

def p_termo_2(left_value):
    """Termo' -> MUL Fator Termo' | DIV Fator Termo' | epsilon"""
    global current_token
    if current_token and current_token.type == 'MUL':
        match('MUL')
        right_value = p_fator()
        result = left_value * right_value
        return p_termo_2(result)
    elif current_token and current_token.type == 'DIV':
        match('DIV')
        right_value = p_fator()
        if right_value == 0:
            raise Exception("Erro: Divisão por zero!")
        result = left_value / right_value
        return p_termo_2(result)
    else:
        return left_value

def p_fator():
    """Fator -> NUM | PA Expr PF"""
    global current_token
    if current_token and current_token.type == 'NUM':
        value = match('NUM')
        return value
    elif current_token and current_token.type == 'PA':
        match('PA')
        expr_value = p_expr_1()
        match('PF')
        return expr_value
    else:
        found = current_token.type if current_token else 'FIM'
        line = current_token.lineno if current_token else 'desconhecida'
        raise Exception(f"Erro de sintaxe na linha {line}: Esperado 'NUM' ou 'PA', encontrado '{found}'")

def parse(input_string):
    global current_token_index, current_token, tokens_list
    lexer.input(input_string)
    tokens_list[:] = list(lexer)
    print(f"Tokens: {tokens_list}")

    if not tokens_list:
        return 0

    advance()

    final_result = p_expr_1()

    if current_token is not None:
        raise Exception(f"Erro de sintaxe: Token inesperado '{current_token.value}' ({current_token.type}) no final da expressão.")

    return final_result


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
            result = parse(expr)
            print(f"Resultado: {result}")
        except Exception as e:
            print(f"{e}")
        print("-" * 15)
