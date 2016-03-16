setwd("/Users/aarizvi/Desktop/wk11/Data_HW1(1)/")
install.packages("xlsReadWrite")
list.files()

# HOMEWORK #1
#         Perform student’s t-test on a breast cancer dataset to identify genes differently 
#expressed between good prognosis (> 5 years) and bad prognosis (<= 5 years) with p-values 
#less than 0.05 and compute FDRs using Benjamini–Hochberg method 
# •	Plot in the same figure P-values and FDRs in an ascending order using two different colors 
# •	The data will be posted in the class website 
# •	Hint:  there are some software packages written in Python that contain the BH method 


#fdr = false discovery rate

expression <- read.table("expression.txt", header=TRUE)
expression <- log2(expression + 0.01)
survival_time <- read.csv("survivial_time.csv", header=TRUE)


expression.2 <- rbind(expression,survival_time$Survival.Time..in.days.)

good <- expression.2[,which(expression.2[25135,] > 1826.21)]
good <- good[-25135,]
bad <- expression.2[,which(expression.2[25135,] < 1826.21)]
bad <- bad[-25135,]

combined = cbind(good, bad)

library(limma)
colnames(combined) <- c(paste(colnames(combined[1:50]), "G", sep="_"), 
                        paste(colnames(combined[51:100]), "B", sep="_"))
cols <- cbind(colnames(combined), c(rep(c("G","B"), 50)))
target <- as.data.frame(cols)
colnames(target) <- c("ID", "GB")
rownames(target) <- colnames(combined)
target <- target[sort(target$GB),]
paired_pca <- factor(target$ID)
Treat <- factor(target$GB, levels=c("G","B"))
design.matched <- model.matrix(~paired_pca+Treat)
rownames(design.matched) <- colnames(combined)
matched.fit <- lmFit(combined, design=design.matched)
matched.fit <- eBayes(matched.fit)
results.matched <- topTable(matched.fit, coef=2, number=100, adjust="BH")
#compute t-test
x <- results.matched$P.Value < 0.05

#5 years in days 1826.21




#########################
# 
# HOMEWORK #2
# •     Implement the K-means method using Python and test the code on the Old Faithful data 
# •	Plot the result in each iteration
# •	The data is available at: 
#         •	http://www.stat.cmu.edu/~larry/all-of-statistics/ =data/faithful.dat 
#########################
