# Leitura do valor inteiro N
N = int(input())

# Loop para gerar as saídas
for i in range(1, N + 1):
    # Primeira linha: i, i^2, i^3
    print(f"{i} {i**2} {i**3}")
    # Segunda linha: i, i^2 + 1, i^3 + 1
    print(f"{i} {i**2 + 1} {i**3 + 1}")
