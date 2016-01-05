---
title: Hello MySQL
layout: post
categories: [Database]
tags: [MySQL]
image: /figure
---
{% include JB/setup %}

### Install MySQL on Windows 7

#### Download MySQL Installer
* Windows 7
* mysql-installer-web-community-5.6.15.0.msi

[MySQL Installer](http://dev.mysql.com/downloads/installer/)

If you do not want to creat a new account, just click **"No thanks, just start my download."** (at the bottom of the page).

**Note:** MySQL Installer is 32 bit, but will install both 32 bit and 64 bit binaries.

#### Install MySQL

* Double-click the downloaded file to install

### Creating A New MySQL Connection

[Creating A New MySQL Connection](http://dev.mysql.com/doc/workbench/en/wb-mysql-connections-new.html) "MyFirstConnection".

### Load data from csv file

The example data used is a typical PLINK association output contains 13 columns (CHR, SNP, BP, A1, F_A, F_U, A2, CHISQ, P, OR, SE, L95, U95).

First create tables.

```
CREATE TABLE `gwas`(
`CHR` INT NOT NULL,
`SNP` VARCHAR(45) NOT NULL,
`BP` INT NOT NULL,
`A1` VARCHAR(45) NOT NULL,
`F_A` DOUBLE NOT NULL,
`F_U` DOUBLE NOT NULL,
`A2` VARCHAR(45) NOT NULL,
`CHISQ` DOUBLE NOT NULL,
`P` DOUBLE NOT NULL,
`OR` DOUBLE NOT NULL,
`SE` DOUBLE NOT NULL,
`L95` DOUBLE NOT NULL,
`U95` DOUBLE NOT NULL,
PRIMARY KEY (`SNP`));
```

```
CREATE TABLE `replicate`(
`CHR` INT NOT NULL,
`SNP` VARCHAR(45) NOT NULL,
`BP` INT NOT NULL,
`A1` VARCHAR(45) NOT NULL,
`F_A` DOUBLE NOT NULL,
`F_U` DOUBLE NOT NULL,
`A2` VARCHAR(45) NOT NULL,
`CHISQ` DOUBLE NOT NULL,
`P` DOUBLE NOT NULL,
`OR` DOUBLE NOT NULL,
`SE` DOUBLE NOT NULL,
`L95` DOUBLE NOT NULL,
`U95` DOUBLE NOT NULL,
PRIMARY KEY (`SNP`));
```

Then load the data.

```
LOAD DATA LOCAL INFILE 'C:/Users/alice/Documents/MySQL/LoadFileExample/gwas.csv' INTO TABLE gwas FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';
```

```
LOAD DATA LOCAL INFILE 'C:/Users/alice/Documents/MySQL/LoadFileExample/replicate.csv' INTO TABLE replicate FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';
```

Note 1: The original PLINK output was import to EXCEL and the csv file was exported. That's why I used **FIELDS TERMINATED BY ','** here.

Note 2: I delete the first line (the header), if the header line was kept, you need to add **IGNORE 1 LINES**.

### SELECT from table

#### select all from table 'gwas', order the output by 'CHR' and 'BP' (both in ascending order)

```
SELECT * FROM gwas ORDER BY CHR ASC, BP ASC;
```

Equivalent to (ascending order is default)

```
SELECT * FROM gwas ORDER BY CHR, BP;
```

#### select by condition

```
SELECT * FROM gwas WHERE P<0.00001;
```

order the output by 'CHR' and 'BP'


```
SELECT * FROM gwas WHERE P<0.00001 ORDER BY CHR, BP;
```

```
SELECT * FROM gwas WHERE P<0.00001 AND gwas.OR>2 ORDER BY CHR, BP;
```

Note: 'OR' is the key word of MySQL. when select the row with 'OR>2', you need to add the table name 'gwas' here.

### JOIN two tables

```
SELECT * FROM gwas INNER JOIN replicate ON gwas.snp = replicate.snp;
```

```
SELECT * FROM gwas INNER JOIN replicate ON gwas.P<0.00001 AND replicate.P<0.005;
```

Equivalent to

```
SELECT * FROM gwas a INNER JOIN replicate b ON a.P<0.00001 AND b.P<0.005;
```

### Further reading

* [A Visual Explanation of SQL Joins](http://www.codinghorror.com/blog/2007/10/a-visual-explanation-of-sql-joins.html)
* [Using Database Joins to Compare Results Sets](http://gettinggeneticsdone.blogspot.hk/2013/11/using-database-joins-to-compare-results.html)




