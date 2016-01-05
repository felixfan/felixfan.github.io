---
title: data.table
layout: post
categories: [RStudy]
tags: [R, data.table]
image: /figure
---
{% include JB/setup %}


```r
library(data.table)
```


### Create data table


```r
# it is similar with data frame
set.seed(999)
dt = data.table(x = sample(c("a", "b", "c", "d"), 10, replace = TRUE), y = rnorm(10))
dt
```

```
x       y
1: b -0.5660
2: c -1.8787
3: a -1.2668
4: d -0.9677
5: d -1.1210
6: a  1.3255
7: c  0.1340
8: a  0.9387
9: b  0.1725
10: c  0.9577
```

```r
dt[2]  # 2nd row
```

```
x      y
1: c -1.879
```

```r
dt[, y]  # y column (as vector)
```

```
[1] -0.5660 -1.8787 -1.2668 -0.9677 -1.1210  1.3255  0.1340  0.9387
[9]  0.1725  0.9577
```

```r
dt[, list(y)]  # y column (as data.table)
```

```
y
1: -0.5660
2: -1.8787
3: -1.2668
4: -0.9677
5: -1.1210
6:  1.3255
7:  0.1340
8:  0.9387
9:  0.1725
10:  0.9577
```

```r


# convert existing data.frame objects to data.table.
dt.cars = data.table(cars)
head(dt.cars)
```

```
speed dist
1:     4    2
2:     4   10
3:     7    4
4:     7   22
5:     8   16
6:     9   10
```


### list out all data.tables in memory


```r
tables()  # The result of tables() is itself a data.table
```

```
NAME    NROW MB COLS       KEY
[1,] dt        10 1  x,y
[2,] dt.cars   50 1  speed,dist
Total: 2MB
```


### Keys

A key consists of one or more columns of rownames, which may be integer, factor, character or some other class, not simply character. The rows are sorted by the key. A data.table can have at most one key, but duplicate key values are allowed.


```r
# use data.frame syntax in a data.table
dt[2, ]  # the second row of df
```

```
x      y
1: c -1.879
```

```r
dt[dt$x == "a", ]  # all rows with first column is 'a'
```

```
x       y
1: a -1.2668
2: a  1.3255
3: a  0.9387
```

```r

# data.table unique key
setkey(dt, x)  # set x column as key
dt["a", ]  # all rows with first column is 'a', The comma is optional.
```

```
x       y
1: a -1.2668
2: a  1.3255
3: a  0.9387
```

```r
dt["a"]
```

```
x       y
1: a -1.2668
2: a  1.3255
3: a  0.9387
```

```r

# By default all the rows in the group are returned The mult argument allows
# only the first or last row of the group to be returned
dt["a", mult = "first"]
```

```
x      y
1: a -1.267
```

```r
dt["a", mult = "last"]
```

```
x      y
1: a 0.9387
```


### binary search (faster)

The vector scan is linear, but the binary search is O(log n).


```r
df2 <- data.frame(x = sample(LETTERS, 1e+07, replace = T), y = sample(letters,
1e+07, replace = T), z = rnorm(1e+07))
system.time(ans1 <- df2[df2$x == "R" & df2$y == "h", ])  # 'vector scan'
```

```
user  system elapsed
5.81    0.28    6.11
```

```r

dt2 <- data.table(df2)
setkey(dt2, x, y)
system.time(ans2 <- dt2[J("R", "h")])  # binary search, faster
```

```
user  system elapsed
0.02    0.00    0.01
```

```r

identical(ans1$z, ans2$z)
```

```
[1] TRUE
```


### Fast grouping


```r
system.time(sum1 <- dt2[, sum(z), by = x])
```

```
user  system elapsed
0.21    0.05    0.25
```

```r
head(sum1)
```

```
x       V1
1: A  -211.43
2: B   -60.01
3: C  -723.30
4: D   392.90
5: E -1251.52
6: F    92.21
```

```r

dt2[, sum(z), by = list(x == "A")]  # by expression
```

```
x      V1
1:  TRUE  -211.4
2: FALSE -6875.4
```

```r

system.time(sum2 <- dt2[, sum(z), by = "x,y"])
```

```
user  system elapsed
0.14    0.04    0.19
```

```r
head(sum2)
```

```
x y      V1
1: A a 147.617
2: A b   2.296
3: A c 203.767
4: A d  77.195
5: A e -16.550
6: A f  58.810
```


### Fast time series join (or a rolling join)


```r
set.seed(9999)
dt3 = data.table(x = sample(letters, 10, replace = T), y = sample(1:20, 10,
replace = T), z = sample(1:99, 10, replace = T))
setkey(dt3, x)
dt3["o"]  # join to 1st column of key
```

```
x  y  z
1: o NA NA
```

```r
dt3[J("o")]  # same. J() stands for Join, an alias for list()
```

```
x  y  z
1: o NA NA
```

```r
dt3[!"o"]  # all rows other than 'o'
```

```
x  y  z
1: f 16 55
2: f 19 34
3: r  1 98
4: r  9 34
5: t  3 35
6: u  4 85
7: v 19 39
8: v  2  7
9: w 17 33
10: z 17 45
```

```r
dt3[!2:4]  # all rows other than 2:4
```

```
x  y  z
1: f 16 55
2: t  3 35
3: u  4 85
4: v 19 39
5: v  2  7
6: w 17 33
7: z 17 45
```

```r

setkey(dt3, x, y)
dt3[J("o", 3)]  # join to 2 columns
```

```
x y  z
1: o 3 NA
```

```r
dt3[J("o", 3:6)]  # join 4 rows (1 missing)
```

```
x y  z
1: o 3 NA
2: o 4 NA
3: o 5 NA
4: o 6 NA
```

```r
dt3[!J("o", 3)]  # multiple join
```

```
x  y  z
1: f 16 55
2: f 19 34
3: r  1 98
4: r  9 34
5: t  3 35
6: u  4 85
7: v  2  7
8: v 19 39
9: w 17 33
10: z 17 45
```

```r
dt3[, sum(z), by = x][order(-V1)]  # ordering results
```

```
x  V1
1: r 132
2: f  89
3: u  85
4: v  46
5: z  45
6: t  35
7: w  33
```


### Learn more


```r
vignette("datatable-intro")
example(data.table)
```

