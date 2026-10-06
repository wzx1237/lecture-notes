# This is a note about math used in mechine learning

Time: 2026/05/05

## Gradient:
Nabla Operator: $\nabla$

For example, in $\mathbb{R}^3$: 
$$\nabla = \frac{\partial}{\partial{x}}\vec{i} + \frac{\partial}{\partial{y}}\vec{j} + \frac{\partial}{\partial{z}}\vec{k} = (\frac{\partial}{\partial{x}}\vec{i}, \frac{\partial}{\partial{y}}\vec{j}, \frac{\partial}{\partial{z}}\vec{k})$$

The gradient of a scalar function $f: \mathbb{R}^{3} \rightarrow \mathbb{R}$ is given by: 
$$\nabla f = (\frac{\partial{f}}{\partial{x}}\vec{i}, \frac{\partial{f}}{\partial{y}}\vec{j}, \frac{\partial{f}}{\partial{z}}\vec{k})$$
which is a **vector field**!

## Divergence:
Divergence of a **vector field** $\vec{F} = (F_{x}, F_{y}, F_{z})$ is given by: 
$$\nabla \cdot \vec{F} = \frac{\partial{F_{x}}}{\partial{x}} + \frac{\partial{F_{y}}}{\partial{y}} + \frac{\partial{F_{z}}}{\partial{z}}$$

which is a **scalar field**!

## Curl:
Curl of a **vector field** $\vec{F} = (F_{x}, F_{y}, F_{z})$
$$\text{Curl of } F = \nabla \times \vec{F}$$

## Fundamental Theorem of vector calculus (in $\mathbb{R}^{3}$)
$$F = - \nabla \phi + \nabla \times \vec{A}$$
, where $\phi$ and $\vec{A}$ is a vector field in $\mathbb{R}^{3}$

## Example of calculating gradient for a Loss Function:

Given Loss function:

$$L(\vec{\omega}, b) = \frac{1}{n} \sum_{i=1}^{n} (\hat{y_{i}} - y_i)^{2} + \lambda ||\vec{\omega}||^{2}$$

where $\hat{y_i} = \vec{\omega}^{T} \dot x_{i} + b$