---
title: R aggregate()
layout: post
categories: [RStudy]
tags: [R,aggregate]
image: /figure
---

{% include JB/setup %}

### Attach data


```r
head(mtcars)
```

```
mpg cyl disp  hp drat    wt  qsec vs am gear carb
Mazda RX4         21.0   6  160 110 3.90 2.620 16.46  0  1    4    4
Mazda RX4 Wag     21.0   6  160 110 3.90 2.875 17.02  0  1    4    4
Datsun 710        22.8   4  108  93 3.85 2.320 18.61  1  1    4    1
Hornet 4 Drive    21.4   6  258 110 3.08 3.215 19.44  1  0    3    1
Hornet Sportabout 18.7   8  360 175 3.15 3.440 17.02  0  0    3    2
Valiant           18.1   6  225 105 2.76 3.460 20.22  1  0    3    1
```

```r
attach(mtcars)
```



### Aggregate data frame mtcars by cyl and vs, returning means for numeric variables

When using the aggregate() function, the by variables must be in a list (even if there is only one). The function can be built-in or user provided.


```r
aggregate(mtcars, by = list(cyl, vs), FUN = mean, na.rm = TRUE)
```

```
Group.1 Group.2   mpg cyl  disp    hp  drat    wt  qsec vs     am  gear
1       4       0 26.00   4 120.3  91.0 4.430 2.140 16.70  0 1.0000 5.000
2       6       0 20.57   6 155.0 131.7 3.807 2.755 16.33  0 1.0000 4.333
3       8       0 15.10   8 353.1 209.2 3.229 3.999 16.77  0 0.1429 3.286
4       4       1 26.73   4 103.6  81.8 4.035 2.300 19.38  1 0.7000 4.000
5       6       1 19.12   6 204.6 115.2 3.420 3.389 19.21  1 0.0000 3.500
carb
1 2.000
2 4.667
3 3.500
4 1.500
5 2.500
```


or


```r
aggregate(. ~ cyl + vs, data = mtcars, FUN = mean, na.rm = TRUE)
```

```
cyl vs   mpg  disp    hp  drat    wt  qsec     am  gear  carb
1   4  0 26.00 120.3  91.0 4.430 2.140 16.70 1.0000 5.000 2.000
2   6  0 20.57 155.0 131.7 3.807 2.755 16.33 1.0000 4.333 4.667
3   8  0 15.10 353.1 209.2 3.229 3.999 16.77 0.1429 3.286 3.500
4   4  1 26.73 103.6  81.8 4.035 2.300 19.38 0.7000 4.000 1.500
5   6  1 19.12 204.6 115.2 3.420 3.389 19.21 0.0000 3.500 2.500
```


### Mean of mpg by cyl


```r
aggregate(mpg, by = list(cyl), FUN = mean, na.rm = TRUE)
```

```
Group.1     x
1       4 26.66
2       6 19.74
3       8 15.10
```


or


```r
aggregate(mpg ~ cyl, data = mtcars, FUN = mean, na.rm = TRUE)
```

```
cyl   mpg
1   4 26.66
2   6 19.74
3   8 15.10
```


### The number of rows for that cyl & vs combination


```r
aggregate(mtcars, by = list(cyl, vs), FUN = length)
```

```
Group.1 Group.2 mpg cyl disp hp drat wt qsec vs am gear carb
1       4       0   1   1    1  1    1  1    1  1  1    1    1
2       6       0   3   3    3  3    3  3    3  3  3    3    3
3       8       0  14  14   14 14   14 14   14 14 14   14   14
4       4       1  10  10   10 10   10 10   10 10 10   10   10
5       6       1   4   4    4  4    4  4    4  4  4    4    4
```


or


```r
aggregate(. ~ cyl + vs, data = mtcars, FUN = length)
```

```
cyl vs mpg disp hp drat wt qsec am gear carb
1   4  0   1    1  1    1  1    1  1    1    1
2   6  0   3    3  3    3  3    3  3    3    3
3   8  0  14   14 14   14 14   14 14   14   14
4   4  1  10   10 10   10 10   10 10   10   10
5   6  1   4    4  4    4  4    4  4    4    4
```


### Detach data


```r
detach(mtcars)
```


### Session information


```r
sessionInfo()
```

```
R version 3.0.3 (2014-03-06)
Platform: x86_64-w64-mingw32/x64 (64-bit)

locale:
[1] LC_COLLATE=English_United States.1252
[2] LC_CTYPE=English_United States.1252
[3] LC_MONETARY=English_United States.1252
[4] LC_NUMERIC=C
[5] LC_TIME=English_United States.1252

attached base packages:
[1] stats     graphics  grDevices utils     datasets  methods   base

other attached packages:
[1] knitr_1.5

loaded via a namespace (and not attached):
[1] evaluate_0.5.3 formatR_0.10   stringr_0.6.2  tools_3.0.3
```


### References

* [Quick-R: Aggregating Data](http://www.statmethods.net/management/aggregate.html)
* [Using aggregate and apply in R](http://davetang.org/muse/2013/05/22/using-aggregate-and-apply-in-r/)
