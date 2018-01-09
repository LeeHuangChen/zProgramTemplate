import os
import Configuration as conf
import util


def forAllInputFiles(doworkwithfile):
	inputfiles=os.listdir(conf.inputFolder)

	for i, inputfile in enumerate(inputfiles):
		doworkwithfile(i,inputfile)

def main():
	pass

if __name__ == '__main__':
	main()