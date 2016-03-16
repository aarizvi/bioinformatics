
###################################
######### Old Faithful ############
###################################

setwd("/Users/aarizvi/Desktop/")


old_faithful <- read.table("old faithful.txt", header=TRUE)

#check distribution of variables
jpeg(filename="wk11-hw2-density-eruption", width = 1200, height = 1000, units="px", pointsize = 16, quality = 100)
plot(density(old_faithful$eruptions))
dev.off()

jpeg(filename="wk11-hw2-density-waiting", width = 1200, height = 1000, units="px", pointsize = 16, quality = 100)
plot(density(old_faithful$waiting))
dev.off()

#the distributions show that there are clearly two normally distributed groups

library(ggplot2)
jpeg(filename="wk11-hw2-kmeans-default-alg", width = 1200, height = 1000, units="px", pointsize = 16, quality = 100)
ggplot(data=x, aes(x=eruptions, y=waiting, color=cluster )) + geom_point() + geom_point(data=centers, aes(x=eruptions,y=waiting, color='Center')) + geom_point(data=centers, aes(x=eruptions,y=waiting, color='Center'), size=52, alpha=.3, show_guide=FALSE)
dev.off()
k$iter 
#see how many iterations there are. there is only 1 iteration.   if there were more iterations, however,
#does not seem like R has an easy way to implement plotting per iteration
#"Lloyd" algorithm seems have more iterations than the default one.  

#install.packages("cclust")
library(cclust)
of <- old_faithful[,-3]

#tried cclust to see if any different than kmeans - 'changes' object within result was interesting 
#and more objects are available in the list produced

cl <- cclust (as.matrix(of), 2, iter.max=100, dist="euclidean",method= "kmeans")
plot(as.matrix(of), col=cl$cluster)

