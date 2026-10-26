Our primary goal will be to find information about the unknown function, which is called the **solution** to the D.E. Ideally, we analytically *SOLVE* to D.E. and explicitly find the solution y. when we are unable to do this, we will instead find information about the solution by way of **numerical approximation** or **graphical representation**.

## Type of Differential Equation
1. **linear differential equation** is a differential equation that is linear in the unknown function and its derivatives, so it can be written in the form:
$$a_0(x)y + a_1(x)y' + a_2(x)y'' + ... + a_n(x)y^{(n)} = b(x)$$
where $a_0(x), ..., a_n(x)$ and $b(x)$ are arbitrary differentiable functions that **do not need to be linear**, and $y′, ..., y(n)$ are the **successive derivatives of an unknown function $y$ of the variable $x$**.

2. **The order of the differential equation is the highest order of derivative of the unknown function that appears in the differential equation**. For example, an equation containing only first-order derivatives is a first-order differential equation, an equation containing the second-order derivative is a second-order differential equation, and so on

3. A linear differential equation is **homogeneous** if each term in the equation includes either the dependent variable or one of its derivatives. If this is not the case, so that there is a term that does not include either the dependent variable itself or a derivative of it, the equation is inhomogeneous or heterogeneous. See the examples section below.

### Example of different differential equation


## Example
Show that $y = e^x + x + 1$ is a solution to the D.E. $\frac{dy}{dx} = y - x$

Ans: 

$$
\begin{aligned}
\text{Let: } y = e^x + x + 1 \\
\text{LHS: } \frac{dy}{dx} = e^x + 1 \\
\text{RHS: } y - x = e^x + 1
\end{aligned}
$$

## Practice
Determine if $y = -t\mathbb{cos}t + t$ is a solution to the D.E. $t\frac{dy}{dt} = y + t^2\mathbb{sin}t$

Ans:

$$
\begin{aligned}
\text{Let: } y = -t\mathbb{cos}t + t\\
\text{LHS: } t\frac{dy}{dx} = -t\mathbb{cos}t + t^2\mathbb{sin}t + t \\
\text{RHS: } y + t^2\mathbb{sin}t = -t\mathbb{cos}t + t + t^2\mathbb{sin}t
\end{aligned}
$$

So, it is a solution.

## Def 1
An **initial value problem (IVP)** is a D.E. coupled with an initial condition that gives the value $y_I$ of the unknown function at some specified time $t_I$ (initial time). For a 1st order D.E. the initial condition is given in the form $y(t_I) = y_I$

Given a 1st-order linear D.E. in **explicit form** $\frac{dy}{dt} = f(t)$ (no $y$ in $f(t)$) one may find a solution by integrating both sides with repects to $t$.

### Example
Find a general solution of $\frac{dy}{dx} = 3x^4 + 10$

Solution:

$$
\begin{aligned}
\int \frac{dy}{dx} dx = \int 3x^4 + 10 dx \\
y = \frac{3}{5}x^5 + 10x + C
\end{aligned}
$$

## Def 2
Given a D.E. the **interval of defination** is the longest interval **for the independent variable** on which a solution exists. For an IVP, this interval must include the initial time ($t_I$)

Find the interval of definition by examing the domain of all function of $t$ in the D.E.

### Example
Find the interval of definition of $(4 - t^2)\frac{dy}{dt} = e^t, y(0) = 1$

$$
\frac{dy}{dt} = \frac{e^t}{4 - t^2}, t \not = -2, 2
$$

So, we have candidates: $(-\infty, -2), (-2, 2), (2, \infty)$, but our **initial condition is only on $(-2, 2)$**. Thus, the answer is: $(-2, 2)$

## Def 3
Given the first order, linear D.E. 
$$p_1(t)\frac{dy}{dt} + p_0(t)y = r(t)$$
, where $p_1(t) \not = 0$, its **normal form** is:
$$\frac{dy}{dt}+ a(t)y = f(t)$$
, where $a(t) = \frac{p_0(t)}{p_1(t)}$ and $f(t) = \frac{r(t)}{p_1(t)}$

## Integrating Factor Method (used for 1st-order, linear)
### Example
Solve the IVP
$$y' - y = 2te^{2t}, y(0) = 1$$

Solution:

i) Already in normal form

ii) Find the integration factor:
$$\mu = e^{\int a(t)dt}$$

in our example, it is: $\mu = e^{\int -1 dt} = e^{-t}$

iii) Mutiply both sides of (i) by $\mu$

in our example, the equation becomes: $e^{-t}y' - ye^{-t} = 2te^{2t}$

iv) Rewrite (iii) using the product rule

in our example, the equation in (iii) can be rewrited as $\frac{d}{dt} [ye^{-t}] = \frac{d}{dt} [(t-\frac{1}{2})e^{2t}]$

So, the answer is $y = (t - \frac{1}{2})e^{3t}$

## How to solve homogenous differential equation in a general way?
### characteristic polynomial method

Now, consider we have differential equation:

$$\frac{\mathrm{d}^{n}y}{\mathrm{d}t} + a_{n-1} \frac{\mathrm{d}^{n-1}y}{\mathrm{d}t} + ... + a_{1} \frac{\mathrm{d}y}{\mathrm{d}t} + a_{0} y = 0$$

where $a_{n-1}$, ... , $a_{0}$ is constant and the equation is homogenous linear equation in normal form.

Obviously, directly solving this question (find general solution) by integrating some part would be almost impossible. So, why not change our mind: finding the general solution by find the possible solution space? For example, if we have two possible solution $e^{2t}$ and $e^{3t}$ of differential equation $y'' - 5y' + 6 = 0$ (you can verify it by pulging the solution into the equation). What would our final general solution looks like? In the form $e^{2} \cdot e^{3}$? or $e^{2} + e^{3}$. To answer this question, we can first look at the properties that derivative has.

#### Derivative is Linear Operator

Recall what is linear operator. Linear Operator should have following properties:
1. $L(\vec{x} + \vec{y}) = L(\vec{x}) + L(\vec{y})$
2. $L(a\vec{x}) = aL(\vec{x})$, where $a$ is a constant

Obviously, the derivative we studied is linear operator, since:
1. $(f + g)' = f' + g'$
2. $(af)' = af'$

Thus, let's denote derivative as Linear Operator $D$. And the differential equation can be written in the form of **Linear Transformation**. That is $Ly = 0$, where $L = D^{n} + a_{n-1} D^{n-1} + ... + a_{1} D + a_{0}$. By doing so we successfully transform the problem os solving differential equation into finding Null space of $L$

Then, how can we find the Null space? Notice that linear space is defined by its dimension. That means $A = B \leftrightarrow dim A = dim B$. That is, as long as we can find the basis of Null space, the Null space is found. Then, there are two problems pops:
1. how many number of basis we need (dim)
2. are these vectors really form the basis

The answer of first question is given by the **Basic Existance and Uniqueness Theorem**. It suggests: Assume all cofficients $a_{0}(t)$, ... , $a_{n-1}(t)$ and $f(t)$ are continous over interval $(t_{1}, t_{2})$. Then given any initial time $t_{I}$ in $(t_{1}, t_{2})$ and any initial data $y_1$, ... , $y_{n-1}$. There **exists** a **unique solution** $y = Y(t)$ of our differential equation (even with forcing term).

So, we can ealisy construct a bijection between the solution space and $\mathbb{R}^{n}$. That is because the value we need is: $y_1$, ... , $y_{n-1}$ and $t_{I}$, totally $n$ numbers. We can simply assemble them into a n-dimension vector, which is in $\mathbb{R}^{n}$. Thus, by the **Basic Existance and Uniqueness Theorem**, the solution is determined by these vector (existance implies "onto"; uniqueness suggests "one-to-one"). So, this is a bijection.

From above discussion, finding n linear independent basis of solution space can directly solve our problem. **But how can we determine whether the solution we find is linear independent from each other?** That is why we ask for problem 2. To address this problem, we need to introduce a new technique: **determinant and Wronskain**

As we know in linear algebra, **Linear system** $A\vec{x} = 0$ **will have nonzero solution if and only if** $\mathrm{det}(A) = 0$. So, determinants provide us a way to machincally exam whether the given basis is linear independent or not. To illustrate how can we apply it, let's use determinants to solve the second problem.

**Lemma: solutions to the differential equation $Ly = 0$ are linear dependent if and only if the Wronskain is always zero over interval of definition $I$.** Where the Wronskain is defined by:
```math
Wr[y_{1}, y_{2}, \cdots, y_{n}] = 
\begin{vmatrix}
y_{1} & y_{2} & \cdots & y_{n} \\
y_{1}^{(1)} & y_{2}^{(1)} & \cdots & y_{n}^{(1)} \\
\vdots & \vdots & \ddots & \vdots \\
y_{1}^{(n-1)} & y_{2}^{(n-1)} & \cdots & y_{n}^{(n-1)}
\end{vmatrix} = \mathrm{det} \begin{pmatrix}
y_{1} & y_{2} & \cdots & y_{n} \\
y_{1}^{(1)} & y_{2}^{(1)} & \cdots & y_{n}^{(1)} \\
\vdots & \vdots & \ddots & \vdots \\
y_{1}^{(n-1)} & y_{2}^{(n-1)} & \cdots & y_{n}^{(n-1)}
\end{pmatrix}
```

($\Rightarrow$): since we assume solutions $y_{1}(t)$, $y_{2}(t)$, ..., $y_{n}(t)$ are linear dependent, we clearly know there is a set of real number $a_{1}$, $a_{2}$, ..., $a_{n}$ satisfies:

$$a_{1}y_{1}(t) + a_{2}y_{2}(t) + ... + a_{n}y_{n}(t) = 0, \forall t \in I$$

Let's take derivative of the above equation, we get ($\forall t \in I$):
```math
\begin{align}
&a_{1}y_{1}^{(1)}(t) + a_{2}y_{2}^{(1)}(t) + \cdots + a_{n}y_{n}^{(1)}(t) = 0 \\
&a_{1}y_{1}^{(2)}(t) + a_{2}y_{2}^{(2)}(t) + \cdots + a_{n}y_{n}^{(2)}(t) = 0 \\
&... \\
&a_{1}y_{1}^{(n-1)}(t) + a_{2}y_{2}^{(n-1)}(t) + \cdots + a_{n}y_{n}^{(n-1)}(t) = 0 \\
\end{align}
```

Further write it into Matrix form:
```math
\begin{bmatrix}
y_{1} & y_{2} & \cdots & y_{n} \\
y_{1}^{(1)} & y_{2}^{(1)} & \cdots & y_{n}^{(1)} \\
\vdots & \vdots & \ddots & \vdots \\
y_{1}^{(n-1)} & y_{2}^{(n-1)} & \cdots & y_{n}^{(n-1)}
\end{bmatrix} \begin{bmatrix} a_{1} \\ a_{2} \\ \vdots \\ a_{n} \end{bmatrix} = 
\begin{bmatrix} 0 \\ 0 \\ \vdots \\ 0 \end{bmatrix}
```

Let's denote:
```math
A = \begin{bmatrix}
y_{1} & y_{2} & \cdots & y_{n} \\
y_{1}^{(1)} & y_{2}^{(1)} & \cdots & y_{n}^{(1)} \\
\vdots & \vdots & \ddots & \vdots \\
y_{1}^{(n-1)} & y_{2}^{(n-1)} & \cdots & y_{n}^{(n-1)}
\end{bmatrix}
```

Obviously, $A$ has a none zero solution $\vec{a} = [a_{1}, a_{2}, \cdots, a_{n}]^{T}$ for equation $A\vec{x} = 0$, that means $\mathrm{det}(A) = 0 = Wr[y_{1}, y_{2}, \cdots, y_{n}]$

($\Leftarrow$): Given the Wronskain is zero, we know: $\mathrm{det}(A) = 0$, which suggest that there exist a non-zeor solution $\vec{a}$ such that $A\vec{a} = 0$, which means: $[y_{1}, y_{2}, \cdots, y_{n}] \cdot \vec{a} = 0$. So we conclude:

$$a_{1}y_{1}^{(1)}(t) + a_{2}y_{2}^{(1)}(t) + \cdots + a_{n}y_{n}^{(1)}(t) = 0, \forall t \in I$$

So, $y_{1}(t)$, $y_{2}(t)$, ..., $y_{n}(t)$ are linear dependent.

Thus, we proved Wronskain can help us check whether solutions are linear independent ($Wr \not = 0$). From above discussion, we also know how important tool Linear Algebra is. It can help us solve such difficult and unseemingly unrelated questions.

#### Find the exact solution

We already know finding n linear independent solution is suffcient to get the general solution and get the way to test whether our solution is valid. Here, I will introduce a straightforward and simple way to find the possible solution of our differential equation, which called **"characteristic polynomial method"**

Notice that $\frac{\mathrm{d}}{\mathrm{d}t}e^{\mu t} = \mu e^{\mu t}$, we can use this interesting property to construct our solution. Let's assume our solution has form: $y_{k}(t) = e^{rt}$. Thus $Ly = 0$ becomes:

$$(r^{n} + a_{n-1}r^{n-1} + \cdots + a_{0})e^{rt} = 0$$

since exponential function is alway positive, we further sinplify it into:

$$r^{n} + a_{n-1}r^{n-1} + \cdots + a_{0} = 0$$

which is the **"characteristic polynomial"**. And if $r$ is the root of characteristic polynomial, it suggests that $e^{rt}$ will become one solution of $Ly = 0$. By solving the characteristic equation, we can find the general solution.

## Extend to nonhomogenous equation
### Undetermined Coefficient
While we mentioned how to solve homogenous differential equation, but obviously there are more non-homogenous differential equation. How can we solve these equations?

Let's consider the following equations:

$$ Ly = \frac{\mathrm{d}^{n}y}{\mathrm{d}t} + a_{n-1} \frac{\mathrm{d}^{n-1}y}{\mathrm{d}t} + ... + a_{1} \frac{\mathrm{d}y}{\mathrm{d}t} + a_{0} y = f(t)$$

here, we call $f(t)$ "forcing term". And this time, the forcing term wouldn't be always zero, which makes the equation more complex.