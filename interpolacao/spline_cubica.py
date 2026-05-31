def spline_cubica_natural(x, y, xp):
    n = len(x)
    a = y.copy()

    h = []
    for i in range(n - 1):
        h.append(x[i + 1] - x[i])

    alpha = [0] * n

    for i in range(1, n - 1):
        alpha[i] = (3 / h[i]) * (a[i + 1] - a[i]) - (3 / h[i - 1]) * (a[i] - a[i - 1])

    l = [0] * n
    u = [0] * n
    z = [0] * n

    l[0] = 1
    u[0] = 0
    z[0] = 0

    for i in range(1, n - 1):
        l[i] = 2 * (x[i + 1] - x[i - 1]) - h[i - 1] * u[i - 1]
        u[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / l[i]

    l[n - 1] = 1
    z[n - 1] = 0

    c = [0] * n
    b = [0] * (n - 1)
    d = [0] * (n - 1)

    c[n - 1] = 0

    for j in range(n - 2, -1, -1):
        c[j] = z[j] - u[j] * c[j + 1]
        b[j] = ((a[j + 1] - a[j]) / h[j]) - (h[j] * (c[j + 1] + 2 * c[j]) / 3)
        d[j] = (c[j + 1] - c[j]) / (3 * h[j])

    for i in range(n - 1):
        if x[i] <= xp <= x[i + 1]:
            dx = xp - x[i]
            resultado = a[i] + b[i] * dx + c[i] * dx ** 2 + d[i] * dx ** 3
            return resultado

    return None


# Dados do exercício
x = [0.0, 1.0, 2.0, 3.0]
y = [2.5, 4.5, 3.0, 6.0]

# Ponto que queremos interpolar
xp = 1.5

valor = spline_cubica_natural(x, y, xp)

print("Valor pela Spline Cubica Natural:", valor)