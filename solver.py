#########################################################
## FileName    : solver
## Input       : Dictionary File and The Jumbled word
## Description : returns all possible words found in the 
##            dictionary for that combinations of string
#########################################################
import sys
import itertools
dictionary=[]

#########################################################
### createDictionary: takes the dictionary location
###                as input and populates the dictitionary
##########################################################
def createDictionary(filePath):
    global dictionary
    try:
        f = open(filePath,'r')
    except IOError:
        print 'cannot open', filePath
	sys.exit(0)
    line = f.readline()
    while line :
        dictionary.append(line.strip().lower())
        line = f.readline()
    ## creating a set of dictionary
    dictionary = set(dictionary)
    f.close()

##########################################################
## permute function takes a string and return a list of
## all possible permutaions 
##########################################################
def permute(jumbledWord):
    return ["".join(p) for p in itertools.permutations(jumbledWord, len(jumbledWord,))]

def main():
    """This application takes a jumbled word string and returns all possible words found in the dictionary for that combinations of string"""
    if(len(sys.argv) <= 1):
	print "This program takes two arguments <Dictionary_file> <series of characters>"
	sys.exit(1)

    createDictionary(sys.argv[1])
    found = False
    ## creating the string of jumbledWord from the given series of characters
    jumbledWord = "".join(" ".join(sys.argv[3:]).split());
    words = [];
    toRestrictWordLength = 0 != int(sys.argv[2]);
    for length in range(3, len(jumbledWord)+1):
        for combination in ["".join(p) for p in itertools.combinations(jumbledWord,length)]:
            # print combination
            if(not toRestrictWordLength or len(combination) == int(sys.argv[2])):
                for each in sorted(set(permute(combination))):
                	if (each.lower() in dictionary):
                	    found = True
                	    words.append(each)

    length = 2;
    if(found == False):
	   print "No word found in dictionary for the character"," ".join(sys.argv[3:])
    else:
        for each in  sorted(words, key=lambda x: (len(x),x)):
            if(len(each) > length):
                length = len(each);
                print "\n============ "+ str(length) +" character words =============\n"
            print each

if __name__ == '__main__':
    main()
