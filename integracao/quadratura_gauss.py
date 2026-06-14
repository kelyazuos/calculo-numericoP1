def funcao(x):
    return 5 * x**3 + x**2 - 12 * x + 4


def quadratura_gauss(funcao, a, b, n_pontos):
    if n_pontos == 2:
        pontos = [-1 / (3 ** 0.5), 1 / (3 ** 0.5)]
        pesos = [1, 1]
    elif n_pontos == 3:
        pontos = [-(3 / 5) ** 0.5, 0, (3 / 5) ** 0.5]
        pesos = [5 / 9, 8 / 9, 5 / 9]
    else:
        return None

    soma = 0

    for i in range(n_pontos):
        x_transformado = ((b - a) / 2) * pontos[i] + ((a + b) / 2)
        soma = soma + pesos[i] * funcao(x_transformado)

    resultado = ((b - a) / 2) * soma

    return resultado


# Dados do problema
a = -1
b = 1
n_pontos = 2

resultado = quadratura_gauss(funcao, a, b, n_pontos)

print("\nQuadratura de Gauss")
print("-" * 40)
print(f"Trabalho total no intervalo [{a}, {b}]: {resultado:.2f}")