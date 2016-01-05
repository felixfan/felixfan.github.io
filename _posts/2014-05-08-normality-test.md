---
title: Normality test
layout: post
categories: [RStudy]
tags: [R]
image: /figure
---
{% include JB/setup %}

### Data


```r
set.seed(999)
x1 <- rbinom(15, 5, 0.6)
x2 <- rbinom(30, 5, 0.6)
x3 <- rbinom(500, 5, 0.6)
x4 <- rlnorm(15)
x5 <- rlnorm(30)
x6 <- rlnorm(500)
x7 <- rnorm(15)
x8 <- rnorm(500)
x9 <- rnorm(5e+06)
```


### Shapiro-Wilk Normality Test

```
shapiro.test() in package stats. length of data: 3-5000
```


```r
shapiro.test(x1)
```

```

Shapiro-Wilk normality test

data:  x1
W = 0.9157, p-value = 0.1653
```

```r
shapiro.test(x2)
```

```

Shapiro-Wilk normality test

data:  x2
W = 0.834, p-value = 0.0002918
```

```r
shapiro.test(x3)
```

```

Shapiro-Wilk normality test

data:  x3
W = 0.919, p-value = 9.795e-16
```

```r
shapiro.test(x4)
```

```

Shapiro-Wilk normality test

data:  x4
W = 0.6059, p-value = 2.884e-05
```

```r
shapiro.test(x5)
```

```

Shapiro-Wilk normality test

data:  x5
W = 0.8451, p-value = 0.0004895
```

```r
shapiro.test(x6)
```

```

Shapiro-Wilk normality test

data:  x6
W = 0.4848, p-value < 2.2e-16
```

```r
shapiro.test(x7)
```

```

Shapiro-Wilk normality test

data:  x7
W = 0.975, p-value = 0.9235
```

```r
shapiro.test(x8)
```

```

Shapiro-Wilk normality test

data:  x8
W = 0.9987, p-value = 0.9779
```

```r
shapiro.test(x9)
```

```
Error: sample size must be between 3 and 5000
```


### Anderson-Darling test for normality

```
ad.test() in package nortest
```


```r
library(nortest)
ad.test(x1)
```

```

Anderson-Darling normality test

data:  x1
A = 0.7072, p-value = 0.05103
```

```r
ad.test(x2)
```

```

Anderson-Darling normality test

data:  x2
A = 1.96, p-value = 4.006e-05
```

```r
ad.test(x3)
```

```

Anderson-Darling normality test

data:  x3
A = 17.95, p-value < 2.2e-16
```

```r
ad.test(x4)
```

```

Anderson-Darling normality test

data:  x4
A = 2.059, p-value = 1.542e-05
```

```r
ad.test(x5)
```

```

Anderson-Darling normality test

data:  x5
A = 1.806, p-value = 9.715e-05
```

```r
ad.test(x6)
```

```

Anderson-Darling normality test

data:  x6
A = Inf, p-value = NA
```

```r
ad.test(x7)
```

```

Anderson-Darling normality test

data:  x7
A = 0.1743, p-value = 0.908
```

```r
ad.test(x8)
```

```

Anderson-Darling normality test

data:  x8
A = 0.1436, p-value = 0.9704
```

```r
ad.test(x9)
```

```

Anderson-Darling normality test

data:  x9
A = 0.2392, p-value = 0.7793
```


### Summary

When the sample size is big, the test result is quite reliable.


