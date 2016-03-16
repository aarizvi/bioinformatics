setwd("/Users/aarizvi/Google Drive/AE/Bioinformatics -w11/")

library("ggplot2")
# install.packages("reshape")
library("reshape")
# install.packages("dplyr")
library("dplyr")

expression <- read.table("expression.txt", header=T)
expression <- log2(expression + 0.01)
survival <- read.csv("survivial_time.csv", header=T) #changed to .csv because xlsx library was crashing on my R 

good_in <- which(survival$Survival.Time..in.days. > 1826.21) #1826.21 days is equivalent to 5 years
good_sur <- as.character(survival[good_in, 1])
bad_sur <- as.character(survival[-good_in, 1])

pvalue <- apply(expression,1,function(x) {t.test(x[good_sur],x[bad_sur], alternative="two.sided")$p.value})
qvalue <- p.adjust(pvalue, method= "BH", n=length(pvalue)) #calculate q-value witwh BH method

pqval <- as.data.frame(cbind(pvalue, qvalue)) #cbind pval and qval 
pqval <- arrange(pqval, pvalue, qvalue)
sig_genes <- subset(pqval, pvalue <= 0.05)
sig_genes_q <- subset(sig_genes, qvalue <= 0.05)

sig_genes$genes <- row.names(sig_genes) 

sig_genes_plot <- melt(sig_genes, id.vars="genes")
sig_genes_plot <- arrange(sig_genes_plot, value, variable)
sig_genes <- arrange(sig_genes, pvalue, qvalue)


jpeg(filename="wk11-hw1", width = 1200, height = 1000, units="px", pointsize = 16, quality = 100)
plot(sig_genes$pvalue,type="l",col=2, ylim=c(0,1), xlab="genes", ylab = "p-value and q-value")
lines(sig_genes$qvalue,col=3)
legend(1,1, legend=c("pvalue","qvalue"), col=c(2,3), lty=1)
