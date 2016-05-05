---
title: Survival analysis - Kaplan-Meier Curve
layout: post
categories: [Bioinformatics]
tags: [SurvivalAnalysis]
image: /figure2016
---

{% include JB/setup %}



# NCCTG Lung Cancer Data

Description: Survival in patients with advanced lung cancer from the North Central Cancer Treatment Group.  Performance scores rate how well the patient can perform usual daily activities.


```r
library(survival)
data(lung)
head(lung)
```

```
  inst time status age sex ph.ecog ph.karno pat.karno meal.cal wt.loss
1    3  306      2  74   1       1       90       100     1175      NA
2    3  455      2  68   1       0       90        90     1225      15
3    3 1010      1  56   1       0       90        90       NA      15
4    5  210      2  57   1       1       90        60     1150      11
5    1  883      2  60   1       0      100        90       NA       0
6   12 1022      1  74   1       1       50        80      513       0
```

```
inst:       Institution code
time:       Survival time in days
status:     censoring status 1=censored, 2=dead
age:        Age in years
sex:        Male=1 Female=2
ph.ecog:    ECOG performance score (0=good 5=dead)
ph.karno:   Karnofsky performance score (bad=0-good=100) rated by physician
pat.karno:  Karnofsky performance score as rated by patient
meal.cal:   Calories consumed at meals
wt.loss:    Weight loss in last six months
```
# Kaplan-Meier Analysis

## Estimate survival-function

### Global Estimate


```r
km.as.one <- survfit(Surv(time, status) ~ 1,  
                     type="kaplan-meier", 
                     conf.type="log", 
                     data=lung)
```

### separate estimate for all sex


```r
km.by.sex <- survfit(Surv(time, status) ~ sex,  
                     type="kaplan-meier", 
                     conf.type="log", data=lung)
```

## Plot estimated survival function


```r
plot(km.as.one, main="Kaplan-Meier estimate with CI", 
     xlab="Survival time in days", 
     ylab="Survival probability", lwd=2)
```

![](/figure2016/km1-1.png)


```r
plot(km.by.sex, main="Kaplan-Meier estimate by sex", 
     xlab="Survival time in days", 
     ylab="Survival probability", 
     lwd=2, col = c("red","blue"))
legend(x="topright", col=c("red","blue"), lwd=2, 
       legend=c("male","female"))
```

![](/figure2016/km2-1.png)

## Plot cumulative incidence function


```r
plot(km.by.sex, main="Kaplan-Meier cumulative incidence by sex", 
     xlab="Survival time in days", ylab="Cumulative incidence", 
     lwd=2, col = c("red","blue"),
     fun = function(x){1-x})
legend(x="bottomright", col=c("red","blue"), 
       lwd=2, legend=c("male","female"))
```

![](/figure2016/km3-1.png)

## Plot cumulative hazard


```r
plot(km.as.one, main="Kaplan-Meier estimate", 
     xlab="Survival time in days", 
     ylab="Cumulative hazard", lwd=2,
     fun="cumhaz")
```

![](/figure2016/km4-1.png)

## Log-rank-test for equal survival-functions

With rho = 0 (default) this is the log-rank or Mantel-Haenszel test, and with rho = 1 it is equivalent to the Peto & Peto modification of the Gehan-Wilcoxon test.


```r
survdiff(Surv(time, status) ~ sex, data=lung)
```

```
Call:
survdiff(formula = Surv(time, status) ~ sex, data = lung)

        N Observed Expected (O-E)^2/E (O-E)^2/V
sex=1 138      112     91.6      4.55      10.3
sex=2  90       53     73.4      5.68      10.3

 Chisq= 10.3  on 1 degrees of freedom, p= 0.00131 
```

# References

* [http://www.ats.ucla.edu/stat/r/examples/asa/asa_ch2_r.htm](http://www.ats.ucla.edu/stat/r/examples/asa/asa_ch2_r.htm)
* [http://rstudio-pubs-static.s3.amazonaws.com/5588_72eb65bfbe0a4cb7b655d2eee0751584.html](http://rstudio-pubs-static.s3.amazonaws.com/5588_72eb65bfbe0a4cb7b655d2eee0751584.html)

