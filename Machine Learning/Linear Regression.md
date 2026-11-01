# What is Linear Regression?
1. Problem setting:
  - set of possible instances X (each one is a feature vector)
  - unknown target function $f: X \rightarrow Y$
  - set of function hypothesis: $H = \{h | h: X \rightarrow Y\}$
2. Input: Training examples of unknown target function $f$
3. Output: Hypothesis $h \in H$ that best approximates target function $f$
4. Should be linear ($Y = \omega^{T} \cdot \vec{x} + \vec{b}$)

## Least Square Regression
Target: Estimated Regression Line should minimize error (MSE error)

Define MSE error as:
$$\frac{1}{N} \sum_{i=1}^{N} (y_{i} - \hat{y_{i}})^{2}$$
where $N$ is number of samples we have.

## How to minimize MSE error?

let's consider the problem in the most simple way: $A\vec{\omega} = \vec{y}$. That is because we can add one more column to matrix $A$ and fix the last entry in $\vex{\omega}$ to be 1. By doing so, the additional term $b$ , which is annoying, can be integrated into matrix $A$.

Then, let's look at the MSE error in a different way: the MSE error is the square of L2 norm between our prediction ($\hat{Y}$) and the ground truth ($Y$), where $\hat{Y} = (\hat{y_1}, \hat{y_2}, \cdots, \hat{y_n})$ and $Y = (y_1 ,y_2, \cdots, y_n)$. Thus, we cast a complex sum problem into a simple linear algebra question: finding a solution $\hat{Y}$ that best approximate our ground truth $Y$ by minimizing the distance between $\hat{Y}$ and $Y$.

Clearly, as we studied in junior school, **the shortest distance is given by the projection** and the Least Square Method (in Linear Algebra) tells us how to find it. If you forgot it, not worry, there will be a review fot it.

The solution is given by equation:
```math
A\vec{\omega} = \hat{\vec{y}} = \mathrm{proj}_{\mathrm{Col} A} \vec{y}
```

However, finding the projection is hard, do we have a way to avoid that?

lemma: $\mathrm{Col} A \vert mathrm{Nul} A^{T}$

Proof:

given $\forall b \in \mathrm{Col} A \text{and} \forall y \in \mathrm{Nul} A^{T}$, we have:
$b = Ax$ for some x and $A^{T}y = 0$. Thus we find: $b \cdot y = Ax \cdot y$, by definition of dot product, we know: $Ax \cdot y = xA^{T}y$. That means: $b \cdot y = Ax \cdot y = x(A^{T}y) = x \cdot 0 = 0$. So, by definition od orthogonal, we know: $\mathrm{Col} A \vert mathrm{Nul} A^{T}$

Now, back to our question, where should we use our lemma? Notice that the shorest distance is given by the projection, which means: $\vec{y} - \hat{\vec{y}} \vert \mathrm{Col}A$. Applying our lemma, we know: $\vec{y} - \hat{\vec{y}} \in \mathrm{Col}A^{\vert} = \methrm{Nul}A^{T}$.

Thus, we have:
```math
\vec{0} = A^{T}(\vec{y} - \hat{\vec{y}}) = A^{T} (A\omega - \vec{y})
```
So:
```math
A^{T} A\omega = A^{T}\vec{y}
```

To get the weight vector, we just need to solve the above equation. And since this method grows from the Least Square method in Linear Algebra, we follow the same name and apply it to machine learning. Furthermore, if you want, you can also use gradient to derive thsi formula, which will provide you same result but longer and more complex arguments are required.

## Polynomial Feature and regularization term

Though Linear regression provide us a good way to do regression task, it still has some drawbacks and the most noticabel one is it can only solve problem linearly. When it comes to non-linear regression task, linear regression usually cannot solve it perfectly.

However, this problem can be improved by putting some trick on features. For example, the boundary we want is $x_{1}^{2} + x_{2}^{2} + x_{1}x_{2} = 4$. Obviously, this question is too hard for stanard linear regression. However, what if we introduce new features manually, i.e. $(1, x_{1}, x_{2}, x_{1}^{2}, x_{2}^{2}, x_{1}x_{2})$. Can linear regression works on this revised feature vector? Appearantly, the answer is yes. Let's let $\omega = (-4, 0, 0, 1, 1, 1)$, we perfectly finnd the decision boundary.

Since the features we add usually would be polynomial, we call this method "Polynomial Feature Method".