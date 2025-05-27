<div style="font-size: 12px; line-height: 2;">

# [问题1] ：等离子体中的荷电粒子产生的电场的方程，其解与德拜长度的关系，以及库仑对数

## 等离子体中荷电粒子电场、德拜长度与库仑对数 (プラズマ中荷電粒子電場、デバイ長とクーロン対数)

## 1. 方程与解 (方程式と解法)

*   **泊松方程 (Poisson's eq. / ポアソン方程式):**
    $$ \nabla^2 \phi = -\frac{\rho}{\varepsilon_0} $$
*   **电荷密度 (Charge density / 電荷密度):** $\rho = q_{test}\delta(\mathbf{r}) + \rho_{ind}$.
    *   感生电荷 (Induced charge / 誘起電荷) $\rho_{ind}$ 来自线性化玻尔兹曼分布 (Linearized Boltzmann dist. / 線形化ボルツマン分布):
        $n_{e,i} \approx n_0 (1 \pm \frac{e\phi}{k_B T_{e,i}})$, 故 $\rho_{ind} \approx -n_0 e^2 \phi (\frac{1}{k_B T_e} + \frac{1}{k_B T_i})$.
*   **屏蔽泊松方程 (Screened Poisson eq. / 遮蔽されたポアソン方程式):**
    $$ \nabla^2 \phi - \frac{1}{\lambda_D^2} \phi = -\frac{q_{test}\delta(\mathbf{r})}{\varepsilon_0} $$
    **德拜长度 (Debye length / デバイ長) $\lambda_D$**:
    $$ \frac{1}{\lambda_D^2} = \frac{n_0 e^2}{\varepsilon_0} \left(\frac{1}{k_B T_e} + \frac{1}{k_B T_i}\right) $$
    (电子屏蔽 (Electron screening / 電子遮蔽)时: $\lambda_D \to \lambda_{De} = \sqrt{\frac{\varepsilon_0 k_B T_e}{n_0 e^2}}$)
*   **解 - 汤川势 (Solution - Yukawa pot. / 解 - 湯川ポテンシャル):**
    $$ \phi(r) = \frac{q_{test}}{4\pi\varepsilon_0 r} e^{-r/\lambda_D} $$

## 2. 德拜长度与库仑对数 (デバイ長とクーロン対数)

*   **$\lambda_D$ 意义 (Significance / 意義):**
    *   电荷屏蔽特征尺度 (Charge screening scale / 電荷遮蔽の特性スケール).
    *   $r \ll \lambda_D$: 近似库仑势 (Approx. Coulomb pot. / 近似クーロンポテンシャル).
    *   $r \gg \lambda_D$: 电场被屏蔽 (Field shielded / 電場は遮蔽される).

*   **库仑对数 (Coulomb logarithm / クーロン対数) $\ln \Lambda$:** 修正碰撞积分发散 (Corrects collision integral divergence / 衝突積分の発散を修正).
    $$ \ln \Lambda = \ln \left( \frac{\lambda_D}{b_0} \right) $$
    *   $\lambda_D$: 最大碰撞参数 (Max. impact parameter / 最大衝突径数).
    *   $b_0$: 最小碰撞参数 (Min. impact parameter / 最小衝突径数), e.g., $b_0 \approx \frac{e^2}{4\pi\varepsilon_0 k_B T_e}$.


# [问题2] 均质等离子体中入射了以 $E(\mathbf{r}, t) = E_0 \exp[i(\mathbf{k} \cdot \mathbf{r} - \omega t)]$ 表示的电磁波。求等离子体的介电常数 $\varepsilon(k, \omega)$ 和电磁波的色散关系。讨论电磁波能在等离子体中传播的条件。

## 等离子体介电常数、色散关系与传播 (プラズマの誘電率、分散関係と伝播)

**前提 (Assumptions / 前提条件):** 均质 (Homogeneous / 均一), 未磁化 (Unmagnetized / 非磁化) 冷等离子体 (Cold plasma / 冷たいプラズマ), 忽略离子运动 (Ignore ion motion / イオン運動を無視), 电子密度 (Electron density / 電子数密度) $n_0$.

## 1. 介电常数 (誘電率)

1.  **电子运动 (Electron motion / 電子運動):** $m_e \frac{d\mathbf{v}_e}{dt} = -e\mathbf{E}$ ($d/dt \to -i\omega$)
    $\implies \mathbf{v}_e = -\frac{ie\mathbf{E}}{\omega m_e}$.
2.  **感应电流 (Induced current / 誘起電流):** $\mathbf{J}_{ind} = -n_0 e \mathbf{v}_e = \frac{i n_0 e^2}{\omega m_e} \mathbf{E}$.
3.  **电导率 (Conductivity / 電気伝導率):** $\sigma = \frac{i n_0 e^2}{\omega m_e}$.
4.  **介电常数 (Dielectric const. / 誘電率):** $\varepsilon(\omega) = \varepsilon_0 + \frac{i\sigma}{\omega} = \varepsilon_0 - \frac{n_0 e^2}{m_e \omega^2}$.
    **等离子体频率 (Plasma freq. / プラズマ周波数) $\omega_p^2 = \frac{n_0 e^2}{\varepsilon_0 m_e}$**.
    $\implies$ 相对介电常数 (Relative permittivity / 比誘電率) $\varepsilon_r(\omega) = 1 - \frac{\omega_p^2}{\omega^2}$.
    (*注: 此处 $\varepsilon(\omega)$, 非 $\varepsilon(k,\omega)$ (not $k$-dependent / $k$非依存)*).

## 2. 色散关系 (分散関係)

麦克斯韦方程 (Maxwell's eqns. / マクスウェル方程式) for 横向波 (transverse wave / 横波) ($\mathbf{k} \cdot \mathbf{E}=0$):
$i\mathbf{k} \times \mathbf{E} = i\omega \mathbf{B}$ and $i\mathbf{k} \times \mathbf{B}/\mu_0 = -i\omega\varepsilon(\omega)\mathbf{E}$.
$\implies -k^2 \mathbf{E} = -\omega^2 \mu_0 \varepsilon(\omega) \mathbf{E} \implies k^2 = \omega^2 \mu_0 \varepsilon(\omega)$.
代入 $\varepsilon(\omega)$ 及 $c^2 = 1/(\mu_0 \varepsilon_0)$:
$k^2 = \frac{\omega^2}{c^2} \left(1 - \frac{\omega_p^2}{\omega^2}\right)$.
**色散关系 (Dispersion relation / 分散関係):**
$$ \omega^2 = \omega_p^2 + k^2 c^2 $$

## 3. 传播条件 (Propagation condition / 伝播条件)

波传播 (Wave propagates / 波伝播) $\iff k$ 为实数 (real / 実数) $\implies k^2 \ge 0$:
$\frac{\omega^2 - \omega_p^2}{c^2} \ge 0 \implies \omega^2 \ge \omega_p^2$.
**传播条件 (Propagation condition / 伝播条件):** $\omega \ge \omega_p$.
*   $\omega > \omega_p$: 传播 (Propagates / 伝播).
*   $\omega < \omega_p$: 衰减/反射 (Evanescent/Reflected / 減衰/反射).
*   $\omega = \omega_p$: 截止 (Cut-off / 遮断).

# [问题3] 13.6eV 的能量的质子撞击静止的氢原子。能够使其电离吗？请说明理由。如果换成相同能量的电子情况如何？此外，质子要电离氢原子，所需的最低能量是多少？（提示：从质心运动和相对运动的观点考虑。）

## H原子电离阈能 (H-atom Ionization Threshold / 水素原子の電離閾エネルギー)

*   **电离能 (Ionization Energy / 電離エネルギー) $E_{ion} = 13.6 \text{ eV}$**.
*   仅**质心系能量 (CM Energy / 重心系エネルギー) $E_{CM}$** 可用于电离 (Ionization / 電離).
*   $E_{CM} = \frac{m_2}{m_1 + m_2} K_{lab}$ ($m_1$: 入射 (incident / 入射), $m_2$: 靶 (target / 標的), $K_{lab}$: 实验室系动能 (Lab KE / 実験室系運動エネルギー)). 电离需 (Need for ionization / 電離の必要条件): $E_{CM} \ge E_{ion}$.
*   符号 (Symbols / 記号): $m_p$ (质子 / proton / 陽子), $m_e$ (电子 / electron / 電子), $m_H \approx m_p$ (H原子 / H-atom / H原子).

---

1.  **13.6eV 质子 (Proton / 陽子) + H**:
    $m_1=m_p, m_2 \approx m_p, K_{lab}=13.6 \text{ eV}$.
    $E_{CM} = \frac{m_p}{m_p+m_p} K_{lab} = \frac{1}{2} K_{lab} = 6.8 \text{ eV}$.
    $6.8 \text{ eV} < E_{ion} \implies$ **不电离 (No Ionization / 電離不可)**. ($E_{CM}$ 不足 / insufficient).

---

2.  **13.6eV 电子 (Electron / 電子) + H**:
    $m_1=m_e, m_2 \approx m_p, K_{lab}=13.6 \text{ eV}$.
    $E_{CM} = \frac{m_p}{m_e+m_p} K_{lab} \approx K_{lab} = 13.6 \text{ eV}$ (因 $m_e \ll m_p$).
    $13.6 \text{ eV} \ge E_{ion} \implies$ **可电离 (阈值) (Can Ionize (threshold) / 電離可能 (閾値))**.

---

3.  **质子 (Proton / 陽子) 电离H所需最低 $K_{lab}$ (Min. $K_{lab}$ for p to ionize H / 陽子がHを電離する最低$K_{lab}$)**:
    需 (Need / 必要) $E_{CM} = E_{ion} = 13.6 \text{ eV}$.
    $\frac{1}{2} K_{lab, min} = E_{ion} \implies K_{lab, min} = 2 E_{ion} = 2 \times 13.6 \text{ eV} = \mathbf{27.2 \text{ eV}}$.

# [问题4] 中性气体的扩散系数を推定しなさい。気体分子の半径を $0.5 \times 10^{-10} \text{ m}^{-1}$、個数を $N = 3 \times 10^{25} \text{ m}^{-3}$、速度を $350 \text{ m/s}$ とする。また、プラズマ衝突振動数は温度にどのように依存するか。
(估计中性气体的扩散系数。设气体分子半径为 $0.5 \times 10^{-10} \text{ m}$，数密度为 $N = 3 \times 10^{25} \text{ m}^{-3}$，速度为 $350 \text{ m/s}$。此外，等离子体碰撞频率如何依赖于温度？)

## 气体扩散与等离子体碰撞 (Gas Diffusion & Plasma Collision / 気体拡散とプラズマ衝突)

**1. 气体扩散系数 (Gas Diffusion / 気体の拡散係数)**

*   **公式 (Formula / 公式):** $D \approx \frac{1}{3} \lambda \bar{v}$.
    *   $\lambda = (\sqrt{2} N \sigma_{coll})^{-1}$: 平均自由程 (Mean free path / 平均自由行程).
    *   $\sigma_{coll} = 4\pi r_m^2$: 碰撞截面 (Collision cross-section / 衝突断面積).
*   **参数 (Parameters / パラメータ):** $r_m=0.5 \text{e-10m}, N=3 \text{e}25 \text{m}^{-3}, \bar{v}=350 \text{m/s}$.
*   **计算 (Calculation / 計算):**
    1.  $\sigma_{coll} = 4\pi (0.5 \text{e-10})^2 = \pi \text{e-20 m}^2$.
    2.  $\lambda = (\sqrt{2} \cdot 3 \text{e}25 \cdot \pi \text{e-20})^{-1} \approx 7.50 \text{e-7 m}$.
    3.  $D \approx \frac{1}{3} (7.50 \text{e-7}) (350) \approx 8.75 \text{e-6 m}^2/\text{s}$.
*   **结果 (Result / 結果):** $D \approx 8.75 \times 10^{-6} \text{ m}^2/\text{s}$.

---

**2. 等离子体碰撞频率-温度依赖性 (Plasma Collision Freq-Temp Dependence / プラズマ衝突振動数-温度依存性)**

*   碰撞频率 (Collision freq. / 衝突振動数) $\nu \approx n \sigma v_{rel}$.
*   $v_{th} \propto T^{1/2}$ (热速度 / Thermal velocity / 熱速度).
*   $\sigma_{Coulomb} \propto \frac{\ln \Lambda}{T^2}$ (库仑截面 / Coulomb cross-section / クーロン断面積), $\ln \Lambda$ (库仑对数 / Coulomb log / クーロン対数) 弱依赖 $T$ (weak T-dependence / 弱いT依存性).
*   电子-离子碰撞 (e-i collision / 電子イオン衝突) $\nu_{ei} \propto n_i (\frac{\ln \Lambda}{T_e^2}) T_e^{1/2} \propto n_i \frac{\ln \Lambda}{T_e^{3/2}}$.
*   **结论 (Conclusion / 結論):** $\nu_{ei} \propto T_e^{-3/2}$.

# [问题5] 电子的流体方程式を用いて、ボルツマン関係を導出しなさい。また、電子音波の分散関係を導出しなさい。
(使用电子的流体方程，推导玻尔兹曼关系。另外，推导电子声波的色散关系。)

## 电子流体：玻尔兹曼关系与电子声波 (e-Fluid: Boltzmann & e-Acoustic Wave / 電子流体：ボルツマンと電子音波)

## 1. 玻尔兹曼关系 (Boltzmann Relation / ボルツマン関係)

*   **电子动量方程 (e-Momentum / 電子運動量) (1D, 无碰撞 / collisionless / 無衝突, 忽略惯性 / ignore inertia / 慣性無視):**
    $0 = -e n_e E - \frac{\partial p_e}{\partial x}$.
*   静电场 (Electrostatic / 静電場) $E = -\frac{\partial \phi}{\partial x}$. 等温 (Isothermal / 等温) $p_e = n_e k_B T_e$.
    $\implies e d\phi = k_B T_e \frac{dn_e}{n_e}$.
*   **积分 (Integral / 積分):** $n_e = n_{e0} \exp\left(\frac{e\phi}{k_B T_e}\right)$.
    (线性化 (Linearized / 線形化): $n_{e1} \approx n_{e0} \frac{e\phi}{k_B T_e}$)

## 2. 电子声波 (朗缪尔波) 色散 (e-Acoustic (Langmuir) Wave Dispersion / 電子音波 (ラングミュア波) 分散)

*   **线性化方程组 (Linearized system / 線形化方程式系):**
    (离子不动 / Ions immobile / イオン不動)
    1.  连续性 (Continuity / 連続): $-i\omega n_{e1} + ik n_{e0} v_{e1} = 0$. (A)
    2.  动量 (Momentum / 運動量): $-i\omega m_e v_{e1} = -e E_1 - ik \frac{\gamma_e k_B T_e}{n_{e0}} n_{e1}$. (B)
    3.  泊松 (Poisson / ポアソン): $ik E_1 = -\frac{e n_{e1}}{\varepsilon_0} \implies E_1 = \frac{ie n_{e1}}{k \varepsilon_0}$. (C)
*   **求解 (Solve / 解法):** (A) $\to v_{e1}$. (A,C) $\to$ (B).
    $$ \omega^2 m_e = \frac{n_{e0} e^2}{\varepsilon_0} + \gamma_e k_B T_e k^2 $$
*   **色散关系 (Dispersion / 分散関係):**
    $$ \omega^2 = \omega_{pe}^2 + v_{the}^2 k^2 $$
    *   $\omega_{pe}^2 = \frac{n_{e0} e^2}{m_e \varepsilon_0}$ (电子等离子体频率 / e-plasma freq. / 電子プラズマ周波数).
    *   $v_{the}^2 = \frac{\gamma_e k_B T_e}{m_e}$ (电子热速度 / e-thermal vel. / 電子熱速度).

# [问题6] 解 MHD 方程式以说明阿尔文波 (Alfvén wave) 的色散关系。此处，压力的效果可以忽略。解弦的波动方程并讨论其关系。

## 阿尔文波与弦波 (Alfvén & String Waves / アルフベン波と弦の波)

**A. 阿尔文波 (Alfvén Wave / アルフベン波)** (无压 / Pressureless / 無圧力)

1.  **MHD方程 (MHD Eqns. / MHD方程式):**
    *   动量 (Momentum / 運動量): $\rho_{m0} \frac{\partial \delta \mathbf{v}}{\partial t} = \frac{1}{\mu_0} (\nabla \times \delta \mathbf{B}) \times \mathbf{B}_0$.
    *   感应 (Induction / 誘導): $\frac{\partial \delta \mathbf{B}}{\partial t} = (\mathbf{B}_0 \cdot \nabla)\delta \mathbf{v}$.
2.  **色散 (Dispersion / 分散):**
    设 $\propto e^{i(\mathbf{k} \cdot \mathbf{r} - \omega t)}$. 联立得 (Combining gives / 連立して得る):
    $$ \omega^2 \rho_{m0} = \frac{(\mathbf{k} \cdot \mathbf{B}_0)^2}{\mu_0} $$
    **阿尔文速度 (Alfvén Vel. / アルフベン速度) $v_A^2 = \frac{B_0^2}{\mu_0 \rho_{m0}}$**.
    $\implies \omega = k v_A |\cos\theta|$. ($\theta$: $\mathbf{k}$ 与 $\mathbf{B}_0$ 夹角 / angle between $\mathbf{k}, \mathbf{B}_0$ / $\mathbf{k}$ と $\mathbf{B}_0$ の角度).

---

**B. 弦波 (String Wave / 弦の波)**

1.  **方程 (Eq. / 方程式):** $\frac{\partial^2 y}{\partial t^2} = v_s^2 \frac{\partial^2 y}{\partial x^2}$. $v_s = \sqrt{T/\lambda}$ ($T$: 张力 / Tension / 張力, $\lambda$: 线密度 / Linear density / 線密度).
2.  **色散 (Dispersion / 分散):** $\omega = k v_s$.

---

**C. 关系 (Relationship / 関係)**

*   **相似 (Similar / 類似):** $\theta=0 \Rightarrow \omega = k v_A$, 形似 (like / 同形式) $\omega = k v_s$.
*   **类比 (Analogy / アナロジー):** 磁力线 (Field lines / 磁力線) $\leftrightarrow$ 弦 (String / 弦); 磁张力 ($B_0^2/\mu_0$) (Mag. tension / 磁気張力) $\leftrightarrow$ 弦张力 ($T$); $\rho_{m0} \leftrightarrow \lambda$.
*   **物理 (Physics / 物理):** 磁力线为介质 (Field lines as medium / 磁力線が媒体)、等离子体供惯性 (Plasma provides inertia / プラズマが慣性を提供)。

# [问题7] 托卡马克中为了约束等离子体，需要在等离子体中通入电流。这是为什么？

## 托卡马克等离子体电流必要性 (Tokamak Current Need / トカマク電流の必要性)

**目的 (Purpose / 目的):** 磁约束 (Magnetic Confinement / 磁気閉じ込め).

1.  **产生 $B_p$ (Generate $B_p$ / $B_p$ 生成):**
    环向电流 ($I_p$) (Toroidal Current / トロイダル電流) $\xrightarrow{\text{Ampere}}$ 极向磁场 ($B_p$) (Poloidal Field / ポロイダル磁場).

2.  **形成螺旋磁面 (Form Helical Surfaces / 螺旋磁気面形成):**
    $B_p + B_T$ (外加环向场 / External Toroidal Field / 外部トロイダル磁場) $\implies$ **螺旋磁场/磁面 (Helical Field/Surfaces / 螺旋磁場/磁気面)**.

3.  **螺旋磁面作用 (Helical Surfaces Function / 螺旋磁気面の役割):**
    *   **约束 (Confinement / 閉じ込め):** 粒子沿磁面运动 (Particles follow surfaces / 粒子は磁気面に沿って運動).
    *   **减漂移 (Reduce Drift / ドリフト低減):** “短路” (Short-circuit / 短絡) 由 $\nabla B$/曲率漂移 (curvature drift / 曲率ドリフト) 引起的电荷分离 (charge separation / 電荷分離), 减小 $E \times B$ 损失.
    *   **平衡 (Equilibrium / 平衡):** 洛伦兹力 ($\mathbf{J}_p \times \mathbf{B}_p$) (Lorentz force / ローレンツ力) 平衡压力梯度 ($\nabla p$) (Balances pressure gradient / 圧力勾配と平衡).

**核心 (Core / 核心):** $I_p \Rightarrow B_p \Rightarrow$ 螺旋结构 (Helical Structure / 螺旋構造) $\Rightarrow$ 约束与平衡 (Confinement & Equilibrium / 閉じ込めと平衡).

# [问题8] フォッカープランクの式を導出し、衝突拡散の表式について説明しなさい。
(推导福克-普朗克方程，并说明碰撞扩散的表达式。)

## 福克-普朗克方程与碰撞扩散 (Fokker-Planck Eq. & Collisional Diffusion / フォッカー・プランク方程式と衝突拡散)

## 1. 福克-普朗克方程 (Fokker-Planck Eq. / フォッカー・プランク方程式)

描述 $f(\mathbf{v},t)$ 因小角度碰撞 (small-angle collisions / 小角度衝突) 的演化。
从主方程 (Master Eq.) 泰勒展开 (Taylor expand) 跃迁概率 (transition probability / 遷移確率)。

$$ \left(\frac{\partial f}{\partial t}\right)_{\text{coll}} = -\sum_i \frac{\partial}{\partial v_i} (A_i f) + \frac{1}{2} \sum_{i,j} \frac{\partial^2}{\partial v_i \partial v_j} (B_{ij} f) $$

*   $A_i(\mathbf{v}) = \langle \Delta v_i \rangle_t$: **漂移矢量 (Drift vector / ドリフトベクトル)** (动力学摩擦 / Dynamical friction / 動摩擦力).
*   $B_{ij}(\mathbf{v}) = \langle \Delta v_i \Delta v_j \rangle_t$: **扩散张量 (Diffusion tensor / 拡散テンソル)**.
(库仑碰撞 (Coulomb collisions / クーロン衝突) $\Rightarrow$ 朗道积分 (Landau integral / ランダウ積分)).

## 2. 碰撞扩散 (实空间) (Collisional Diffusion (Real Space) / 衝突拡散 (実空間))

*   通量 (Flux / フラックス): $\mathbf{\Gamma} = -D \nabla n$.
*   **平行B场/无B场 ($D_{\parallel}$ / B-field Parallel/None / 磁場平行/なし):**
    $D_{\parallel} \approx v_{th}^2 / \nu_c$ ($v_{th}$: 热速率 / Thermal speed / 熱速度, $\nu_c$: 碰撞频率 / Collision freq. / 衝突周波数).
*   **垂直B场 (经典) ($D_{\perp}$ / B-field Perpendicular (Classical) / 磁場垂直 (古典的)):**
    $D_{\perp} \approx \rho_L^2 \nu_{coll}$ ($\rho_L$: 拉莫尔半径 / Larmor radius / ラーマー半径).
    *   例：电子 (Electron / 電子) $D_{\perp,e} \approx \rho_{Le}^2 \nu_{ei}$.
        *   依赖性 (Dependence / 依存性): $D_{\perp,e} \propto n_e T_e^{-1/2} B^{-2}$.

</div>