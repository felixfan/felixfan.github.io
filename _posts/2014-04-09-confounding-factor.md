---
title: Confounding factor
layout: post
categories: [Bioinformatics]
tags: [Genetics]
image: /figure
---
{% include JB/setup %}

### 1. Definition

"In statistics, a **confounding variable** (also **confounding factor**, a **confound**, or **confounder**) is an extraneous variable in a statistical model that correlates (directly or inversely) with both the dependent variable and the independent variable. A perceived relationship between an independent variable and a dependent variable that has been misestimated due to the failure to account for a confounding factor is termed a **spurious relationship**, and the presence of misestimation for this reason is termed **omitted-variable bias**." -- [wikipedia](http://en.wikipedia.org/wiki/Confounding)

### 2. Example

Suppose that there is a positive correlation between ice-cream consumption and number of drowning deaths for a given period. An evaluator might attempt to explain this correlation by inferring a causal relationship between the two variables. However, a more likely explanation is that, during the summer, warmer temperatures lead to increased ice-cream consumption as well as more people swimming and thus more drowning deaths. The relationship between ice-cream consumption and drowning is spurious.

### 3. Decreasing the potential for confounding to occur

#### 3.1 Matched variables

"In case-control studies, matched variables most often are the age and sex."

Matching assumes that the risk is evenly distributed in the controlled factor. Such situation is not always the case.

#### 3.2 Stratification

Suppose that age is assumed to be a possible confounder between activity and infarct. Then the association between activity and infarct would be analyzed in each stratified age group. If the stratified age groups  yield much different risk ratios, age must be viewed as a confounding variable.

#### 3.3 Randomization

The study population is divided randomly in order to mitigate the chances of self-selection by participants or bias by the study designers.

### References

* [Confounding wikipedia](http://en.wikipedia.org/wiki/Confounding)
* [What is the best method to deal with confounding? Stratification or matching?](https://www.researchgate.net/post/What_is_the_best_method_to_deal_with_confounding_Stratification_or_matching)
