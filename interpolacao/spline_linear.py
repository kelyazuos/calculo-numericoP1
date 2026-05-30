def spline_linear(x, y, xp):
    for i in range(len(x) - 1):
        if x[i] <= xp <= x[i + 1]:
            resultado = y[i] + ((y[i + 1] - y[i]) / (x[i + 1] - x[i])) * (xp - x[i])
            return resultado

    return None


# Dados do exercício
x = [0.0, 1.0, 2.0, 3.0]
y = [2.5, 4.5, 3.0, 6.0]

# Ponto que queremos interpolar
xp = 1.5

valor = spline_linear(x, y, xp)

print("Valor pela Spline Linear:", valor)