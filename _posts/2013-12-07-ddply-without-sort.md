---
title: Divide the first column by the number of each element in the second column
layout: post
categories: [RStudy]
tags: [R,plyr]
image: /figure
---

{% include JB/setup %}

#### Example data


```r
m = data.frame(x = c(3, 2, 3, 4, 5), y = c(2, 1, 2, 1, 1))
m
```

```
x y
1 3 2
2 2 1
3 3 2
4 4 1
5 5 1
```


#### Do not preserve order of m


```r
library(plyr)
ddply(m, .(y), transform, num = length(which(y == y)), result = x/length(which(y == y)))
```

```
x y num result
1 2 1   3 0.6667
2 4 1   3 1.3333
3 5 1   3 1.6667
4 3 2   2 1.5000
5 3 2   2 1.5000
```


#### Preserves order of m


```r
keeping.order <- function(data, fn, ...) {
col <- ".sortColumn"
data[, col] <- 1:nrow(data)
out <- fn(data, ...)
if (!col %in% colnames(out))
stop("Ordering column not preserved by function")
out <- out[order(out[, col]), ]
out[, col] <- NULL
out
}

keeping.order(m, ddply, .(y), transform, num = length(which(y == y)), result = x/length(which(y == y)))
```

```
x y num result
4 3 2   2 1.5000
1 2 1   3 0.6667
5 3 2   2 1.5000
2 4 1   3 1.3333
3 5 1   3 1.6667
```


### Further reading

* [How to ddply() without sorting?](http://stackoverflow.com/questions/7235421/how-to-ddply-without-sorting)

