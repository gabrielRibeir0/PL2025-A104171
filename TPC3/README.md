# TPC3

26-02-2025

![](../images/author.png)

## Identificação

- **Nome:** Gabriel Pereira Ribeiro
- **Número:** A104171

## Descrição Trabalho

No TPC3 o objetivo é criar um conversor de MarkDown para HTML.

Para isso, é necessário identificar os elementos mais básicos da linguagem a transformar:

- **Cabeçalhos**: linhas iniciadas por "# texto", ou "## texto" ou "### texto"
- **Bold**: pedaços de texto entre "**"
- **Itálico**: pedaços de texto entre "*"
- **Lista numerada**
- **Link**: [texto](endereço URL)
- **Imagem**: ![texto alternativo](path para a imagem)

O texto em Markdown está em memória guardado numa string.

Inicialmente, o programa separa as várias linhas do texto.
Depois, para cada linha são executadas as várias funções para tratar os tipos identificados.

Cada função tem uma expressão regular correspondente ao seu elemento e procura substituir o texto na linha.
Destaque para o funcionamento da função *check_list* que utiliza um *bool* para gerir o início e fim da lista.

Por fim, as linhas transformadas são novamente concatenadas e o texto HTML é apresentado ao utilizador.

Uma funcionalidade opcional implementada é a de abrir o ficheiro HTML no browser para visualizar o resultado.
Para isso é apresentado um *input* ao utilizador de **(y/n)**.

## Resultados

- Conversor [converter.py](https://github.com/gabrielRibeir0/PL2025-A104171/blob/main/TPC3/converter.py)
- Ficheiro temporário HTML (opcional) [temp.html](https://github.com/gabrielRibeir0/PL2025-A104171/blob/main/TPC3/temp.html)
