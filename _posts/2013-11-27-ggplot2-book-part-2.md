---
title: ggplot2 part 2
layout: post
categories: [RStudy]
tags: [R,Plot,ggplot2]
image: /figure
---
{% include JB/setup %}

### Mastering the grammar


```r
library(ggplot2)
mpg = na.omit(mpg)
# The fuel economy dataset, mpg, records make, model, class, engine size,
# transmission and fuel economy for a selection of US cars in 1999 and 2008

# A scatterplot of engine displacement in litres (displ) vs.  average
# highway miles per gallon (hwy).  # Points are coloured according to number
# of cylinders.  This plot summarises the most important factor governing
# fuel economy: engine size.
qplot(displ, hwy, data = mpg, colour = factor(cyl))
```

![plot of chunk ggplot2-part2-1](/figure/ggplot2-part2-11.png)

```r

# Instead of using points to represent the data, we could use other geoms
# like lines (left) or bars (right).  Neither of these geoms makes sense for
# this data, but they are still grammatically valid.
qplot(displ, hwy, data = mpg, colour = factor(cyl), geom = "line") + theme(legend.position = "none")
```

![plot of chunk ggplot2-part2-1](/figure/ggplot2-part2-12.png)

```r
qplot(displ, hwy, data = mpg, colour = factor(cyl), geom = "bar", stat = "identity",
position = "identity") + theme(legend.position = "none")
```

![plot of chunk ggplot2-part2-1](/figure/ggplot2-part2-13.png)

```r

# More complicated plots don't have their own names. This plot overlays a
# per group regression line on the existing plot.  What would you call this
# plot?
qplot(displ, hwy, data = mpg, colour = factor(cyl)) + geom_smooth(data = subset(mpg,
cyl != 5), method = "lm")
```

![plot of chunk ggplot2-part2-1](/figure/ggplot2-part2-14.png)

```r

# A more complex plot with facets and multiple layers.
qplot(displ, hwy, data = mpg, facets = . ~ year) + geom_smooth()
```

![plot of chunk ggplot2-part2-1](/figure/ggplot2-part2-15.png)

```r

# Examples of legends from four different scales.  continuous variable
# mapped to size, and to colour, discrete variable mapped to shape, and to
# colour.  The ordering of scales seems upside-down, but this matches the
# labelling of the $y$-axis: small values occur at the bottom.
x <- 1:10
y <- factor(letters[1:5])
qplot(x, x, size = x)
```

![plot of chunk ggplot2-part2-1](/figure/ggplot2-part2-16.png)

```r
qplot(x, x, 1:10, colour = x)
```

![plot of chunk ggplot2-part2-1](/figure/ggplot2-part2-17.png)

```r
qplot(y, y, 1:10, shape = y)
```

![plot of chunk ggplot2-part2-1](/figure/ggplot2-part2-18.png)

```r
qplot(y, y, 1:10, colour = y)
```

![plot of chunk ggplot2-part2-1](/figure/ggplot2-part2-19.png)

```r

# Examples of axes and grid lines for three coordinate systems: Cartesian,
# semi-log and polar.  The polar coordinate system illustrates the
# difficulties associated with non-Cartesian coordinates: it is hard to draw
# the axes well.
x1 <- c(1, 10)
y1 <- c(1, 5)
p <- qplot(x1, y1, geom = "blank", xlab = NULL, ylab = NULL) + theme_bw()
p
```

![plot of chunk ggplot2-part2-1](/figure/ggplot2-part2-110.png)

```r
p + coord_trans(y = "log10")
```

![plot of chunk ggplot2-part2-1](/figure/ggplot2-part2-111.png)

```r
p + coord_polar()
```

![plot of chunk ggplot2-part2-1](/figure/ggplot2-part2-112.png)

```r

p <- qplot(displ, hwy, data = mpg, colour = factor(cyl))
summary(p)
```

```
data: manufacturer, model, displ, year, cyl, trans, drv, cty, hwy,
fl, class [234x11]
mapping:  colour = factor(cyl), x = displ, y = hwy
faceting: facet_null()
-----------------------------------
geom_point:
stat_identity:
position_identity: (width = NULL, height = NULL)
```



```r
# Save plot object to disk
save(p, file = "plot.rdata")
# Load from disk
load("plot.rdata")
# Save png to disk
ggsave("plot.png", width = 5, height = 5)
```

### Further reading
* [ggplot2 part 1](http://felixfan.github.io/ggplot2-book-part-1/)
* [ggplot2 part 2](http://felixfan.github.io/ggplot2-book-part-2/)
* [ggplot2 part 3](http://felixfan.github.io/ggplot2-book-part-3/)
* [ggplot2 part 4](http://felixfan.github.io/ggplot2-book-part-4/)
* [Remove grid and background from plot (ggplot2)](http://felixfan.github.io/ggplot2-remove-grid-background-margin/)
* [Formatting plots for publications (ggplot2)](http://felixfan.github.io/formatting-plots-for-pubs/)
* [ggplot2 book code](http://ggplot2.org/book/)
* [R Cookbook: Graphs](http://www.cookbook-r.com/Graphs/)
