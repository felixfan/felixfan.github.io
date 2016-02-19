---
title: Extract R code from Rmd document
layout: post
categories: [RStudy]
tags: [R,kintr]
image: /figure
---

{% include JB/setup %}

```r
library(knitr)
```


### Extract R code only


```r
purl("test.Rmd")
```

```


processing file: test.Rmd
```

```
|                                                                       
  |                                                                 |   0%
  |                                                                       
  |.................................................................| 100%
```

```
output file: test.R
```

```
[1] "test.R"
```


###  Extract R code and also include documentation


```r
purl("test.Rmd", output = "test2.R", documentation = 2)
```

```


processing file: test.Rmd
```

```
|                                                                       
  |                                                                 |   0%
  |                                                                       
  |.................................................................| 100%
```

```
output file: test2.R
```

```
[1] "test2.R"
```

