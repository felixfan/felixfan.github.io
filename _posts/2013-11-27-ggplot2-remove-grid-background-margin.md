---
title: Remove grid and background from plot (ggplot2)
layout: post
categories: [RStudy]
tags: [R,Plot,ggplot2]
image: /figure
---
{% include JB/setup %}

#### Generate data


```r
library(ggplot2)
a <- seq(1, 20)
b <- a^0.25
df <- as.data.frame(cbind(a, b))
```


#### basic plot


```r
myplot = ggplot(df, aes(x = a, y = b)) + geom_point()
myplot
```

![plot of chunk ggplot-2-1](/figure/ggplot-2-1.png)


#### theme_bw() will get rid of the background


```r
myplot + theme_bw()
```

![plot of chunk ggplot-2-2](/figure/ggplot-2-2.png)


#### remove grid (does not remove backgroud colour and border lines)


```r
myplot + theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank())
```

![plot of chunk ggplot-2-3](/figure/ggplot-2-3.png)


#### remove border lines (does not remove backgroud colour and grid lines)


```r
myplot + theme(panel.border = element_blank())
```

![plot of chunk ggplot-2-4](/figure/ggplot-2-4.png)


#### remove background (remove backgroud colour and border lines, but does not remove grid lines)


```r
myplot + theme(panel.background = element_blank())
```

![plot of chunk ggplot-2-5](/figure/ggplot-2-5.png)


#### add axis line


```r
myplot + theme(axis.line = element_line(colour = "black"))
```

![plot of chunk ggplot-2-6](/figure/ggplot-2-6.png)


#### put all together - method 1


```r
myplot + theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank(),
panel.background = element_blank(), axis.line = element_line(colour = "black"))
```

![plot of chunk ggplot-2-8](/figure/ggplot-2-7.png)


#### put all together - method 2


```r
myplot + theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
panel.grid.minor = element_blank(), axis.line = element_line(colour = "black"))
```

![plot of chunk ggplot-2-9](/figure/ggplot-2-8.png)



#### Further reading

[remove grid, background color and top and right borders from ggplot2](http://stackoverflow.com/questions/10861773/remove-grid-background-color-and-top-and-right-borders-from-ggplot2)

