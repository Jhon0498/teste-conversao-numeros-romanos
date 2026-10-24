# Teste de Conversão de Números Romanos

## Sobre o projeto

Este projeto foi desenvolvido como atividade acadêmica em Python. O objetivo é corrigir um programa que converte números romanos em números inteiros e verificar seu funcionamento por meio de testes unitários.

## Tecnologias utilizadas

- Python
- PyUnit (`unittest`)
- Git
- GitHub

## Arquivos do projeto

- `main.py`: arquivo principal do programa.
- `numeroromano.py`: contém a função que converte números romanos em inteiros.
- `testes.py`: contém os testes unitários.
- `README.md`: apresenta as informações do projeto.

## Correção realizada

Foi corrigida a função `converte(numeroEmRomano)`, responsável por transformar os numerais romanos em números inteiros.

A correção considera a regra de que símbolos menores posicionados antes de símbolos maiores devem ser subtraídos.

Por exemplo:

- `IX` corresponde a 9.
- `XXIV` corresponde a 24.

Também foi ajustado o valor do símbolo romano `M`, que representa 1000.

## Testes unitários

Foram criados seis testes utilizando a biblioteca `unittest` do Python.

| Número romano | Resultado esperado |
|---|---:|
| I | 1 |
| V | 5 |
| II | 2 |
| XXII | 22 |
| IX | 9 |
| XXIV | 24 |

Os seis testes foram executados e passaram com sucesso.

## Como executar

É necessário ter o Python instalado.

Para executar o programa:

```bash
python main.py
```

Para executar os testes unitários:

```bash
python -m unittest testes.py -v
```

O parâmetro `-v` mostra o resultado de cada teste.

## Objetivo da atividade

Praticar a identificação e correção de erros em um programa Python e aprender a utilizar testes unitários para verificar se os resultados estão corretos.

## Autor

Jhonatan Mendes Morão
