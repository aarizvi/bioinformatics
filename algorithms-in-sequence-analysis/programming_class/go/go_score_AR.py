import sys

def getMapping(mapFile):
    #open the file
    file = open(mapFile)
    #result is a list that will contain several dictionaries
    result = []
    #skip the first line, we don't care about the header
    first_line = file.readline()
    length_column = len(first_line.split('\t')) 

    for i in range(length_column-1): #write about why the column is -1
        d = {}
        result.append(d)
    
    for line in file:   
        columns = line.strip('\n').split('\t')
        for i in range(1, len(columns)):
            ids = columns[i]
            id_dict = result[i-1]
            if not id_dict.has_key(ids) and ids != '':
                id_dict[ids] = columns[0]
    return result     
    
def parseGO(mappingList, GO_file, blacklist):
    #open the file
    file = open(GO_file)
    #this will be the dictionary that this function returns
    #entries will have a key as an Ensembl ID
    #and add the value will be a set of GO terms
    result = {}
    
    skipped = 0 #going to count the number of skipped lines by the specificed evidence codes .... skipped line count starts at 0 and will start from 0 before the counting occurs through the iterations
    for line in file:
        if line[0] != '!':
            columns = line.strip('\n').split('\t')
            prot_ID = columns[1] #the 2nd column is in the '1' position because it starts at 0
            GO_term = columns[4]
            source  = columns[6] #goes to the 7th column of the GO file (where the evidence code is)
            
            if source not in blacklist: #if the 7th column doesnt have any items in 'blacklist' list, then continue with creating mapping list
                mappedProt_ID = eNon  #assigns an empty string 
                for mapDict in mappingList:
                    if mapDict.has_key(prot_ID):
                        mappedProt_ID = mapDict[prot_ID]
                        break
                if not result.has_key(mappedProt_ID):
                    result[mappedProt_ID] = set()
                result[mappedProt_ID].add(GO_term)
            else:
                skipped += 1
    return result, skipped
    
def computeScore(alignmentFile, GO1, GO2):
    #result will hold the score of alignment and is intialized to 0
    result = 0
    
    #open the file
    file = open(alignmentFile)
    nlines = 0
    for line in file:
        nlines += 1
        id1 = line.split()[0] 
        id2 = line.split()[1] 
        try:
            gp1 = GO1[id1] #species 1 in argument identifiers in column 1
            gp2 = GO2[id2] #spceies 2 in argument identifiers in column 2 
  
            score = float(len(gp1.intersection(gp2)))/float(len(gp1.union(gp2)))
            result = result + score
        except KeyError:
            pass 
    print 'Sum of Jaccard Indices          :', result  #This number was not easily interpreted to me -- so I normalized it by the number of mapping -- seen in the next line
    print ' ^  normalized by # of mappings :', result / float(nlines)
    return result
    
def main(SIF, GO1, GO2, MAP1, MAP2, blacklist):
    try:
        map1 = getMapping(MAP1)
        map2 = getMapping(MAP2)
        parseGO_subject1,skip1 = parseGO(map1, GO1, blacklist)
        parseGO_subject2,skip2 = parseGO(map2, GO2, blacklist)
        print 'Skipped',skip1,'lines in',GO1
        print 'Skipped',skip2,'lines in',GO2
        compute_score = computeScore(SIF, parseGO_subject1, parseGO_subject2)
    except:
        print "There was an error with the arguments.  Please enter in specific order from correct directories.  The argument order proceeds as the following: 1. alignments; 2. species_1 GO; 3. species_2 GO; 4. species_1 mapping; 5. species_2 mapping; 6. optional: evidence codes"  
    
if __name__ == "__main__":
    blacklist = []
    if len(sys.argv) == 7:
        blacklist = sys.argv[6].split(',') #splits the evidence codes provided in this argument by commma, because if this wasn't done, there would be one more sys argument
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], blacklist)
       
#Put error handling here .... checking whether the # of arguments are correct
