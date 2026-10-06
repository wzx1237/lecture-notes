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
$$\frac{1}{N} \sum_{i=1}^{N} (Y_{i} - \hat{Y_{i}})^{2}$$
where $N$ is number of samples we have.

## How to minimize MSE error?
