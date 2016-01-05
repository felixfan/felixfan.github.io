---
title: data.table outperforms other methods
layout: post
categories: [RStudy]
tags: [R, data.table]
image: /figure
---
{% include JB/setup %}

#### {data.table} outperforms other methods


```r
library(data.table)
fread("data.csv", header = T, sep = ",")
```


##### Data used

size of csv file: 689.4MB (7,009,728 rows * 29 columns)

##### Methods tested

* read.csv
* fread {data.table}
* read.big.matrix {bigmemory}
* read.csv.ffdf {ff}
* read.csv.sql {sqldf}

**Details** are available at the [original post](http://statcompute.wordpress.com/2014/02/11/efficiency-of-importing-large-csv-files-in-r/)

