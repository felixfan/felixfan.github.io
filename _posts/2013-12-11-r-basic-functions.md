---
title: Basic R functions
layout: post
categories: [RStudy]
tags: [R]
image: /figure
---
{% include JB/setup %}


### 1. all, any, which


```r
x = -5:5

all(x)  # Given a set of logical vectors, are all of the values true?
```

```
[1] FALSE
```

```r
all(x > 3)
```

```
[1] FALSE
```

```r

any(x)  # Given a set of logical vectors, is at least one of the values true?
```

```
[1] TRUE
```

```r
any(x > 3)
```

```
[1] TRUE
```

```r

which(x > 3)  # Give the TRUE indices of a logical object, allowing for array indices.
```

```
[1] 10 11
```

```r
x[which(x > 3)]
```

```
[1] 4 5
```

```r
x[x > 3]
```

```
[1] 4 5
```

```r

which.max(x)  # Give the indices of max
```

```
[1] 11
```

```r
x[which.max(x)]
```

```
[1] 5
```

```r
max(x)
```

```
[1] 5
```

```r

which.min(x)  # Give the indices of min
```

```
[1] 1
```

```r
x[which.min(x)]
```

```
[1] -5
```

```r
min(x)
```

```
[1] -5
```


### 2. summary, max, min, mean, median, range, quantile


```r
options(digits = 4)
y = rnorm(10)
y
```

```
[1] -0.4460 -0.2693 -0.1460 -1.9396 -0.0134  0.1919  0.4205  0.5393
[9]  0.2638  0.9963
```

```r
summary(y)
```

```
Min. 1st Qu.  Median    Mean 3rd Qu.    Max.
-1.9400 -0.2380  0.0893 -0.0402  0.3810  0.9960
```

```r
max(y)
```

```
[1] 0.9963
```

```r
min(y)
```

```
[1] -1.94
```

```r
mean(y)
```

```
[1] -0.04025
```

```r
median(y)
```

```
[1] 0.08926
```

```r
range(y)
```

```
[1] -1.9396  0.9963
```

```r
quantile(y, c(0.25, 0.75, 0.95))
```

```
25%     75%     95%
-0.2384  0.3813  0.7906
{% include JB/setup %}
```


### 3. dim, nrow, ncol, colMeans, colSums, rowMeans, rowSums


```r
df = data.frame(x = 1:5, y = 3:7, z = 23:27)
df
```

```
x y  z
1 1 3 23
2 2 4 24
3 3 5 25
4 4 6 26
5 5 7 27
```

```r

dim(df)
```

```
[1] 5 3
```

```r
nrow(df)
```

```
[1] 5
```

```r
ncol(df)
```

```
[1] 3
```

```r

colMeans(df)
```

```
x  y  z
3  5 25
```

```r
colSums(df)
```

```
x   y   z
15  25 125
```

```r
rowMeans(df)
```

```
[1]  9 10 11 12 13
```

```r
rowSums(df)
```

```
[1] 27 30 33 36 39
```


### 4. nchar, strsplit, substr, toupper, tolower


```r
z = "Hello World"
nchar(z)
```

```
[1] 11
```

```r
strsplit(z, " ")
```

```
[[1]]
[1] "Hello" "World"
```

```r
substr(z, 1, 1)
```

```
[1] "H"
```

```r
substr(z, 1, 3)
```

```
[1] "Hel"
```

```r
toupper(z)
```

```
[1] "HELLO WORLD"
```

```r
tolower(z)
```

```
[1] "hello world"
```


### 5. cummax, cummin, cumprod, and cumsum


```r
x = c(1, 2, -3, 4, -6, 9, 6, 7)
x
```

```
[1]  1  2 -3  4 -6  9  6  7
```

```r
cumsum(x)
```

```
[1]  1  3  0  4 -2  7 13 20
```

```r
cumprod(x)
```

```
[1]     1     2    -6   -24   144  1296  7776 54432
```

```r
cummax(x)
```

```
[1] 1 2 2 4 4 9 9 9
```

```r
cummin(x)
```

```
[1]  1  1 -3 -3 -6 -6 -6 -6
```


### 6. diff, duplicated, unique, order, and sort


```r
x = c(1, 0, -2, 3, 6, 0, 9)
x
```

```
[1]  1  0 -2  3  6  0  9
```

```r

diff(x, 1)  # x[i] - x[i-1]
```

```
[1] -1 -2  5  3 -6  9
```

```r

duplicated(x)
```

```
[1] FALSE FALSE FALSE FALSE FALSE  TRUE FALSE
```

```r
x[!duplicated(x)]
```

```
[1]  1  0 -2  3  6  9
```

```r

unique(x)
```

```
[1]  1  0 -2  3  6  9
```

```r

order(x)
```

```
[1] 3 2 6 1 4 5 7
```

```r
x[order(x)]
```

```
[1] -2  0  0  1  3  6  9
```

```r

sort(x)
```

```
[1] -2  0  0  1  3  6  9
```


### ifelse


```r
a = c(4, -4)
sqrt(ifelse(a >= 0, a, NA))
```

```
[1]  2 NA
```


### do.call


```r
# Execute a Function Call
do.call(paste, list("Hello", "World", sep = " "))
```

```
[1] "Hello World"
```

```r

x = seq(1, 2, by = 0.2)
y = seq(3, 4, by = 0.2)
do.call(cbind, list(x, y))
```

```
[,1] [,2]
[1,]  1.0  3.0
[2,]  1.2  3.2
[3,]  1.4  3.4
[4,]  1.6  3.6
[5,]  1.8  3.8
[6,]  2.0  4.0
```

```r
do.call(rbind, list(x, y))
```

```
[,1] [,2] [,3] [,4] [,5] [,6]
[1,]    1  1.2  1.4  1.6  1.8    2
[2,]    3  3.2  3.4  3.6  3.8    4
```


### expression and eval


```r
# Evaluate an (Unevaluated) Expression
x = 3
y = 5
z = expression(x + y)
z
```

```
expression(x + y)
```

```r
eval(z)
```

```
[1] 8
```

