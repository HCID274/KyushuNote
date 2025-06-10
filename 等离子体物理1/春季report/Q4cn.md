好的，这是最后一个问题。

---

### **问题 4 (最终)**

从之前推导出的关系式：
$$
|\Delta R| \approx \frac{m|v_{\parallel 1}|(R_1+R_2)}{e\bar{R}\bar{B}_z} \approx \frac{2m|v_{\parallel 1}|}{e\bar{B}_z}
$$
推导出囚禁粒子轨道宽度 (香蕉轨道宽度) 的最终表达式：
$$
|\Delta R| \sim \Delta_{tr} \sim 2\left(\frac{2R}{r}\right)^{1/2} q r_L
$$
**提示:**
*   在推导拉莫尔半径时，使用 $B_\phi \gg B_\theta$。
*   对于关系式 $\frac{v_{\parallel}^2}{v_{\perp 0}^2} = \varepsilon(1 - \cos\theta) \le 2\varepsilon$，请使用其可能的最大值。

---

### **最终推导**

我们将从综合前几问得到的关系式出发，逐步替换各项。
$$
|\Delta R| \approx \frac{2m|v_{\parallel}|}{eB_p}
$$
> **参数说明:**
> - $B_p$: 极向磁场，这里用 $B_p$ 代替赤道面上的 $\bar{B}_z$。
> - $|v_{\parallel}|$: 囚禁粒子在赤道面上的平行速度，这里用 $|v_{\parallel}|$ 代替 $|v_{\parallel 1}|$。

**1. 估算平行速度 $|v_{\parallel}|$**

根据提示，对于典型的囚禁粒子，其速度分量满足：
$$
\frac{v_{\parallel}^2}{v_{\perp}^2} \le 2\varepsilon
$$
我们取其最大值进行估算，即粒子在$\theta=0$（赤道面外侧）的平行速度：
$$
|v_{\parallel}| \sim \sqrt{2\varepsilon} v_{\perp}
$$
> **参数说明:**
> - $v_{\perp}$: 垂直于磁场线的速度。
> - $\varepsilon = r/R$: 逆环径比 (Inverse aspect ratio)，其中 $r$ 是小半径。

**2. 用安全因子 $q$ 表示极向磁场 $B_p$**

安全因子 $q$ 的定义为：
$$
q \equiv \frac{rB_\phi}{RB_p} \implies B_p = \frac{rB_\phi}{qR}
$$
> **参数说明:**
> - $q$: 安全因子 (Safety factor)。
> - $B_\phi$: 环向磁场。

**3. 引入拉莫尔半径 $r_L$**

拉莫尔半径的定义为 $r_L = \frac{mv_{\perp}}{eB}$。根据提示，$B_\phi \gg B_p$，因此总磁场 $B = \sqrt{B_\phi^2 + B_p^2} \approx B_\phi$。
$$
r_L \approx \frac{mv_{\perp}}{eB_\phi}
$$
> **参数说明:**
> - $r_L$: 拉莫尔半径 (Larmor radius)。

**4. 组合与化简**

将以上各项代入初始表达式：
$$
\begin{aligned}
|\Delta R| &\approx \frac{2m|v_{\parallel}|}{eB_p} \\
&\approx \frac{2m(\sqrt{2\varepsilon}v_{\perp})}{e \left( \frac{rB_\phi}{qR} \right)} \\
&= \left( \frac{mv_{\perp}}{eB_\phi} \right) \cdot \frac{2\sqrt{2\varepsilon}qR}{r} \\
&\approx r_L \cdot \frac{2\sqrt{2(r/R)}qR}{r} \\
&= 2 r_L q \sqrt{2} \sqrt{\frac{r}{R}} \frac{R}{r} \\
&= 2 r_L q \sqrt{2} \sqrt{\frac{R^2}{r^2}\frac{r}{R}} \\
&= 2 r_L q \sqrt{\frac{2R}{r}}
\end{aligned}
$$
整理后得到最终形式：
$$
\Delta_{tr} \approx 2 \left( \frac{2R}{r} \right)^{1/2} q r_L
$$
证明完毕。