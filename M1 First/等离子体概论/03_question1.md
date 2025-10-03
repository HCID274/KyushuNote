## 在磁场 $\vec{B} = (0, 0, B)$ 中带电粒子的运动方程、电导率张量与介电张量推导

### 1. 写出运动方程

我们从单个带电粒子的洛伦兹力定律出发。设粒子质量为 $m$，电荷为 $q$。其运动方程为：
$m \frac{d\vec{v}}{dt} = q\vec{E} + q(\vec{v} \times \vec{B})$
给定的磁场为 $\vec{B} = (0, 0, B_0)$（为了区分磁场大小和矢量的分量，这里用 $B_0$ 表示磁感应强度大小）。
所以运动方程为：
$m \frac{d\vec{v}}{dt} = q\vec{E} + q(\vec{v} \times (0, 0, B_0))$

### 2. 假设稳态解

假设电场 $\vec{E}$ 和粒子速度 $\vec{v}$ 都以角频率 $\omega$ 随时间作正弦（或复指数）变化：
$\vec{E}(t) = \vec{E} e^{-i\omega t}$
$\vec{v}(t) = \vec{v} e^{-i\omega t}$
这里，等式右边的 $\vec{E}$ 和 $\vec{v}$ 代表复振幅，不显含时间。
利用这个假设，时间导数 $d/dt$ 可以替换为乘以 $-i\omega$：
$\frac{d\vec{v}}{dt} = -i\omega \vec{v}$
代入运动方程，得到代数方程：
$-i\omega m \vec{v} = q\vec{E} + q(\vec{v} \times \vec{B})$

### 3. 分量求解

首先计算叉乘项 $\vec{v} \times \vec{B}$：
$\vec{v} \times \vec{B} = \begin{vmatrix} \hat{x} & \hat{y} & \hat{z} \\ v_x & v_y & v_z \\ 0 & 0 & B_0 \end{vmatrix} = (v_y B_0)\hat{x} - (v_x B_0)\hat{y} + 0\hat{z} = (B_0 v_y, -B_0 v_x, 0)$
将矢量方程 $-i\omega m \vec{v} = q\vec{E} + q(\vec{v} \times \vec{B})$ 写成三个分量形式：

*   **z 分量:**
    $-i\omega m v_z = q E_z + q (\vec{v} \times \vec{B})_z$
    $-i\omega m v_z = q E_z + 0$
    直接解出 $v_z$:
    $v_z = \frac{q E_z}{-i\omega m} = \frac{i q}{\omega m} E_z$ (1)

*   **x 分量:**
    $-i\omega m v_x = q E_x + q (\vec{v} \times \vec{B})_x$
    $-i\omega m v_x = q E_x + q B_0 v_y$ (2)

*   **y 分量:**
    $-i\omega m v_y = q E_y + q (\vec{v} \times \vec{B})_y$
    $-i\omega m v_y = q E_y - q B_0 v_x$ (3)

现在我们需要解关于 $v_x$ 和 $v_y$ 的二元线性方程组 (2) 和 (3)。
为了简化，引入回旋频率 (Cyclotron Frequency) $\omega_c = \frac{q B_0}{m}$。注意 $\omega_c$ 的符号取决于 $q$ 的符号。
方程组 (2) 和 (3) 可以改写为：
$-i\omega v_x = \frac{q}{m} E_x + \omega_c v_y$
$-i\omega v_y = \frac{q}{m} E_y - \omega_c v_x$

整理得到：
$(-i\omega) v_x - \omega_c v_y = \frac{q}{m} E_x$ (2')
$\omega_c v_x + (-i\omega) v_y = \frac{q}{m} E_y$ (3')

我们可以用矩阵形式求解：
$\begin{pmatrix} -i\omega & -\omega_c \\ \omega_c & -i\omega \end{pmatrix} \begin{pmatrix} v_x \\ v_y \end{pmatrix} = \frac{q}{m} \begin{pmatrix} E_x \\ E_y \end{pmatrix}$
矩阵的行列式 $D = (-i\omega)(-i\omega) - (-\omega_c)(\omega_c) = -\omega^2 + \omega_c^2 = \omega_c^2 - \omega^2$.
逆矩阵为 $\frac{1}{\omega_c^2 - \omega^2} \begin{pmatrix} -i\omega & \omega_c \\ -\omega_c & -i\omega \end{pmatrix}$.
所以：
$\begin{pmatrix} v_x \\ v_y \end{pmatrix} = \frac{1}{\omega_c^2 - \omega^2} \begin{pmatrix} -i\omega & \omega_c \\ -\omega_c & -i\omega \end{pmatrix} \frac{q}{m} \begin{pmatrix} E_x \\ E_y \end{pmatrix}$
解出 $v_x$ 和 $v_y$:
$v_x = \frac{q/m}{\omega_c^2 - \omega^2} (-i\omega E_x + \omega_c E_y)$ (4)
$v_y = \frac{q/m}{\omega_c^2 - \omega^2} (-\omega_c E_x - i\omega E_y)$ (5)

### 4. 计算电导率张量 $\overleftrightarrow{\sigma}$

电流密度 $\vec{j}$ 由 $\vec{j} = n q \vec{v}$ 给出，其中 $n$ 是带电粒子数密度。
我们将上面得到的 $v_x, v_y, v_z$ 代入。
为了与更一般的情况（多种带电粒子）兼容，我们用下标 $s$ 表示粒子种类，则 $\omega_{cs} = q_s B_0 / m_s$ 和 $\omega_{ps}^2 = n_s q_s^2 / (\epsilon_0 m_s)$。总电流是各种粒子电流之和 $\vec{j} = \sum_s n_s q_s \vec{v}_s$。
这里为了简化，我们先考虑单一粒子种类，最后再推广。
$\frac{nq^2}{m} = \epsilon_0 \omega_p^2$, 其中 $\omega_p = \sqrt{\frac{nq^2}{\epsilon_0 m}}$ 是等离子体频率。

$j_x = nq v_x = nq \frac{q/m}{\omega_c^2 - \omega^2} (-i\omega E_x + \omega_c E_y) = \frac{nq^2/m}{\omega_c^2 - \omega^2}(-i\omega E_x + \omega_c E_y)$
$j_y = nq v_y = nq \frac{q/m}{\omega_c^2 - \omega^2} (-\omega_c E_x - i\omega E_y) = \frac{nq^2/m}{\omega_c^2 - \omega^2}(-\omega_c E_x - i\omega E_y)$
$j_z = nq v_z = nq \frac{iq}{\omega m} E_z = \frac{inq^2}{\omega m} E_z$

电导率张量 $\overleftrightarrow{\sigma}$ 定义为 $\vec{j} = \overleftrightarrow{\sigma} \vec{E}$，即：
$j_k = \sum_l \sigma_{kl} E_l$
对比系数，我们得到：
$\sigma_{xx} = \frac{nq^2/m (-i\omega)}{\omega_c^2 - \omega^2} = \frac{-i\omega (nq^2/m)}{\omega_c^2 - \omega^2} = \frac{i\omega \epsilon_0 \omega_p^2}{\omega^2 - \omega_c^2}$
$\sigma_{xy} = \frac{nq^2/m (\omega_c)}{\omega_c^2 - \omega^2} = \frac{\omega_c (nq^2/m)}{\omega_c^2 - \omega^2} = \frac{-\omega_c \epsilon_0 \omega_p^2}{\omega^2 - \omega_c^2}$
$\sigma_{xz} = 0$

$\sigma_{yx} = \frac{nq^2/m (-\omega_c)}{\omega_c^2 - \omega^2} = \frac{-\omega_c (nq^2/m)}{\omega_c^2 - \omega^2} = \frac{\omega_c \epsilon_0 \omega_p^2}{\omega^2 - \omega_c^2}$
$\sigma_{yy} = \frac{nq^2/m (-i\omega)}{\omega_c^2 - \omega^2} = \frac{-i\omega (nq^2/m)}{\omega_c^2 - \omega^2} = \frac{i\omega \epsilon_0 \omega_p^2}{\omega^2 - \omega_c^2}$
$\sigma_{yz} = 0$

$\sigma_{zx} = 0$
$\sigma_{zy} = 0$
$\sigma_{zz} = \frac{inq^2}{\omega m} = \frac{i\epsilon_0 \omega_p^2}{\omega}$

所以电导率张量为：
$\overleftrightarrow{\sigma} = \begin{pmatrix} \sigma_{xx} & \sigma_{xy} & 0 \\ \sigma_{yx} & \sigma_{yy} & 0 \\ 0 & 0 & \sigma_{zz} \end{pmatrix} = \epsilon_0 \omega_p^2 \begin{pmatrix} \frac{i\omega}{\omega^2 - \omega_c^2} & \frac{-\omega_c}{\omega^2 - \omega_c^2} & 0 \\ \frac{\omega_c}{\omega^2 - \omega_c^2} & \frac{i\omega}{\omega^2 - \omega_c^2} & 0 \\ 0 & 0 & \frac{i}{\omega} \end{pmatrix}$
注意到 $\sigma_{xx} = \sigma_{yy}$ 且 $\sigma_{yx} = -\sigma_{xy}$。

### 5. 计算介电张量 $\overleftrightarrow{\varepsilon}$

介电张量 $\overleftrightarrow{\varepsilon}(\omega)$ 与电导率张量 $\overleftrightarrow{\sigma}(\omega)$ 的关系为：
$\overleftrightarrow{\varepsilon}(\omega) = \epsilon_0 \overleftrightarrow{I} + \frac{i}{\omega} \overleftrightarrow{\sigma}(\omega)$
其中 $\overleftrightarrow{I}$ 是 $3 \times 3$ 的单位矩阵。
$\varepsilon_{xx} = \epsilon_0 + \frac{i}{\omega} \sigma_{xx} = \epsilon_0 + \frac{i}{\omega} \left( \frac{i\omega \epsilon_0 \omega_p^2}{\omega^2 - \omega_c^2} \right) = \epsilon_0 + \frac{-\omega \epsilon_0 \omega_p^2}{\omega(\omega^2 - \omega_c^2)} = \epsilon_0 \left(1 - \frac{\omega_p^2}{\omega^2 - \omega_c^2}\right)$
$\varepsilon_{yy} = \epsilon_0 + \frac{i}{\omega} \sigma_{yy} = \varepsilon_{xx}$

$\varepsilon_{xy} = \frac{i}{\omega} \sigma_{xy} = \frac{i}{\omega} \left( \frac{-\omega_c \epsilon_0 \omega_p^2}{\omega^2 - \omega_c^2} \right) = \frac{-i\omega_c \epsilon_0 \omega_p^2}{\omega(\omega^2 - \omega_c^2)}$
$\varepsilon_{yx} = \frac{i}{\omega} \sigma_{yx} = \frac{i}{\omega} \left( \frac{\omega_c \epsilon_0 \omega_p^2}{\omega^2 - \omega_c^2} \right) = \frac{i\omega_c \epsilon_0 \omega_p^2}{\omega(\omega^2 - \omega_c^2)}$
注意到 $\varepsilon_{yx} = -\varepsilon_{xy}$.

$\varepsilon_{zz} = \epsilon_0 + \frac{i}{\omega} \sigma_{zz} = \epsilon_0 + \frac{i}{\omega} \left( \frac{i\epsilon_0 \omega_p^2}{\omega} \right) = \epsilon_0 + \frac{-\epsilon_0 \omega_p^2}{\omega^2} = \epsilon_0 \left(1 - \frac{\omega_p^2}{\omega^2}\right)$
其余非对角元 $\varepsilon_{xz}, \varepsilon_{zx}, \varepsilon_{yz}, \varepsilon_{zy}$ 均为0。

所以介电张量为：
$\overleftrightarrow{\varepsilon}(\omega) = \epsilon_0 \begin{pmatrix}
1 - \frac{\omega_p^2}{\omega^2 - \omega_c^2} & \frac{-i\omega_c \omega_p^2}{\omega(\omega^2 - \omega_c^2)} & 0 \\
\frac{i\omega_c \omega_p^2}{\omega(\omega^2 - \omega_c^2)} & 1 - \frac{\omega_p^2}{\omega^2 - \omega_c^2} & 0 \\
0 & 0 & 1 - \frac{\omega_p^2}{\omega^2}
\end{pmatrix}$

### 6. 最终结果与老师黑板展示的对比

老师黑板上展示的介电张量形式为：
$\overleftrightarrow{\varepsilon}(\omega) = \begin{pmatrix} \varepsilon_{\perp} & i\varepsilon_x & 0 \\ -i\varepsilon_x & \varepsilon_{\perp} & 0 \\ 0 & 0 & \varepsilon_{\parallel} \end{pmatrix}$
其中，对于包含多种带电粒子 $s$ 的情况 (例如电子和不同种类的离子，我们将上面单粒子推导中的 $\omega_p^2$ 替换为 $\sum_s \omega_{ps}^2$，并将 $\omega_c$ 相关的项也进行加和处理，其中 $\omega_{ps}^2 = n_s q_s^2 / (\epsilon_0 m_s)$ 和 $\Omega_s = q_s B_0 / m_s$ (这里用 $\Omega_s$ 代替 $\omega_{cs}$ 以匹配老师的符号)):

$\varepsilon_{\perp}(\omega) = \epsilon_0 \left(1 - \sum_s \frac{\omega_{ps}^2}{\omega^2 - \Omega_s^2}\right)$
$\varepsilon_{\parallel}(\omega) = \epsilon_0 \left(1 - \sum_s \frac{\omega_{ps}^2}{\omega^2}\right)$
$\varepsilon_x(\omega) = \epsilon_0 \left(\sum_s \frac{\omega_{ps}^2 \Omega_s}{\omega(\omega^2 - \Omega_s^2)}\right)$

对比我们的推导结果 (以单粒子为例，将 $\omega_p \rightarrow \omega_{ps}$, $\omega_c \rightarrow \Omega_s$ 并考虑求和)：
1.  $\varepsilon_{\perp}$:
    我们的 $\varepsilon_{xx} = \varepsilon_{yy} = \epsilon_0 \left(1 - \frac{\omega_p^2}{\omega^2 - \omega_c^2}\right)$.
    推广到多粒子： $\varepsilon_{\perp} = \epsilon_0 \left(1 - \sum_s \frac{\omega_{ps}^2}{\omega^2 - \Omega_s^2}\right)$. 这与老师的结果完全一致。

2.  $\varepsilon_{\parallel}$:
    我们的 $\varepsilon_{zz} = \epsilon_0 \left(1 - \frac{\omega_p^2}{\omega^2}\right)$.
    推广到多粒子： $\varepsilon_{\parallel} = \epsilon_0 \left(1 - \sum_s \frac{\omega_{ps}^2}{\omega^2}\right)$. 这与老师的结果完全一致。

3.  $i\varepsilon_x$ 和 $-i\varepsilon_x$:
    老师的矩阵中，$\varepsilon_{xy} = i\varepsilon_x$ 和 $\varepsilon_{yx} = -i\varepsilon_x$.
    我们的推导中：
    $\varepsilon_{xy} = \frac{-i\omega_c \epsilon_0 \omega_p^2}{\omega(\omega^2 - \omega_c^2)}$
    $\varepsilon_{yx} = \frac{i\omega_c \epsilon_0 \omega_p^2}{\omega(\omega^2 - \omega_c^2)}$

    要使我们的结果匹配老师的矩阵元素 $\varepsilon_{xy} = i\varepsilon_x$, 我们需要：
    $i\varepsilon_x = \frac{-i\omega_c \epsilon_0 \omega_p^2}{\omega(\omega^2 - \omega_c^2)}$
    $\varepsilon_x = \frac{-\omega_c \epsilon_0 \omega_p^2}{\omega(\omega^2 - \omega_c^2)}$
    推广到多粒子 (用 $\Omega_s$ 替换 $\omega_c$, $\omega_{ps}$ 替换 $\omega_p$):
    $\varepsilon_x = \epsilon_0 \left(\sum_s \frac{-\Omega_s \omega_{ps}^2}{\omega(\omega^2 - \Omega_s^2)}\right)$

    老师黑板上给出的 $\varepsilon_x$ 表达式为：
    $\varepsilon_x(\omega) = \epsilon_0 \left(\sum_s \frac{\omega_{ps}^2 \Omega_s}{\omega(\omega^2 - \Omega_s^2)}\right)$

    **可以看出，我们推导出的 $\varepsilon_x$ (为了匹配老师矩阵右上角 $i\varepsilon_x$ 这一项) 与老师黑板上直接给出的 $\varepsilon_x$ 表达式相差一个负号。**

    这种符号差异通常源于 $\Omega_s = q_s B_0 / m_s$ (回旋频率) 定义中 $q_s$ 的符号，或者在定义 $\varepsilon_x$ 时如何提取因子 $i$。
    如果 $\Omega_s$ 本身包含电荷 $q_s$ 的符号 (标准做法)，那么我们的推导是标准的。
    例如，在Jackson的《经典电动力学》或Stix的《等离子体波》中，$\varepsilon_{xy}$ 通常定义为包含 $i$ 的项，其系数（类似于老师的 $\varepsilon_x$）与我们推导出的 $\frac{-\Omega_s \omega_{ps}^2}{\omega(\omega^2 - \Omega_s^2)}$ 形式一致 (即包含负号)。

    **结论**：
    我们的详细推导得到的介电张量各分量为：
    $\varepsilon_{xx} = \varepsilon_{yy} = \varepsilon_{\perp} = \epsilon_0 \left(1 - \sum_s \frac{\omega_{ps}^2}{\omega^2 - \Omega_s^2}\right)$
    $\varepsilon_{zz} = \varepsilon_{\parallel} = \epsilon_0 \left(1 - \sum_s \frac{\omega_{ps}^2}{\omega^2}\right)$
    $\varepsilon_{xy} = \sum_s \frac{-i\Omega_s \epsilon_0 \omega_{ps}^2}{\omega(\omega^2 - \Omega_s^2)}$
    $\varepsilon_{yx} = \sum_s \frac{i\Omega_s \epsilon_0 \omega_{ps}^2}{\omega(\omega^2 - \Omega_s^2)}$

    如果老师的矩阵形式 $\begin{pmatrix} \varepsilon_{\perp} & i\varepsilon_x & 0 \\ -i\varepsilon_x & \varepsilon_{\perp} & 0 \\ 0 & 0 & \varepsilon_{\parallel} \end{pmatrix}$ 是严格定义的，那么 $\varepsilon_x$ 应该等于 $\frac{1}{i}\varepsilon_{xy} = \sum_s \frac{-\Omega_s \epsilon_0 \omega_{ps}^2}{\omega(\omega^2 - \Omega_s^2)}$。
    这与老师黑板上给出的 $\varepsilon_x$ 表达式 $\epsilon_0 \left(\sum_s \frac{\omega_{ps}^2 \Omega_s}{\omega(\omega^2 - \Omega_s^2)}\right)$ 相差一个负号。
    请与老师确认 $\varepsilon_x$ 的定义或 $\Omega_s$ 的符号约定。不过，推导的物理过程和各分量的结构是正确的。

### 总结

这个推导过程展示了如何从单个粒子的运动方程（洛伦兹力）出发，在考虑外加磁场和时谐电场的情况下，求解粒子速度，进而得到宏观的电流密度，并最终推导出电导率张量和介电张量。这些张量描述了介质在电磁场作用下的响应，是研究波在磁化等离子体（或类似介质）中传播的基础。