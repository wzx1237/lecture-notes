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
  \text{margin}(\mathbf{D}, \boldsymbol{w}, b) = 
  \begin{cases} 
    \min_{(x,y) \in \mathbf{D}} y(\boldsymbol{w} \cdot x + b) & \text{if } \boldsymbol{w} \text{ separates } \mathbf{D} \\
    -\infty & \text{otherwise}
  \end{cases}
  \tag{3.8}
\end{equation}
```

which is the nearest dictince between the decision boundary and some points in dataset $\mathbf{D}$, And the margin for a dataset $\mathbf{D}$ is defined by the largest attainable margin for dataset $mathbf{D}$:

$$\text{margin}(\mathbf{D}) = \sup_{\boldsymbol{w}, b} \text{margin}(\mathbf{D}, \boldsymbol{w}, b)$$

## How to find it?

Obviously, the distance between the nearest positive data and decision bounary (denoted as: $d_{+}$) should equal to the distance between the nearest negative data and the decision boundary (denoted as: $d_{-}$). That is because if not, assume our best decision boundary has property $d_{-} > d_{+}$, let move the decision boundary towards to the negative direction, we find the margin increase. So, the old decision boundary is not the best one (contradictory), which proves $d_{+} = d_{-}$ for the best decision boundary.

Then, let's assume we have two hyperplanes: $\omega \cdot x + b = c_{1}$ and $\omega \cdot x + b = c_{2}$. $\omega \cdot x + b = c_{1}$ touches the positive instance (called "plus-plane") and $\omega \cdot x + b = c_{2}$ (called "minus-plane"). From above discussion, we know $d_{+} = \frac{\abs{\omega \cdot x + b = c_{1}}}{\|\omega\|} = d_{-} = \frac{\abs{\omega \cdot x + b = c_{2}}}{\|\omega\|}$. Solve this equation we get: $\abs{c_{1}} = \abs{c_{2}}$, and we know $c_{1} \ne c_{2}$ (otherwise, plus-plane and the minus-plane will be the same plane). we get: $c_{1} = -c_{2}$. Let's denote $c_{1} = c$, so we have:

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