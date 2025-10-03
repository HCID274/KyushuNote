### **(1) 冷たいプラズマ中の遮断と共鳴**

#### **基本概念**

*   **遮断 (Cutoff)**: 屈折率 $n \to 0 \implies$ 波数 $k \to 0$。波は全反射される。
*   **共鳴 (Resonance)**: 屈折率 $n \to \infty \implies$ 波数 $k \to \infty$。波のエネルギーが高効率で吸収される。

#### **特性周波数の定義**

*   電子プラズマ周波数 $\omega_{pe} = \sqrt{\frac{n_e e^2}{m_e \epsilon_0}}$ ($n_e$: 電子数密度, $m_e$: 電子の質量, $e$: 電気素量, $\epsilon_0$: 真空の誘電率)
*   電子サイクロトロン周波数 $\omega_{ce} = \frac{e B_0}{m_e}$ ($B_0$: 外部磁場強度)
*   イオンサイクロトロン周波数 $\omega_{ci} = \frac{Z e B_0}{m_i}$ ($Z$: イオンの価数, $m_i$: イオンの質量)

#### **代表的な遮断周波数 ($n^2=0$)**

1.  **O波 (通常波)**
    $$ \omega_{co} = \omega_{pe} $$
    $\implies$ 波の周波数 $\omega < \omega_{pe}$ のとき、波は伝搬できない。

2.  **R波 (右回り円偏波)**
    $$ \omega_{co} = \omega_R = \frac{1}{2} \left( \omega_{ce} + \sqrt{\omega_{ce}^2 + 4\omega_{pe}^2} \right) $$

3.  **L波 (左回り円偏波)**
    $$ \omega_{co} = \omega_L = \frac{1}{2} \left( -\omega_{ce} + \sqrt{\omega_{ce}^2 + 4\omega_{pe}^2} \right) $$

#### **代表的な共鳴周波数 ($n^2 \to \infty$)**

1.  **イオンサイクロトロン共鳴**
    $$ \omega_{res} = \omega_{ci} $$
    $\implies$ 波のエネルギーがイオンに効率よく吸収される。イオンサイクロトロン共鳴加熱(ICRH)に用いられる。

2.  **電子サイクロトロン共鳴**
    $$ \omega_{res} = \omega_{ce} $$
    $\implies$ 波のエネルギーが電子に効率よく吸収される。電子サイクロトロン共鳴加熱(ECRH)に用いられる。

3.  **低域混成共鳴**
    $$ \omega_{res} = \omega_{LH} $$
    $$ \frac{1}{\omega_{LH}^2} = \frac{1}{\omega_{ci}^2 + \omega_{pi}^2} + \frac{1}{|\omega_{ce}\omega_{ci}|} $$
    ($\omega_{pi}$ はイオンのプラズマ周波数)

4.  **上部混成共鳴**
    $$ \omega_{res} = \omega_{UH} = \sqrt{\omega_{pe}^2 + \omega_{ce}^2} $$

***

### **(2) 電子プラズマ波の冷たいプラズマ近似**

#### **熱いプラズマ (Warm Plasma)**

*   **分散関係 (Bohm-Gross)**:
    $$ \omega^2 = \omega_{pe}^2 + 3k^2 v_{th,e}^2 $$
    ここで、$v_{th,e} = \sqrt{\frac{k_B T_e}{m_e}}$ は電子の熱速度である ($k_B$: ボルツマン定数, $T_e$: 電子温度)。
*   **性質**: $\omega$ は $k$ に依存するため、波は分散性を持ち伝搬する。

#### **冷たいプラズマ近似 (Cold Plasma Approximation)**

*   **近似条件**:
    $$ T_e \to 0 \implies v_{th,e} \to 0 $$

*   **導出**:
    $$ \omega^2 = \omega_{pe}^2 + 3k^2 (0)^2 \implies \omega^2 = \omega_{pe}^2 $$
    $$ \implies \omega = \omega_{pe} $$

#### **近似後の性質**

*   **周波数**: $\omega$ は波数 $k$ に依存しない定数となる。
*   **群速度 (Group Velocity)**:
    $$ v_g = \frac{d\omega}{dk} = \frac{d}{dk}(\omega_{pe}) = 0 $$
*   **物理的意味**:
    $$ v_g = 0 \implies \text{エネルギーは伝搬しない} $$
    $\implies$ 波は、伝搬可能な**進行波 (Propagating Wave)** から、局在した**集団振動 (Localized Collective Oscillation)** へと性質が変化する。