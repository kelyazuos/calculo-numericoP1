import numpy as np

def euler_sir(S0, I0, R0, beta, gamma, h, t_max):
    n = int(t_max / h)

    # listas para armazenar resultados
    S = np.zeros(n)
    I = np.zeros(n)
    R = np.zeros(n)
    t = np.zeros(n)

    # condições iniciais
    S[0] = S0
    I[0] = I0
    R[0] = R0

    # loop de Euler
    for i in range(n - 1):
        dS = -beta * S[i] * I[i]
        dI = beta * S[i] * I[i] - gamma * I[i]
        dR = gamma * I[i]

        S[i + 1] = S[i] + h * dS
        I[i + 1] = I[i] + h * dI
        R[i + 1] = R[i] + h * dR

        t[i + 1] = t[i] + h

    return t, S, I, R
