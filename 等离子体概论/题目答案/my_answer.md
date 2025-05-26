<div style="font-size: 12px; line-height: 2;">

# [问题1] ：等离子体中的荷电粒子产生的电场的方程，其解与德拜长度的关系，以及库仑对数

## 等离子体中荷电粒子电场 (プラズマ中の荷電粒子電場)

## 1. 方程推导 (方程式の導出)

1.  **泊松方程 (Poisson's eq. / ポアソン方程式):**
    $$ \nabla^2 \phi = -\frac{\rho}{\varepsilon_0} $$
2.  **电荷密度 (Charge density / 電荷密度):**
    $\rho = q_{test}\delta(\mathbf{r}) + \rho_{ind}$
    感生电荷 (Induced charge / 誘起電荷): $\rho_{ind} = e(n_i - n_e)$
3.  **玻尔兹曼分布 (Boltzmann dist. / ボルツマン分布) & 线性化 (Linearization / 線形化):**
    设未扰动密度 (Undisturbed density / 非摂動密度) $n_0$。若 $|e\phi| \ll k_B T_{e,i}$:
    $$ n_e \approx n_0 \left(1 + \frac{e\phi}{k_B T_e}\right), \quad n_i \approx n_0 \left(1 - \frac{e\phi}{k_B T_i}\right) $$
    $$ \rho_{ind} \approx -n_0 e^2 \phi \left(\frac{1}{k_B T_e} + \frac{1}{k_B T_i}\right) $$
4.  **屏蔽泊松方程 (Screened Poisson eq. / 遮蔽されたポアソン方程式):**
    $$ \nabla^2 \phi - \frac{1}{\lambda_D^2} \phi = -\frac{q_{test}\delta(\mathbf{r})}{\varepsilon_0} $$
    其中 **德拜长度 (Debye length / デバイ長) $\lambda_D$** 定义为:
    $$ \frac{1}{\lambda_D^2} = \frac{n_0 e^2}{\varepsilon_0} \left(\frac{1}{k_B T_e} + \frac{1}{k_B T_i}\right) $$
    若仅考虑电子屏蔽 (Electron screening / 電子遮蔽): $\lambda_D \to \lambda_{De} = \sqrt{\frac{\varepsilon_0 k_B T_e}{n_0 e^2}}$
5.  **电势解 - 汤川势 (Potential solution - Yukawa pot. / ポテンシャル解 - 湯川ポテンシャル):**
    $$ \phi(r) = \frac{q_{test}}{4\pi\varepsilon_0 r} e^{-r/\lambda_D} $$
6.  **电场 (Electric field / 電場):** $\mathbf{E} = -\nabla \phi$
    $$ \mathbf{E}(r) = \frac{q_{test}}{4\pi\varepsilon_0} \left(\frac{1}{r^2} + \frac{1}{r\lambda_D}\right) e^{-r/\lambda_D} \hat{\mathbf{r}} $$

## 2. 德拜长度与库仑对数 (デバイ長とクーロン対数)

*   **德拜长度 $\lambda_D$ 意义 (Significance / 意義):**
    *   电荷屏蔽特征尺度 (Charge screening characteristic scale / 電荷遮蔽の特性スケール).
    *   $r \ll \lambda_D$: $\phi \approx \frac{q_{test}}{4\pi\varepsilon_0 r}$ (库仑势 / クーロンポテンシャル).
    *   $r \gg \lambda_D$: $\phi \to 0$ (电场被屏蔽 / 電場は遮蔽される).

*   **库仑对数 (Coulomb logarithm / クーロン対数) $\ln \Lambda$:**
    用于修正碰撞积分发散 (Corrects divergence in collision integrals / 衝突積分の発散を修正).
    $$ \ln \Lambda = \ln \left( \frac{\lambda_D}{b_0} \right) $$
    *   $\lambda_D$: 最大碰撞参数 (Max. impact parameter / 最大衝突径数) (屏蔽长度).
    *   $b_0$: 最小碰撞参数 (Min. impact parameter / 最小衝突径数), e.g., $b_0 \approx \frac{Z_1 Z_2 e^2}{4\pi\varepsilon_0 \mu v_{th}^2}$ 或 $\frac{e^2}{4\pi\varepsilon_0 k_B T_e}$.

# [问题2] 均质等离子体中入射了以 $E(\mathbf{r}, t) = E_0 \exp[i(\mathbf{k} \cdot \mathbf{r} - \omega t)]$ 表示的电磁波。求等离子体的介电常数 $\varepsilon(k, \omega)$ 和电磁波的色散关系。讨论电磁波能在等离子体中传播的条件。

## 等离子体介电常数与色散关系 (プラズマの誘電率と分散関係)

**假设 (前提 / 前提条件):**
*   均质 (Homogeneous / 均一), 未磁化 (Unmagnetized / 非磁化) 等离子体。
*   冷等离子体近似 (Cold plasma approx. / 冷たいプラズマ近似)。
*   忽略离子运动 (Ignore ion motion / イオン運動を無視)。电子密度 (Electron density / 電子数密度) $n_0$。

## 1. 介电常数推导 (誘電率の導出)

1.  **电子运动方程 (Electron eq. of motion / 電子の運動方程式):**
    $m_e \frac{d\mathbf{v}_e}{dt} = -e\mathbf{E}$. 设 $\mathbf{E} \propto e^{-i\omega t}$, 则 $\frac{d}{dt} \to -i\omega$:
    $$ -i\omega m_e \mathbf{v}_e = -e\mathbf{E} \implies \mathbf{v}_e = -\frac{ie\mathbf{E}}{\omega m_e} $$

2.  **感应电流密度 (Induced current density / 誘起電流密度):**
    $$ \mathbf{J}_{ind} = n_0 (-e) \mathbf{v}_e = \frac{i n_0 e^2}{\omega m_e} \mathbf{E} $$

3.  **电导率 (Conductivity / 電気伝導率):** $\mathbf{J}_{ind} = \sigma \mathbf{E}$
    $$ \sigma = \frac{i n_0 e^2}{\omega m_e} $$

4.  **介电常数 (Dielectric constant / 誘電率):**
    $$ \varepsilon(\omega) = \varepsilon_0 + \frac{i\sigma}{\omega} = \varepsilon_0 - \frac{n_0 e^2}{m_e \omega^2} $$
    定义 **等离子体频率 (Plasma frequency / プラズマ周波数) $\omega_p$**:
    $$ \omega_p^2 = \frac{n_0 e^2}{\varepsilon_0 m_e} $$
    则绝对介电常数 (Absolute permittivity / 絶対誘電率):
    $$ \varepsilon(\omega) = \varepsilon_0 \left(1 - \frac{\omega_p^2}{\omega^2}\right) $$
    相对介电常数 (Relative permittivity / 比誘電率):
    $$ \varepsilon_r(\omega) = 1 - \frac{\omega_p^2}{\omega^2} $$
    *注: 此模型中介电常数为 $\varepsilon(\omega)$ (非 $\varepsilon(k,\omega)$ (not $\varepsilon(k,\omega)$ / $\varepsilon(k,\omega)$ではない))。*

## 2. 色散关系 (分散関係)

从麦克斯韦方程 (Maxwell's eqns. / マクスウェル方程式) 对于横向波 ($\mathbf{k} \cdot \mathbf{E}=0$):
$$ \nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t} \implies i\mathbf{k} \times \mathbf{E} = i\omega \mathbf{B} $$
$$ \nabla \times \mathbf{H} = \mathbf{J}_{ind} + \frac{\partial \mathbf{D}}{\partial t} \implies i\mathbf{k} \times \frac{\mathbf{B}}{\mu_0} = \sigma\mathbf{E} - i\omega\varepsilon_0\mathbf{E} = -i\omega(\varepsilon_0 + \frac{i\sigma}{\omega})\mathbf{E} = -i\omega\varepsilon(\omega)\mathbf{E} $$
联立消去 $\mathbf{B}$ (Eliminating $\mathbf{B}$ / $\mathbf{B}$を消去):
$$ \mathbf{k} \times (\mathbf{k} \times \mathbf{E}) = -\omega^2 \mu_0 \varepsilon(\omega) \mathbf{E} $$
$$ -k^2 \mathbf{E} = -\omega^2 \mu_0 \varepsilon(\omega) \mathbf{E} $$
得到: $k^2 = \omega^2 \mu_0 \varepsilon(\omega)$。代入 $\varepsilon(\omega)$ 及 $c^2 = 1/(\mu_0 \varepsilon_0)$:
$$ k^2 = \omega^2 \mu_0 \varepsilon_0 \left(1 - \frac{\omega_p^2}{\omega^2}\right) = \frac{\omega^2}{c^2} \left(1 - \frac{\omega_p^2}{\omega^2}\right) $$
**色散关系 (Dispersion relation / 分散関係):**
$$ \omega^2 = \omega_p^2 + k^2 c^2 $$

## 3. 传播条件 (Propagation condition / 伝播条件)

波传播要求波数 $k$ 为实数 (real number / 実数), 即 $k^2 \ge 0$:
$$ \frac{\omega^2 - \omega_p^2}{c^2} \ge 0 \implies \omega^2 \ge \omega_p^2 $$
故传播条件为 (Propagation condition / 伝播条件):
$$ \omega \ge \omega_p $$
*   $\omega > \omega_p$: $k$ 为实数, 波传播 (Wave propagates / 波は伝播する)。
*   $\omega < \omega_p$: $k$ 为纯虚数 (pure imaginary / 純虚数), 波衰减 (倏逝波 (Evanescent wave / エバネッセント波)), 反射 (Reflection / 反射)。
*   $\omega = \omega_p$: $k=0$, 截止频率 (Cut-off frequency / 遮断周波数)。

# [问题3] 13.6eV 的能量的质子撞击静止的氢原子。能够使其电离吗？请说明理由。如果换成相同能量的电子情况如何？此外，质子要电离氢原子，所需的最低能量是多少？（提示：从质心运动和相对运动的观点考虑。）

## 氢原子电离阈能 (水素原子の電離閾エネルギー)

**核心概念 (Core Concepts / コア概念):**
*   氢原子电离能 (H-atom ionization energy / 水素原子の電離エネルギー): $E_{ion} = 13.6 \text{ eV}$.
*   碰撞中，仅 **质心系能量 (Center-of-Mass energy / 重心系エネルギー)** $E_{CM}$ (即相对动能 / relative kinetic energy / 相対運動エネルギー) 可用于非弹性过程 (inelastic processes / 非弾性過程) 如电离。

**质心系可用能量公式 (CM Available Energy Formula / 重心系で利用可能なエネルギーの公式):**
入射粒子 (Incident particle / 入射粒子) $m_1$, 实验室系动能 (Lab frame kinetic energy / 実験室系運動エネルギー) $K_{lab}$。
靶粒子 (Target particle / 標的粒子) $m_2$ (静止 / at rest / 静止)。
$$ E_{CM} = \frac{m_2}{m_1 + m_2} K_{lab} $$
电离条件 (Ionization condition / 電離条件): $E_{CM} \ge E_{ion}$.

**符号 (Symbols / 記号):** $m_p$ (质子质量 / proton mass / 陽子質量), $m_e$ (电子质量 / electron mass / 電子質量), $m_H \approx m_p$ (氢原子质量 / H-atom mass / 水素原子質量).

---

**1. 13.6 eV 质子撞击氢原子 (13.6 eV proton impacting H-atom / 13.6 eV 陽子による水素原子衝突):**
*   入射 (Incident / 入射): 质子 (proton / 陽子) $m_1=m_p$, $K_{lab}=13.6 \text{ eV}$.
*   靶 (Target / 標的): H原子 (H-atom / H原子) $m_2 \approx m_p$.
$$ E_{CM} = \frac{m_p}{m_p+m_p} K_{lab} = \frac{1}{2} K_{lab} = \frac{1}{2} (13.6 \text{ eV}) = 6.8 \text{ eV} $$
$E_{CM} (6.8 \text{ eV}) < E_{ion} (13.6 \text{ eV})$.
**结论 (Conclusion / 結論):** 不能电离 (Cannot ionize / 電離不可).
**理由 (Reason / 理由):** $E_{CM}$ 不足 (insufficient / 不足).

---

**2. 13.6 eV 电子撞击氢原子 (13.6 eV electron impacting H-atom / 13.6 eV 電子による水素原子衝突):**
*   入射 (Incident / 入射): 电子 (electron / 電子) $m_1=m_e$, $K_{lab}=13.6 \text{ eV}$.
*   靶 (Target / 標的): H原子 (H-atom / H原子) $m_2 \approx m_p$.
$$ E_{CM} = \frac{m_p}{m_e+m_p} K_{lab} \approx \frac{m_p}{m_p} K_{lab} = K_{lab} = 13.6 \text{ eV} \quad (\text{因 } m_e \ll m_p) $$
$E_{CM} (13.6 \text{ eV}) \ge E_{ion} (13.6 \text{ eV})$.
**结论 (Conclusion / 結論):** 可电离 (阈值状态) (Can ionize (threshold) / 電離可能 (閾値)).
**理由 (Reason / 理由):** $E_{CM} \approx K_{lab}$ (因 $m_e \ll m_p$ / due to $m_e \ll m_p$ / $m_e \ll m_p$ のため).

---

**3. 质子电离H原子所需最低能量 (Min. proton energy for H-atom ionization / 陽子によるH原子電離の最低エネルギー):**
需 (Required / 必要) $E_{CM, min} = E_{ion} = 13.6 \text{ eV}$.
对于质子-氢原子碰撞 (For p-H collision / p-H衝突): $E_{CM} = \frac{1}{2} K_{lab}$.
$$ \frac{1}{2} K_{lab, min} = E_{ion} $$
$$ K_{lab, min} = 2 E_{ion} = 2 \times 13.6 \text{ eV} = 27.2 \text{ eV} $$
**结论 (Conclusion / 結論):** 最低入射能量 (Min. incident energy / 最低入射エネルギー) $K_{lab, min} = 27.2 \text{ eV}$.

# [问题4] 中性气体的扩散系数を推定しなさい。気体分子の半径を $0.5 \times 10^{-10} \text{ m}^{-1}$、個数を $N = 3 \times 10^{25} \text{ m}^{-3}$、速度を $350 \text{ m/s}$ とする。また、プラズマ衝突振動数は温度にどのように依存するか。
(估计中性气体的扩散系数。设气体分子半径为 $0.5 \times 10^{-10} \text{ m}$，数密度为 $N = 3 \times 10^{25} \text{ m}^{-3}$，速度为 $350 \text{ m/s}$。此外，等离子体碰撞频率如何依赖于温度？)

## 气体扩散与等离子体碰撞 (気体拡散とプラズマ衝突)

**1. 中性气体扩散系数 (Neutral Gas Diffusion / 中性気体の拡散係数)**

*   **公式 (Formula / 公式):** $D \approx \frac{1}{3} \lambda \bar{v}$
    *   $\lambda$: 平均自由程 (Mean free path / 平均自由行程)
    *   $\bar{v}$: 平均速度 (Average velocity / 平均速度)
*   **平均自由程 (Mean free path / 平均自由行程):** $\lambda = \frac{1}{\sqrt{2} N \sigma_{coll}}$
    *   $N$: 数密度 (Number density / 数密度)
    *   $\sigma_{coll}$: 碰撞截面 (Collision cross-section / 衝突断面積) $= 4\pi r_m^2$ ($r_m$: 分子半径 / molecular radius / 分子半径)
*   **参数 (Parameters / パラメータ):**
    *   $r_m = 0.5 \times 10^{-10} \text{ m}$
    *   $N = 3 \times 10^{25} \text{ m}^{-3}$
    *   $\bar{v} = 350 \text{ m/s}$
*   **计算 (Calculation / 計算):**
    1.  $\sigma_{coll} = 4\pi (0.5 \times 10^{-10})^2 = \pi \times 10^{-20} \text{ m}^2$
    2.  $\lambda = \frac{1}{\sqrt{2} (3 \times 10^{25}) (\pi \times 10^{-20})} \approx 7.50 \times 10^{-7} \text{ m}$
    3.  $D \approx \frac{1}{3} (7.50 \times 10^{-7} \text{ m}) (350 \text{ m/s}) \approx 8.75 \times 10^{-6} \text{ m}^2/\text{s}$
*   **结果 (Result / 結果):** $D \approx 8.75 \times 10^{-6} \text{ m}^2/\text{s}$

---

**2. 等离子体碰撞频率与温度依赖性 (Plasma Collision Freq. vs Temp. / プラズマ衝突振動数と温度依存性)**

*   碰撞频率 (Collision freq. / 衝突振動数): $\nu \approx n \sigma v_{rel}$
*   热速度 (Thermal velocity / 熱速度): $v_{th} \propto T^{1/2}$
*   库仑碰撞截面 (Coulomb cross-section / クーロン衝突断面積): $\sigma_{Coulomb} \propto \frac{\ln \Lambda}{T^2}$
    *   $\ln \Lambda$: 库仑对数 (Coulomb logarithm / クーロン対数) (弱依赖 $T$ / weakly T-dependent / Tに弱く依存)
*   电子-离子碰撞频率 (e-i collision freq. / 電子イオン衝突振動数) $\nu_{ei}$:
    $$ \nu_{ei} \propto n_i \sigma_{ei} v_{th,e} \propto n_i \left(\frac{\ln \Lambda}{T_e^2}\right) T_e^{1/2} \propto n_i \frac{\ln \Lambda}{T_e^{3/2}} $$
*   **结论 (Conclusion / 結論):** $\nu_{ei} \propto T_e^{-3/2}$ (忽略 $\ln \Lambda$ 的弱依赖性 / ignoring weak dependence of $\ln \Lambda$ / $\ln \Lambda$ の弱い依存性を無視).

# [问题5] 电子的流体方程式を用いて、ボルツマン関係を導出しなさい。また、電子音波の分散関係を導出しなさい。
(使用电子的流体方程，推导玻尔兹曼关系。另外，推导电子声波的色散关系。)

## 电子流体：玻尔兹曼关系与电子声波 (Electron Fluid: Boltzmann Relation & Electron Acoustic Wave)
(電子流体：ボルツマン関係と電子音波)

## 1. 玻尔兹曼关系推导 (Boltzmann Relation Derivation / ボルツマン関係の導出)

*   **电子动量方程 (e-Momentum Eq. / 電子運動量方程式) (1D, 无碰撞 / collisionless / 無衝突):**
    $$ m_e n_e \left( \frac{\partial v_e}{\partial t} + v_e \frac{\partial v_e}{\partial x} \right) = -e n_e E - \frac{\partial p_e}{\partial x} $$
*   **假设 (Assumptions / 仮定):**
    1.  忽略惯性 (Neglect inertia / 慣性を無視): 左侧 $\approx 0$ (因 $m_e$ 小 / $m_e$ is small / $m_e$が小さいため).
    2.  静电场 (Electrostatic field / 静電場): $E = -\frac{\partial \phi}{\partial x}$.
    3.  等温电子 (Isothermal e- / 等温電子): $p_e = n_e k_B T_e \implies \frac{\partial p_e}{\partial x} = k_B T_e \frac{\partial n_e}{\partial x}$.
*   **简化方程 (Simplified Eq. / 単純化された方程式):**
    $$ 0 = e n_e \frac{\partial \phi}{\partial x} - k_B T_e \frac{\partial n_e}{\partial x} \implies e d\phi = k_B T_e \frac{dn_e}{n_e} $$
*   **积分 (Integration / 積分):**
    $$ e\phi = k_B T_e \ln n_e + \text{Const} \implies n_e = n_{e0} \exp\left(\frac{e\phi}{k_B T_e}\right) $$
    其中 $n_{e0}$ 为 $\phi=0$ 处的密度 (density at $\phi=0$ / $\phi=0$での密度)。
    线性化 (Linearized / 線形化): $n_{e1} = n_e - n_{e0} \approx n_{e0} \frac{e\phi}{k_B T_e}$.

## 2. 电子声波色散关系 (Electron Acoustic Wave Dispersion / 電子音波の分散関係)
(也称朗缪尔波 / aka Langmuir wave / ラングミュア波とも呼ばれる)

*   **线性化流体方程 (Linearized fluid eqs. / 線形化流体方程式):**
    (离子不动 / Ions immobile / イオン不動)
    1.  **连续性 (Continuity / 連続の式):** $\frac{\partial n_{e1}}{\partial t} + n_{e0} \frac{\partial v_{e1}}{\partial x} = 0 \xrightarrow{FT} -i\omega n_{e1} + ik n_{e0} v_{e1} = 0 \quad (A)$
    2.  **动量 (Momentum / 運動量):** $m_e n_{e0} \frac{\partial v_{e1}}{\partial t} = -e n_{e0} E_1 - \gamma_e k_B T_e \frac{\partial n_{e1}}{\partial x} \xrightarrow{FT} -i\omega m_e n_{e0} v_{e1} = -e n_{e0} E_1 - ik \gamma_e k_B T_e n_{e1} \quad (B)$
        ($\gamma_e$: 绝热指数 / adiabatic index / 断熱指数, e.g., 1 or 3)
    3.  **泊松方程 (Poisson / ポアソン):** $\frac{\partial E_1}{\partial x} = -\frac{e n_{e1}}{\varepsilon_0} \xrightarrow{FT} ik E_1 = -\frac{e n_{e1}}{\varepsilon_0} \implies E_1 = \frac{ie n_{e1}}{k \varepsilon_0} \quad (C)$
*   **求解 (Solving / 解法):**
    由 (A): $v_{e1} = \frac{\omega}{k n_{e0}} n_{e1}$. 代入 (B), 并用 (C) 消 $E_1$:
    $$ -i\omega m_e n_{e0} \left(\frac{\omega}{k n_{e0}} n_{e1}\right) = -e n_{e0} \left(\frac{ie n_{e1}}{k \varepsilon_0}\right) - ik \gamma_e k_B T_e n_{e1} $$
    $$ \omega^2 m_e = \frac{n_{e0} e^2}{\varepsilon_0} + \gamma_e k_B T_e k^2 $$
*   **色散关系 (Dispersion Relation / 分散関係):**
    $$ \omega^2 = \omega_{pe}^2 + v_{the}^2 k^2 $$
    *   $\omega_{pe}^2 = \frac{n_{e0} e^2}{m_e \varepsilon_0}$: 电子等离子体频率平方 (e-plasma freq. squared / 電子プラズマ周波数二乗).
    *   $v_{the}^2 = \frac{\gamma_e k_B T_e}{m_e}$: 电子热速度平方 (e-thermal velocity squared / 電子熱速度二乗).
    (玻姆-格罗斯色散关系 / Bohm-Gross dispersion / ボームグロス分散関係)

# [问题6] 解 MHD 方程式以说明阿尔文波 (Alfvén wave) 的色散关系。此处，压力的效果可以忽略。解弦的波动方程并讨论其关系。

## 阿尔文波与弦波 (アルフベン波と弦の波)

**A. 阿尔文波色散关系 (Alfvén Wave Dispersion / アルフベン波の分散関係)**

1.  **MHD 方程 (MHD Eqns. / MHD方程式) (无压 / Pressureless / 無圧力):**
    *   动量 (Momentum / 運動量): $\rho_{m0} \frac{\partial \delta \mathbf{v}}{\partial t} = \frac{1}{\mu_0} (\nabla \times \delta \mathbf{B}) \times \mathbf{B}_0$
    *   感应 (Induction / 誘導): $\frac{\partial \delta \mathbf{B}}{\partial t} = (\mathbf{B}_0 \cdot \nabla)\delta \mathbf{v}$ (不可压 / Incompressible / 非圧縮)

2.  **平面波解 (Plane Wave Solution / 平面波解):** $\propto \exp[i(\mathbf{k} \cdot \mathbf{r} - \omega t)]$, $\nabla \to i\mathbf{k}, \frac{\partial}{\partial t} \to -i\omega$.
    *   $-i\omega \delta \mathbf{B} = i(\mathbf{B}_0 \cdot \mathbf{k})\delta \mathbf{v} \implies \delta \mathbf{B} = -\frac{(\mathbf{B}_0 \cdot \mathbf{k})}{\omega} \delta \mathbf{v}$
    *   $-i\omega \rho_{m0} \delta \mathbf{v} = \frac{i}{\mu_0} (\mathbf{k} \cdot \mathbf{B}_0)\delta \mathbf{B}$

3.  **色散关系 (Dispersion Relation / 分散関係):** 联立消去 $\delta\mathbf{B}$ 与 $\delta\mathbf{v}$:
    $$ \omega^2 \rho_{m0} = \frac{(\mathbf{k} \cdot \mathbf{B}_0)^2}{\mu_0} = \frac{k^2 B_0^2 \cos^2\theta}{\mu_0} $$
    定义 **阿尔文速度 (Alfvén Velocity / アルフベン速度) $v_A$**: $v_A^2 = \frac{B_0^2}{\mu_0 \rho_{m0}}$.
    $$ \omega^2 = k^2 v_A^2 \cos^2\theta \implies \omega = k v_A |\cos\theta| $$
    ($\theta$ 为 $\mathbf{k}$ 与 $\mathbf{B}_0$ 夹角 / angle between $\mathbf{k}$ and $\mathbf{B}_0$ / $\mathbf{k}$ と $\mathbf{B}_0$ の間の角度).

---

**B. 弦波 (String Wave / 弦の波)**

1.  **波动方程 (Wave Equation / 波動方程式):** $\frac{\partial^2 y}{\partial t^2} = v_s^2 \frac{\partial^2 y}{\partial x^2}$
    *   $v_s = \sqrt{T/\lambda}$ (波速 / Wave speed / 波の速度)
    *   $T$: 张力 (Tension / 張力)
    *   $\lambda$: 线密度 (Linear density / 線密度)

2.  **色散关系 (Dispersion Relation / 分散関係):** 设 $y \propto e^{i(kx-\omega t)}$:
    $$ \omega^2 = k^2 v_s^2 \implies \omega = k v_s $$

---

**C. 关系 (Relationship / 関係)**

*   **相似性 (Similarity / 類似性):** 当 $\theta=0$, $\omega = k v_A$, 与 $\omega = k v_s$ 形式相同。
*   **类比 (Analogy / アナロジー):**
    *   磁力线 (Magnetic field lines / 磁力線) $\leftrightarrow$ 弦 (String / 弦)
    *   磁张力 ($B_0^2/\mu_0$) (Magnetic tension / 磁気張力) $\leftrightarrow$ 弦张力 $T$ (String tension / 弦の張力)
    *   等离子体密度 ($\rho_{m0}$) (Plasma density / プラズマ密度) $\leftrightarrow$ 弦线密度 $\lambda$ (String density / 弦の密度)
*   **物理图像 (Physical Picture / 物理的描像):** 阿尔文波是磁力线作为弹性介质的横向扰动 (transverse disturbance / 横方向の摂動)，等离子体提供惯性 (inertia / 慣性)。$\cos\theta$ 因子表示波主要沿磁场传播 (propagates mainly along B-field / 主に磁場に沿って伝播)。

# [问题7] 托卡马克中为了约束等离子体，需要在等离子体中通入电流。这是为什么？

## 托卡马克等离子体电流必要性 (トカマクプラズマ電流の必要性)

**核心目的 (Core Purpose / 主な目的):** 磁约束 (Magnetic confinement / 磁気閉じ込め)

1.  **产生极向磁场 ($B_p$) (Poloidal field generation / ポロイダル磁場生成):**
    *   环向电流 ($I_p$) (Toroidal current / トロイダル電流) $\implies$ 极向磁场 ($B_p$) (Poloidal field / ポロイダル磁場). (安培定律 / Ampere's Law / アンペールの法則).

2.  **形成螺旋磁场线/磁面 (Helical field lines/surfaces / 螺旋磁力線・磁気面の形成):**
    *   $B_p$ + 外部环向磁场 ($B_T$) (External toroidal field / 外部トロイダル磁場) $\implies$ 螺旋磁场 (Helical field / 螺旋磁場) & 嵌套磁面 (Nested magnetic surfaces / 入れ子状磁気面).
    *   粒子沿磁面运动 (Particles follow surfaces / 粒子は磁気面に沿って運動).

3.  **克服粒子漂移损失 (Counteract particle drift loss / 粒子ドリフト損失の抑制):**
    *   **问题 (Problem / 問題点):** 仅 $B_T \implies \nabla B$ & 曲率漂移 (Curvature drift / 曲率ドリフト) $\implies$ 电荷分离 (Charge separation / 電荷分離) $\implies$ 垂直电场 ($E_v$) $\implies \mathbf{E}_v \times \mathbf{B}_T$ 漂移 (向外损失 / outward loss / 外向き損失).
    *   **解决 (Solution / 解決策):** 螺旋磁场线 “短路” (Short-circuit / 短絡) 电荷分离，减小 $E_v$ 和 $\mathbf{E} \times \mathbf{B}$ 漂移。

4.  **实现等离子体平衡 (Achieve plasma equilibrium / プラズマ平衡の実現):**
    *   洛伦兹力 ($\mathbf{J}_p \times \mathbf{B}_p$) (Lorentz force / ローレンツ力) 平衡等离子体压力梯度 ($\nabla p$) (Balances pressure gradient / プラズマ圧力勾配と平衡).
    *   $\nabla p = \mathbf{J} \times \mathbf{B}$ (磁流体平衡 / MHD equilibrium / MHD平衡).

**总结 (Summary / まとめ):**
等离子体电流 ($I_p$) $\implies B_p \implies$ 螺旋磁场 (约束/平衡) (Helical field (confinement/equilibrium) / 螺旋磁場 (閉じ込め/平衡)).

# [问题8] フォッカープランクの式を導出し、衝突拡散の表式について説明しなさい。
(推导福克-普朗克方程，并说明碰撞扩散的表达式。)

## 福克-普朗克方程与碰撞扩散 (フォッカー・プランク方程式と衝突拡散)

## 1. 福克-普朗克方程推导 (Derivation / 導出)

描述分布函数 $f(\mathbf{v},t)$ 因大量小角度碰撞 (small-angle collisions / 小角度衝突) 的演化。

1.  **从主方程 (From Master eq. / マスター方程式から):**
    设 $P(\mathbf{v}', \Delta\mathbf{v})$ 为从 $\mathbf{v}'$ 经碰撞速度改变 $\Delta\mathbf{v}$ 的单位时间跃迁概率 (transition probability per unit time / 単位時間あたりの遷移確率)。
    $$ \left(\frac{\partial f(\mathbf{v})}{\partial t}\right)_{\text{coll}} = \int \left[ f(\mathbf{v}-\Delta\mathbf{v}) P(\mathbf{v}-\Delta\mathbf{v}, \Delta\mathbf{v}) - f(\mathbf{v}) P(\mathbf{v}, \Delta\mathbf{v}) \right] d(\Delta\mathbf{v}) $$
2.  **泰勒展开 (Taylor Expansion / テイラー展開):**
    假设 $\Delta\mathbf{v}$ 小，对 $f(\mathbf{v}-\Delta\mathbf{v})P(\mathbf{v}-\Delta\mathbf{v}, \Delta\mathbf{v})$ 展开至二阶 (Expand to 2nd order / 2次まで展開):
    $$ \left(\frac{\partial f}{\partial t}\right)_{\text{coll}} \approx -\sum_i \frac{\partial}{\partial v_i} \left( f \int \Delta v_i P \,d(\Delta\mathbf{v}) \right) + \frac{1}{2} \sum_{i,j} \frac{\partial^2}{\partial v_i \partial v_j} \left( f \int \Delta v_i \Delta v_j P \,d(\Delta\mathbf{v}) \right) $$
3.  **定义系数 (Define coefficients / 係数の定義):**
    *   **漂移矢量 (Drift vector / ドリフトベクトル) $A_i(\mathbf{v})$**:
        $$ A_i(\mathbf{v}) = \langle \Delta v_i \rangle_t = \int \Delta v_i P(\mathbf{v}, \Delta\mathbf{v}) d(\Delta\mathbf{v}) $$
    *   **扩散张量 (Diffusion tensor / 拡散テンソル) $B_{ij}(\mathbf{v})$**:
        $$ B_{ij}(\mathbf{v}) = \langle \Delta v_i \Delta v_j \rangle_t = \int \Delta v_i \Delta v_j P(\mathbf{v}, \Delta\mathbf{v}) d(\Delta\mathbf{v}) $$
    (其中 $\langle \dots \rangle_t$ 表示单位时间平均 / average per unit time / 単位時間あたりの平均)
4.  **福克-普朗克方程 (Fokker-Planck eq. / フォッカー・プランク方程式):**
    $$ \left(\frac{\partial f}{\partial t}\right)_{\text{coll}} = -\sum_i \frac{\partial}{\partial v_i} (A_i f) + \frac{1}{2} \sum_{i,j} \frac{\partial^2}{\partial v_i \partial v_j} (B_{ij} f) $$
    *   第一项: 速度空间漂移 (Drift in v-space / 速度空間のドリフト) (动力学摩擦 / dynamical friction / 動摩擦力)。
    *   第二项: 速度空间扩散 (Diffusion in v-space / 速度空間の拡散)。
    *   库仑碰撞对应朗道碰撞积分 (Landau collision integral for Coulomb collisions / クーロン衝突に対するランダウ衝突積分)。

## 2. 碰撞扩散表达式 (Collisional Diffusion Expression / 衝突拡散の表式)

指实空间 (real space / 実空間) 由于碰撞的粒子扩散。

1.  **扩散通量 (Diffusion flux / 拡散フラックス):** $\mathbf{\Gamma} = -D \nabla n$ ($D$: 扩散系数 / diffusion coeff. / 拡散係数)
2.  **无磁场或平行磁场 (No B-field / Parallel to B / 磁場なし/磁場に平行):**
    $$ D_{\parallel} \approx v_{th}^2 \tau_c = v_{th}^2 / \nu_c $$
    ($v_{th}$: 热速率 / thermal speed / 熱速度, $\nu_c$: 碰撞频率 / collision freq. / 衝突周波数)
3.  **垂直磁场 (经典) (Perpendicular to B (Classical) / 磁場に垂直 (古典的)):**
    由于拉莫尔轨道引导中心 (guiding center / 案内中心) 的随机行走 (random walk / ランダムウォーク)。
    $$ D_{\perp} \approx \rho_L^2 \nu_{coll} $$
    *   $\rho_L = m v_{\perp} / (qB)$: 拉莫尔半径 (Larmor radius / ラーマー半径)
    *   $\nu_{coll}$: 有效碰撞频率 (Effective collision freq. / 有効衝突周波数) (e.g., $\nu_{ei}$ for electrons)
4.  **电子经典扩散 (Electron classical diffusion / 電子の古典的拡散):**
    $D_{\perp,e} \approx \rho_{Le}^2 \nu_{ei}$
    $$ \nu_{ei} \propto n_i Z^2 T_e^{-3/2} \ln\Lambda $$
    $$ D_{\perp,e} \propto n_e Z_{eff} (m_e^{1/2}) T_e^{-1/2} B^{-2} \ln\Lambda $$
    *   关键依赖 (Key dependencies / 主要な依存性): $n_e$, $T_e^{-1/2}$, $B^{-2}$.

</div>