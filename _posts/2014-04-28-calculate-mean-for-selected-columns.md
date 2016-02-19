---
title: Calculate the mean using selected column(s)
layout: post
categories: [RStudy]
tags: [R, reshape2, plyr]
image: /figure
---

{% include JB/setup %}


```r
head(iris)
```

```
Sepal.Length Sepal.Width Petal.Length Petal.Width Species
1          5.1         3.5          1.4         0.2  setosa
2          4.9         3.0          1.4         0.2  setosa
3          4.7         3.2          1.3         0.2  setosa
4          4.6         3.1          1.5         0.2  setosa
5          5.0         3.6          1.4         0.2  setosa
6          5.4         3.9          1.7         0.4  setosa
```

```r
mydata = iris
mydata$ID = rep(c(1, 2, 3, 4), length.out = nrow(mydata))
head(mydata)
```

```
Sepal.Length Sepal.Width Petal.Length Petal.Width Species ID
1          5.1         3.5          1.4         0.2  setosa  1
2          4.9         3.0          1.4         0.2  setosa  2
3          4.7         3.2          1.3         0.2  setosa  3
4          4.6         3.1          1.5         0.2  setosa  4
5          5.0         3.6          1.4         0.2  setosa  1
6          5.4         3.9          1.7         0.4  setosa  2
```


### melt()


```r
library(reshape2)
molten = melt(mydata, id = c("ID", "Species"), na.rm = TRUE)
# each row will represent one observation of one variable.
molten[c(1:5, 55, 140), ]
```

```
ID    Species     variable value
1    1     setosa Sepal.Length   5.1
2    2     setosa Sepal.Length   4.9
3    3     setosa Sepal.Length   4.7
4    4     setosa Sepal.Length   4.6
5    1     setosa Sepal.Length   5.0
55   3 versicolor Sepal.Length   6.5
140  4  virginica Sepal.Length   6.9
```


### dcast()

#### One variable (column)


```r
dcast(molten, formula = ID ~ variable)
```

```
ID Sepal.Length Sepal.Width Petal.Length Petal.Width
1  1           38          38           38          38
2  2           38          38           38          38
3  3           37          37           37          37
4  4           37          37           37          37
```

```r
dcast(molten, formula = ID ~ variable, mean)
```

```
ID Sepal.Length Sepal.Width Petal.Length Petal.Width
1  1        5.853       3.118        3.800       1.258
2  2        5.787       3.026        3.689       1.163
3  3        5.827       3.008        3.751       1.178
4  4        5.908       3.076        3.792       1.197
```

```r
dcast(molten, formula = ID ~ variable, median)
```

```
ID Sepal.Length Sepal.Width Petal.Length Petal.Width
1  1         5.75         3.1         4.35        1.35
2  2         5.60         3.0         4.10        1.30
3  3         5.80         3.0         4.50        1.30
4  4         6.00         3.0         4.40        1.30
```



```r
dcast(molten, formula = Species ~ variable)
```

```
Species Sepal.Length Sepal.Width Petal.Length Petal.Width
1     setosa           50          50           50          50
2 versicolor           50          50           50          50
3  virginica           50          50           50          50
```

```r
dcast(molten, formula = Species ~ variable, mean)
```

```
Species Sepal.Length Sepal.Width Petal.Length Petal.Width
1     setosa        5.006       3.428        1.462       0.246
2 versicolor        5.936       2.770        4.260       1.326
3  virginica        6.588       2.974        5.552       2.026
```


#### two variables (columns)


```r
dcast(molten, formula = ID + Species ~ variable)
```

```
ID    Species Sepal.Length Sepal.Width Petal.Length Petal.Width
1   1     setosa           13          13           13          13
2   1 versicolor           12          12           12          12
3   1  virginica           13          13           13          13
4   2     setosa           13          13           13          13
5   2 versicolor           12          12           12          12
6   2  virginica           13          13           13          13
7   3     setosa           12          12           12          12
8   3 versicolor           13          13           13          13
9   3  virginica           12          12           12          12
10  4     setosa           12          12           12          12
11  4 versicolor           13          13           13          13
12  4  virginica           12          12           12          12
```

```r
dcast(molten, formula = ID + Species ~ variable, mean)
```

```
ID    Species Sepal.Length Sepal.Width Petal.Length Petal.Width
1   1     setosa        5.092       3.515        1.492      0.2231
2   1 versicolor        5.925       2.725        4.292      1.3500
3   1  virginica        6.546       3.085        5.654      2.2077
4   2     setosa        4.931       3.292        1.438      0.2308
5   2 versicolor        5.800       2.717        4.108      1.2833
6   2  virginica        6.631       3.046        5.554      1.9846
7   3     setosa        4.950       3.442        1.417      0.2333
8   3 versicolor        6.054       2.823        4.323      1.3538
9   3  virginica        6.458       2.775        5.467      1.9333
10  4     setosa        5.050       3.467        1.500      0.3000
11  4 versicolor        5.954       2.808        4.308      1.3154
12  4  virginica        6.717       2.975        5.525      1.9667
```



```r
# the order of ID and Species was changed, then the result was also changed
dcast(molten, formula = Species + ID ~ variable)
```

```
Species ID Sepal.Length Sepal.Width Petal.Length Petal.Width
1      setosa  1           13          13           13          13
2      setosa  2           13          13           13          13
3      setosa  3           12          12           12          12
4      setosa  4           12          12           12          12
5  versicolor  1           12          12           12          12
6  versicolor  2           12          12           12          12
7  versicolor  3           13          13           13          13
8  versicolor  4           13          13           13          13
9   virginica  1           13          13           13          13
10  virginica  2           13          13           13          13
11  virginica  3           12          12           12          12
12  virginica  4           12          12           12          12
```

```r
dcast(molten, formula = Species + ID ~ variable, mean)
```

```
Species ID Sepal.Length Sepal.Width Petal.Length Petal.Width
1      setosa  1        5.092       3.515        1.492      0.2231
2      setosa  2        4.931       3.292        1.438      0.2308
3      setosa  3        4.950       3.442        1.417      0.2333
4      setosa  4        5.050       3.467        1.500      0.3000
5  versicolor  1        5.925       2.725        4.292      1.3500
6  versicolor  2        5.800       2.717        4.108      1.2833
7  versicolor  3        6.054       2.823        4.323      1.3538
8  versicolor  4        5.954       2.808        4.308      1.3154
9   virginica  1        6.546       3.085        5.654      2.2077
10  virginica  2        6.631       3.046        5.554      1.9846
11  virginica  3        6.458       2.775        5.467      1.9333
12  virginica  4        6.717       2.975        5.525      1.9667
```


#### subset of data


```r
library(plyr)  # needed to access . function
dcast(molten, formula = ID ~ variable, subset = .(Species == "setosa"))
```

```
ID Sepal.Length Sepal.Width Petal.Length Petal.Width
1  1           13          13           13          13
2  2           13          13           13          13
3  3           12          12           12          12
4  4           12          12           12          12
```

```r
dcast(molten, formula = ID ~ variable, mean, subset = .(Species == "setosa"))
```

```
ID Sepal.Length Sepal.Width Petal.Length Petal.Width
1  1        5.092       3.515        1.492      0.2231
2  2        4.931       3.292        1.438      0.2308
3  3        4.950       3.442        1.417      0.2333
4  4        5.050       3.467        1.500      0.3000
```


#### include margins


```r
dcast(molten, formula = ID ~ variable, mean, margins = TRUE)
```

```
ID Sepal.Length Sepal.Width Petal.Length Petal.Width (all)
1     1        5.853       3.118        3.800       1.258 3.507
2     2        5.787       3.026        3.689       1.163 3.416
3     3        5.827       3.008        3.751       1.178 3.441
4     4        5.908       3.076        3.792       1.197 3.493
5 (all)        5.843       3.057        3.758       1.199 3.465
```

```r
dcast(molten, formula = ID ~ variable, mean, margins = "ID")
```

```
ID Sepal.Length Sepal.Width Petal.Length Petal.Width
1     1        5.853       3.118        3.800       1.258
2     2        5.787       3.026        3.689       1.163
3     3        5.827       3.008        3.751       1.178
4     4        5.908       3.076        3.792       1.197
5 (all)        5.843       3.057        3.758       1.199
```


### Reference

* [Reshape and aggregate data with the R package reshape2](http://tgmstat.wordpress.com/2013/10/31/reshape-and-aggregate-data-with-the-r-package-reshape2/)
