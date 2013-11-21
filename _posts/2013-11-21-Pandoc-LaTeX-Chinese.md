---
title: Convert Markdown files into PDF via LaTeX using Pandoc
layout: post
categories: [RStudy]
tags: [R,Pandoc,LaTeX,MiKTeX,RStudio,kintr]
image: /figure
---

### 1. R Markdown

[R Markdown](http://www.rstudio.com/ide/docs/r_markdown) "is a format that enables easy authoring of reproducible web reports from R. It combines the core syntax of [Markdown](http://daringfireball.net/projects/markdown/) (an easy-to-write plain text format for web content) with embedded R code chunks that are run so their output can be included in the final document."

### 2. Using R Markdown with RStudio

[RStudio](http://www.rstudio.com/) IDE is a powerful and productive user interface for R. An overview of how to use R Markdown within RStudio is available [here](http://www.rstudio.com/ide/docs/authoring/using_markdown)

### 3. Convert R Markdown to Markdown

[knitr](http://yihui.name/knitr/) can convert R Markdown (.Rmd) files into plain markdown (.md) files. With Rstudio, you only need to click the 'Knit HTML' button.

You can also use the following command:   

```
library(knitr)
knit("test.Rmd")
```

### 4. Convert Markdown files into PDF via LaTeX using Pandoc

#### 4.1 Install Pandoc and MiKTeX

We need to install the following tools first.   

[Pandoc](http://johnmacfarlane.net/pandoc/) can convert files from one markup format into another, see the webpage for more details.    

[MiKTeX](http://miktex.org/) is an up-to-date implementation of [TeX](http://www.ctan.org/tex/)/[LaTeX](http://www.latex-project.org/) and related programs for Windows.     

#### 4.2 Convert Markdown files into PDF

```
pandoc -o test.pdf test.md
```

Run Pandoc from Rstudio directly:   

```
system("pandoc -o test.pdf test.md")
```

**Note:** you may need to add the path of 'pandoc' to your Environment Variables. [How?](http://www.computerhope.com/issues/ch000549.htm)   

#### 4.3 When Markdown files include Chinese

Run Pandoc from Rstudio directly:   

```
system("pandoc -o test.pdf test.md  --latex-engine=xelatex --template=pm-template-felix.latex")
```

**Note:** MiKTeX need to install several packages when you run this command at the first time, this may need several minutes.

**Note:** You need to put [pm-template-felix.latex](https://dl.dropboxusercontent.com/u/8272421/latex/pm-template-felix.latex) under the same dir with .md files.  'pm-template-felix.latex' is a revised version of [pm-template.latex](https://github.com/tzengyuxio/pages/tree/gh-pages/pandoc)

**Note:** 该模板默认字体为宋体(SimSun),若需要其他字体只需替换SimSun即可。[更多字体](http://hotoo.googlecode.com/svn/trunk/labs/css/css-fonts.html)。

