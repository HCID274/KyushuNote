好的，我们继续。

---

### **问题 2**

推导下式：
$$
\int_{R_2}^{R_1} \frac{\partial}{\partial R}(RA_{\phi}) dR = \int_{R_2}^{R_1} R B_z dR
$$
**提示**：$RA_\phi$ 是极向磁通函数 $\psi$。

---

### **推导过程**

该推导可从磁场与磁矢势的关系出发。在轴对称的柱坐标系中，极向磁场 $B_z$ 与极向磁通函数 $\psi$ 的关系为：
$$
B_z = \frac{1}{R} \frac{\partial \psi}{\partial R}
$$
> **参数说明:**
> - $\psi$: 极向磁通函数 (Poloidal magnetic flux function)，定义为 $\psi = RA_\phi$
> - $B_z$: 极向磁场 (Poloidal magnetic field)，在赤道面上即为垂直于该面的磁场分量

将上式两边同乘以 $R$：
$$
R B_z = \frac{\partial \psi}{\partial R}
$$
根据提示，将 $\psi = RA_\phi$ 代入上式：
$$
R B_z = \frac{\partial (RA_\phi)}{\partial R}
$$
最后，将上式两边同时对大半径 $R$ 从 $R_2$ 到 $R_1$ 进行积分，即可得证：
$$
\int_{R_2}^{R_1} R B_z dR = \int_{R_2}^{R_1} \frac{\partial (RA_\phi)}{\partial R} dR
$$
证明完毕。