# TPC2

19-02-2025

![](../images/author.png)

## Identificação

- **Nome:** Gabriel Pereira Ribeiro
- **Número:** A104171

## Descrição Trabalho

No TPC2 é necessário ler e processar um dataset (sem usar o módulo csv do python) para conseguir responder às seguintes queries:

- Listar alfabeticamente os compositores musicais
- Distribuição das obras por período: quantas obras catalogadas em cada período
- Dicionário em que a cada período está a associada uma lista alfabética dos títulos das obras
desse período

O programa primeiramente lê o ficheiro csv saltando a primeira linha (headers) e depois lendo o resto do texto e separando no caracter ';'.

Depois, enquanto não chegar ao fim, são lidos de 7 em 7 campos correspondentes a uma obra fazendo a formatação necessária ao texto
e essa informação é guardada num dicionário.

Para responder às queries, existem funções para cada uma que manipulam o dicionário dos dados e geram uma estrutura com os dados a serem apresentados.

## Resultados

- Programa [processor.py](https://github.com/gabrielRibeir0/PL2025-A104171/blob/main/TPC2/processor.py)
