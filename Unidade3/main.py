import numpy as np
import matplotlib.pyplot as plt
from euler import euler_sir
from rk4 import rk4_sir

# 1. Parâmetros da simulação e Condições Iniciais
S0 = 999
I0 = 1
R0 = 0
beta = 0.0003
gamma = 0.1
t_max = 60  # Tempo máximo da simulação (ex: 60 dias)
h = 0.5     # Tamanho do passo de tempo

# 2. Execução dos métodos numéricos
t_euler, S_euler, I_euler, R_euler = euler_sir(S0, I0, R0, beta, gamma, h, t_max)
t_rk4, S_rk4, I_rk4, R_rk4 = rk4_sir(S0, I0, R0, beta, gamma, h, t_max)

# 3. Construção do Gráfico Comparativo
plt.figure(figsize=(10, 6))

# Curvas do Método de Euler (linhas tracejadas '--')
plt.plot(t_euler, S_euler, 'r--', label='Suscetíveis (Euler)', alpha=0.6)
plt.plot(t_euler, I_euler, 'g--', label='Infectados (Euler)', alpha=0.6)
plt.plot(t_euler, R_euler, 'b--', label='Recuperados (Euler)', alpha=0.6)

# Curvas do Método RK4 (linhas contínuas '-')
plt.plot(t_rk4, S_rk4, 'r-', label='Suscetíveis (RK4)', linewidth=2)
plt.plot(t_rk4, I_rk4, 'g-', label='Infectados (RK4)', linewidth=2)
plt.plot(t_rk4, R_rk4, 'b-', label='Recuperados (RK4)', linewidth=2)

# Configurações estéticas (padrão para o artigo da SBC)
plt.title('Comparação Numérica do Modelo SIR: Euler vs RK4', fontsize=14)
plt.xlabel('Tempo (t)', fontsize=12)
plt.ylabel('População', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='best', fontsize=10)

# 4. Guardar o gráfico e exibir
plt.tight_layout()
plt.savefig("resultados/grafico_sir.png", dpi=300)
plt.show()

print("Simulação concluída! O arquivo 'grafico_sir.png' foi salvo na pasta 'resultados'.")