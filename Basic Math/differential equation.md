Our primary goal will be to find information about the unknown function, which is called the **solution** to the D.E. Ideally, we analytically *SOLVE* to D.E. and explicitly find the solution y. when we are unable to do this, we will instead find information about the solution by way of **numerical approximation** or **graphical representation**.

## Type of Differential Equation
1. **linear differential equation** is a differential equation that is linear in the unknown function and its derivatives, so it can be written in the form:
$$a_0(x)y + a_1(x)y' + a_2(x)y'' + ... + a_n(x)y^{(n)} = b(x)$$
where $a_0(x), ..., a_n(x)$ and $b(x)$ are arbitrary differentiable functions that **do not need to be linear**, and $y′, ..., y(n)$ are the **successive derivatives of an unknown function $y$ of the variable $x$**.

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

iii) Mutiply both sides of (i) by $\mu$

iv) Rewrite (iii) using the product rule