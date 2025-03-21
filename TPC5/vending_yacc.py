import json
import ply.yacc as yacc
from datetime import date
from vending_lex import tokens

produtos = {}
saldo = 0

def p_comando(p):
    '''comando : listar
                | selecionar
                | moeda
                | sair
    '''
    p[0] = p[1]

def p_listar(p):
    'listar : LISTAR'
    print('Código | Nome | Quantidade | Preço')
    for k, v in produtos.items():
        print(f'{k} | {v['nome']} | {v['quant']} | {v['preco']}')

def p_selecionar(p):
    'selecionar : SELECIONAR PROD_ID'
    global saldo

    if p[2] not in produtos or produtos[p[2]]['quant'] <= 0:
        print('maq: Produto inexistente')
        return
    
    if saldo >= produtos[p[2]]['preco']:
        saldo -= produtos[p[2]]['preco']
        produtos[p[2]]['quant'] -= 1
        print(f'maq: Pode retirar o produto dispensado "{produtos[p[2]]["nome"]}"')
        print(f'maq: Saldo restante = {saldo_to_str()}')
    else:
        print(f'maq: Saldo insuficiente (saldo = {saldo_to_str()}, preço = {produtos[p[2]]["preco"]})')
        return

def p_sair(p):
    'sair : SAIR'
    troco = calcula_troco()
    print('maq: Pode retirar o troco', end=' ')
    for moeda in troco:
        print(moeda, end=', ')
    
    with open('stock.json', 'w', encoding='utf-8') as f:
        json.dump(produtos, f, ensure_ascii=False, indent=4)

    print('Até à próxima!')
    exit()

def p_moeda(p):
    'moeda : MOEDA moedas'
    global saldo
    saldo += sum(map(get_valor_moeda, p[2]))
    print(f'maq: Saldo atual = {saldo_to_str()}')

def p_moedas(p):
    '''moedas : VALOR
                | VALOR VIRG moedas
    '''
    p[0] = [p[1]]
    if len(p) > 2:
        p[0] += p[3]

def p_error(p):
    raise Exception

def get_valor_moeda(moeda):
    valor = int(moeda[:-1])
    grandeza = moeda[-1]
    if grandeza == 'c':
        return valor/100
    elif grandeza == 'e':
        return valor

def saldo_to_str():
    i, d = divmod(saldo, 1)
    return f'{int(i)}e{int(d*100)}c'

def calcula_troco():
    global saldo
    troco = []
    epsilon = 1e-9
    while saldo >= epsilon:
        for moeda in ['2e', '1e', '50c', '20c', '10c', '5c', '2c', '1c']:
            valor = get_valor_moeda(moeda)
            if saldo >= valor - epsilon:
                saldo -= valor
                troco.append(moeda)
                break
    return troco

parser = yacc.yacc()

if __name__ == '__main__':
    with open('stock.json', 'r', encoding='utf-8') as f:
        produtos = json.load(f)
    
    print(f'maq: {date.today()}, Stock carregado, Estado atualizado.')
    print('maq: Bom dia. Estou disponível para atender o seu pedido.')
    while True:
        try:
            inp = input('>> ')
            parser.parse(inp)
        except Exception as e:
            print('Erro no input: ' + str(e))
            continue