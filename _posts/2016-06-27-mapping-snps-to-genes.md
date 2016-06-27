---
title: 抓取基因内的所有SNPs
layout: post
categories: [Bioinformatics]
tags: [Linux]
image: /figure2016
---

{% include JB/setup %}

# 1. 下载SNP信息

(1) UCSC genome browser 的 [table browser](https://genome.ucsc.edu/cgi-bin/hgTables)           
(2) 选择需要的 assembly（例如：hg19）
(3) group 选"Variation"
(4) track 选一个需要的数据（例如：Common SNPs(146) )
(5) table 选一个需要的数据（例如：snp146Common ）
(6) output format选'BED-browser extensible data'
(7)  点击‘get output’下载数据, 保存为‘hg19_commonSNPs146.txt’

# 2. 下载基因信息

可以使用这个基因数据[genes that are consistently annotated across Ensembl and Entrez-gene databases, and which have HUGO identifiers.](https://figshare.com/articles/hg19_GRCh37_Consensus_Genes/103113)。      

注意这个数据用的是hg19/GRChB37的位置信息。   

# 3. 抓取基因内的所有SNPs

(1) 安装[BEDTools](https://github.com/arq5x/bedtools2)    

(2) 提取常染色体及x，y染色体上的snp并排序        

```
awk '$1!~"_" && $1!~"M" {printf("%s\t%d\t%d\t%s\n", $1,$2,$3,$4);}' hg19_commonSNPs146.txt | sort -k1,1 -k2,2n -k3,3n -k4,4  > hg19_snp146_auto_sorted.txt
```

(3) 基因的位置上下游各加2000bp    

```
awk '{printf("%s\t%d\t%d\t%s\n", "chr"$1,$2-2000,$3+2000,$4);}' hugo.txt > hugo_2kb.txt
```

(4) 基因文件里23， 24表示x,y染色体，改正后并排序     

```
sed 's/chr23/chrX/' hugo_2kb.txt > hugo_2kb_v1.txt          
sed 's/chr24/chrY/' hugo_2kb_v1.txt > hugo_2kb_v2.txt          
sort -k1,1 -k2,2n -k3,3n hugo_2kb_v2.txt > hugo_2kb_v2_sorted.txt          
```

(5)  mapping (时间比较久)   
 
```
intersectBed -a hg19_snp146_auto_sorted.txt -b hugo_2kb_v2_sorted.txt -wa -wb | awk '{print $4, $8}' > geneSNPs_2kb.txt
```

**Reference**   

- [Mapping SNPs to Genes for GWAS Enrichment Analysis](http://www.gettinggeneticsdone.com/2011/06/mapping-snps-to-genes-for-gwas.html)    

