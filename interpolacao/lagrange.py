def lagrange(x, y, xp):

    n = len(x)

    resultado = 0


    for i in range(n):

        termo = y[i]


        for j in range(n):

            if j != i:

                termo = termo * ((xp - x[j]) / (x[i] - x[j]))


        resultado = resultado + termo


    return resultado



# valores de x
x = [1.0, 2.0, 3.0, 4.0, 5.0]

# valores de y
y = [1.2, 1.9, 3.2, 5.5, 8.2]

# ponto que queremos descobrir
xp = 3.5


valor = lagrange(x, y, xp)


print("Valor interpolado:", valor)