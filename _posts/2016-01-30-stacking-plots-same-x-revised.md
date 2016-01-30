---
title: Stacking multiple plots vertically with the same X axis but different Y axes --revised
layout: post
categories: [RStudy]
tags: [R, ggplot2, Plot, reshape2]
image: /figure2016
---
{% include JB/setup %}


## 1 download data   


```r
library(FinCal)
require(gridExtra)
library(ggplot2)

dat <- get.ohlc.yahoo('AAPL', '2015-12-01', '2015-12-31')
dat$date <- as.Date(dat$date, "%Y-%m-%d")
dat$volume <- dat$volume/1000000
```

## 2 two different plots   

Use these two options.      

```
axis.text.y = element_text(angle = 90)
xlim(range(dat$date))
```


```r
p1 <- ggplot(dat, aes(date, adjusted)) + geom_line() + 
      theme(
            axis.title.x = element_blank(), 
            axis.text.x = element_blank(),
            axis.text.y = element_text(angle = 90)
            ) +
    xlim(range(dat$date))
p2 <- ggplot(dat,aes(date, volume)) + geom_bar(stat="identity") + 
      theme(
            axis.text.x = element_text(angle=90),
            axis.text.y = element_text(angle = 90)
            ) +
    ylab("volume(millions)") +
    xlim(range(dat$date))

grid.arrange(p1, p2, ncol = 1, heights = c(2, 1))
```

![](/figure2016/stacking_v2_b1-1.png)


```r
p1 <- p1 + theme(plot.margin = unit(c(0, .5, -1.5, 0), "lines"))
p2 <- p2 + theme(plot.margin = unit(c(0, .5, 0, 0), "lines"))
grid.arrange(p1, p2, ncol = 1, heights = c(2, 1))
```

![](/figure2016/stacking_v2_b2-1.png)

