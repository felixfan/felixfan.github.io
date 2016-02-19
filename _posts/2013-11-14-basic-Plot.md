---
title: Bar plot, pie chart, histgrams and density plot, Scatterplots
layout: post
categories: [RStudy]
tags: [R,Plot]
image: /figure
---

{% include JB/setup %}

### Bar plot

#### Simple Bar Plot


```r
counts <- table(mtcars$gear)
barplot(counts, main = "Car Distribution", xlab = "Number of Gears")
```

![plot of chunk basicplot1](/figure/basicplot1.png)


#### Simple Horizontal Bar Plot with Added Labels


```r
barplot(counts, main = "Car Distribution", horiz = TRUE, names.arg = c("3 Gears",
"4 Gears", "5 Gears"))
```

![plot of chunk basicplot2](/figure/basicplot2.png)


#### Stacked Bar Plot


```r
counts <- table(mtcars$vs, mtcars$gear)
barplot(counts, main = "Car Distribution by Gears and VS", xlab = "Number of Gears",
col = c("darkblue", "red"), legend = rownames(counts))
```

![plot of chunk basicplot3](/figure/basicplot3.png)


#### Grouped Bar Plot


```r
barplot(counts, main = "Car Distribution by Gears and VS", xlab = "Number of Gears",
col = c("darkblue", "red"), legend = rownames(counts), beside = TRUE)
```

![plot of chunk basicplot4](/figure/basicplot4.png)


### Pie Charts

#### Simple Pie Chart


```r
slices <- c(10, 12, 4, 16, 8)
lbls <- c("US", "UK", "Australia", "Germany", "France")
pie(slices, labels = lbls, main = "Pie Chart of Countries")
```

![plot of chunk basicplot5](/figure/basicplot5.png)


#### Pie Chart with Annotated Percentages


```r
pct <- round(slices/sum(slices) * 100)
lbls <- paste(lbls, pct)  # add percents to labels
lbls <- paste(lbls, "%", sep = "")  # ad % to labels
pie(slices, labels = lbls, col = rainbow(length(lbls)), main = "Pie Chart of Countries")
```

![plot of chunk basicplot6](/figure/basicplot6.png)


#### 3D Pie Chart


```r
library(plotrix)
slices <- c(10, 12, 4, 16, 8)
lbls <- c("US", "UK", "Australia", "Germany", "France")
pie3D(slices, labels = lbls, explode = 0.1, main = "Pie Chart of Countries ")
```

![plot of chunk basicplot7](/figure/basicplot7.png)


### Scatterplots

#### Simple Scatterplot


```r
plot(mtcars$wt, mtcars$mpg, main = "Scatterplot Example", xlab = "Car Weight ",
ylab = "Miles Per Gallon ", pch = 19)
```

![plot of chunk basicplot8](/figure/basicplot8.png)


#### Add fit lines


```r
attach(mtcars)
plot(wt, mpg, main = "Scatterplot Example", xlab = "Car Weight ", ylab = "Miles Per Gallon ",
pch = 19)
abline(lm(mpg ~ wt), col = "red")  # regression line (y~x)
lines(lowess(wt, mpg), col = "blue")  # lowess line (x,y)
```

![plot of chunk basicplot9](/figure/basicplot9.png)


### Scatterplot Matrices


#### Basic Scatterplot Matrix


```r
pairs(~mpg + disp + drat + wt, data = mtcars, main = "Simple Scatterplot Matrix")
```

![plot of chunk basicplot10](/figure/basicplot10.png)


#### Scatterplot Matrices from the lattice Package

The lattice package provides options to condition the scatterplot matrix on a factor.


```r
library(lattice)
super.sym <- trellis.par.get("superpose.symbol")
splom(mtcars[c(1, 3, 5, 6)], groups = cyl, data = mtcars, panel = panel.superpose,
key = list(title = "Three Cylinder Options", columns = 3, points = list(pch = super.sym$pch[1:3],
col = super.sym$col[1:3]), text = list(c("4 Cylinder", "6 Cylinder",
"8 Cylinder"))))
```

![plot of chunk basicplot11](/figure/basicplot11.png)


#### Scatterplot Matrices from the car Package

The car package can condition the scatterplot matrix on a factor, and optionally include lowess and linear best fit lines, and boxplot, densities, or histograms in the principal diagonal, as well as rug plots in the margins of the cells.


```r
library(car)
scatterplot.matrix(~mpg + disp + drat + wt | cyl, data = mtcars, main = "Three Cylinder Options")
```

![plot of chunk basicplot12](/figure/basicplot12.png)


#### Scatterplot Matrices from the glus Package

The gclus package provides options to rearrange the variables so that those with higher correlations are closer to the principal diagonal. It can also color code the cells to reflect the size of the correlations.


```r
library(gclus)
dta <- mtcars[c(1, 3, 5, 6)]  # get data
dta.r <- abs(cor(dta))  # get correlations
dta.col <- dmat.color(dta.r)  # get colors
# reorder variables so those with highest correlation are closest to the
# diagonal
dta.o <- order.single(dta.r)
cpairs(dta, dta.o, panel.colors = dta.col, gap = 0.5, main = "Variables Ordered and Colored by Correlation")
```

![plot of chunk basicplot13](/figure/basicplot13.png)


### Histograms

#### Simple Histogram


```r
hist(mtcars$mpg)
```

![plot of chunk basicplot14](/figure/basicplot14.png)


#### Colored Histogram with Different Number of Bins


```r
hist(mtcars$mpg, breaks = 12, col = "red")
```

![plot of chunk basicplot15](/figure/basicplot15.png)


#### Add a Normal Curve


```r
x <- mtcars$mpg
h <- hist(x, breaks = 10, col = "red", xlab = "Miles Per Gallon", main = "Histogram with Normal Curve")
xfit <- seq(min(x), max(x), length = 40)
yfit <- dnorm(xfit, mean = mean(x), sd = sd(x))
yfit <- yfit * diff(h$mids[1:2]) * length(x)
lines(xfit, yfit, col = "blue", lwd = 2)
```

![plot of chunk basicplot16](/figure/basicplot16.png)


### Kernel Density Plots

Kernal density plots are usually a much more effective way to view the distribution of a variable. Create the plot using plot(density(x)) where x is a numeric vector.

#### simple Kernel Density Plot


```r
plot(density(mtcars$mpg))
```

![plot of chunk basicplot17](/figure/basicplot17.png)


#### Filled Density Plot


```r
d <- density(mtcars$mpg)
plot(d, main = "Kernel Density of Miles Per Gallon")
polygon(d, col = "red", border = "blue")
```

![plot of chunk basicplot18](/figure/basicplot18.png)


### par()

xaxt="n" will suppresses plotting of the axis


```r
# par() # view current settings
opar <- par()  # make a copy of current settings
par(col.lab = "red")  # red x and y labels
hist(mtcars$mpg)  # create a plot with these new settings
```

![plot of chunk basicplot20](/figure/basicplot20.png)

```r
par(opar)  # restore original settings
```


### text() and mtext()

text() places text within the graph while mtext() places text in one of the four margins.


```r
# attach(mtcars)
plot(wt, mpg, main = "Milage vs. Car Weight", xlab = "Weight", ylab = "Mileage",
pch = 18, col = "blue")
text(wt, mpg, row.names(mtcars), cex = 0.6, pos = 4, col = "red")
```

![plot of chunk basicplot21](/figure/basicplot21.png)


### combine figures


```r
par(mfrow = c(2, 2))
plot(wt, mpg, main = "Scatterplot of wt vs. mpg")
plot(wt, disp, main = "Scatterplot of wt vs disp")
hist(wt, main = "Histogram of wt")
boxplot(wt, main = "Boxplot of wt")
```

![plot of chunk basicplot22](/figure/basicplot22.png)



```r
# One figure in row 1 and two figures in row 2 row 1 is 1/3 the height of
# row 2 column 2 is 1/4 the width of the column 1
layout(matrix(c(1, 1, 2, 3), 2, 2, byrow = TRUE), widths = c(3, 1), heights = c(1,
2))
hist(wt)
hist(mpg)
hist(disp)
```

![plot of chunk basicplot23](/figure/basicplot23.png)



```r
# Add boxplots to a scatterplot
par(fig = c(0, 0.8, 0, 0.8), new = TRUE)
plot(mtcars$wt, mtcars$mpg, xlab = "Miles Per Gallon", ylab = "Car Weight")
par(fig = c(0, 0.8, 0.55, 1), new = TRUE)
boxplot(mtcars$wt, horizontal = TRUE, axes = FALSE)
par(fig = c(0.65, 1, 0, 0.8), new = TRUE)
boxplot(mtcars$mpg, axes = FALSE)
mtext("Enhanced Scatterplot", side = 3, outer = TRUE, line = -3)
```

![plot of chunk basicplot24](/figure/basicplot24.png)


To understand this graph, think of the full graph area as going from (0,0) in the lower left corner to (1,1) in the upper right corner. The format of the fig= parameter is a numerical vector of the form c(x1, x2, y1, y2). The first fig= sets up the scatterplot going from 0 to 0.8 on the x axis and 0 to 0.8 on the y axis. The top boxplot goes from 0 to 0.8 on the x axis and 0.55 to 1 on the y axis. I chose 0.55 rather than 0.8 so that the top figure will be pulled closer to the scatter plot. The right hand boxplot goes from 0.65 to 1 on the x axis and 0 to 0.8 on the y axis. Again, I chose a value to pull the right hand boxplot closer to the scatterplot. You have to experiment to get it just right.

### legend()


```r
# attach(mtcars)
boxplot(mpg ~ cyl, main = "Milage by Car Weight", yaxt = "n", xlab = "Milage",
horizontal = TRUE, col = terrain.colors(3))
legend("topright", inset = 0.05, title = "Number of Cylinders", c("4", "6",
"8"), fill = terrain.colors(3), horiz = TRUE)
```

![plot of chunk basicplot19](/figure/basicplot19.png)


### Further reading       
[Quick-R: Basic Graphs](http://www.statmethods.net/graphs/)        


