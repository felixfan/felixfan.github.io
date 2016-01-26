# google scholar citations


```r
library(scholar)
library(ggplot2)
usr <- '8fX1TSQAAAAJ' # change this to your own google scholar id
cit <- get_citation_history(usr)
ggplot(cit,aes(x=year,y=cites))+
    geom_bar(stat='identity')+
    theme_bw()+
    xlab('Year of citation')+
    ylab('Google Scholar Cites')+
    annotate('text',label=format(Sys.time(), "%Y-%m-%d %H:%M:%S %Z"),
             x=-Inf,y=Inf,vjust=1.5,hjust=-0.05,size=3,colour='gray')
```

![](2016-01-26-google-scholar_files/figure-html/scholar-1.png) 
