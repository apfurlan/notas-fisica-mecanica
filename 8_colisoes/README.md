
# Colisões Unidimensionais

## Impulso e Momento Linear

Vamos considerar uma colisão frontal entre duas esferas como mostra a figura. Durante a colisão,
o corpo 1 exerce uma força $\boldsymbol{F}_{2(1)}$ sobre 2 e este exerce uma força
$-\boldsymbol{F}_{1(2)}$ sobre 1. Observe que as forças $\boldsymbol{F}_{1(2)}$ e
$-\boldsymbol{F}_{2(1)}$ formam um par ação e reação. Aplicando a segunda lei de Newton na forma
diferencial para o sistema da figura, ficaríamos com:

$$
\frac{d \boldsymbol{p}_1}{dt} = \boldsymbol{F}_{1(2)} = -\boldsymbol{F}_{2(1)}= \frac{d \boldsymbol{p}_2}{dt}
$$

Tais forças existirão somente no momento em que os corpos 1 e 2 estiverem em contato. São forças
de contato. Em geral estas colisões duram um tempo muito pequeno, chamado "tempo de colisão".
Vamos supor que as esferas se toquem no instante $t_i$ e deixem de se tocar no instante $t_f$.
Para saber então qual o efeito dessas forças no estado de movimento do sistema após transcorrido
um período de tempo $t_f-t_i$, vamos integrar ambos os lados da equação acima:

$$
\int_{t_i}^{t_f}\frac{d \boldsymbol{p}_1}{dt}dt = \int_{\boldsymbol{p}_{1i}}^{\boldsymbol{p}_{1f}}d\boldsymbol{p}_{1} = {\boldsymbol{p}_{1f}} - {\boldsymbol{p}_{1i}} = \Delta \boldsymbol{p}_1= \int_{t_i}^{t_f} \boldsymbol{F}_{1(2)}dt
$$

Mas como sabemos que as forças em questão satisfazem a terceira lei de Newton, podemos trocar a
força $\boldsymbol{F}_{1(2)}$ por $-\boldsymbol{F}_{2(1)}$ e então concluímos que:

$$
\Delta \boldsymbol{p}_1 = -\Delta \boldsymbol{p}_2
$$

Não há nada de novo na equação acima, ela só está nos dizendo que o momento linear é conservado
na colisão. Veja:

$$
\boldsymbol{p}_{1f} - \boldsymbol{p}_{1i} = - \left( \boldsymbol{p}_{2f} - \boldsymbol{p}_{2i} \right) \to \boldsymbol{p}_{1i} + \boldsymbol{p}_{2i} = \boldsymbol{p}_{1f} + \boldsymbol{p}_{2f} \to \boldsymbol{P}_{i} = \boldsymbol{P}_{f}
$$

Reconhecemos a integral no tempo da força como o **impulso** da força $\boldsymbol{F}$ durante o
intervalo $t_f-t_i$, e sua definição fica:

$$
\boldsymbol{J} \equiv \int_{t_i}^{t_f} \boldsymbol{F}(t)dt = \Delta \boldsymbol{p}
$$

ou seja, o impulso de uma força aplicada durante um intervalo de tempo $t_f-t_i$ é igual à
variação de momento da partícula durante esse intervalo.

> **Atenção:** Não confunda $\int \boldsymbol{F}(t)dt$ com $\int \boldsymbol{F}(x)dx$. A primeira
> é o **impulso**, a segunda é o **trabalho** — lembre-se do **teorema trabalho-energia cinética**.

A demonstração acima, ainda que uma mera consequência da segunda lei de Newton, é conhecida como o
**Teorema do Impulso**. Observe que o teorema do impulso dá origem a uma equação vetorial que pode
ser escrita em três equações escalares, uma para cada componente:

$$
\Delta \boldsymbol{p} = \boldsymbol{J} \Longrightarrow \begin{cases} p_{fx} - p_{ix} = \Delta p_x = J_x \\ p_{fy} - p_{iy} = \Delta p_y = J_y \\ p_{fz} - p_{iz} = \Delta p_z = J_z \end{cases}
$$

Vimos acima que quando duas partículas se aproximam e se chocam, sua interação de contato altera
os seus movimentos através da troca de momento. Quando isso ocorre dizemos que houve uma
**colisão**. Além do momento, a energia total do sistema também é conservada. Por exemplo, em uma
colisão entre bolas de bilhar a energia cinética se converte em energia potencial elástica oriunda
da deformação da superfície das bolas, até que toda a energia cinética tenha sido convertida.
Ao fim deste processo, a energia potencial elástica volta a converter-se em energia cinética,
afastando as duas partículas. No caso ideal, toda a energia cinética é conservada — este tipo de
colisão é conhecido como **colisão elástica**.

---

## Colisões Elásticas em Uma Dimensão

Colisões elásticas são aquelas em que a energia cinética do sistema permanece a mesma antes e
depois da colisão, ou seja, é **conservada**. Em um sistema fechado (sem forças externas) o
momento também se conserva, seja a colisão elástica ou não. Vamos aplicar essas duas leis de
conservação para uma colisão elástica, considerando inicialmente um alvo estacionário.

### Caso 1: Alvo estacionário $(v_{i2}=0)$

$$
m_1v_{1i} = m_1v_{1f} + m_2v_{2f} \qquad \text{(conservação do momento)}
$$

$$
\frac{1}{2}m_1v^2_{1i} = \frac{1}{2}m_1v^2_{1f} + \frac{1}{2}m_2v^2_{2f} \qquad \text{(conservação da energia cinética)}
$$

Nossa tarefa é obter expressões para as velocidades finais em função das velocidades iniciais e
das massas. Temos duas equações e duas incógnitas. Da conservação do momento:

$$
m_1(v_{1i}-v_{1f})=m_2v_{2f}
$$

Da conservação da energia:

$$
m_1(v^2_{1i}-v^2_{1f})=m_2v^2_{2f} \Longrightarrow m_1(v_{1i}-v_{1f})(v_{1i}+v_{1f}) = m_2v^2_{2f}
$$

$$
v_{2f}=\frac{m_1}{m_2}(v_{1i}-v_{1f}) \Longrightarrow m_1(v_{1i}-v_{1f})(v_{1i}+v_{1f}) = m_2\left[ \frac{m_1}{m_2}(v_{1i}-v_{1f})\right]^2
$$

$$
m_2(v_{1i}-v_{1f}) = m_1(v_{1i}-v_{1f}) \Longrightarrow m_2v_{1i}-m_2v_{1f}=m_1v_{1i} - m_1v_{1f}
$$

E finalmente obtemos a velocidade final do corpo 1:

$$
v_{1f}=\frac{m_1-m_2}{m_1+m_2}v_{1i}
$$

Para encontrar $v_{2f}$, dividimos as equações de conservação e usamos o resultado para $v_{1f}$:

$$
v_{1i}+v_{1f}=v_{2f} \Longrightarrow v_{2f}=v_{1i}+ \frac{m_1-m_2}{m_1+m_2}v_{1i} = \frac{m_1+m_2}{m_1+m_2}v_{1i}+\frac{m_1-m_2}{m_1+m_2}v_{1i}
$$

$$
v_{2f}=\frac{2m_1}{m_1+m_2}v_{1i}
$$

Observe que $v_{2f} > 0$, ou seja, o corpo 2 (alvo) sempre se move para "frente". Já $v_{1f}$
pode ter qualquer sinal, dependendo das massas $m_1$ e $m_2$. Vamos estudar três subcasos:

#### Caso 1.1: Massas iguais $(m_1=m_2)$

Fazendo $m_1=m_2$ nas equações, obtemos $v_{1f}=0$ e $v_{2f}=v_{1i}$. Este seria o caso de
colisões entre bolas de sinuca: a bola branca (projétil) para completamente ao passo que a outra
bola (alvo) parte com a mesma velocidade. As bolas simplesmente <u>trocam</u> suas velocidades.

#### Caso 1.2: Alvo com massa grande $(m_2 \gg m_1)$

Colocando $m_2$ em evidência:

$$
v_{1f}=\frac{m_2\left(\frac{m_1}{m_2}-1\right)}{m_2\left(\frac{m_1}{m_2}+1\right)}v_{1i}
$$

Como $\frac{m_1}{m_2} \to 0$, temos $v_{1f}\simeq -v_{1i}$. O projétil retorna com a mesma
velocidade que chegou — como uma bolinha de ping-pong colidindo com uma bola de boliche.
Para o alvo:

$$
v_{2f}=\frac{2m_1}{m_2\left(\frac{m_1}{m_2}+1\right)}v_{1i}= 2\left(\frac{m_1}{m_2}\right)v_{1i} \simeq 0
$$

O alvo se mantém praticamente parado, exatamente como esperado.

#### Caso 1.3: Projétil com massa grande $(m_1 \gg m_2)$

Colocando $m_1$ em evidência:

$$
v_{1f}=\frac{m_1\left(1-\frac{m_2}{m_1}\right)}{m_1\left(1+\frac{m_2}{m_1}\right)}v_{1i} \simeq v_{1i} \qquad \text{e} \qquad v_{2f}=\frac{2m_1}{m_1\left(1+\frac{m_2}{m_1}\right)}v_{1i} \simeq 2v_{1i}
$$

O corpo 1 (projétil) prossegue como se nada tivesse acontecido, ao passo que o corpo 2 (alvo)
dispara à frente com o dobro da velocidade do projétil.

O **centro de massa** do sistema continua a se deslocar sem sofrer qualquer alteração (verifique!),
e sua velocidade é:

$$
P = MV_{CM} = (m_1+m_2)V_{CM} \Longrightarrow V_{CM}=\frac{m_1}{m_1+m_2}v_{1i}
$$

---

### Caso 2: Alvo em movimento $(v_{i2} \neq 0)$

Quando ambos os corpos estão em movimento, as equações de conservação ficam:

$$
m_1v_{1i}+m_2v_{2i} = m_1v_{1f}+m_2v_{2f} \Longrightarrow m_1(v_{1i}-v_{1f}) = -m_2(v_{2i} - v_{2f})
$$

$$
\frac{1}{2}m_1v^2_{1i}+\frac{1}{2}m_2v^2_{2i} = \frac{1}{2}m_1v^2_{1f}+ \frac{1}{2}m_2v^2_{2f} \Longrightarrow m_1(v_{1i}-v_{1f})(v_{1i}+v_{1f}) = -m_2(v_{2i} - v_{2f})(v_{2i} + v_{2f})
$$

Dividindo a equação da energia pela do momento:

$$
v_{1i}+v_{1f} = v_{2i} + v_{2f} \to v_{1f} = v_{2i}+v_{2f}-v_{1i}
$$

Substituindo $v_{1f}$ na equação da conservação do momento:

$$
m_1\left(v_{1i} - \left[ v_{2i} + v_{2f} - v_{1i}\right] \right) = v_{2f}(m_1+m_2)=v_{2i}(m_2-m_1) + 2m_1v_{1i}
$$

E finalmente:

$$
v_{2f} = \dfrac{2m_1}{m_1+m_2}v_{1i} + \dfrac{m_2-m_1}{m_1+m_2}v_{2i}
$$

$$
v_{1f} = \dfrac{m_1 - m_2}{m_1+m_2}v_{1i} + \dfrac{2m_2}{m_1+m_2}v_{2i}
$$

Observe que resolvemos o problema: dadas as condições iniciais, podemos encontrar os valores
finais. Todo o desenvolvimento se baseou na conservação de energia e momento em uma colisão
elástica.