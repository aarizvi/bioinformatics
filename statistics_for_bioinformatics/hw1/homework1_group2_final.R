#############################
# This code is for sta525 hw1
# Group 2
# Feb 18, 2016
#############################

# clear the environment
rm(list=ls())

# required packages
if(F){
  install.packages("graphics")
  install.packages("knitr")
  install.packages("GEOquery")
  install.packages("gplot")
  install.packages("vioplot")
  install.packages("beanplot")
  install.packages("affy")
  install.packages("affyPLM")
  install.packages("multtest")
  install.packages("pROC")
}

#-------------------------#
# Problem 1
#------------------------#


library(knitr)
library(GEOquery)

## save the data in a data file ##
# gse19439 = getGEO("GSE19439", GSEMatrix = T)
# gse19439 = gse19439[[1]]
# save(file = "gse19439.RData", gse19439)

## load the data
load(file = "gse19439.RData")
gse19439
experimentData(gse19439)
feat <- featureData(gse19439)
varLabels(feat)

# make a factor object for Control, latent TB and Positive TB
tmp=as.character(pData(phenoData(gse19439))[,1]) # pData=phenoData
J=length(tmp) # J=number of samples (42)
TBgroup=rep("",J) # create a null vector
for(j in 1:J) TBgroup[j]=substring(tmp[j],1,3) # get the first 3 letters from each tmp

# make a factor for TBgroup
TBgroup # class character
FTB=factor(TBgroup,levels=c("CON","LTB","PTB")) # withdraw "", only keep the letters # class factor

# get our expression set
X=exprs(gse19439)
dim(X) # 48791 features and 42 samples


# do a quick kruskal-wallis scan 
myKrusk=function(i){
  cat(i,"...",fill=F)
  kruskal.test(x=X[i,],g=FTB)$p.value
}

# originally, I ran this in the HW1 directory:
#  myPvals=mapply(myKrusk,1:(dim(X)[1])) 
# save(file="myPvals.RData",myPvals)

# so that now I can save time and just load:
load("myPvals.RData")

# populate vector with last names of the groups in the class.
# note: the code is written this way, becasue it used to be student nameas and not Group names

GroupLabels=c("Group I","Group II","Group III","Group IV")

# pick the best 4 p-values and assign them to the students.

best4=order(myPvals)[1:4]   

# print out list of best 4
print(best4)


for(i in 1:length(GroupLabels)) 
  cat("Group Label:",GroupLabels[i],
      "\t\t row assignment:",best4[i],fill=T)    

myrow <- gse19439[10685,]
dim(myrow)
featureNames(myrow)
gene.info <- pData(featureData(myrow))

# 10685 GENE IS LACTB
# LACTB (Lactamase, Beta) is a Protein Coding gene. 
# Diseases associated with LACTB include lung abscess and bacterial conjunctivitis. 
# GO annotations related to this gene include hydrolase activity.

#------------------------#
# Problem 2
#-----------------------#
# boxplot
sampleNames(myrow)
boxplot(log2(X[10685,sampleNames(myrow)[FTB == 'CON']]),
        log2(X[10685,sampleNames(myrow)[FTB == 'LTB']]),
        log2(X[10685,sampleNames(myrow)[FTB == 'PTB']]),
        main = "Boxplot of Row Data as Function of TB Phenotype",
        names = c("CON", "LTB", "PTB"))
# boxplots disguise multimodal data 

# violin plot # a combination of a box plot and a kernel density plot
library(vioplot)
vioplot(log2(X[10685,sampleNames(myrow)[FTB == 'CON']]),
        log2(X[10685,sampleNames(myrow)[FTB == 'LTB']]),
        log2(X[10685,sampleNames(myrow)[FTB == 'PTB']]),
        names = c("CON", "LTB", "PTB"))
title("Violin Plot of Row Data as Function of TB Phenotype")

# beanplot
library(beanplot)
beanplot(log2(X[10685,sampleNames(myrow)[FTB == 'CON']]),
         log2(X[10685,sampleNames(myrow)[FTB == 'LTB']]),
         log2(X[10685,sampleNames(myrow)[FTB == 'PTB']]),
         names = c("CON", "LTB", "PTB"))
title("Bean Plot of Row Data as Function of TB Phenotype")

#----------------------#
# Prblem 3
#---------------------#

library(gplots)
best20 <- order(myPvals)[1:20]
x.best <- X[best20,]
heatmap.2(X[best20,], main="20 student features", scale = "row", trace="none",key = T)
heatmap.2(X[best20,], main="20 student features", scale = "row", trace="none", labCol = FTB) 
# change sample names into group name
# Does a decent job discriminating the groups



#-----------------------#
# Problem 4
#----------------------#

library(affy)
library(affyPLM)
# this provides an AffyBatch object
load("PSpikeAffyBatch.RData")

spikeDF <- read.table(file="AffyProbeSpikeValues.csv",sep="\t")
levels(spikeDF[,2])
summary(spikeDF[,2])

# grab Spike fold changes for all entries as numeric ... so anything that was not a number is now an NA
SpikeFC <- as.numeric(levels(spikeDF[,2])[spikeDF[,2]])

# grab IDs
names(SpikeFC) <- spikeDF$V1

# remove NAs
nonZeroDX <- which(!is.na(SpikeFC) & (SpikeFC != 0)) 
spikeFC.clean <- SpikeFC[nonZeroDX]

# check how many genes are left in dataset
length(spikeFC.clean)

# the eight routes
bgcorrect.mtd <- c("rma", "mas", "rma", "mas", "rma", "none", "mas", "mas")
normalized.mtd <- c("constant", "quantiles", "quantiles", "loess", "loess", "constant", "qspline", "qspline")
pmcorrect.mtd <- c("pmonly", "pmonly", "subtractmm", "mas", "mas", "pmonly", "subtractmm", "mas")
summary.mtd <- c("mas", "mas", "avgdiff", "medianpolish", "medianpolish", "avgdiff", "mas", "mas")

route.expsets <- list()
for (i in 1:length(bgcorrect.mtd)){
  routes <- expresso(affydata, 
                     bgcorrect.method = bgcorrect.mtd[i], 
                     normalize.method = normalized.mtd[i],
                     pmcorrect.method = pmcorrect.mtd[i], 
                     summary.method = summary.mtd[i])
  route.expsets[[i]] <- exprs(routes)[nonZeroDX,]
}
length(route.expsets)

# create labels for multitesting class labels -- 18 samples, 9 control, 9 experimental
labels <- factor(c(rep(0, 9), rep(1, 9))) #0 is control, 1 is experimental

library(multtest)
library(pROC)
stats <- list()
for (i in 1:length(route.expsets)){
  testing.routes <- mt.maxT(route.expsets[[i]], classlabel = labels, B = 10000) #conduct multiple t test for 10000 permutations  
  stats[[i]] <- testing.routes$adjp[order(testing.routes$index)]
}

nrow <- nrow(route.expsets[[1]])
myresponse <- rep(NA, nrow)
myresponse[which(spikeFC.clean == 1)] = 1 #if the spike value is 1 ... assign as 0s in matrix ... 1s are the control	
myresponse[which(spikeFC.clean != 1)] = 0 #if spike value is not 1 ... assign as 1s in the matrix ... 0s are exp.
roc.fnct <- function(x){roc(response = myresponse, predictor = abs(x), plot=TRUE, print.auc=TRUE)} #apply roc function on input 
roc <- lapply(stats, roc.fnct) #apply roc function on all the ordered test statistics in the list stats

# make roc curves
pdf('homework1-question4-ROCcurves.pdf')
rainbow <-  palette(rainbow(length(route.expsets)))
plot(roc[[1]], main = "ROC curves for different normalization routes using expresso()", col=rainbow[1])
legendText <- c()
for(i in 1:length(route.expsets)){
  plot(roc[[i]], add=TRUE, col=rainbow[i])
  legendText[i] <- paste(bgcorrect.mtd[i],"/",normalized.mtd[i],"/", 
                         pmcorrect.mtd[i],"/",summary.mtd[i], "   AUC: ", round(as.numeric(roc[[i]]$auc),3), sep="")
}
legend("bottomright",
       legendText,
       lty=c(rep(1,length(route.expsets))), 				
       lwd=c(rep(3,length(route.expsets))),
       col=rainbow)
dev.off()
















