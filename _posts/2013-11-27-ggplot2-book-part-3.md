---
title: ggplot2 part 3
layout: post
categories: [RStudy]
tags: [R,Plot,ggplot2]
image: /figure
---

### Build a plot layer by layer

#### Layers


```r
library(ggplot2)
data(Oxboys, package = "nlme")
diamonds = na.omit(diamonds)
msleep = na.omit(msleep)
mtcars = na.omit(mtcars)
Oxboys = na.omit(Oxboys)
p <- ggplot(diamonds, aes(carat, price, colour = cut))
# This plot object cannot be displayed until we add a layer
p <- p + layer(geom = "point")
p
```

![plot of chunk ggplot-part3-1](/figure/ggplot-part3-11.png) 

```r

# Here is what a more complicated call looks like.  It produces a histogram
# coloured “steelblue” with a bin width of 2 histogram is a combination of
# bars and binning
p <- ggplot(diamonds, aes(x = carat))
p <- p + layer(geom = "bar", geom_params = list(fill = "steelblue"), stat = "bin", 
    stat_params = list(binwidth = 2))
p
```

![plot of chunk ggplot-part3-1](/figure/ggplot-part3-12.png) 



```r
# same as the following command
ggplot(diamonds, aes(x = carat)) + geom_histogram(binwidth = 2, fill = "steelblue")

# The following example shows the equivalence between these two ways of
# making plots

ggplot(msleep, aes(sleep_rem/sleep_total, awake)) + geom_point()
# which is equivalent to
qplot(sleep_rem/sleep_total, awake, data = msleep)

# You can add layers to qplot too:
qplot(sleep_rem/sleep_total, awake, data = msleep) + geom_smooth()
# This is equivalent to
qplot(sleep_rem/sleep_total, awake, data = msleep, geom = c("point", "smooth"))
# or
ggplot(msleep, aes(sleep_rem/sleep_total, awake)) + geom_point() + geom_smooth()
```



```r
# plot objects can be stored as variables. The summary function can be
# helpful for inspecting the structure of a plot without plotting it
p <- ggplot(msleep, aes(sleep_rem/sleep_total, awake))
summary(p)
```

```
data: name, genus, vore, order, conservation, sleep_total,
  sleep_rem, sleep_cycle, awake, brainwt, bodywt [20x11]
mapping:  x = sleep_rem/sleep_total, y = awake
faceting: facet_null() 
```

```r
p <- p + geom_point()
summary(p)
```

```
data: name, genus, vore, order, conservation, sleep_total,
  sleep_rem, sleep_cycle, awake, brainwt, bodywt [20x11]
mapping:  x = sleep_rem/sleep_total, y = awake
faceting: facet_null() 
-----------------------------------
geom_point: na.rm = FALSE 
stat_identity:  
position_identity: (width = NULL, height = NULL)
```

```r

# a set of plots can be initialised using different data then enhanced with
# the same layer

bestfit <- geom_smooth(method = "lm", se = F, colour = "steelblue", alpha = 0.5, 
    size = 2)

qplot(sleep_rem, sleep_total, data = msleep) + bestfit
```

![plot of chunk ggplot-part3-2](/figure/ggplot-part3-21.png) 

```r
qplot(awake, brainwt, data = msleep, log = "y") + bestfit
```

![plot of chunk ggplot-part3-2](/figure/ggplot-part3-22.png) 

```r
qplot(bodywt, brainwt, data = msleep, log = "xy") + bestfit
```

![plot of chunk ggplot-part3-2](/figure/ggplot-part3-23.png) 


#### Data


```r
# You can replace the old dataset with %+%
p <- ggplot(mtcars, aes(mpg, wt, colour = cyl)) + geom_point()
p
```

![plot of chunk ggplot-part3-3](/figure/ggplot-part3-31.png) 

```r
mtcars <- transform(mtcars, mpg = mpg^2)
p %+% mtcars
```

![plot of chunk ggplot-part3-3](/figure/ggplot-part3-32.png) 


#### Aesthetic mappings

##### Plots and layers


```r
# The **aes** function takes a list of aesthetic-variable pairs aes(x =
# weight, y = height, colour = age)
p <- ggplot(mtcars, aes(x = mpg, y = wt))
p + geom_point()
```

![plot of chunk ggplot-part3-4](/figure/ggplot-part3-41.png) 

```r

# Overriding aesthetics.
p + geom_point(aes(colour = factor(cyl)))
```

![plot of chunk ggplot-part3-4](/figure/ggplot-part3-42.png) 

```r
# overriding y-position (now y is 'disp',although the y lab is still 'wt')
p + geom_point(aes(y = disp))
```

![plot of chunk ggplot-part3-4](/figure/ggplot-part3-43.png) 


##### Setting vs. mapping


```r
# The difference between setting colour to 'darkblue' and mapping colour to
# 'darkblue'.
p <- ggplot(mtcars, aes(mpg, wt))
p + geom_point(colour = "darkblue")  # setting 
```

![plot of chunk ggplot-part3-5](/figure/ggplot-part3-51.png) 

```r
# This sets the point colour to be dark blue instead of black. This is quite
# different than
p + geom_point(aes(colour = "darkblue"))  # mapping
```

![plot of chunk ggplot-part3-5](/figure/ggplot-part3-52.png) 



```r
# qplot
qplot(mpg, wt, data = mtcars, colour = I("darkblue"))  # setting
qplot(mpg, wt, data = mtcars, colour = "darkblue")  # mapping
```


##### Grouping

###### Multiple groups, one aesthetic


```r
# Correctly specifying produces one line per subject.
p <- ggplot(Oxboys, aes(age, height, group = Subject)) + geom_line()
p
```

![plot of chunk ggplot-part3-6](/figure/ggplot-part3-6.png) 



```r
qplot(age, height, data = Oxboys, group = Subject, geom = "line")
```



```r
# A single line connects all observations.  This pattern is characteristic
# of an **incorrect** grouping aesthetic, and is what we see if the group
# aesthetic is omitted, which in this case is equivalent to group = 1
ggplot(Oxboys, aes(age, height, group = 1)) + geom_line()
```

![plot of chunk ggplot-part3-7](/figure/ggplot-part3-7.png) 



```r
qplot(age, height, data = Oxboys, geom = "line")
```


###### Different groups on different layers


```r
# Adding smooths to the Oxboys data. Using the same grouping as the lines
# results in a line of best fit for each boy.
p + geom_smooth(aes(group = Subject), method = "lm", se = F)
```

![plot of chunk ggplot-part3-8](/figure/ggplot-part3-8.png) 



```r
# or
qplot(age, height, data = Oxboys, group = Subject, geom = "line") + geom_smooth(method = "lm", 
    se = F)
```



```r
# Using aes(group = 1) in the smooth layer fits a single line of best fit
# across all boys.
p + geom_smooth(aes(group = 1), method = "lm", size = 2, se = F)
```

![plot of chunk ggplot-part3-9](/figure/ggplot-part3-9.png) 



```r
qplot(age, height, data = Oxboys, group = Subject, geom = "line") + geom_smooth(aes(group = 1), 
    method = "lm", size = 2, se = F)
```

### Further reading
* [ggplot2 part 1](http://felixfan.github.io/rstudy/2013/11/27/ggplot2-book-part-1/)
* [ggplot2 part 2](http://felixfan.github.io/rstudy/2013/11/27/ggplot2-book-part-2/)
* [ggplot2 part 3](http://felixfan.github.io/rstudy/2013/11/27/ggplot2-book-part-3/)
* [ggplot2 part 4](http://felixfan.github.io/rstudy/2013/11/27/ggplot2-book-part-4/)
* [Remove grid and background from plot (ggplot2)](http://felixfan.github.io/rstudy/2013/11/27/ggplot2-remove-grid-background-margin/)
* [Formatting plots for publications (ggplot2)](http://felixfan.github.io/rstudy/2013/11/27/formatting-plots-for-pubs/)
* [ggplot2 book code](http://ggplot2.org/book/)
* [R Cookbook: Graphs](http://www.cookbook-r.com/Graphs/)
