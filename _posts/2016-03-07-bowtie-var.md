---
title: bowtie examples
layout: post
categories: [Bioinformatics]
tags: [NGS]
image: /figure2016
---
{% include JB/setup %}

# 1. generate bowtie2 index

```bash
bowtie2-build ref.fasta indexDir/ref
```

# 2. read alignments

## 2.1 end-to-end read alignments

```bash
bowtie2 –x indexDir/ref –U seq.fastq –S out.full.sam
```

## 2.2 partial read alignments

```bash
bowtie2 –x indexDir/ref –U seq.fastq –S out.local.sam --local
```

# 3. statistics of the alignments

## 3.1 How many matches (alignments) were reported? 

Check the SAM file to determine the number of alignment lines, excluding lines that refer to unmapped reads. A SAM line indicating an unmapped read can be recognized by a "*" in column 3 (chrom).   

```bash
grep -v "^@" out.full.sam | cut -f3 | grep -v "*" | wc -l
```

```bash
grep -v "^@" out.local.sam | cut -f3 | grep -v "*" | wc -l
```

## 3.2 How many alignments contained insertions and/or deletions?

This information is captured in the CIGAR field (col 6), marked with 'D' and 'I', respectively.

```bash
cut -f6 out.full.sam | grep -c "[I,D]"
```

```bash
cut -f6 out.local.sam | grep -c "[I,D]"
```

or    

```bash
grep -v "^@" out.full.sam | awk '$6~"I" || $6~"D"' | wc -l
```

```bash
grep -v "^@" out.local.sam | awk '$6~"I" || $6~"D"' | wc -l
```

# 4. call variants

## 4.1 converting the SAM file to BAM format

```bash
samtools view –bT ref.fasta out.full.sam > out.full.bam
```

## 4.2 sort the bam file

```bash
samtools sort out.full.bam -o out.full.sorted.bam
```

## 4.3 Determine candidate sites

```bash
samtools mpileup –f ref.fasta –g out.full.sorted.bam > out.full.mpileup.bcf
```

```bash
bcftools call -m -v -O v -o out.mileup.vcf out.full.mileup.bcf
```

# 5. variants statistics

## 5.1 How many variants were reported for Chr1?

```bash
grep -c "^Chr1" out.full.mpileup.vcf 
```

## 5.2 How many variants have 'A' as the reference allele?

```bash
grep -v "^#" out.full.mpileup.vcf | awk '$4=="A"' | wc -l
```

## 5.3 How many variants have exactly 20 supporting reads (read depth)?

```bash
grep -v "^#" out.full.mpileup.vcf | grep "DP=20;" | wc -l
```

## 5.4 How many variants represent indels?

```bash
grep -v "^#" out.full.mpileup.vcf | grep "INDEL" | wc -l
```



