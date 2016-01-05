---
title: R Data type
layout: post
categories: [RStudy]
tags: [R]
image: /figure
---
{% include JB/setup %}

### vectors and assignment


```r
x <- c(10, 5, 3, 6, 21)

x
```

```
[1] 10  5  3  6 21
```

```r

assign("y", c(10.4, 5.6, 3.1, 6.4, 21.7))

y
```

```
[1] 10.4  5.6  3.1  6.4 21.7
```

```r

z <- c(4, 6, 1, 4, 7)

z
```

```
[1] 4 6 1 4 7
```

```r

a <- c(x, y, z)

a
```

```
[1] 10.0  5.0  3.0  6.0 21.0 10.4  5.6  3.1  6.4 21.7  4.0  6.0  1.0  4.0
[15]  7.0
```

```r

v <- 2 * x + y + 1

v
```

```
[1] 31.4 16.6 10.1 19.4 64.7
```

```r

mean(v)
```

```
[1] 28.44
```

```r

median(v)
```

```
[1] 19.4
```

```r

var(v)
```

```
[1] 470.5
```

```r

sd(v)
```

```
[1] 21.69
```

```r

min(v)
```

```
[1] 10.1
```

```r

max(v)
```

```
[1] 64.7
```

```r

range(v)
```

```
[1] 10.1 64.7
```

```r

cumsum(v)
```

```
[1]  31.4  48.0  58.1  77.5 142.2
```

```r

cumprod(v)
```

```
[1]      31.4     521.2    5264.5  102131.8 6607925.2
```

```r

cummax(v)
```

```
[1] 31.4 31.4 31.4 31.4 64.7
```

```r

cummin(v)
```

```
[1] 31.4 16.6 10.1 10.1 10.1
```

```r

sum(v)
```

```
[1] 142.2
```

```r

summary(v)
```

```
Min. 1st Qu.  Median    Mean 3rd Qu.    Max.
10.1    16.6    19.4    28.4    31.4    64.7
```

```r

length(v)
```

```
[1] 5
```

```r

sort(v)
```

```
[1] 10.1 16.6 19.4 31.4 64.7
```

```r

sqrt(v)
```

```
[1] 5.604 4.074 3.178 4.405 8.044
```

```r

log(v)
```

```
[1] 3.447 2.809 2.313 2.965 4.170
```

```r

s3 <- seq(-5, 5, by = 0.2)

s3
```

```
[1] -5.0 -4.8 -4.6 -4.4 -4.2 -4.0 -3.8 -3.6 -3.4 -3.2 -3.0 -2.8 -2.6 -2.4
[15] -2.2 -2.0 -1.8 -1.6 -1.4 -1.2 -1.0 -0.8 -0.6 -0.4 -0.2  0.0  0.2  0.4
[29]  0.6  0.8  1.0  1.2  1.4  1.6  1.8  2.0  2.2  2.4  2.6  2.8  3.0  3.2
[43]  3.4  3.6  3.8  4.0  4.2  4.4  4.6  4.8  5.0
```

```r

s4 <- seq(length = 51, from = -5, by = 0.2)

s4
```

```
[1] -5.0 -4.8 -4.6 -4.4 -4.2 -4.0 -3.8 -3.6 -3.4 -3.2 -3.0 -2.8 -2.6 -2.4
[15] -2.2 -2.0 -1.8 -1.6 -1.4 -1.2 -1.0 -0.8 -0.6 -0.4 -0.2  0.0  0.2  0.4
[29]  0.6  0.8  1.0  1.2  1.4  1.6  1.8  2.0  2.2  2.4  2.6  2.8  3.0  3.2
[43]  3.4  3.6  3.8  4.0  4.2  4.4  4.6  4.8  5.0
```

```r

s5 <- rep(x, times = 5)

s5
```

```
[1] 10  5  3  6 21 10  5  3  6 21 10  5  3  6 21 10  5  3  6 21 10  5  3
[24]  6 21
```

```r

s6 <- rep(x, each = 5)

s6
```

```
[1] 10 10 10 10 10  5  5  5  5  5  3  3  3  3  3  6  6  6  6  6 21 21 21
[24] 21 21
```

```r

a
```

```
[1] 10.0  5.0  3.0  6.0 21.0 10.4  5.6  3.1  6.4 21.7  4.0  6.0  1.0  4.0
[15]  7.0
```

```r

a[1:5]
```

```
[1] 10  5  3  6 21
```

```r

a[-(1:5)]
```

```
[1] 10.4  5.6  3.1  6.4 21.7  4.0  6.0  1.0  4.0  7.0
```

```r

a[c(1, 3, 5)]
```

```
[1] 10  3 21
```


### Matrices


```r
# generates 5 x 4 numeric matrix
x <- matrix(1:20, nrow = 5, ncol = 4)

# another example
cells <- c(1, 26, 24, 68)
rnames <- c("R1", "R2")
cnames <- c("C1", "C2")
mymatrix <- matrix(cells, nrow = 2, ncol = 2, byrow = TRUE, dimnames = list(rnames,
cnames))

# Combining Matrices
B = matrix(c(2, 4, 3, 1, 5, 7), nrow = 3, ncol = 2)
C = matrix(c(7, 4, 2), nrow = 3, ncol = 1)
cbind(B, C)
```

```
[,1] [,2] [,3]
[1,]    2    1    7
[2,]    4    5    4
[3,]    3    7    2
```

```r

D = matrix(c(6, 2), nrow = 1, ncol = 2)
rbind(B, D)
```

```
[,1] [,2]
[1,]    2    1
[2,]    4    5
[3,]    3    7
[4,]    6    2
```

```r

# Deconstruction
c(B)
```

```
[1] 2 4 3 1 5 7
```

```r

# Identify rows, columns or elements using subscripts.
x[, 4]  # 4th column of matrix
```

```
[1] 16 17 18 19 20
```

```r
x[3, ]  # 3rd row of matrix
```

```
[1]  3  8 13 18
```

```r
x[2:4, 1:3]  # rows 2,3,4 of columns 1,2,3
```

```
[,1] [,2] [,3]
[1,]    2    7   12
[2,]    3    8   13
[3,]    4    9   14
```

```r

# Transpose
t(x)
```

```
[,1] [,2] [,3] [,4] [,5]
[1,]    1    2    3    4    5
[2,]    6    7    8    9   10
[3,]   11   12   13   14   15
[4,]   16   17   18   19   20
```


### Data Frame


```r
d <- c(1, 2, 3, 4)
e <- c("red", "white", "red", NA)
f <- c(TRUE, TRUE, TRUE, FALSE)
mydata <- data.frame(d, e, f)
mydata
```

```
d     e     f
1 1   red  TRUE
2 2 white  TRUE
3 3   red  TRUE
4 4  <NA> FALSE
```

```r

# variable names
names(mydata)
```

```
[1] "d" "e" "f"
```

```r
names(mydata) <- c("ID", "Color", "Passed")
names(mydata)
```

```
[1] "ID"     "Color"  "Passed"
```

```r

# There are a variety of ways to identify the elements of a data frame .
mydata[, 1:2]  # columns 1,2 of data frame
```

```
ID Color
1  1   red
2  2 white
3  3   red
4  4  <NA>
```

```r
mydata[c("ID", "Color")]  # columns ID and Color from data frame
```

```
ID Color
1  1   red
2  2 white
3  3   red
4  4  <NA>
```

```r
mydata$Passed  # variable Passed in the data frame
```

```
[1]  TRUE  TRUE  TRUE FALSE
```

```r
subset(mydata, Passed == "TRUE")
```

```
ID Color Passed
1  1   red   TRUE
2  2 white   TRUE
3  3   red   TRUE
```

```r
subset(mydata, ID > 3)
```

```
ID Color Passed
4  4  <NA>  FALSE
```

```r
subset(mydata, ID < 3, select = c(ID, Passed))
```

```
ID Passed
1  1   TRUE
2  2   TRUE
```

```r
subset(mydata, ID < 3, select = -c(Color, Passed))
```

```
ID
1  1
2  2
```

```r
subset(mydata, Color == "red" & Passed == "TRUE")
```

```
ID Color Passed
1  1   red   TRUE
3  3   red   TRUE
```

```r
mydata[mydata$ID %in% c(1, 3), ]
```

```
ID Color Passed
1  1   red   TRUE
3  3   red   TRUE
```

```r

# number of data rows and columns
nrow(mydata)
```

```
[1] 4
```

```r
ncol(mydata)
```

```
[1] 3
```


### List


```r
# example of a list with 4 components: a string, a numeric vector, a matrix,
# and a scaler
a <- c(1, 2, 5.3, 6, -2, 4)  # numeric vector
y <- matrix(1:20, nrow = 5, ncol = 4)
w <- list(name = "Fred", mynumbers = a, mymatrix = y, age = 5.3)
w
```

```
$name
[1] "Fred"

$mynumbers
[1]  1.0  2.0  5.3  6.0 -2.0  4.0

$mymatrix
[,1] [,2] [,3] [,4]
[1,]    1    6   11   16
[2,]    2    7   12   17
[3,]    3    8   13   18
[4,]    4    9   14   19
[5,]    5   10   15   20

$age
[1] 5.3
```



```r
# example of a list containing two lists
list1 = list(mynumbers = a)
list2 = list(mymatrix = y)
v <- c(list1, list2)
v
```

```
$mynumbers
[1]  1.0  2.0  5.3  6.0 -2.0  4.0

$mymatrix
[,1] [,2] [,3] [,4]
[1,]    1    6   11   16
[2,]    2    7   12   17
[3,]    3    8   13   18
[4,]    4    9   14   19
[5,]    5   10   15   20
```



```r
# Identify elements of a list using the [[]] convention.
v[[2]]  # 2nd component of the list
```

```
[,1] [,2] [,3] [,4]
[1,]    1    6   11   16
[2,]    2    7   12   17
[3,]    3    8   13   18
[4,]    4    9   14   19
[5,]    5   10   15   20
```

```r
v[["mynumbers"]]  # component named mynumbers in list
```

```
[1]  1.0  2.0  5.3  6.0 -2.0  4.0
```


### Factor


```r
# variable gender with 20 'male' entries and 30 'female' entries
gender <- c(rep("male", 20), rep("female", 30))
gender <- factor(gender)
# stores gender as 20 1s and 30 2s and associates 1=female, 2=male
# internally (alphabetically) R now treats gender as a nominal variable
summary(gender)
```

```
female   male
30     20
```

```r

# variable rating coded as 'large', 'medium', 'small'
rating <- c(rep("large", 5), rep("small", 10), rep("medium", 5))
rating <- ordered(rating)
# recodes rating to 1,2,3 and associates 1=large, 2=medium, 3=small
# internally R now treats rating as ordinal
```


**References**    
       
[Quick-R: Data type](http://www.statmethods.net/input/datatypes.html)          
[R Tutorial: Data Frame](http://www.r-tutor.com/r-introduction/data-frame)          
