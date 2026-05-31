def regra_trapezios(x, y):
    n = len(x)
    soma = 0

    for i in range(n - 1):
        h = x[i + 1] - x[i]
        area = (h / 2) * (y[i] + y[i + 1])
        soma = soma + area

    return soma


# Dados do exercício
x = [0.0, 0.5, 1.0, 1.5, 2.0]
y = [0, 40, 65, 80, 90]

resultado = regra_trapezios(x, y)

print("\nRegra dos Trapézios")
print("-" * 40)
print(f"Distância total percorrida: {resultado:.2f} km")