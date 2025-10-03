### **(1) 最尤推定 (MLE)**

1.  **データ統計**
    - データ系列 $D = \{1,2,4,3,3,4,1,2,2,3\}$
    - サンプル数 $N=10$
    - 各値の出現回数: $n_1=2, n_2=3, n_3=3, n_4=2$

2.  **目的関数と制約条件**
    - 対数尤度関数:
      $$ \ln L(q) = 2\ln q_1 + 3\ln q_2 + 3\ln q_3 + 2\ln q_4 $$
    - 制約条件:
      $$ g(q) = q_1 + q_2 + q_3 + q_4 - 1 = 0 $$

3.  **ラグランジュの未定乗数法**
    - ラグランジュ関数:
      $$ \Lambda(q, \lambda) = (2\ln q_1 + 3\ln q_2 + 3\ln q_3 + 2\ln q_4) - \lambda(q_1 + q_2 + q_3 + q_4 - 1) $$
    - 偏微分して0とおく:
      $$ \frac{\partial \Lambda}{\partial q_k} = \frac{n_k}{q_k} - \lambda = 0 \implies q_k = \frac{n_k}{\lambda} $$
    - 制約条件に代入してλを解く:
      $$ \sum_{k=1}^4 q_k = \frac{1}{\lambda} \sum_{k=1}^4 n_k = \frac{1}{\lambda}(2+3+3+2) = \frac{10}{\lambda} = 1 \implies \lambda = 10 $$
    - $q_k$ を解く:
      $$ q_1 = \frac{n_1}{\lambda} = \frac{2}{10} = 0.2 $$
      $$ q_2 = \frac{n_2}{\lambda} = \frac{3}{10} = 0.3 $$
      $$ q_3 = \frac{n_3}{\lambda} = \frac{3}{10} = 0.3 $$
      $$ q_4 = \frac{n_4}{\lambda} = \frac{2}{10} = 0.2 $$

4.  **最終的な答え (1)**
    $$ (q_1, q_2, q_3, q_4) = (0.2, 0.3, 0.3, 0.2) $$

---

### **(2) MAP (最大事後確率) 推定**

1.  **事後確率**
    - 尤度関数: $P(D|q) \propto q_1^2 q_2^3 q_3^3 q_4^2$
    - 事前分布: $p(q) \propto q_1^2 q_2^1 q_3^2 q_4^3$
    - 事後分布 (尤度と事前分布の積に比例):
      $$ h(q|D) \propto (q_1^2 q_2^3 q_3^3 q_4^2) \cdot (q_1^2 q_2^1 q_3^2 q_4^3) = q_1^4 q_2^4 q_3^5 q_4^5 $$

2.  **目的関数と制約条件**
    - 対数事後確率関数 (定数項を無視):
      $$ \ln h(q|D) = 4\ln q_1 + 4\ln q_2 + 5\ln q_3 + 5\ln q_4 $$
    - 制約条件:
      $$ g(q) = q_1 + q_2 + q_3 + q_4 - 1 = 0 $$

3.  **ラグランジュの未定乗数法**
    - ラグランジュ関数:
      $$ \Lambda_{MAP}(q, \lambda) = (4\ln q_1 + 4\ln q_2 + 5\ln q_3 + 5\ln q_4) - \lambda(q_1 + q_2 + q_3 + q_4 - 1) $$
    - 偏微分して0とおく:
      $$ \frac{\partial \Lambda_{MAP}}{\partial q_1} = \frac{4}{q_1} - \lambda = 0 \implies q_1 = \frac{4}{\lambda} $$
      $$ \frac{\partial \Lambda_{MAP}}{\partial q_2} = \frac{4}{q_2} - \lambda = 0 \implies q_2 = \frac{4}{\lambda} $$
      $$ \frac{\partial \Lambda_{MAP}}{\partial q_3} = \frac{5}{q_3} - \lambda = 0 \implies q_3 = \frac{5}{\lambda} $$
      $$ \frac{\partial \Lambda_{MAP}}{\partial q_4} = \frac{5}{q_4} - \lambda = 0 \implies q_4 = \frac{5}{\lambda} $$
    - 制約条件に代入してλを解く:
      $$ \sum_{k=1}^4 q_k = \frac{4}{\lambda} + \frac{4}{\lambda} + \frac{5}{\lambda} + \frac{5}{\lambda} = \frac{18}{\lambda} = 1 \implies \lambda = 18 $$
    - $q_k$ を解く:
      $$ q_1 = \frac{4}{18} = \frac{2}{9} $$
      $$ q_2 = \frac{4}{18} = \frac{2}{9} $$
      $$ q_3 = \frac{5}{18} $$
      $$ q_4 = \frac{5}{18} $$

4.  **最終的な答え (2)**
    $$ (q_1, q_2, q_3, q_4) = \left(\frac{2}{9}, \frac{2}{9}, \frac{5}{18}, \frac{5}{18}\right) $$