"""
Animação de Colisão Frontal (1D) — Colisão Elástica
=====================================================
Parâmetros configuráveis no início do script:
  m1, m2   : massas dos corpos (kg)
  v1i, v2i : velocidades iniciais (m/s) — positivo = direita, negativo = esquerda
  elastic  : True = colisão elástica, False = colisão perfeitamente inelástica
"""

import numpy as np

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, Button

# ── Parâmetros iniciais ───────────────────────────────────────────────────────
M1_0  = 2.0    # massa do corpo 1 (kg)
M2_0  = 1.0    # massa do corpo 2 (kg)
V1I_0 = 3.0    # velocidade inicial do corpo 1 (m/s)
V2I_0 = -1.0   # velocidade inicial do corpo 2 (m/s)
ELASTIC = True  # True = elástica | False = perfeitamente inelástica

# ── Física ────────────────────────────────────────────────────────────────────

def velocidades_finais(m1, m2, v1i, v2i, elastic=True):
    if elastic:
        v1f = ((m1 - m2) * v1i + 2 * m2 * v2i) / (m1 + m2)
        v2f = ((m2 - m1) * v2i + 2 * m1 * v1i) / (m1 + m2)
    else:  # perfeitamente inelástica
        vf  = (m1 * v1i + m2 * v2i) / (m1 + m2)
        v1f = v2f = vf
    return v1f, v2f

def simular(m1, m2, v1i, v2i, elastic=True, dt=0.02, total_time=6.0):
    """Retorna arrays de posição x1(t), x2(t) e instante de colisão."""
    v1f, v2f = velocidades_finais(m1, m2, v1i, v2i, elastic)

    # tamanhos visuais proporcionais à massa
    r1 = 0.3 + 0.15 * m1
    r2 = 0.3 + 0.15 * m2

    # posições iniciais: corpos separados, se aproximando
    x1_0 = -3.0
    x2_0 =  3.0

    t = np.arange(0, total_time, dt)
    n = len(t)
    x1 = np.zeros(n)
    x2 = np.zeros(n)

    collided = False
    t_col    = None

    x1[0] = x1_0
    x2[0] = x2_0

    for i in range(1, n):
        if not collided:
            # verifica colisão: bordas se tocam
            if x1[i-1] + r1 >= x2[i-1] - r2:
                collided = True
                t_col = t[i-1]
                x1[i] = x1[i-1] + v1f * dt
                x2[i] = x2[i-1] + v2f * dt
            else:
                x1[i] = x1[i-1] + v1i * dt
                x2[i] = x2[i-1] + v2i * dt
        else:
            x1[i] = x1[i-1] + v1f * dt
            x2[i] = x2[i-1] + v2f * dt

    return t, x1, x2, r1, r2, t_col, v1f, v2f

# ── Figura ────────────────────────────────────────────────────────────────────

fig, ax = plt.subplots(figsize=(11, 5))
plt.subplots_adjust(left=0.08, right=0.98, top=0.88, bottom=0.38)

ax.set_xlim(-7, 7)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.axhline(0, color='#cccccc', lw=1, zorder=0)
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor('#ffffff')
ax.set_xlabel('Posição (m)', fontsize=10)
ax.set_title('Colisão Frontal 1D', fontsize=13, fontweight='bold')
ax.tick_params(left=False, labelleft=False)

# corpos
corpo1 = plt.Circle((-3, 0), 0.5, color='#3a86ff', zorder=5, label='Corpo 1')
corpo2 = plt.Circle(( 3, 0), 0.45, color='#ff6b6b', zorder=5, label='Corpo 2')
ax.add_patch(corpo1)
ax.add_patch(corpo2)

# rótulos sobre os corpos
lbl1 = ax.text(-3, 0, 'm₁', ha='center', va='center',
               color='white', fontsize=10, fontweight='bold', zorder=6)
lbl2 = ax.text( 3, 0, 'm₂', ha='center', va='center',
               color='white', fontsize=10, fontweight='bold', zorder=6)

# setas de velocidade
arr1 = ax.annotate('', xy=(-2, 0), xytext=(-3, 0),
                   arrowprops=dict(arrowstyle='->', color='#3a86ff', lw=2), zorder=7)
arr2 = ax.annotate('', xy=( 4, 0), xytext=( 3, 0),
                   arrowprops=dict(arrowstyle='->', color='#ff6b6b', lw=2), zorder=7)

# painel de info
info_txt = ax.text(0, 1.6, '', ha='center', va='top', fontsize=9,
                   bbox=dict(boxstyle='round,pad=0.4', fc='#fffbe6', ec='#f0a500', lw=1))

fase_txt = ax.text(0, -1.7, '', ha='center', va='bottom', fontsize=10,
                   color='#555555', style='italic')

# ── Sliders ───────────────────────────────────────────────────────────────────

ax_m1  = plt.axes([0.10, 0.28, 0.35, 0.03])
ax_m2  = plt.axes([0.10, 0.22, 0.35, 0.03])
ax_v1  = plt.axes([0.55, 0.28, 0.35, 0.03])
ax_v2  = plt.axes([0.55, 0.22, 0.35, 0.03])

sl_m1 = Slider(ax_m1, 'm₁ (kg)', 0.5, 5.0, valinit=M1_0, color='#3a86ff')
sl_m2 = Slider(ax_m2, 'm₂ (kg)', 0.5, 5.0, valinit=M2_0, color='#ff6b6b')
sl_v1 = Slider(ax_v1, 'v₁ inicial (m/s)', -5.0, 5.0, valinit=V1I_0, color='#3a86ff')
sl_v2 = Slider(ax_v2, 'v₂ inicial (m/s)', -5.0, 5.0, valinit=V2I_0, color='#ff6b6b')

# botões
ax_btn_play  = plt.axes([0.10, 0.10, 0.12, 0.07])
ax_btn_reset = plt.axes([0.25, 0.10, 0.12, 0.07])
ax_btn_tipo  = plt.axes([0.40, 0.10, 0.20, 0.07])

btn_play  = Button(ax_btn_play,  '▶ Play',  color='#d4edda', hovercolor='#a8d5b5')
btn_reset = Button(ax_btn_reset, '↺ Reset', color='#fde8d8', hovercolor='#f5c6a0')
btn_tipo  = Button(ax_btn_tipo,  '⚡ Elástica', color='#e8d4f0', hovercolor='#c9a8e0')

# legenda
ax.legend(handles=[corpo1, corpo2], loc='upper right', fontsize=9)

# ── Estado da animação ────────────────────────────────────────────────────────

state = {
    'running': False,
    'frame': 0,
    'elastic': ELASTIC,
    't': None, 'x1': None, 'x2': None,
    'r1': None, 'r2': None,
    't_col': None, 'v1f': None, 'v2f': None,
    'v1i': V1I_0, 'v2i': V2I_0,
    'm1': M1_0, 'm2': M2_0,
}

def recalcular():
    m1  = sl_m1.val
    m2  = sl_m2.val
    v1i = sl_v1.val
    v2i = sl_v2.val
    elastic = state['elastic']
    t, x1, x2, r1, r2, t_col, v1f, v2f = simular(m1, m2, v1i, v2i, elastic)
    state.update({'t': t, 'x1': x1, 'x2': x2, 'r1': r1, 'r2': r2,
                  't_col': t_col, 'v1f': v1f, 'v2f': v2f,
                  'm1': m1, 'm2': m2, 'v1i': v1i, 'v2i': v2i})

recalcular()

def atualizar_frame(frame):
    x1 = state['x1']
    x2 = state['x2']
    r1 = state['r1']
    r2 = state['r2']
    t_col = state['t_col']
    t     = state['t']
    v1i   = state['v1i']
    v2i   = state['v2i']
    v1f   = state['v1f']
    v2f   = state['v2f']
    m1    = state['m1']
    m2    = state['m2']
    elastic = state['elastic']

    i = frame % len(x1)

    # posições
    corpo1.center = (x1[i], 0)
    corpo2.center = (x2[i], 0)
    corpo1.set_radius(r1)
    corpo2.set_radius(r2)
    lbl1.set_position((x1[i], 0))
    lbl2.set_position((x2[i], 0))

    # fase
    colided = t_col is not None and t[i] >= t_col
    if not colided:
        v1_atual, v2_atual = v1i, v2i
        fase_txt.set_text('Antes da colisão')
        fase_txt.set_color('#3a7ca5')
    else:
        v1_atual, v2_atual = v1f, v2f
        tipo = 'elástica' if elastic else 'inelástica'
        fase_txt.set_text(f'Após a colisão ({tipo})')
        fase_txt.set_color('#c0392b')

    # setas de velocidade
    escala = 0.4
    def atualizar_seta(seta, x, v, r):
        seta.remove()
        dx = v * escala
        x_tip = x + np.sign(dx) * (r + abs(dx)) if dx != 0 else x + r + 0.01
        nova = ax.annotate('', xy=(x_tip, 0), xytext=(x, 0),
                           arrowprops=dict(arrowstyle='->', lw=2,
                                          color='#3a86ff' if 'corpo1' in str(seta) else '#ff6b6b'))
        return nova

    # info
    ek1i = 0.5 * m1 * v1i**2
    ek2i = 0.5 * m2 * v2i**2
    ek1f = 0.5 * m1 * v1f**2
    ek2f = 0.5 * m2 * v2f**2
    pi = m1 * v1i + m2 * v2i
    pf = m1 * v1f + m2 * v2f

    tipo_str = 'Elástica' if elastic else 'Inelástica'
    info = (f"[{tipo_str}]   "
            f"v₁: {v1i:+.2f} → {v1f:+.2f} m/s   |   "
            f"v₂: {v2i:+.2f} → {v2f:+.2f} m/s\n"
            f"Ek total: antes = {ek1i+ek2i:.2f} J  |  depois = {ek1f+ek2f:.2f} J   |   "
            f"p total: antes = {pi:.2f}  |  depois = {pf:.2f} kg·m/s")
    info_txt.set_text(info)

    return corpo1, corpo2, lbl1, lbl2, info_txt, fase_txt

# ── Animação ──────────────────────────────────────────────────────────────────

anim_container = [None]

def animate(frame):
    if not state['running']:
        return
    state['frame'] += 1
    atualizar_frame(state['frame'])
    fig.canvas.draw_idle()

def toggle_play(event):
    state['running'] = not state['running']
    btn_play.label.set_text('⏸ Pause' if state['running'] else '▶ Play')
    if state['running']:
        anim_container[0] = FuncAnimation(fig, animate, interval=30, cache_frame_data=False)
    else:
        if anim_container[0]:
            anim_container[0].event_source.stop()
    fig.canvas.draw_idle()

def reset(event):
    state['running'] = False
    state['frame'] = 0
    btn_play.label.set_text('▶ Play')
    if anim_container[0]:
        anim_container[0].event_source.stop()
    recalcular()
    atualizar_frame(0)
    fig.canvas.draw_idle()

def toggle_tipo(event):
    state['elastic'] = not state['elastic']
    label = '⚡ Elástica' if state['elastic'] else '💥 Inelástica'
    btn_tipo.label.set_text(label)
    reset(None)

btn_play.on_clicked(toggle_play)
btn_reset.on_clicked(reset)
btn_tipo.on_clicked(toggle_tipo)

for sl in [sl_m1, sl_m2, sl_v1, sl_v2]:
    sl.on_changed(lambda val: reset(None))

# frame inicial
atualizar_frame(0)

plt.show()