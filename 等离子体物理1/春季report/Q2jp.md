はい、承知いたしました。続きを翻訳します。

---

### **問題2**

次式を導出しなさい。
$$
\int_{R_2}^{R_1} \frac{\partial}{\partial R}(RA_{\phi}) dR = \int_{R_2}^{R_1} R B_z dR
$$
**ヒント**：$RA_\phi$ はポロイダル磁束関数 $\psi$ です。

---

### **導出過程**

この導出は、磁場と磁気ベクトルポテンシャルの関係から始めます。軸対称の円筒座標系において、ポロイダル磁場 $B_z$ とポロイダル磁束関数 $\psi$ の関係は次式で与えられます。
$$
B_z = \frac{1}{R} \frac{\partial \psi}{\partial R}
$$
> **各記号の説明:**
> - $\psi$: ポロイダル磁束関数 (Poloidal magnetic flux function)。$\psi = RA_\phi$ と定義されます。
> - $B_z$: ポロイダル磁場 (Poloidal magnetic field)。赤道面においては、この面に垂直な磁場成分を指します。

上式の両辺に $R$ を掛けます。
$$
R B_z = \frac{\partial \psi}{\partial R}
$$
ヒントに基づき、$\psi = RA_\phi$ を上式に代入します。
$$
R B_z = \frac{\partial (RA_\phi)}{\partial R}
$$
最後に、この式の両辺を主半径 $R$ について $R_2$ から $R_1$ まで積分することで、証明すべき式が得られます。
$$
\int_{R_2}^{R_1} R B_z dR = \int_{R_2}^{R_1} \frac{\partial (RA_\phi)}{\partial R} dR
$$
証明完了。