def regra_38_simpson(x, y):
    h = x[1] - x[0]

    resultado = (3 * h / 8) * (y[0] + 3 * y[1] + 3 * y[2] + y[3])

    return resultado


# Dados do problema

x = [0, 2, 4, 6]
y = [10, 15, 12, 8]

resultado = regra_38_simpson(x, y)

print("\nRegra 3/8 de Simpson - Newton-Cotes")
print("-" * 40)
print(f"Total de dados transferidos: {resultado:.2f} MB")