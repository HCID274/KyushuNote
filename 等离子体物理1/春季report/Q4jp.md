はい、承知いたしました。最後の問題ですね。

---

### **問題4（最終）**

以前に導出された関係式：
$$
|\Delta R| \approx \frac{m|v_{\parallel 1}|(R_1+R_2)}{e\bar{R}\bar{B}_z} \approx \frac{2m|v_{\parallel 1}|}{e\bar{B}_z}
$$
から、捕捉粒子軌道幅（バナナ軌道幅）の最終的な表式：
$$
|\Delta R| \sim \Delta_{tr} \sim 2\left(\frac{2R}{r}\right)^{1/2} q r_L
$$
を導出しなさい。

**ヒント:**
*   ラーモア半径を導出する際は、$B_\phi \gg B_\theta$ を用いなさい。
*   関係式 $\frac{v_{\parallel}^2}{v_{\perp 0}^2} = \varepsilon(1 - \cos\theta) \le 2\varepsilon$ については、その取りうる最大値を用いなさい。

---

### **最終導出**

これまでの問いで得られた関係式から出発し、各項を段階的に置き換えていきます。
$$
|\Delta R| \approx \frac{2m|v_{\parallel}|}{eB_p}
$$
> **各記号の説明:**
> - $B_p$: ポロイダル磁場。ここでは赤道面上の $\bar{B}_z$ を $B_p$ で置き換えています。
> - $|v_{\parallel}|$: 捕捉粒子が赤道面上にいるときの平行速度。ここでは $|v_{\parallel 1}|$ を $|v_{\parallel}|$ で置き換えています。

**1. 平行速度 $|v_{\parallel}|$ の評価**

ヒントに基づき、典型的な捕捉粒子に対して、その速度成分は次式を満たします。
$$
\frac{v_{\parallel}^2}{v_{\perp}^2} \le 2\varepsilon
$$
この最大値を用いて評価します。すなわち、粒子が$\theta=0$（赤道面外側）にいるときの平行速度は、
$$
|v_{\parallel}| \sim \sqrt{2\varepsilon} v_{\perp}
$$
> **各記号の説明:**
> - $v_{\perp}$: 磁力線に垂直な速度。
> - $\varepsilon = r/R$: 逆アスペクト比 (Inverse aspect ratio)。$r$ は小半径です。

**2. 安全係数 $q$ を用いたポロイダル磁場 $B_p$ の表現**

安全係数 $q$ の定義は次の通りです。
$$
q \equiv \frac{rB_\phi}{RB_p} \implies B_p = \frac{rB_\phi}{qR}
$$
> **各記号の説明:**
> - $q$: 安全係数 (Safety factor)。
> - $B_\phi$: トロイダル磁場。

**3. ラーモア半径 $r_L$ の導入**

ラーモア半径は $r_L = \frac{mv_{\perp}}{eB}$ と定義されます。ヒントより $B_\phi \gg B_p$ であるため、全磁場 $B = \sqrt{B_\phi^2 + B_p^2} \approx B_\phi$ となります。
$$
r_L \approx \frac{mv_{\perp}}{eB_\phi}
$$
> **各記号の説明:**
> - $r_L$: ラーモア半径 (Larmor radius)。

**4. 組み合わせと簡略化**

以上の各項を最初の式に代入します。
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
整理すると、最終的な形が得られます。
$$
\Delta_{tr} \approx 2 \left( \frac{2R}{r} \right)^{1/2} q r_L
$$
証明完了。