import random
from termcolor import colored

# This program generates a list of excerpts based on a series of file inputs containing lists of excerpts by instrument.

def main():
	# initialize sets
	xylo = []
	snare = []
	bell = []
	cymb = []
	tamb = []
	timp = []

	# load excerpts into the sets
	load(xylo,"xylophone.txt")
	load(snare,"snare.txt")
	load(bell,"bells.txt")
	load(cymb,"cymbals.txt")
	load(tamb,"tambourine.txt")
	load(timp,"timpani.txt")

	# generate random list of excerpts based on user input and write them to a file
	f = open("mockList.txt", "w+")
	f.write("Mock Audition List\n\n")

	f.write("Xylophone Excerpts:\n")
	randomList(xylo,int(input("how many xylo excerpts: ")), f)

	f.write("\nSnare Excerpts:\n")
	randomList(snare,int(input("how many snare excerpts: ")), f)

	f.write("\nBell Excerpts:\n")
	randomList(bell,int(input("how many bell excerpts: ")), f)
	
	f.write("\nCymbal Excerpts:\n")
	randomList(cymb,int(input("how many cymb excerpts: ")), f)
	
	f.write("\nTambourine Excerpts:\n")
	randomList(tamb,int(input("how many tamb excerpts: ")), f)
	
	f.write("\nTimpani Excerpts:\n")
	randomList(timp,int(input("how many timp excerpts: ")), f)

	f.close()

	return None


# creates lists of excerpts, where listName = list var. and excerptList = file w/ list of all excerpts
def load(listName,excerptList):
	# open list of excerpts in read mode
	excerpts = open(excerptList, "r")

	# iterate over excerpt and add it to the list
	for line in excerpts:
		listName.append(line.strip("\n"))

	excerpts.close()

	return None

# writes a list of random excerpts to an output file, where listName = list var., n = # excerpts chosen, and outfile = file to write the list to
def randomList(listName,n,outfile):
	# use system time as a seed to ensure different results
	random.seed()

	# check inputs and print out appropriate response for various inputs
	if n > len(listName):
		print(colored("chosen number of excerpts is more than number in the list so all excerpts will be chosen", "blue"))
		n = len(listName)
	elif n == len(listName):
		print(colored("you have chosen all of the excerpts from the list", "blue"))

	# generate random list of numbers and write the corresponding excerpt to a file
	randIntList = random.sample(range(0,len(listName)),n)
	for index in randIntList:
		outfile.write(listName[index]+"\n")
	
	return None

if __name__ == "__main__":
	main()