---
title: Aesthetic mappings and setting of ggplot2
layout: post
categories: [RStudy]
tags: [R, ggplot2, Plot]
image: /figure2016
---
{% include JB/setup %}


```r
library(ggplot2)
```

## 1. Setting vs. mapping

### 1.1 sets the colour of the points to a constant, using the colour parameter of the layer


```r
p <- ggplot(mtcars, aes(mpg, wt))
p + geom_point(colour = "darkblue")
```

![](/figure2016/mapset1-1.png)

### 1.2 maps an aesthetic to a variable


```r
p + geom_point(aes(colour = factor(cyl)))
```

![](/figure2016/mapset2-1.png)

### 1.3 maps the colour to the value "darkblue"

```
"This effiectively creates a new variable containing only the value "darkblue" and 
then maps colour to that new variable. Because this value is discrete, the default
colour scale uses evenly spaced colours on the colour wheel, and since there is 
only one value this colour is pinkish."
```


```r
p + geom_point(aes(colour = "darkblue"))
```

![](/figure2016/mapset3-1.png)
