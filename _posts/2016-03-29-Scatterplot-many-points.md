---
title: Scatterplot with a lot of points
layout: post
categories: [RStudy]
tags: [ggplot2]
image: /figure2016
---
{% include JB/setup %} 


```r
library(ggplot2)
dat <- data.frame(x=rnorm(10000), y=rnorm(10000))
```

## point plot


```r
ggplot(dat, aes(x=x, y=y)) + geom_point()
```

![](/figure2016/ggplot_point1-1.png)

## jittering


```r
ggplot(dat, aes(x=x, y=y)) + geom_point(position = 'jitter')
```

![](/figure2016/ggplot_point2-1.png)

## alpha


```r
ggplot(dat, aes(x=x, y=y)) + geom_point(alpha = 0.3)
```

![](/figure2016/ggplot_point31-1.png)


```r
ggplot(dat, aes(x=x, y=y)) + geom_point(alpha = 0.1)
```

![](/figure2016/ggplot_point32-1.png)

## contour lines


```r
ggplot(dat, aes(x=x, y=y)) + geom_point() + geom_density2d()
```

![](/figure2016/ggplot_point4-1.png)

## HexBins


```r
ggplot(dat, aes(x=x, y=y)) + stat_binhex()
```

![](/figure2016/ggplot_point5-1.png)

## combined


```r
ggplot(dat, aes(x=x, y=y)) + geom_point(colour='black',alpha=0.3) + geom_density2d(colour='red')
```

![](/figure2016/ggplot_point6-1.png)


