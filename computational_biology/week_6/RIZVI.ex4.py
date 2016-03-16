from __future__ import division
import sys

def parseblast(blast):
	with open(blast,'r') as f:
		blastlist = [] #empty list to append blast
		for line in f:
			line = line.rstrip() #removes trailing characters
			if line.startswith("#"): #skip headers
				continue
			else:
				line = line.split("\t") #split the tabs
				blastlist.append(line) #append the hits (with duplicates) into a list
		hits = 0 #start counting hits at 0
		blastdict = {} #empty dictionary to be appended to in for loop
		for ids in range(0,len(blastlist)):
			query = blastlist[ids][0]
			subject = blastlist[ids][1]
			if query in blastdict:
				if subject in blastdict[query]: 
					continue
				else:
					hits += 1 #start counting subjects (values) that are in query (keys)
					blastdict[query] += subject #makes dictionary of key (query) and values (subject)
			else:
				blastdict[query] = subject  
				hits += 1
		return blastdict, hits	 

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
	parse = parseblast(file)
	hits = parse[1]
	print 'total number of hits are:    ',hits
	queries = len(parse[0])
	print 'total number of queries are: ',queries
	avghpq = hits/queries
	print 'average hits/queries are:    ',avghpq

if __name__ == "__main__":
    main(sys.argv[1])