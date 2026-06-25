import numpy as np

def rk4_sir(S0, I0, R0, beta, gamma, h, t_max):
    n = int(t_max / h)

    S = np.zeros(n)
    I = np.zeros(n)
    R = np.zeros(n)
    t = np.zeros(n)

    S[0] = S0
    I[0] = I0
    R[0] = R0

    for i in range(n - 1):
        # k1 (Inclinação no início do intervalo - equivalente ao Euler)
        k1_S = -beta * S[i] * I[i]
        k1_I = beta * S[i] * I[i] - gamma * I[i]
        k1_R = gamma * I[i]

        # k2 (Inclinação no ponto médio usando k1)
        S_k2 = S[i] + (h / 2) * k1_S
        I_k2 = I[i] + (h / 2) * k1_I
        
        k2_S = -beta * S_k2 * I_k2
        k2_I = beta * S_k2 * I_k2 - gamma * I_k2
        k2_R = gamma * I_k2

        # k3 (Inclinação no ponto médio usando k2)
        S_k3 = S[i] + (h / 2) * k2_S
        I_k3 = I[i] + (h / 2) * k2_I

        k3_S = -beta * S_k3 * I_k3
        k3_I = beta * S_k3 * I_k3 - gamma * I_k3
        k3_R = gamma * I_k3

        # k4 (Inclinação no final do intervalo usando k3)
        S_k4 = S[i] + h * k3_S
        I_k4 = I[i] + h * k3_I

        k4_S = -beta * S_k4 * I_k4
        k4_I = beta * S_k4 * I_k4 - gamma * I_k4
        k4_R = gamma * I_k4

        # Atualização dos valores usando a média ponderada das inclinações
        S[i + 1] = S[i] + (h / 6) * (k1_S + 2 * k2_S + 2 * k3_S + k4_S)
        I[i + 1] = I[i] + (h / 6) * (k1_I + 2 * k2_I + 2 * k3_I + k4_I)
        R[i + 1] = R[i] + (h / 6) * (k1_R + 2 * k2_R + 2 * k3_R + k4_R)

        # Atualização do tempo
        t[i + 1] = t[i] + h

    return t, S, I, R
