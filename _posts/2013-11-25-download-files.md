---
title: Download files from internet using R
layout: post
categories: [RStudy]
tags: [R]
image: /figure
---

{% include JB/setup %}

### Download a file

```r
require(RCurl)
myCsv <- getURL("https://dl.dropboxusercontent.com/u/8272421/test.txt", ssl.verifypeer = FALSE)
myData <- read.csv(textConnection(myCsv))
myData
```

```
test   class
1    1    case
2    2 control
```

### Downloading multiple files from FTP server

```r
url = "ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE1nnn/GSE1297/suppl/"
filenames = getURL(url, ftp.use.epsv = FALSE, dirlistonly = TRUE)
filenames <- strsplit(filenames, "\r\n")
filenames = unlist(filenames)
filenames
```

```
[1] "filelist.txt"    "GSE1297_RAW.tar"
```

```r
for (filename in filenames) {
download.file(paste(url, filename, sep = ""), paste(getwd(), "/", filename,
sep = ""))
}
```

### Load a given URL into a WWW browser

```r
browseURL("http://cran.r-project.org/web/packages/FinCal/index.html")
```

