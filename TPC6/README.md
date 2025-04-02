# TPC5

02-04-2025

![](../images/author.png)

## Identificação

- **Nome:** Gabriel Pereira Ribeiro
- **Número:** A104171

## Descrição Trabalho

O TPC6 consiste em fazer um parser LL(1) recursivo descendente que reconheça expressões aritméticas do estilo abaixo e calcule o respetivo valor.

Exemplos de algumas frases:

```txt
2+3
67-(2+3*4)
(9-2)*(13-4)
```

Gramática adequada a LL(1) desenvolvida:

```txt
Expr   -> Termo Expr'
Expr'  -> ADD Termo Expr' 
        | SUB Termo Expr' 
        | epsilon
Termo   -> Factor Term'
Termo'  -> MUL Fator Term' 
         | DIV Fator Term' 
         | epsilon
Fator -> NUM 
       | PA Expr PF
```

## Resultados

- Analisador Léxico [analex.py](https://github.com/gabrielRibeir0/PL2025-A104171/blob/main/TPC6/analex.py)

- Analisador Sintático [anasin.py](https://github.com/gabrielRibeir0/PL2025-A104171/blob/main/TPC6/anasin.py)
