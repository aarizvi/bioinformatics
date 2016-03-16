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

expression <- read.table("expression.txt", header=TRUE)
survival_time <- read.csv("survivial_time.csv", header=TRUE)
survival_time <- t(survival_time)

#5 years in days 1826.21




#########################
# 
# HOMEWORK #2
# •     Implement the K-means method using Python and test the code on the Old Faithful data 
# •	Plot the result in each iteration
# •	The data is available at: 
#         •	http://www.stat.cmu.edu/~larry/all-of-statistics/ =data/faithful.dat 
