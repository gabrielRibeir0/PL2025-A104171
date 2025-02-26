# TPC4

26-02-2025

![](../images/author.png)

## Identificação

- **Nome:** Gabriel Pereira Ribeiro
- **Número:** A104171

## Descrição Trabalho

No TPC4 o objetivo é construir um analisador léxico para uma linguagem de query do estilo:

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

## Resultados

Analisador léxico [lexer.py](https://github.com/gabrielRibeir0/PL2025-A104171/blob/main/TPC3/lexer.py)