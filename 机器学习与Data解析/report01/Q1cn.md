### **(1) 最大似然估计 (MLE)**

1.  **数据统计**
    - 数据序列 $D = \{1,2,4,3,3,4,1,2,2,3\}$
    - 样本数 $N=10$
    - 各值出现次数: $n_1=2, n_2=3, n_3=3, n_4=2$

2.  **目标函数与约束**
    - 对数似然函数:
      $$ \ln L(q) = 2\ln q_1 + 3\ln q_2 + 3\ln q_3 + 2\ln q_4 $$
    - 约束条件:
      $$ g(q) = q_1 + q_2 + q_3 + q_4 - 1 = 0 $$

3.  **拉格朗日乘数法**
    - 拉格朗日函数:
      $$ \Lambda(q, \lambda) = (2\ln q_1 + 3\ln q_2 + 3\ln q_3 + 2\ln q_4) - \lambda(q_1 + q_2 + q_3 + q_4 - 1) $$
    - 求偏导并设为0:
      $$ \frac{\partial \Lambda}{\partial q_k} = \frac{n_k}{q_k} - \lambda = 0 \implies q_k = \frac{n_k}{\lambda} $$
    - 代入约束条件求解 $\lambda$:
      $$ \sum_{k=1}^4 q_k = \frac{1}{\lambda} \sum_{k=1}^4 n_k = \frac{1}{\lambda}(2+3+3+2) = \frac{10}{\lambda} = 1 \implies \lambda = 10 $$
    - 求解 $q_k$:
      $$ q_1 = \frac{n_1}{\lambda} = \frac{2}{10} = 0.2 $$
      $$ q_2 = \frac{n_2}{\lambda} = \frac{3}{10} = 0.3 $$
      $$ q_3 = \frac{n_3}{\lambda} = \frac{3}{10} = 0.3 $$
      $$ q_4 = \frac{n_4}{\lambda} = \frac{2}{10} = 0.2 $$

4.  **最终答案 (1)**
    $$ (q_1, q_2, q_3, q_4) = (0.2, 0.3, 0.3, 0.2) $$

---

### **(2) MAP (最大后验) 估计**

1.  **后验概率**
    - 似然函数: $P(D|q) \propto q_1^2 q_2^3 q_3^3 q_4^2$
    - 先验分布: $p(q) \propto q_1^2 q_2^1 q_3^2 q_4^3$
    - 后验分布 (正比于似然 $\times$ 先验):
      $$ h(q|D) \propto (q_1^2 q_2^3 q_3^3 q_4^2) \cdot (q_1^2 q_2^1 q_3^2 q_4^3) = q_1^4 q_2^4 q_3^5 q_4^5 $$

2.  **目标函数与约束**
    - 对数后验函数 (忽略常数项):
      $$ \ln h(q|D) = 4\ln q_1 + 4\ln q_2 + 5\ln q_3 + 5\ln q_4 $$
    - 约束条件:
      $$ g(q) = q_1 + q_2 + q_3 + q_4 - 1 = 0 $$

3.  **拉格朗日乘数法**
    - 拉格朗日函数:
      $$ \Lambda_{MAP}(q, \lambda) = (4\ln q_1 + 4\ln q_2 + 5\ln q_3 + 5\ln q_4) - \lambda(q_1 + q_2 + q_3 + q_4 - 1) $$
    - 求偏导并设为0:
      $$ \frac{\partial \Lambda_{MAP}}{\partial q_1} = \frac{4}{q_1} - \lambda = 0 \implies q_1 = \frac{4}{\lambda} $$
      $$ \frac{\partial \Lambda_{MAP}}{\partial q_2} = \frac{4}{q_2} - \lambda = 0 \implies q_2 = \frac{4}{\lambda} $$
      $$ \frac{\partial \Lambda_{MAP}}{\partial q_3} = \frac{5}{q_3} - \lambda = 0 \implies q_3 = \frac{5}{\lambda} $$
      $$ \frac{\partial \Lambda_{MAP}}{\partial q_4} = \frac{5}{q_4} - \lambda = 0 \implies q_4 = \frac{5}{\lambda} $$
    - 代入约束条件求解 $\lambda$:
      $$ \sum_{k=1}^4 q_k = \frac{4}{\lambda} + \frac{4}{\lambda} + \frac{5}{\lambda} + \frac{5}{\lambda} = \frac{18}{\lambda} = 1 \implies \lambda = 18 $$
    - 求解 $q_k$:
      $$ q_1 = \frac{4}{18} = \frac{2}{9} $$
      $$ q_2 = \frac{4}{18} = \frac{2}{9} $$
      $$ q_3 = \frac{5}{18} $$
      $$ q_4 = \frac{5}{18} $$

4.  **最终答案 (2)**
    $$ (q_1, q_2, q_3, q_4) = \left(\frac{2}{9}, \frac{2}{9}, \frac{5}{18}, \frac{5}{18}\right) $$