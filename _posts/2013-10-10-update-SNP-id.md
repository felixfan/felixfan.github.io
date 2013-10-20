---
title: Updating kgp IDs to rs IDs for SNPs on Illumina HumanOmni2.5M array
layout: post
categories: [Bioinformatics]
tags: [SNP, id, kgp, rs, ngs, gwas, illumina]
---

### Step 1: Create a file of genomic coordinates from your map file

The format is like this:        

```
chr1 4158539 4158540 kgp499505
```

In linux, you can use the following command:      

```
awk '{print "chr"$1,$4-1,$4,$2}' yourdata.bim > genomicCoordinates.txt
```

or

```
awk '{print "chr"$1,$4-1,$4,$2}' yourdata.map > genomicCoordinates.txt
```

**Note:** yourdata.bim and yourdata.map are in [PLINK](http://pngu.mgh.harvard.edu/~purcell/plink/data.shtml#map) format.    

### Step 2: Navigate to [UCSC Table Browser](http://genome.ucsc.edu/cgi-bin/hgTables)

### Step 3: Options selection

* Clade: Mammal
* Genome: Human
* Assembly: Feb. 2009 (GRCh37/hg19)
* Group: Variation and Repeats
* Track: All SNPs(137)
* Table: snp137
* Output format: selected fields from primary and related tables

**Note:** Make sure your genomic coordinates is same as hg19. If you are not sure about this, you can search one SNP with rs ID to check whether it is hg19 or hg18.     

### Step 4: Upload input file

On the "region" line, click the "define regions" button. Upload "genomicCoordinates.txt" file generated in step 1 by clicking "Choose File" button. Then click the "submit" button.    

**Note:** There is a limit of 1,000 defined regions. It should be fine if you only update the significant SNPs.       

### Step 5: Select output format

On the "output format" line, select "selected fileds from primary and related tables".    
     
### Step 6: Get output

You can enter a filename on the "output file" line or leave it blank to see the results on the screen. Enter "output.txt" and click the "get output" button.          

In the new opened page "Select Fields from hg19.snp137",  check the "chrom", "chromStart", "chromEnd" and "name" checkboxes. Then click the "get output" button.        

### Step 7: Delete deletions?

You may got multiple records for one search. For example:     

Input:    

```
chr12  72650313	72650314	rs201804413
```

And the output:     

```
chr12  72650313	72650317	rs66927394
chr12	72650313	72650314	rs201804413
```

I am not sure whether the first record in the output is a 'deletion', but I only want the second record, so I will remove the first record.    

In linux, you can remove all first record like records using the following command:    

```
awk '$3-$2==1{print}' output.txt > output2.txt
```

**Note:** "output.txt" is the output in step 6.      

### Step 8: Update IDs

In linux,     

```
sort -k1 genomicCoordinates.txt > genomicCoordinates.sort.txt
sort -k1 output2.txt > output.sort.txt
join genomicCoordinates.sort.txt output.sort.txt | awk '{if($2==$5 && $3==$6) print $4,$7}' > updateIDs.txt
```

Use "--update-map updateIDs.txt --update-name" command of PLINK to update SNP IDs.     

**Reference**      

[Reg. Updating SNP ids for SNPs on Illumina HumanOmni2.5M array](http://redmine.soe.ucsc.edu/forum/index.php?t=msg&goto=13224&S=29fba0172e0e677085609b8e1da196cb)     
[PLINK](http://pngu.mgh.harvard.edu/~purcell/plink/index.shtml)    
