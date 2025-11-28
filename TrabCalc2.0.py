import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ==========================================
# 1. DEFININDO A "VERDADE" (Ground Truth)
# ==========================================
# Para calcular o erro, precisamos de uma função matemática "perfeita"
# para comparar com a nossa aproximação polinomial.
def funcao_real_trajetoria(x):
    # Exemplo: uma combinação de seno e cosseno para criar uma curva complexa
    return np.sin(x) + np.cos(x * 0.8) * 1.5 + 2

# ==========================================
# 2. AMOSTRAGEM (Os Pontos Conhecidos)
# ==========================================
# Vamos fingir que só conhecemos 6 pontos dessa função (os keyframes)
x_pontos = np.linspace(0, 10, 6) 
y_pontos = funcao_real_trajetoria(x_pontos)

# ==========================================
# 3. INTERPOLAÇÃO DE LAGRANGE
# ==========================================
def interpolacao_lagrange(x_alvo, x_dados, y_dados):
    n = len(x_dados)
    soma = 0
    for i in range(n):
        termo_l = 1
        for j in range(n):
            if i != j:
                termo_l = termo_l * (x_alvo - x_dados[j]) / (x_dados[i] - x_dados[j])
        soma += y_dados[i] * termo_l
    return soma

# ==========================================
# 4. PREPARANDO OS DADOS PARA O GRÁFICO
# ==========================================
# Criamos pontos densos para desenhar as linhas suaves
x_denso = np.linspace(0, 10, 200)

# 1. A curva "Real" (Se tivéssemos dados infinitos)
y_real = funcao_real_trajetoria(x_denso)

# 2. A curva Interpolada (O que o computador calculou)
y_interpolada = [interpolacao_lagrange(x, x_pontos, y_pontos) for x in x_denso]

# 3. O Erro (Diferença absoluta entre a Real e a Interpolada)
# Usamos abs() pois queremos a magnitude do erro, não o sinal
erro_absoluto = np.abs(np.array(y_real) - np.array(y_interpolada))

# ==========================================
# 5. CONFIGURAÇÃO VISUAL (DOIS GRÁFICOS)
# ==========================================
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
plt.subplots_adjust(hspace=0.3) # Espaço entre os gráficos

# --- Gráfico 1: A Trajetória ---
ax1.set_title("Comparação: Trajetória Real vs. Interpolada")
ax1.set_ylabel("Posição Y")
ax1.plot(x_denso, y_real, 'k--', alpha=0.3, label='Trajetória Real (Desconhecida pelo PC)')
ax1.plot(x_denso, y_interpolada, 'g-', label='Polinômio de Lagrange')
ax1.scatter(x_pontos, y_pontos, color='blue', s=80, label='Keyframes (Pontos Conhecidos)', zorder=5)
objeto, = ax1.plot([], [], 'ro', markersize=10, label='Objeto')
ax1.legend(loc='upper right')
ax1.grid(True, linestyle='--', alpha=0.5)

# --- Gráfico 2: O Erro ---
ax2.set_title("Gráfico de Erro Absoluto (|Real - Lagrange|)")
ax2.set_xlabel("Tempo / Distância (x)")
ax2.set_ylabel("Erro")
# Plotamos a "sombra" do erro total
ax2.fill_between(x_denso, erro_absoluto, color='red', alpha=0.2, label='Área de Erro')
ax2.plot(x_denso, erro_absoluto, color='red', linewidth=1)
# Ponto que mostra o erro atual
ponto_erro, = ax2.plot([], [], 'ro', markersize=8)
# Linhas verticais indicando onde o erro é zero (nos nós)
for x_p in x_pontos:
    ax2.axvline(x=x_p, color='blue', linestyle=':', alpha=0.3)

ax2.set_ylim(0, max(erro_absoluto) * 1.1)
ax2.grid(True, alpha=0.5)

# ==========================================
# 6. ANIMAÇÃO
# ==========================================
def init():
    objeto.set_data([], [])
    ponto_erro.set_data([], [])
    return objeto, ponto_erro

def update(frame):
    # Atualiza posição do objeto no gráfico de cima
    x = x_denso[frame]
    y = y_interpolada[frame]
    objeto.set_data([x], [y])
    
    # Atualiza a bolinha indicadora no gráfico de erro (em baixo)
    y_err = erro_absoluto[frame]
    ponto_erro.set_data([x], [y_err])
    
    return objeto, ponto_erro

anim = FuncAnimation(fig, update, frames=len(x_denso), init_func=init, interval=20, blit=True)

plt.show()