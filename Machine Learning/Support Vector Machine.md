# What is Support Vector Machine?

1. problem setting: 
  - we want to separate a set of linear separable data points
  - unknown target function $f: X \rightarrow Y$ that correctly separate the data points and satisify our goal
  - set of function hypothesis: $H = \{h | h: X \rightarrow Y\}$
2. Input: Training examples of unknown target function $f$
3. Output: Hypothesis $h \in H$ that can maximize the distance between the decision boundary while correctly classifies our data points
4. Should be linear ($Y = \omega^{T} \cdot \vec{x} + \vec{b}$)

## Define the margin

Margin of dataset $mathbf{D}$ and decision boundary $\omega \cdot x + b$ is given by:

```math
\begin{equation}
  \text{margin}(\mathbf{D},\omega, b) = \begin{cases} \min_{(x,y) \in \mathbf{D}} y(\omega \cdot x + b) & \text{if } \omega \text{ separates } \mathbf{D} \\
    -\infty & \text{otherwise}
  \end{cases}
  \tag{3.8}
\end{equation}
```

which is the nearest dictince between the decision boundary and some points in dataset $\mathbf{D}$, And the margin for a dataset $\mathbf{D}$ is defined by the largest attainable margin for dataset $mathbf{D}$:

$$\text{margin}(\mathbf{D}) = \sup_{\boldsymbol{w}, b} \text{margin}(\mathbf{D}, \boldsymbol{w}, b)$$

## How to find it?

Obviously, the distance between the nearest positive data and decision bounary (denoted as: $d_{+}$) should equal to the distance between the nearest negative data and the decision boundary (denoted as: $d_{-}$). That is because if not, assume our best decision boundary has property $d_{-} > d_{+}$, let move the decision boundary towards to the negative direction, we find the margin increase. So, the old decision boundary is not the best one (contradictory), which proves $d_{+} = d_{-}$ for the best decision boundary.

Then, let's assume we have two hyperplanes: $\omega \cdot x + b = c_{1}$ and $\omega \cdot x + b = c_{2}$. $\omega \cdot x + b = c_{1}$ touches the positive instance and all positive instances are above this plane (called "plus-plane") and $\omega \cdot x + b = c_{2}$ touches the negative instance and all negative instances are below this plane (called "minus-plane"). From above discussion, we know $d_{+} = \frac{\left |c_{1}\right |}{\|\omega\|} = d_{-} = \frac{\left |c_{2}\right|}{\|\omega\|}$. Solve this equation we get: $\left|c_{1}\right| = \left|c_{2}\right|$, and we know $c_{1} \ne c_{2}$ (otherwise, plus-plane and the minus-plane will be the same plane). we get: $c_{1} = -c_{2}$. Let's denote $c_{1} = c$, so we have:

```math
\begin{align}
\text{plus-plane: }\omega \cdot x + b = c \\
\text{minus-plane: }\omega \cdot x + b = -c
\end{align}
```

Let's further devide both side by c ($c \ne 0$), we get: 
```math
\begin{align}
\text{plus-plane: }\frac{\omega}{c} \cdot x + \frac{b}{c} = 1 \\
\text{minus-plane: }\frac{\omega}{c} \cdot x + \frac{b}{c} = -1
\end{align}
```

And replacing $\frac{\omega}{c}$ by $\omega$ and $\frac{b}{c}$ by $b$, we get:
```math
\begin{align}
\text{plus-plane: }\omega \cdot x + b = 1 \\
\text{minus-plane: }\omega \cdot x + b = -1
\end{align}
```

We call equations in above form: **canonical form**, and it has one interesting property: the margin of this hyperplane (in canaical form) is: $\frac{1}{\|\omage\|}$

That is because: $\text{distance} = \frac{\left| \omega \cdot x + b \right|}{\|\omage\|} = \frac{1}{\|\omage\|}$. So, we can maximize the margin by minimize the $\|\omega\|$

## Optimalization

Since minimizing $\|\omega\|$ is same as minimizing $\frac{1}{2}\|\omega\|^{2}$, we can minimize $\frac{1}{2}\|\omega\|^{2}$ instead.

So, our optimalizatio problem is defined below:
```math
\begin{aligned}
& \text{Minimize} \quad && f(\omega, b) = \frac{\|\omega\|^2}{2} \\
& \text{subject to} \quad && y_n(\omega^T \mathbf{x}_n + b) \ge 1, \quad \forall \, n = 1, \dots, N
\end{aligned}
```

To solve this problem, noticing that $x, y, \omega, b$ are continues and bounded, we can directly apply `Lagrange Multuplier` to find where the multipilers give us minimum. (multipliers are: $\alpha_{1}, \alpha_{2}, \dots, \alpha_{N}$)
```math
\begin{align}
\frac{\partial{(\frac{1}{2}\|\omega\|^{2})}}{\partial{\omega}} = \sum_{i=1}^{N} \alpha_{i} \frac{\partial{(1 - y_n(\omega^T \mathbf{x}_n + b))}}{\partial{\omega}} \\
\frac{\partial{(\frac{1}{2}\|\omega\|^{2})}}{\partial{b}} = \sum_{i=1}^{N} \alpha_{i} \frac{\partial{(1 - y_n(\omega^T \mathbf{x}_n + b))}}{\partial{b}}
\end{align}
```

and our problem becomes (if you want to know why this holds, please refer to /Basic Math/Lagrange Multiplier.md):
```math
\begin{aligned}
& \text{Minimize} \quad && f(\omega, b, \alpha) = \frac{\|\omega\|^2}{2} + \sum_{n = 1}^{N} \alpha_{n}(1 - y_{n}(\omega^T \mathbf{x}_n + b)) \\
& \text{subject to} \quad && \alpha_{n} \ge 0, \quad \forall \, n = 1, \dots, N
\end{aligned}
```

By taking the partial derivative, we get:
```math
\begin{align}
\frac{\partial{(\frac{1}{2}\|\omega\|^{2})}}{\partial \omega} = \omega = \sum_{n=1}^{N} \alpha_n y_n \mathbf{x}_n, \\
\frac{\partial{(\frac{1}{2}\|\omega\|^{2})}}{\partial b} = 0 = -\sum_{n=1}^{N} \alpha_n y_n
\end{align}
```
Substituting our above result into $f(\omega, b, \alpha)$, we get:
```math
\begin{aligned}
f_{D}(\omega, b, \alpha) &= \frac{1}{2} \omega^{T}\omega + \sum_{n=1}^{N}\alpha_{n} - \sum_{n=1}^{N} \alpha_{n} y_{n} \omega^{T} \mathbf{x}_{n} - \sum_{n=1}^{N} \alpha_{n} y_{n} b \\
&= \frac{1}{2} (\sum_{n=1}^{N} \alpha_{n} y_{n} \mathbf{x}_n)^{T} (\sum_{m=1}^{N} \alpha_{m} y_{m} \mathbf{x}_m) + \sum_{n=1}^{N}\alpha_{n} - \sum_{n=1}^{N} \alpha_{n} y_{n} (\sum_{m=1}^{N} \alpha_{m} y_{m} \mathbf{x}_m)^{T} \mathbf{x}_{n} \\
&= \frac{1}{2} \sum_{n=1}^{N}\sum_{m=1}^{N} \alpha_{n}\alpha_{m} y_{n} y_{m} \mathbf{x}_n^{T} \mathbf{x}_m + \sum_{n=1}^{N}\alpha_{n} - \sum_{n=1}^{N}\sum_{m=1}^{N} \alpha_{n}\alpha_{m} y_{n} y_{m} \mathbf{x}_m^{T} \mathbf{x}_n
\end{aligned} \\
$= sum_{n=1}^{N}\alpha_{n} - \frac{1}{2} \sum_{n=1}^{N}\sum_{m=1}^{N} \alpha_{n}\alpha_{m} y_{n} y_{m} \mathbf{x}_n^{T} \mathbf{x}_m
```
Now, we know we just need to maximize $f_{D}$ under condition $\sum_{n=1}^{N} \alpha_n y_n = 0$ and $\alpha_{n} \ge 0$, which can be done with `Lagrange Multiplier` again.

After we get the solution, we have:
```math
\mathbf{w} = \sum_{n=1}^{N} \alpha_n y_n \mathbf{x}_n
```
and:
```math
b = -\frac{1}{2} \left( \min_{n: y_n=+1} \mathbf{w}^T \mathbf{x}_n + \max_{n: y_n=-1} \mathbf{w}^T \mathbf{x}_n\right)
```

So, we can using above equations to solve $\omega$ and $b$.

## Result
We can check the result, and superisingly we find most of $\alpha_{i}$ are zero and $\alpha_{i}$ is non-zero if and only if $\mathbf{x}_n$ lies on one of the two bounaries (plus-plane and minus-plane). And since they are so speical and can impact our decision boundary a lot, we call them **"support vector"**. It means vector supports the margin boundaries.