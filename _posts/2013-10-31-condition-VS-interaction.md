---
title: PLINK logistic regression - covariant vs interaction
layout: post
categories: [bioinformatics]
tags: [Bioinformatics, Genetics, GWAS,Plink,Logistic regression]
image: /figure
---

### plink `--condition`

Conditioning on a SNP is done when you have two (or more) SNPs and you wish to ask the question "is the effect of SNP two independent of the effect of SNP one?".              

The conditioning SNPs are entered into the model simply as **covariates**, using a simple 0, 1, 2 allele dosage coding.  That is, for two conditioning SNPs, rs1001 and rs1002 say, and also a standard covariate, the model would be:       

```
Y = b0 + b1.ADD + b2.rs1001 + b3.rs1002 + b4.COV1 + e       
```

If the **b1** coefficient for the test SNP is **still significant** after entering these covariates, this would suggest that it does indeeed have an effect **independent** of rs1001, rs1002 and the other covariate. Here the test SNP b1 is the one where we'd like to test independence. The other coefficients may still be highly significant, but these reflect the effects of the conditioning SNPs and covariates, not the test SNP.           

### plink `--interaction`

Testing for interaction is done when you have a covariate (which may not be a SNP) and a SNP and you wish to ask the question, "if I add an interaction coefficient to a model that already has terms for the covariate and the SNP, is that interaction term significant?"              

The PLINK documentation illustrates this with the following model:          
      
```
Y = b0 + b1.ADD + b2.COV1 + b3.COV2 + b4.ADDxCOV1 + b5.ADDxCOV2 + e         
```

Here the test is not "is my SNP independent of the covariate", but instead "if I have both my SNP and the covariate as terms, do they together exert a stronger effect on the phenotype than I would expect to see through the linear addition of their individual effects?"            

**Note:** When including the --interaction flag, you should probably only interpret the interaction p-value.             

### summary

* Conditioning on a SNP is like removing its effect. As an example, let's say you find that SNP1 is strongly associated with your trait. Then you find SNP2, nearby, is also strongly associated. You might then ask whether these are 2 separate signals. By conditioning on SNP1 (i.e., holding SNP1 constant for all subjects), you can examine whether SNP2 still has an effect.

* Testing for interactions answers a different question: Does the association between SNP1 and my trait differ by SNP2 genotype? This is a gene-gene interaction. Or you might ask if SNP1 behaves differently among statin drug users versus non-users. This would be testing a gene-environment interaction.

### Further Reading
[Biostar](http://www.biostars.org/p/14914/)    
[PLINK](http://pngu.mgh.harvard.edu/~purcell/plink/anal.shtml)    
[Informed conditioning on clinical covariates increases power in case-control association studies. PLoS Genet. 2012;8(11):e1003032](http://www.ncbi.nlm.nih.gov/pubmed/23144628)       
[The Covariate's Dilemma. PLoS Genet. 2012 November; 8(11): e1003096.](http://www.ncbi.nlm.nih.gov/pubmed/23162385)      
