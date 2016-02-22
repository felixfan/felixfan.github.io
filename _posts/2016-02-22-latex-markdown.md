---
title: latex in markdown
layout: post
categories: [Bioinformatics]
tags: [LaTeX]
image: /figure2016
---
{% include JB/setup %}


```
Here is an in-line equation $\sqrt{3x-1}+(1+x)^2$ in the body of the text.
```

Here is an in-line equation \\[ \sqrt{3x-1}+(1+x)^2 \\] in the body of the text.

```
Here is an equation: $\left [ - \frac{\hbar^2}{2 m} \frac{\partial^2}{\partial x^2} + V \right ] \Psi
= i \hbar \frac{\partial}{\partial t} \Psi$
```

Here is an equation: \\[\left [ - \frac{\hbar^2}{2 m} \frac{\partial^2}{\partial x^2} + V \right ] \Psi
= i \hbar \frac{\partial}{\partial t} \Psi\\]

## symbols

### 1. & 

used as separators in alignment environments     

```
a &lt; b
```

a &lt; b

### 2. ^, _, { and }

`^` used to indicate exponents;    
`^` used to indicate superscripts;    
`_` used to indicate subscripts;    
`{}` braces, used for grouping;    

```
x^i_2
```

\\[ x^i_2 \\]

```
{x^i}_2
```

\\[ {x^i}_2 \\]

```
x^{i_2}
```

\\[ x^{i_2} \\]

```
x^{i^2}
```

\\[ x^{i^2} \\]

```
{x^i}^2
```

\\[ {x^i}^2 \\]

```
^ax^b
```

\\[ ^ax^b \\]

```
\sum_{n=1}^\infty
```

\\[ \sum_{n=1}^\infty \\]

### 3. Greek letter

```
\alpha, \beta, \chi, \Delta, \delta, \epsilon, \eta, \Gamma, \gamma, \iota, \kappa
```

\\[ \alpha, \beta, \chi, \Delta, \delta, \epsilon, \eta, \Gamma, \gamma, \iota, \kappa \\]

   
```
\Lambda, \lambda, \mu, \omega, \Omega, \phi, \Phi, \pi, \Pi, \psi, \Psi
```

\\[ \Lambda, \lambda, \mu, \omega, \Omega, \phi, \Phi, \pi, \Pi, \psi, \Psi \\]

```
\rho, \sigma, \Sigma, \tau, \theta, \Theta, \upsilon, \Upsilon, \varDelta, \varepsilon, \varGamma
```

\\[ \rho, \sigma, \Sigma, \tau, \theta, \Theta, \upsilon, \Upsilon, \varDelta, \varepsilon, \varGamma \\]

```
\varLambda, \varOmega, \varphi, \varPhi, \varpi, \varPi, \xi, \zeta
```

\\[ \varLambda, \varOmega, \varphi, \varPhi, \varpi, \varPi, \xi, \zeta \\]

### 4. \frac

```
\frac a b
```

\\[ \frac a b \\]

```
\frac{a-1}b-1
```

\\[\frac{a-1}b-1 \\]

```
\frac{a-1}{b-1}
```

\\[ \frac{a-1}{b-1} \\]


```
github pages: delimiters \\(, \\) and \\[, \\] for inline and displayed math, respectively.
Rstudio: delimiters $, $ and $$, $$ for inline and displayed math, respectively.

```

Reference: [TEX Commands available in MathJax](http://www.onemathematicalcat.org/MathJaxDocumentation/TeXSyntax.htm)



