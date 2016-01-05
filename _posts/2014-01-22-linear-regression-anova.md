---
title: Linear regression and ANOVA are the Same Analysis?!
layout: post
categories: [Statistics]
tags: [R,Statistics]
image: /figure
---
{% include JB/setup %}

When I tried to find out the difference between ANOVA and linear Regression, I got this interesting post: [Why ANOVA and Linear Regression are the Same Analysis](http://www.theanalysisfactor.com/why-anova-and-linear-regression-are-the-same-analysis/).

The author used data [employment.sav](https://dl.dropboxusercontent.com/u/8272421/stat/employee.sav) to show why.

I tried both ANOVA and linear Regression using the same data with R *lm* and *aov*/*anova* functions. Not surprisely, I got the same results.

Actually, the description of *aov* is "Fit an analysis of variance model by a call to *lm* for each stratum."

[employee.csv](https://dl.dropboxusercontent.com/u/8272421/stat/employee.csv) is the same data as [employment.sav](https://dl.dropboxusercontent.com/u/8272421/stat/employee.sav) with csv format.


```r
require(RCurl)
```

```
Loading required package: RCurl
Loading required package: bitops
```

```r
myCsv <- getURL("https://dl.dropboxusercontent.com/u/8272421/stat/employee.csv",
ssl.verifypeer = FALSE)
mydata <- read.csv(textConnection(myCsv))
head(mydata)
```

```
id gender     bdate educ jobcat salary salbegin jobtime prevexp minority
1  1      m  2/3/1952   15      3  57000    27000      98     144        0
2  2      m 5/23/1958   16      1  40200    18750      98      36        0
3  3      f 7/26/1929   12      1  21450    12000      98     381        0
4  4      f 4/15/1947    8      1  21900    13200      98     190        0
5  5      m  2/9/1955   15      1  45000    21000      98     138        0
6  6      m 8/22/1958   15      1  32100    13500      98      67        0
```

```r
mydata$jobcat = gsub(1, "Clerical", mydata$jobcat)
mydata$jobcat = gsub(2, "Custodial", mydata$jobcat)
mydata$jobcat = gsub(3, "Manager", mydata$jobcat)
```



```r
library(plyr)
ddply(mydata, .(jobcat), summarize, mean_prevexp = mean(prevexp))
```

```
jobcat mean_prevexp
1  Clerical        85.04
2 Custodial       298.11
3   Manager        77.62
```



```r
lm0 <- lm(prevexp ~ jobcat, data = mydata)
lm0
```

```

Call:
lm(formula = prevexp ~ jobcat, data = mydata)

Coefficients:
(Intercept)  jobcatCustodial    jobcatManager
85.04           213.07            -7.42
```

```r

aov0 <- aov(prevexp ~ jobcat, data = mydata)
aov0
```

```
Call:
aov(formula = prevexp ~ jobcat, data = mydata)

Terms:
jobcat Residuals
Sum of Squares  1174907   3998900
Deg. of Freedom       2       471

Residual standard error: 92.14
Estimated effects may be unbalanced
```



```r
summary(lm0)
```

```

Call:
lm(formula = prevexp ~ jobcat, data = mydata)

Residuals:
Min     1Q Median     3Q    Max
-154.1  -65.0  -32.0   36.7  391.0

Coefficients:
Estimate Std. Error t value Pr(>|t|)
(Intercept)        85.04       4.84   17.58   <2e-16 ***
jobcatCustodial   213.07      18.38   11.59   <2e-16 ***
jobcatManager      -7.42      11.16   -0.67     0.51
---
{% include JB/setup %}
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

Residual standard error: 92.1 on 471 degrees of freedom
Multiple R-squared:  0.227,	Adjusted R-squared:  0.224
F-statistic: 69.2 on 2 and 471 DF,  p-value: <2e-16
```

```r
anova(lm0)
```

```
Analysis of Variance Table

Response: prevexp
Df  Sum Sq Mean Sq F value Pr(>F)
jobcat      2 1174907  587453    69.2 <2e-16 ***
Residuals 471 3998900    8490
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
```

```r
summary(aov0)
```

```
Df  Sum Sq Mean Sq F value Pr(>F)
jobcat        2 1174907  587453    69.2 <2e-16 ***
Residuals   471 3998900    8490
---
{% include JB/setup %}
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
```


what is the difference between anova and aov in R?

* input format: anova use the object as input, that means you need input the lm(); but aov use the formula as input.
* output: output is slightly different as the examples demostrated.


