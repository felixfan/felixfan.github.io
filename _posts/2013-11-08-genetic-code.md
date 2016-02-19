---
title: Genetic code plot
layout: post
categories: [Bioinformatics]
tags: [Genetics]
image: /figure
---
{% include JB/setup %}


### Basic functions


```r
plotCircle <- function(diameter = 1, polygonCol = "white", plotCol = "black",
npoints = 1000) {
r = diameter/2
temp <- seq(0, 2 * pi, length.out = npoints)
x <- r * cos(temp)
y <- r * sin(temp)
dat <- (data.frame(x = x, y = y))
plot(dat$x, dat$y, type = "l", col = plotCol, xaxt = "n", yaxt = "n", xlab = "",
ylab = "", frame.plot = FALSE)
polygon(dat$x, dat$y, col = polygonCol)
}

addCircle <- function(diameter = 1, polygonCol = "white", plotCol = "black",
npoints = 1000) {
r = diameter/2
temp <- seq(0, 2 * pi, length.out = npoints)
x <- r * cos(temp)
y <- r * sin(temp)
dat <- (data.frame(x = x, y = y))
points(dat$x, dat$y, type = "l", col = plotCol)
polygon(dat$x, dat$y, col = polygonCol)
}

addLines <- function(diameter = 1, parts = 4, start.diameter = 0, lineCol = "black",
logic = rep(TRUE, parts)) {
r = diameter/2
y <- r * cos(seq(0, 2 * pi, by = 2 * pi/parts))
x <- r * sin(seq(0, 2 * pi, by = 2 * pi/parts))

r0 = start.diameter/2
y0 <- r0 * cos(seq(0, 2 * pi, by = 2 * pi/parts))
x0 <- r0 * sin(seq(0, 2 * pi, by = 2 * pi/parts))

dat <- (data.frame(x = x, y = y))
dat0 <- (data.frame(x = x0, y = y0))
i = 1
while (i < length(dat$x)) {
if (logic[i]) {
lines(c(dat0$x[i], dat$x[i]), c(dat0$y[i], dat$y[i]), col = lineCol)
}
i = i + 1
}
}

addTexts <- function(diameter = 1, labels = c("G", "C", "T", "A"), cex = 1,
logic = rep(TRUE, length(labels) + 1), start.diameter = 0, textCol = "black") {
parts = length(labels)

r = (start.diameter + diameter)/4
y <- r * cos(seq(0, 2 * pi, by = 2 * pi/parts) + pi/parts)
x <- r * sin(seq(0, 2 * pi, by = 2 * pi/parts) + pi/parts)
dat <- (data.frame(x = x, y = y))

i = 1
last.i = 1
while (i < length(dat$x)) {
j = i + 1
for (tt in j:length(dat$x)) {
if (logic[j]) {
text((dat$x[i] + dat$x[last.i])/2, (dat$y[i] + dat$y[last.i])/2,
labels[i], cex = cex, col = textCol)
last.i = j
break
}
}

i = i + 1
}
}
```


### Demo 1


```r
geneticCodeDemo1 <- function() {
plotCircle(diameter = 6)
addCircle(diameter = 5)
addCircle(diameter = 4)
addCircle(diameter = 3)
addCircle(diameter = 2)
addCircle(diameter = 1)

addLines(diameter = 6, parts = 4, start.diameter = 0)
addLines(diameter = 6, parts = 16, start.diameter = 1)
####
log1 = rep(c(FALSE, TRUE), 2)  #4
log2 = rep(c(FALSE, FALSE, FALSE, TRUE), 3)  #12
log3 = c(FALSE, FALSE, FALSE, TRUE)  #4
addornot = c(TRUE, log1, log2, log1, log2, log1, TRUE, TRUE, FALSE, TRUE,
log3, log1, log1, log1, log3, TRUE, FALSE, FALSE)  #64
addLines(diameter = 6, parts = 64, start.diameter = 2, logic = addornot)

text1 = c("G", "C", "T", "A")
addTexts(diameter = 1, labels = text1)
text2 = rep(c("A", "G", "C", "T"), 4)
addTexts(diameter = 2, labels = text2, cex = 0.8, start.diameter = 1)
text3 = rep(c("A", "G", "C", "T"), 16)
addTexts(diameter = 3, labels = text3, cex = 0.5, start.diameter = 2)
###
text4 = c("E", "E", "D", "D", "G", "G", "G", "G", "A", "A", "A", "A", "V",
"V", "V", "V", "Q", "Q", "H", "H", "R", "R", "R", "R", "P", "P", "P",
"P", "L", "L", "L", "L", "*", "*", "Y", "Y", "*", "W", "C", "C", "S",
"S", "S", "S", "L", "L", "F", "F", "K", "K", "N", "N", "R", "R", "S",
"S", "T", "T", "T", "T", "M", "I", "I", "I")
addTexts(diameter = 4, labels = text4, logic = c(addornot, TRUE), start.diameter = 3)
###
text5 = c("Glu", "Glu", "Asp", "Asp", "Gly", "Gly", "Gly", "Gly", "Ala",
"Ala", "Ala", "Ala", "Val", "Val", "Val", "Val", "Gln", "Gln", "His",
"His", "Arg", "Arg", "Arg", "Arg", "Pro", "Pro", "Pro", "Pro", "Leu",
"Leu", "Leu", "Leu", "*", "*", "Tyr", "Tyr", "*", "Trp", "Cys", "Cys",
"Ser", "Ser", "Ser", "Ser", "Leu", "Leu", "Phe", "Phe", "Lys", "Lys",
"Asn", "Asn", "Arg", "Arg", "Ser", "Ser", "Thr", "Thr", "Thr", "Thr",
"Met", "Ile", "Ile", "Ile")
addTexts(diameter = 5, labels = text5, logic = c(addornot, TRUE), start.diameter = 4)
###
text6 = c("glutamic acid", "glutamic acid", "aspartic acid", "aspartic acid",
"glycine", "glycine", "glycine", "glycine", "alanine", "alanine", "alanine",
"alanine", "valine", "valine", "valine", "valine", "glutamine", "glutamine",
"histidine", "histidine", "arginine", "arginine", "arginine", "arginine",
"proline", "proline", "proline", "proline", "leucine", "leucine", "leucine",
"leucine", "stop", "stop", "tyrosine", "tyrosine", "stop", "tryptophan",
"cysteine", "cysteine", "serine", "serine", "serine", "serine", "leucine",
"leucine", "phenylalanine", "phenylalanine", "lysine", "lysine", "asparagine",
"asparagine", "arginine", "arginine", "serine", "serine", "threonine",
"threonine", "threonine", "threonine", "methionine", "isoleucine", "isoleucine",
"isoleucine")
addTexts(diameter = 6, labels = text6, logic = c(addornot, TRUE), start.diameter = 5,
cex = 0.7)
}
geneticCodeDemo1()
```

![plot of chunk genetic-code-demo1](/figure/genetic-code-demo1.png)


### Demo 2


```r
geneticCodeDemo2 <- function() {
plotCircle(diameter = 4)
addCircle(diameter = 3)
addCircle(diameter = 2)
addCircle(diameter = 1)

addLines(diameter = 4, parts = 4, start.diameter = 0)
addLines(diameter = 4, parts = 16, start.diameter = 1)
####
log1 = rep(c(FALSE, TRUE), 2)  #4
log2 = rep(c(FALSE, FALSE, FALSE, TRUE), 3)  #12
log3 = c(FALSE, FALSE, FALSE, TRUE)  #4
addornot = c(TRUE, log1, log2, log1, log2, log1, TRUE, TRUE, FALSE, TRUE,
log3, log1, log1, log1, log3, TRUE, FALSE, FALSE)  #64
addLines(diameter = 4, parts = 64, start.diameter = 2, logic = addornot)

text1 = c("G", "C", "T", "A")
addTexts(diameter = 1, labels = text1)
text2 = rep(c("A", "G", "C", "T"), 4)
addTexts(diameter = 2, labels = text2, cex = 0.8, start.diameter = 1)
text3 = rep(c("A", "G", "C", "T"), 16)
addTexts(diameter = 3, labels = text3, cex = 0.5, start.diameter = 2)
###
text4 = c("E", "E", "D", "D", "G", "G", "G", "G", "A", "A", "A", "A", "V",
"V", "V", "V", "Q", "Q", "H", "H", "R", "R", "R", "R", "P", "P", "P",
"P", "L", "L", "L", "L", "*", "*", "Y", "Y", "*", "W", "C", "C", "S",
"S", "S", "S", "L", "L", "F", "F", "K", "K", "N", "N", "R", "R", "S",
"S", "T", "T", "T", "T", "M", "I", "I", "I")
addTexts(diameter = 4, labels = text4, logic = c(addornot, TRUE), start.diameter = 3)
}
geneticCodeDemo2()
```

![plot of chunk genetic-code-demo2](/figure/genetic-code-demo2.png)


### Demo 3


```r
geneticCodeDemo3 <- function() {
plotCircle(diameter = 4)
addCircle(diameter = 3)
addCircle(diameter = 2)
addCircle(diameter = 1)

addLines(diameter = 4, parts = 4, start.diameter = 0)
addLines(diameter = 4, parts = 16, start.diameter = 1)
####
log1 = rep(c(FALSE, TRUE), 2)  #4
log2 = rep(c(FALSE, FALSE, FALSE, TRUE), 3)  #12
log3 = c(FALSE, FALSE, FALSE, TRUE)  #4
addornot = c(TRUE, log1, log2, log1, log2, log1, TRUE, TRUE, FALSE, TRUE,
log3, log1, log1, log1, log3, TRUE, FALSE, FALSE)  #64
addLines(diameter = 4, parts = 64, start.diameter = 2, logic = addornot)

text1 = c("G", "C", "T", "A")
addTexts(diameter = 1, labels = text1)
text2 = rep(c("A", "G", "C", "T"), 4)
addTexts(diameter = 2, labels = text2, cex = 0.8, start.diameter = 1)
text3 = rep(c("A", "G", "C", "T"), 16)
addTexts(diameter = 3, labels = text3, cex = 0.5, start.diameter = 2)
###
text4 = c("Glu", "Glu", "Asp", "Asp", "Gly", "Gly", "Gly", "Gly", "Ala",
"Ala", "Ala", "Ala", "Val", "Val", "Val", "Val", "Gln", "Gln", "His",
"His", "Arg", "Arg", "Arg", "Arg", "Pro", "Pro", "Pro", "Pro", "Leu",
"Leu", "Leu", "Leu", "*", "*", "Tyr", "Tyr", "*", "Trp", "Cys", "Cys",
"Ser", "Ser", "Ser", "Ser", "Leu", "Leu", "Phe", "Phe", "Lys", "Lys",
"Asn", "Asn", "Arg", "Arg", "Ser", "Ser", "Thr", "Thr", "Thr", "Thr",
"Met", "Ile", "Ile", "Ile")
addTexts(diameter = 4, labels = text4, logic = c(addornot, TRUE), start.diameter = 3)
}
geneticCodeDemo3()
```

![plot of chunk genetic-code-demo3](/figure/genetic-code-demo3.png)


### Demo 4


```r
geneticCodeDemo4 <- function() {
plotCircle(diameter = 4, plotCol = "chartreuse4", polygonCol = "darkgoldenrod1")
addCircle(diameter = 3, plotCol = "chartreuse4", polygonCol = "cornsilk")
addCircle(diameter = 2, plotCol = "chartreuse4", polygonCol = "cyan")
addCircle(diameter = 1, plotCol = "chartreuse4", polygonCol = "aquamarine")

addLines(diameter = 4, parts = 4, start.diameter = 0, lineCol = "chartreuse4")
addLines(diameter = 4, parts = 16, start.diameter = 1, lineCol = "chartreuse4")
####
log1 = rep(c(FALSE, TRUE), 2)  #4
log2 = rep(c(FALSE, FALSE, FALSE, TRUE), 3)  #12
log3 = c(FALSE, FALSE, FALSE, TRUE)  #4
addornot = c(TRUE, log1, log2, log1, log2, log1, TRUE, TRUE, FALSE, TRUE,
log3, log1, log1, log1, log3, TRUE, FALSE, FALSE)  #64
addLines(diameter = 4, parts = 64, start.diameter = 2, logic = addornot,
lineCol = "chartreuse4")

text1 = c("G", "C", "T", "A")
addTexts(diameter = 1, labels = text1)
text2 = rep(c("A", "G", "C", "T"), 4)
addTexts(diameter = 2, labels = text2, cex = 0.8, start.diameter = 1)
text3 = rep(c("A", "G", "C", "T"), 16)
addTexts(diameter = 3, labels = text3, cex = 0.5, start.diameter = 2)
###
text4 = c("Glu", "Glu", "Asp", "Asp", "Gly", "Gly", "Gly", "Gly", "Ala",
"Ala", "Ala", "Ala", "Val", "Val", "Val", "Val", "Gln", "Gln", "His",
"His", "Arg", "Arg", "Arg", "Arg", "Pro", "Pro", "Pro", "Pro", "Leu",
"Leu", "Leu", "Leu", "*", "*", "Tyr", "Tyr", "*", "Trp", "Cys", "Cys",
"Ser", "Ser", "Ser", "Ser", "Leu", "Leu", "Phe", "Phe", "Lys", "Lys",
"Asn", "Asn", "Arg", "Arg", "Ser", "Ser", "Thr", "Thr", "Thr", "Thr",
"Met", "Ile", "Ile", "Ile")
addTexts(diameter = 4, labels = text4, logic = c(addornot, TRUE), start.diameter = 3)
}
geneticCodeDemo4()
```

![plot of chunk genetic-code-demo4](/figure/genetic-code-demo4.png)

