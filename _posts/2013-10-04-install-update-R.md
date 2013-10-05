---
title: Install and Update R and R packages
layout: post
---

```
OS:      WIN7  
R:       3.02   
RStudio: 0.98.312
```

### 1. Install R

R is available at http://www.r-project.org/.

### 2. Update R


```r
if (!require(installr)) {
    # load / install+load installr
    install.packages("installr")
    require(installr)
}

updateR()
```


### 3. Install R packages

#### 3.1 Installing R packages from CRAN (http://cran.r-project.org/)


```r
install.packages("FinCal", dependencies = TRUE)  # FinCal is the package name
```


or

```
RStudio -> Tools -> Install Packages -> Install from 'Repository (CRAN)'
```

#### 3.2 Installing R packages from Package Archive File (offline)


```r
install.packages("FinCal_0.5.zip")
```


or

```
RStudio -> Tools -> Install Packages -> Install from 'Package Archive File'
```
or


```r
R CMD INSTALL FinCal_0.5.zip
```


#### 3.3 Installing R packages from Bioconductor (http://www.bioconductor.org/)


```r
source("http://bioconductor.org/biocLite.R")  # installs 'BiocInstaller'
biocLite()  # installs automatically 'Biobase' 'IRanges' 'AnnotationDbi' ‘BiocGenerics’ ‘RSQLite’
all_group()  # Get list of all packages in BioConductor
biocLite(c("GenomicFeatures", "AnnotationDbi"))  #installing GenomicFeatures &AnnotationDbi packages
```


#### 3.4 Installing R packages from GitHub (https://github.com/)


```r
install.packages("devtools")  # requires for downloading & installation of GitHub packages
require(devtools)
install_github(repo = "FinCal", username = "felixfan")  # installing FinCal package
```


### 4. Update all existing packages

#### 4.1 Automated Re-Install of Packages (packages in the default library dir)

```r
update.packages(ask = FALSE, repos = "http://cran.rstudio.org", checkBuilt = TRUE)
```


or just


```r
update.packages(ask = FALSE)
```


#### 4.2 Automated Re-Install of Packages (packages do not in the default library dir)


```r
.libPaths()  # gets the library trees within which packages are looked for
myPath = c("C:/Users/alice/Documents/R/win-library/3.0")  # change it to your own dir
package_df <- as.data.frame(installed.packages(myPath))  #Get currently installed packages
package_list <- as.character(package_df$Package)
install.packages(package_list)  #Re-install all installed packages
```


### 5. Reference

[Installing R packages from CRAN/Bioconductor/Omegahat/Github](https://sagarnikam123.snipt.net/install-packges-in-r-from-crangithub/)      
[R 3.0.0 is released! (what’s new, and how to upgrade)](http://www.r-statistics.com/2013/04/r-3-0-0-is-released-whats-new-and-how-to-upgrade/)   
[Automated Re-Install of Packages for R 3.0](http://randyzwitch.com/automated-re-install-of-packages-for-r-3-0/)     

