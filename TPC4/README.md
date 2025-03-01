# TPC4

01-03-2025

![](../images/author.png)

## Identificação

- **Nome:** Gabriel Pereira Ribeiro
- **Número:** A104171

## Descrição Trabalho

No TPC4 o objetivo é construir um analisador léxico para SPARQL:

```sql
# DBPedia: obras de Chuck Berry

select ?nome ?desc where {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en .
    ?w dbo:artist ?s.
    ?w foaf:name ?nome.
    ?w dbo:abstract ?desc
} LIMIT 1000
```

O primeiro passo é identificar os tokens presentes na linguagem (a partir do exemplo dado):

```sql
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
```

Depois, com recurso à biblioteca [PLY](https://www.dabeaz.com/ply/ply.html) apenas é preciso usar o lexer disponibilizado para identificar os tokens no texto.

Também foram definidas algumas funções para processar alguns tokens de forma especial (NUMBER (transformar em int), VAR (separar o '?'), STRING (separar as '""')).

Para além dos tokens identificados também há definições para o caracter '\n', caracteres ignorados (' ' e '\t') e, em último caso, erro.

## Resultados

Analisador léxico [lexer.py](https://github.com/gabrielRibeir0/PL2025-A104171/blob/main/TPC3/lexer.py)