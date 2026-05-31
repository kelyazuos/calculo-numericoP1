def calcular_mmq(x, y):
    n = len(x)

    soma_x = sum(x)
    soma_y = sum(y)
    soma_xy = 0
    soma_x2 = 0

    for i in range(n):
        soma_xy = soma_xy + x[i] * y[i]
        soma_x2 = soma_x2 + x[i] ** 2

    a = (n * soma_xy - soma_x * soma_y) / (n * soma_x2 - soma_x ** 2)
    b = (soma_y - a * soma_x) / n

    return a, b


# Dados do exercício
x = [8, 9, 10, 11, 12]
y = [2.1, 2.8, 3.1, 4.0, 4.8]

# Calcular coeficientes da reta
a, b = calcular_mmq(x, y)

# Prever tráfego às 13h
xp = 13
previsao = a * xp + b

print("\nMétodo dos Mínimos Quadrados")
print("-" * 30)

print(f"Equação da reta: P1(x) = {a:.2f}x + {b:.2f}")
print(f"Tráfego previsto às 13h: {previsao:.2f}")