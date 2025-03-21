# TPC5

15-03-2025

![](../images/author.png)

## Identificação

- **Nome:** Gabriel Pereira Ribeiro
- **Número:** A104171

## Descrição Trabalho

No TPC5 a tarefa é construir uma máquina de venda com recurso ao PLY.

Deve suportar interações do género:

```md
maq: 2024-03-08, Stock carregado, Estado atualizado.
maq: Bom dia. Estou disponível para atender o seu pedido.

>> LISTAR
maq:
cod | nome | quantidade | preço
---------------------------------
A23 água 0.5L 8 0.7
...

>> MOEDA 1e, 20c, 5c, 5c .
maq: Saldo = 1e30c

>> SELECIONAR A23
maq: Pode retirar o produto dispensado "água 0.5L"
maq: Saldo = 60c

>> SELECIONAR A23
maq: Saldo insufuciente para satisfazer o seu pedido
maq: Saldo = 60c; Pedido = 70c

>> SAIR
maq: Pode retirar o troco: 1x 50c, 1x 20c e 2x 2c.
maq: Até à próxima
```

O stock da máquina é persistido num ficheiro JSON e é carregado e guardado ao ligar e sair da máquina.

## Resultados

- Stock da mágina [stock.json](https://github.com/gabrielRibeir0/PL2025-A104171/blob/main/TPC5/stock.json)
- Analisador léxico [vending_lex.py](https://github.com/gabrielRibeir0/PL2025-A104171/blob/main/TPC5/vending_lex.py)
- Analisador sintático [vending_yacc.py](https://github.com/gabrielRibeir0/PL2025-A104171/blob/main/TPC5/vending_yacc.py)
