# README: Problema da Sequência de Números

## Descrição do Problema

Este programa deve ler um valor inteiro \( N \) e imprimir uma sequência específica de saídas baseadas em \( N \). Para cada número de 1 até \( N \), serão impressas duas linhas que seguem um padrão matemático simples:

- A primeira linha contém o número atual, seu quadrado e seu cubo.
- A segunda linha contém o número atual, seu quadrado aumentado em 1 e seu cubo aumentado em 1.

## Especificações

### Entrada

- Um único número inteiro positivo \( N \) (1 < \( N \) < 1000).

### Saída

- Para cada número \( i \) de 1 até \( N \), imprimir:
  - A primeira linha: `i i^2 i^3`
  - A segunda linha: `i (i^2 + 1) (i^3 + 1)`

### Exemplo de Entrada

```
5
```

### Exemplo de Saída

```
1 1 1
1 2 2
2 4 8
2 5 9
3 9 27
3 10 28
4 16 64
4 17 65
5 25 125
5 26 126
```

## Implementação

A implementação do programa pode ser feita em várias linguagens de programação. Abaixo está um exemplo em Python:

```python
# Leitura do valor inteiro N
N = int(input())

# Loop para gerar as saídas
for i in range(1, N + 1):
    # Primeira linha: i, i^2, i^3
    print(f"{i} {i**2} {i**3}")
    # Segunda linha: i, i^2 + 1, i^3 + 1
    print(f"{i} {i**2 + 1} {i**3 + 1}")
```

### Instruções para Execução

1. **Entrada:** O programa solicitará um número inteiro \( N \).
2. **Saída:** O programa imprimirá a sequência de números conforme especificado.
3. **Ambiente:** O código pode ser executado em qualquer ambiente Python que suporte a versão 3.x.

## Considerações Finais

- O programa deve lidar corretamente com a formatação da saída, assegurando que todos os números sejam apresentados com espaços entre eles.
- Este problema é útil para praticar laços e formatação de strings em programação.
