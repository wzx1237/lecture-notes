# This is a note about math used in mechine learning

Time: 2026/05/05

## Gradient:
Nabla Operator: $\nabla$

For example, in $\mathbb{R}^3$: 
$$\nabla = \frac{\partial}{\partial{x}}\vector{i} + \frac{\partial}{\partial{y}}\vector{j} + \frac{\partial}{\partial{z}}\vector{k} = (\frac{\partial}{\partial{x}}\vector{i}, \frac{\partial}{\partial{y}}\vector{j}, \frac{\partial}{\partial{z}}\vector{k})$$

Gradient of a function $f: \mathbb{R}^{3} \rightArrow \mathbb{R}$ (scalar field):
$$\text{Gradient of } f = \nabla f = (\frac{\partial{f}}{\partial{x}}\vector{i}, \frac{\partial{f}}{\partial{y}}\vector{j}, \frac{\partial{f}}{\partial{z}}\vector{k})$$
which is a **vector field**!

## Divergence:
Divergence of a **vector field** (i.e. $\vector{F} = (F_{x}, F_{y}, F_{z})$)
$$\text{Divergence of }F = \nabla \cdot \vector{F} = \frac{\partial{F_{x}}}{\partial{x}} + \frac{\partial{F_{y}}{\partial{y}} + \frac{\partial{F_{z}}}{\partial{z}}$$

which is a **scalar field**!

## Curl:
Curl of a **vector field** (i.e. $\vector{F} = (F_{x}, F_{y}, F_{z})$)
$$\text{Curl of } F = \nabla \times \vector{F}$$

## Fundamental Theorem of vector calculus (in $\mathbb{R}^{3}$)
$$F = - \nabla \phi + \nabla \times \vector{A}$$
, where $\phi$ and $\vector{A}$ is a vector field in $\mathbb{R}^{3}$
