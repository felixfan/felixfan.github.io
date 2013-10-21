---
title: R Manipulation of Files and Directories
layout: post
categories: [RStudy]
tags: [R]
image: /figure
---

### Creat directories


```r
dir.create("test")
```


### Get working wirectory


```r
getwd()
```

```
[1] "E:/360yunpanGmail/study/R/Rmarkdown"
```


### Set working directory


```r
setwd("./test")
getwd()
```

```
[1] "E:/360yunpanGmail/study/R/Rmarkdown/test"
```


### Create file
creates files with the given names if they do not already exist and truncates them if they do.   


```r
file.create("test.csv")
```

```
[1] TRUE
```

```r
file.create("test1.csv", "test2.csv")
```

```
[1] TRUE TRUE
```


### Output data to file


```r
cat("Hello world\n", file = "test1.csv")
cat("Hello R\n", file = "test2.csv")
```



```r
data(iris)
write.table(iris, file = "test.csv", row.names = FALSE, sep = ",")
```


### Test whether file exists


```r
file.exists("test.csv")
```

```
[1] TRUE
```


### Read data from file


```r
mydata1 = read.table("test.csv", header = TRUE, sep = ",")
head(mydata1)
```

```
  Sepal.Length Sepal.Width Petal.Length Petal.Width Species
1          5.1         3.5          1.4         0.2  setosa
2          4.9         3.0          1.4         0.2  setosa
3          4.7         3.2          1.3         0.2  setosa
4          4.6         3.1          1.5         0.2  setosa
5          5.0         3.6          1.4         0.2  setosa
6          5.4         3.9          1.7         0.4  setosa
```


or   


```r
mydata2 = read.csv("test.csv", header = TRUE)
head(mydata2)
```

```
  Sepal.Length Sepal.Width Petal.Length Petal.Width Species
1          5.1         3.5          1.4         0.2  setosa
2          4.9         3.0          1.4         0.2  setosa
3          4.7         3.2          1.3         0.2  setosa
4          4.6         3.1          1.5         0.2  setosa
5          5.0         3.6          1.4         0.2  setosa
6          5.4         3.9          1.7         0.4  setosa
```


### Remove file


```r
file.remove("test2.csv")
```

```
[1] TRUE
```

```r
file.exists("test2.csv")
```

```
[1] FALSE
```


### Delete files and directories


```r
unlink("test1.csv")
file.exists("test1.csv")
```

```
[1] FALSE
```


### Rename file
rename "test.csv" to "test2.csv".    


```r
file.rename("test.csv", "test2.csv")
```

```
[1] TRUE
```


### Append file
Append "test2.csv" to "test1.csv".     


```r
file.append("test1.csv", "test2.csv")
```

```
[1] TRUE
```

```r
head(read.csv("test1.csv", header = FALSE))
```

```
            V1          V2           V3          V4      V5
1 Sepal.Length Sepal.Width Petal.Length Petal.Width Species
2          5.1         3.5          1.4         0.2  setosa
3          4.9           3          1.4         0.2  setosa
4          4.7         3.2          1.3         0.2  setosa
5          4.6         3.1          1.5         0.2  setosa
6            5         3.6          1.4         0.2  setosa
```


### Copy file
Copy "test1.csv" to "test.csv".    


```r
file.copy("test1.csv", "test.csv")
```

```
[1] TRUE
```

```r
head(read.csv("test.csv", header = FALSE))
```

```
            V1          V2           V3          V4      V5
1 Sepal.Length Sepal.Width Petal.Length Petal.Width Species
2          5.1         3.5          1.4         0.2  setosa
3          4.9           3          1.4         0.2  setosa
4          4.7         3.2          1.3         0.2  setosa
5          4.6         3.1          1.5         0.2  setosa
6            5         3.6          1.4         0.2  setosa
```


### Extract file information


```r
file.info("test.csv")
```

```
         size isdir mode               mtime               ctime
test.csv 4177 FALSE  666 2013-10-08 12:45:40 2013-10-08 12:45:05
                       atime exe
test.csv 2013-10-08 12:45:40  no
```


### List the files in a directory/folder


```r
list.files(path = ".", pattern = "*.csv")
```

```
[1] "test.csv"  "test1.csv" "test2.csv"
```

```r
list.dirs(".")
```

```
[1] "."      "./test"
```

```r

Sys.glob("*.csv")
```

```
[1] "test.csv"  "test1.csv" "test2.csv"
```


### Construct path to file


```r
file.path("test.csv")
```

```
[1] "test.csv"
```


### Directory and file name


```r
basename(file.path("test.csv"))
```

```
[1] "test.csv"
```

```r
dirname(file.path("test.csv"))
```

```
[1] "."
```

