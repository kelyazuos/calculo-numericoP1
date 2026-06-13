def regra_simpson_13(x, y):
    n = len(x)

    if (n - 1) % 2 != 0:
        return None

    h = x[1] - x[0]

    soma = y[0] + y[n - 1]

    for i in range(1, n - 1):
        if i % 2 == 0:
            soma = soma + 2 * y[i]
        else:
            soma = soma + 4 * y[i]

    resultado = (h / 3) * soma

    return resultado


x = [0.0, 0.5, 1.0, 1.5, 2.0]
y = [0, 40, 65, 80, 90]

resultado = regra_simpson_13(x, y)

print("\nRegra 1/3 de Simpson")
print("-" * 40)
print(f"Distância total percorrida: {resultado:.2f} km")