---
title: RMA normalization for microarray data
layout: post
categories: [Bioinformatics]
tags: [GEO]
image: /figure
---
{% include JB/setup %}

### Why does microarray data need to be normalized?

account for technical variation between the arrays.

### Methods

Robust Multichip Average (RMA) normalization.

* [RMAExpress for Windows](http://rmaexpress.bmbolstad.com)
* [R for All Platforms](http://www.bioconductor.org/help/workflows/oligo-arrays/)

### Demo (GSE1297)

#### Step 1 Install packages


```r
# install the core bioconductor packages, if not already installed
source("http://bioconductor.org/biocLite.R")
biocLite()

# install additional bioconductor libraries, if not already installed
biocLite("GEOquery")  # Get data from NCBI Gene Expression Omnibus (GEO)
biocLite("affy")  # Methods for Affymetrix Oligonucleotide Arrays
biocLite("hgu133a.db", type = "source")  # GSE1297: Platform_title = [HG-U133A]
biocLite("hgu133acdf")
```


### Download the CEL file


```r
library(GEOquery)

# Set working directory for download
setwd("D:/GEO/AD/GSE/GSE1297")

# Download the CEL file (by GSE - Geo series id), may take very long time
getGEOSuppFiles("GSE1297")
# this command does not work for this chip, so I need to download it
# directly Platform_title = [HG-U133A] Affymetrix Human Genome U133A Array
# Platform information can be found in SOFT file

# Unpack the CEL files
```

```r
setwd("D:/GEO/AD/GSE/GSE1297/GSE1297")
```


```r
untar("GSE1297_RAW.tar", exdir = "data")
cels = list.files("data/", pattern = "cel")
# sometiles, it is 'CEL', you need to check it first
sapply(paste("data", cels, sep = "/"), gunzip)
```


```r
cels = list.files("data/", pattern = "cel")
# sometiles, it is 'CEL', you need to check it first
```


### Perform RMA normalization


```r
library(affy)
library(hgu133a.db)
library(hgu133acdf)

# Set working directory for normalization
setwd("D:/GEO/AD/GSE/GSE1297/GSE1297/data")
raw.data = ReadAffy(verbose = FALSE, filenames = cels, cdfname = "hgu133acdf")

# perform RMA normalization (log2)
data.rma.norm = rma(raw.data)
```

```
Background correcting
Normalizing
Calculating Expression
```

```r

# Get the expression estimates for each array
rma = exprs(data.rma.norm)

# Take a look at the result (first 5 rows and 5 columes)
rma[1:5, 1:5]
```

```
GSM21203.cel GSM21204.cel GSM21205.cel GSM21206.cel GSM21207.cel
1007_s_at       10.606       10.339       10.390       10.523       10.791
1053_at          4.586        4.463        4.572        4.531        4.546
117_at           5.937        6.017        6.234       10.114        6.253
121_at           8.763        8.951        9.026        8.804        9.130
1255_g_at        4.361        4.439        4.598        4.019        4.354
```

```r

# Write RMA-normalized, mapped data to file
write.table(rma, file = "rma.txt", quote = FALSE, sep = "\t")
```


### Annotation





```r
tt = cbind(row.names(rma), rma)
colnames(tt) = c("ProbID", sub(".cel", "", colnames(rma), ignore.case = TRUE))
rownames(tt) = NULL
tt[1:5, 1:5]
```

```
ProbID      GSM21203           GSM21204           GSM21205
[1,] "1007_s_at" "10.6061947450577" "10.3389916272064" "10.390181163724"
[2,] "1053_at"   "4.58630979543013" "4.46270777736086" "4.57178078332995"
[3,] "117_at"    "5.93684658044002" "6.01691505298677" "6.23421446338666"
[4,] "121_at"    "8.76288033305696" "8.9513454849938"  "9.02618022186855"
[5,] "1255_g_at" "4.3610859654913"  "4.43906808970735" "4.59752976632791"
GSM21206
[1,] "10.5230672101482"
[2,] "4.53054651020166"
[3,] "10.1138768429987"
[4,] "8.80361343714862"
[5,] "4.01915640899688"
```

```r

require(RCurl)
myURL <- getURL("https://dl.dropboxusercontent.com/u/8272421/geo/HGU133A.na33.txt",
ssl.verifypeer = FALSE)
annot <- read.table(textConnection(myURL), header = TRUE, sep = "\t")
head(annot)
```

```
ProbeSetID EntrezGene
1  1007_s_at  100616237
2  1007_s_at        780
3    1053_at       5982
4     117_at       3310
5     121_at       7849
6  1255_g_at       2978
```

```r

# probe sets were mapped to Entrez Gene IDs.
# comb=merge(annot,tt,by.x='ProbeSetID',by.y='ProbID',all.y=TRUE)
comb = merge(annot, tt, by.x = "ProbeSetID", by.y = "ProbID")
comb[1:5, 1:5]
```

```
ProbeSetID EntrezGene         GSM21203         GSM21204         GSM21205
1  1007_s_at  100616237 10.6061947450577 10.3389916272064  10.390181163724
2  1007_s_at        780 10.6061947450577 10.3389916272064  10.390181163724
3    1053_at       5982 4.58630979543013 4.46270777736086 4.57178078332995
4     117_at       3310 5.93684658044002 6.01691505298677 6.23421446338666
5     121_at       7849 8.76288033305696  8.9513454849938 9.02618022186855
```

```r
write.table(comb, file = "comb2.txt", quote = FALSE, sep = "\t", row.names = FALSE)

# If multiple probe sets corresponded to the same gene, then the expression
# values of these probe sets were averaged.
comb2 <- subset(comb, select = -c(ProbeSetID))
comb2 <- data.frame(lapply(comb2, as.character), stringsAsFactors = FALSE)
comb2 <- data.frame(lapply(comb2, as.numeric), stringsAsFactors = FALSE)
out <- aggregate(. ~ EntrezGene, data = comb2, mean)

# Format values to 5 decimal places
out = format(out, digits = 5)
out[1:5, 1:5]
```

```
EntrezGene GSM21203 GSM21204 GSM21205 GSM21206
1          2   9.0928   9.7931   9.0962   9.8969
2          9   4.5077   4.3635   4.5445   4.3781
3         10   6.2881   6.2111   7.0938   5.7314
4         12  11.5590   8.0948   8.2142  12.3144
5         13   4.5742   4.6783   5.0740   4.5521
```

```r
write.table(out, file = "GSE1297.RMA.txt", quote = FALSE, sep = "\t", row.names = FALSE)
```


### Session information


```r
sessionInfo()
```

```
R version 3.0.2 (2013-09-25)
Platform: x86_64-w64-mingw32/x64 (64-bit)

locale:
[1] LC_COLLATE=Chinese (Simplified)_People's Republic of China.936
[2] LC_CTYPE=Chinese (Simplified)_People's Republic of China.936
[3] LC_MONETARY=Chinese (Simplified)_People's Republic of China.936
[4] LC_NUMERIC=C
[5] LC_TIME=Chinese (Simplified)_People's Republic of China.936

attached base packages:
[1] parallel  stats     graphics  grDevices utils     datasets  methods
[8] base

other attached packages:
[1] RCurl_1.95-4.1       bitops_1.0-6         hgu133acdf_2.12.0
[4] hgu133a.db_2.9.0     org.Hs.eg.db_2.9.0   RSQLite_0.11.4
[7] DBI_0.2-7            AnnotationDbi_1.22.6 affy_1.38.1
[10] Biobase_2.20.1       BiocGenerics_0.6.0   knitr_1.5

loaded via a namespace (and not attached):
[1] affyio_1.28.0         BiocInstaller_1.10.4  evaluate_0.5.1
[4] formatR_0.10          IRanges_1.18.4        preprocessCore_1.22.0
[7] stats4_3.0.2          stringr_0.6.2         tools_3.0.2
[10] zlibbioc_1.6.0
```


### Further Reading            
[Tutorial: Analysing microarray data in BioConductor](http://www.biostars.org/p/53870/)         
[Using Bioconductor for Microarray Analysis](http://www.bioconductor.org/help/workflows/oligo-arrays/)          
[Methods of RMA Normalization for Affymetrix GeneChip Arrays](http://www.tm4.org/normalizing.html)           
[A Comparison of Normalization Methods for High Density Oligonucleotide Array Data Based on Bias and Variance. Bioinformatics 19(2):185-193](http://bioinformatics.oxfordjournals.org/content/19/2/185.abstract)          
