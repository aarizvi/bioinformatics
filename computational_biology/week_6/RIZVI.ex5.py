from __future__ import division
import sys

def revised_output(blast):
	with open(blast,'r') as f:
		blastlist = [] #empty list to append blast
		for line in f:
			line = line.rstrip() #removes trailing characters
			if line.startswith("#"): #skip headers
				continue
			else:
				line = line.split("\t") #split the tabs
				blastlist.append(line) #append the hits (with duplicates) into a list

		blastv2 = [] #empty list for revised output
		count = 0 #set count to 0
		for ids in range(0,len(blastlist)): 
			query = blastlist[ids][0] #indices for requested columns
			subject = blastlist[ids][1]
			percentid = blastlist[ids][2]
			alignlen = blastlist[ids][3]
			evalue = blastlist[ids][10]
			if (query == subject):
				continue
			elif (float(percentid) < int(95)): #remove percent ID < 95%
				continue
			elif (float(evalue) > 0.1):  #remove e-values > 0.1
				continue
			else:
				blast = [query,subject,percentid,alignlen,evalue]
				blastv2.append(blast)
			if float(alignlen) < 20: #if alignment length <20 ... start counting
				count += 1
			else:
				continue
		return blastv2, count

def writefile(blastoutput, stats):
	output = blastoutput
	output2 = ''.join(str(output))
	myfile = open("RIZVI.ex5.output.txt", 'w')
	myfile.write("".join("%s"%output2))
	myfile.close()

	totalhits = str(len(blastoutput))
	alihits = str(stats)

	statfile = open("RIZVI.ex5.stats.txt", 'w') 
	statfile.write('total number of hits are:         ')
	statfile.write(totalhits)
	statfile.write("\n")
	statfile.write('numbers of hits less than 20 are: ')
	statfile.write(alihits)
	statfile.write("\n")
	statfile.close()

def main(file):
	blast = revised_output(file)
	output = writefile(blast[0], blast[1])

if __name__ == "__main__":
    main(sys.argv[1])