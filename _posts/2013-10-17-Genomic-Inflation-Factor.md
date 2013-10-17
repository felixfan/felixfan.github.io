---
title: Genomic inflation factor and population structure
layout: post
---

The genomic inflation factor $$\lambda$$ is defined as the ratio of the median of the empirically observed distribution of the test statistic to the expected median, thus quantifying the extent of the bulk inflation and the excess false positive rate.    

$$\lambda=median(\chi^2)/0.456$$

$$\chi^2_{adjusted}=\chi^2/\lambda$$

Genomic inflation factor $$\lambda$$ and quantile–quantile (Q–Q) plots were used to compare the genome-wide distribution of the test statistic with the expected null distribution. The Q–Q plot is a useful visual tool to mark deviations of the observed distribution from the expected null distribution. Inflated $$\lambda$$ values or residual deviations in the Q–Q plot may point to undetected sample duplications, unknown familial relationships, a poorly calibrated test statistic, systematic technical bias or gross population stratification.      

Since $$\lambda$$ scales with sample size, some have found it informative to report $$\lambda _{1000}$$, the inflation factor for an equivalent study of 1000 cases and 1000 controls, which can be calculated by rescaling $$\lambda$$:

$$\lambda_{1000}=1+(\lambda_{obs}-1)*(1/n_{cases}+1/n_{controls})/(1/n_{cases,1000}+1/n_{controls,1000})$$

where $$n_{cases}$$ and $$n_{controls}$$ are the study sample size for cases and controls, respectively, and $$n_{cases,1000}$$ and $$n_{controls,1000}$$ are the target sample size (1000).   

**References**   
* de Bakker, P. I. et al. Practical aspects of imputation-driven meta-analysis of genome-wide association studies. Hum. Mol. Genet. 2008; 17, R122–128    

* Devlin B., Roeder K. Genomic control for association studies. Biometrics 1999;55:997-1004.    

* Freedman M.L., Reich D., Penney K.L., McDonald G.J., Mignault A.A., Patterson N., Gabriel S.B., Topol E.J., Smoller J.W., Pato C.N., et al. Assessing the impact of population stratification on genetic association studies. Nat. Genet. 2004;36:388-393.    

* Clayton D.G., Walker N.M., Smyth D.J., Pask R., Cooper J.D., Maier L.M., Smink L.J., Lam A.C., Ovington N.R., Stevens H.E., et al. Population structure, differential bias and genomic control in a large-scale, case–control association study. Nat. Genet. 2005;37:1243-1246.   
 
* [http://en.wikipedia.org/wiki/Population_stratification](http://en.wikipedia.org/wiki/Population_stratification)   

 
