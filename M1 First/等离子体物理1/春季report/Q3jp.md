はい、承知いたしました。問題3の整理内容です。

---

### **問題3**

次に、角運動量保存の式の右辺を考えます。
$$
-e(R_1A_{\phi 1} - R_2A_{\phi 2}) = m(R_1v_{\parallel 1} - R_2v_{\parallel 2})
$$
$v_{\parallel 1}$ と $v_{\parallel 2}$ の関係はどのようになりますか？

**ヒント**：以下の公式を用い、点1と点2が共に赤道面（$\theta=0$）上にあり、それらの点の逆アスペクト比 $\varepsilon$ の差は小さいものとします。
$$
\frac{v_{\parallel}^2}{v_0^2} = 1 - \frac{v_{\perp}^2}{v_0^2} = 1 - \frac{v_{\perp 0}^2}{v_0^2} \frac{(1 - \varepsilon \cos \theta)}{(1 - \varepsilon)}
$$

---

### **導出過程**

捕捉粒子の場合、その軌道の最外側（点1）と最内側（点2）では運動方向が逆になります。ここでは、両点における速度の大きさの関係を求めます。

エネルギー保存則と磁気モーメント保存則より、平行速度 $v_{\parallel}$ の関係式が次のように導出されます。
$$
\frac{v_{\parallel}^2}{v_0^2} = 1 - \frac{\mu B_0}{1/2 mv_0^2} \frac{B}{B_0} = 1 - \frac{v_{\perp 0}^2}{v_0^2} \frac{1 - \varepsilon \cos \theta}{1 - \varepsilon}
$$
> **各記号の説明:**
> - $v_0$: 粒子の全速度（保存量）
> - $v_{\perp 0}$: 磁気軸上（$R=R_0$）での垂直速度
> - $\varepsilon = r/R$: 逆アスペクト比
> - $\theta$: ポロイダル角

問題の条件より、点1と点2は共に $z=0$ の赤道面上にあるため、ポロイダル角は $\theta=0$ となります。これを上式に代入します。
$$
\frac{v_{\parallel}^2}{v_0^2} = 1 - \frac{v_{\perp 0}^2}{v_0^2} \frac{1 - \varepsilon \cos 0}{1 - \varepsilon} = 1 - \frac{v_{\perp 0}^2}{v_0^2} \frac{1 - \varepsilon}{1 - \varepsilon} = 1 - \frac{v_{\perp 0}^2}{v_0^2} = \text{const.}
$$
この結果は、$\theta=0$ において、平行速度の大きさは半径 $R$ に依存しないことを示しています。したがって、点1と点2における平行速度の大きさは等しくなります。
$$
|v_{\parallel 1}| = |v_{\parallel 2}|
$$
図のバナナ軌道の運動からわかるように、点1と点2における粒子の運動方向は逆です。よって、両者の速度の関係は次のようになります。
$$
v_{\parallel 2} = -v_{\parallel 1}
$$