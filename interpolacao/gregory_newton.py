def gregory_newton(x, y, xp):
    n = len(y)
    h = x[1] - x[0]
    u = (xp - x[0]) / h

    diferencas = [y.copy()]

    for i in range(1, n):
        linha = []
        for j in range(n - i):
            valor = diferencas[i - 1][j + 1] - diferencas[i - 1][j]
            linha.append(valor)
        diferencas.append(linha)

    resultado = y[0]
    termo = 1

    for i in range(1, n):
        termo = termo * (u - (i - 1)) / i
        resultado = resultado + termo * diferencas[i][0]

    return resultado


# Dados do exercício
x = [10, 20, 30, 40]
y = [45.0, 52.0, 60.0, 71.0]

# Ponto que queremos estimar
xp = 25

valor = gregory_newton(x, y, xp)

print("Temperatura estimada no minuto 25:", valor)