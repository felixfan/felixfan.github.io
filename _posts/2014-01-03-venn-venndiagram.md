---
title: Make a Venn Diagram using {VennDiagram}
layout: post
categories: [RStudy]
tags: [R,Venn]
image: /figure
---
{% include JB/setup %}

```r
library(VennDiagram)
```

```
## Loading required package: grid
```

```r

set.seed(99999)

## construct some fake gene names..
oneName <- function() paste(sample(LETTERS, 5, replace = TRUE), collapse = "")
geneNames <- replicate(1000, oneName())

##
GroupA <- sample(geneNames, 400, replace = FALSE)
GroupB <- sample(geneNames, 750, replace = FALSE)
GroupC <- sample(geneNames, 250, replace = FALSE)
GroupD <- sample(geneNames, 300, replace = FALSE)
input <- list(GA = GroupA, GB = GroupB, GC = GroupC, GD = GroupD)
filename = "Venn_4set_pretty.png"
venn.diagram(input, filename = filename, fill = c("cornflowerblue", "green",
"yellow", "red"), height = 900, width = 900, resolution = 500, units = "px",
cex = 0.8)
```

The output is a TIFF format figure.

![](/figure/Venn_4set_pretty.jpg)
