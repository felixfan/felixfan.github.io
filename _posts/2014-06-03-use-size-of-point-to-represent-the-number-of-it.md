---
title: Represent the number of data pairs (x,y) by using the point size
layout: post
categories: [RStudy]
tags: [R,Plot]
image: /figure
---
{% include JB/setup %}

```r
set.seed(999)
x=sample(1:10,1000,replace=TRUE)
y=sample(1:10,1000,replace=TRUE)
plot(x,y)
```

![plot of chunk point-size-1](/figure/point-size-1.png)


```r
f=as.data.frame(table(x,y))
f$x=as.numeric(as.vector(f$x))
f$y=as.numeric(as.vector(f$y))
f$Freq=as.numeric(as.vector(f$Freq))
plot(f$x,f$y,cex=2*f$Freq/mean(f$Freq))
```

![plot of chunk point-size-2](/figure/point-size-2.png)

```
cex can be other values related to f$Freq. I divided it by its mean,
so the size of points will not too big.
```

