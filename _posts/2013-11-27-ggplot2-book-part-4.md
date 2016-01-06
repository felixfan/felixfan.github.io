---
title: ggplot2 part 4
layout: post
categories: [RStudy]
tags: [R,Plot,ggplot2]
image: /figure
---
{% include JB/setup %}

#### Basic plot types

* geom_area() draws an area plot, which is a line plot filled to the y-axis.
* geom_bar(stat = "identity")() makes a barchart.
* geom_line() makes a line plot.
* geom_path() is similar to a geom_line, but lines are connected in the order they appear in the data, not from left to right.
* geom_point() produces a scatterplot.
* geom_polygon() draws polygons, which are filled paths.
* geom_text() adds labels at the specified points.
* geom_tile() makes a image plot or level plot.


```r
library(ggplot2)
library(effects)
library(plyr)
diamonds = na.omit(diamonds)

df <- data.frame(x = c(3, 1, 5), y = c(2, 4, 6), label = c("a", "b", "c"))
p <- ggplot(df, aes(x, y, label = label)) + xlab(NULL) + ylab(NULL)
p + geom_point() + labs(title = "geom_point")
```

![plot of chunk ggplot-part4-1](/figure/ggplot-part4-11.png)

```r
# Equivalent to p + geom_point() + ggtitle('geom_point')

# Reduce line spacing and use bold text
p + geom_point() + ggtitle("geom_point") + theme(plot.title = element_text(lineheight = 0.8,
face = "bold"))
```

![plot of chunk ggplot-part4-1](/figure/ggplot-part4-12.png)

```r

p + geom_bar(stat = "identity") + labs(title = "geom_bar(stat=\"identity\")")
```

![plot of chunk ggplot-part4-1](/figure/ggplot-part4-13.png)

```r
p + geom_line() + labs(title = "geom_line")
```

![plot of chunk ggplot-part4-1](/figure/ggplot-part4-14.png)

```r
p + geom_area() + labs(title = "geom_area")
```

![plot of chunk ggplot-part4-1](/figure/ggplot-part4-15.png)

```r
p + geom_path() + labs(title = "geom_path")
```

![plot of chunk ggplot-part4-1](/figure/ggplot-part4-16.png)

```r
p + geom_text() + labs(title = "geom_text")
```

![plot of chunk ggplot-part4-1](/figure/ggplot-part4-17.png)

```r
p + geom_tile() + labs(title = "geom_tile")
```

![plot of chunk ggplot-part4-1](/figure/ggplot-part4-18.png)

```r
p + geom_polygon() + labs(title = "geom_polygon")
```

![plot of chunk ggplot-part4-1](/figure/ggplot-part4-19.png)


#### Displaying distributions


```r
# Never rely on the default parameters to get a revealing view of the
# distribution.  Zooming in on the x axis, and selecting a smaller bin
# width, reveals far more detail.  We can see that the distribution is
# slightly skew-right.  Don't forget to include information about important
# parameters (like bin width) in the caption.
qplot(depth, data = diamonds, geom = "histogram")
```

![plot of chunk ggplot-part4-2](/figure/ggplot-part4-21.png)

```r
qplot(depth, data = diamonds, geom = "histogram", xlim = c(55, 70), binwidth = 0.1)
```

![plot of chunk ggplot-part4-2](/figure/ggplot-part4-22.png)

```r

# Three views of the distribution of depth and cut.  faceted histogram, a
# conditional density plot, and frequency polygons.  All show an interesting
# pattern: as quality increases, the distribution shifts to the left and
# becomes more symmetric.
depth_dist <- ggplot(diamonds, aes(depth)) + xlim(58, 68)
depth_dist + geom_histogram(aes(y = ..density..), binwidth = 0.1) + facet_grid(cut ~
.)
```

![plot of chunk ggplot-part4-2](/figure/ggplot-part4-23.png)

```r
depth_dist + geom_histogram(aes(fill = cut), binwidth = 0.1, position = "fill")
```

![plot of chunk ggplot-part4-2](/figure/ggplot-part4-24.png)

```r
depth_dist + geom_freqpoly(aes(y = ..density.., colour = cut), binwidth = 0.1)
```

![plot of chunk ggplot-part4-2](/figure/ggplot-part4-25.png)

```r

# The boxplot geom can be use to see the distribution of a continuous
# variable conditional on a discrete varable like cut , or continuous
# variable like carat.  For continuous variables, the group aesthetic must
# be set to get multiple boxplots.
qplot(cut, depth, data = diamonds, geom = "boxplot")
```

![plot of chunk ggplot-part4-2](/figure/ggplot-part4-26.png)

```r
qplot(carat, depth, data = diamonds, geom = "boxplot", group = round_any(carat,
0.1, floor), xlim = c(0, 3))
```

![plot of chunk ggplot-part4-2](/figure/ggplot-part4-27.png)

```r

# The jitter geom can be used to give a crude visualisation of 2d
# distributions with a discrete component.  Generally this works better for
# smaller datasets.  Car class vs. continuous variable city mpg and discrete
# variable drive train.
qplot(class, cty, data = mpg, geom = "jitter")
```

![plot of chunk ggplot-part4-2](/figure/ggplot-part4-28.png)

```r
qplot(class, drv, data = mpg, geom = "jitter")
```

![plot of chunk ggplot-part4-2](/figure/ggplot-part4-29.png)

```r

# The density plot is a smoothed version of the histogram.  It has desirable
# theoretical properties, but is more difficult to relate back to the data.
# A density plot of depth, coloured by cut
qplot(depth, data = diamonds, geom = "density", xlim = c(54, 70))
```

![plot of chunk ggplot-part4-2](/figure/ggplot-part4-210.png)

```r
qplot(depth, data = diamonds, geom = "density", xlim = c(54, 70), fill = cut,
alpha = I(0.2))
```

![plot of chunk ggplot-part4-2](/figure/ggplot-part4-211.png)


#### Dealing with overplotting


```r
df <- data.frame(x = rnorm(2000), y = rnorm(2000))
norm <- ggplot(df, aes(x, y))
# the default shape
norm + geom_point()
```

![plot of chunk ggplot-part4-3](/figure/ggplot-part4-31.png)

```r
# hollow points
norm + geom_point(shape = 1)
```

![plot of chunk ggplot-part4-3](/figure/ggplot-part4-32.png)

```r
# pixel points
norm + geom_point(shape = ".")
```

![plot of chunk ggplot-part4-3](/figure/ggplot-part4-33.png)

```r

# Using alpha blending to alleviate overplotting in sample data from a
# bivariate normal.  Alpha values from left to right: 1/3, 1/5, 1/10.
norm + geom_point(colour = "black", alpha = 1/3)
```

![plot of chunk ggplot-part4-3](/figure/ggplot-part4-34.png)

```r
norm + geom_point(colour = "black", alpha = 1/5)
```

![plot of chunk ggplot-part4-3](/figure/ggplot-part4-35.png)

```r
norm + geom_point(colour = "black", alpha = 1/10)
```

![plot of chunk ggplot-part4-3](/figure/ggplot-part4-36.png)

```r

# A plot of table vs. depth from the diamonds data, showing the use of
# jitter and alpha blending to alleviate overplotting in discrete data.
td <- ggplot(diamonds, aes(table, depth)) + xlim(50, 70) + ylim(50, 70)
# geom point
td + geom_point()
```

![plot of chunk ggplot-part4-3](/figure/ggplot-part4-37.png)

```r
# geom jitter with default jitter
td + geom_jitter()
```

![plot of chunk ggplot-part4-3](/figure/ggplot-part4-38.png)

```r
# geom jitter with horizontal jitter of 0.5 (half the gap between bands)
jit <- position_jitter(width = 0.5)
td + geom_jitter(position = jit)
```

![plot of chunk ggplot-part4-3](/figure/ggplot-part4-39.png)

```r
td + geom_jitter(position = jit, colour = "black", alpha = 1/10)
```

![plot of chunk ggplot-part4-3](/figure/ggplot-part4-310.png)

```r
td + geom_jitter(position = jit, colour = "black", alpha = 1/50)
```

![plot of chunk ggplot-part4-3](/figure/ggplot-part4-311.png)

```r
td + geom_jitter(position = jit, colour = "black", alpha = 1/200)
```

![plot of chunk ggplot-part4-3](/figure/ggplot-part4-312.png)


#### Drawing maps


```r
# Example using the borders function.
library(maps)
data(us.cities)
big_cities <- subset(us.cities, pop > 5e+05)
# All cities with population (as of January 2006) of greater than half a
# million
qplot(long, lat, data = big_cities) + borders("state", size = 0.5)
```

![plot of chunk ggplot-part4-4](/figure/ggplot-part4-41.png)

```r
# cities in Texas.
tx_cities <- subset(us.cities, country.etc == "TX")
ggplot(tx_cities, aes(long, lat)) + borders("county", "texas", colour = "grey70") +
geom_point(colour = "black", alpha = 0.5)
```

![plot of chunk ggplot-part4-4](/figure/ggplot-part4-42.png)

### Further reading
* [ggplot2 part 1](http://felixfan.github.io/ggplot2-book-part-1/)
* [ggplot2 part 2](http://felixfan.github.io/ggplot2-book-part-2/)
* [ggplot2 part 3](http://felixfan.github.io/ggplot2-book-part-3/)
* [ggplot2 part 4](http://felixfan.github.io/ggplot2-book-part-4/)
* [Remove grid and background from plot (ggplot2)](http://felixfan.github.io/ggplot2-remove-grid-background-margin/)
* [Formatting plots for publications (ggplot2)](http://felixfan.github.io/formatting-plots-for-pubs/)
* [ggplot2 book code](http://ggplot2.org/book/)
* [R Cookbook: Graphs](http://www.cookbook-r.com/Graphs/)
