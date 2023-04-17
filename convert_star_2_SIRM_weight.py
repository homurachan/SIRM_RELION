#!/usr/bin/env python

import math, os, sys
try:
	from optparse import OptionParser
except:
	from optik import OptionParser

def main():
	(starfile, fscfile) =  parse_command_line()
	g = open(starfile, "r")
	r=open(fscfile,"w")
	star_line=g.readlines()
	r.write("# RELION; version 3.0.8\n\ndata_\n\nloop_\n\n_rlnSpectralIndex #1\n_rlnGoldStandardFsc #2\n") 
	for i in range(0,len(star_line)):
		if(star_line[i].split()):
			if str(star_line[i].split()[0])=="_rlnSpectralIndex":
				res_index=int(star_line[i].split('#')[1])
			if str(star_line[i].split()[0])=="_rlnFourierShellCorrelationCorrected":
				nus=int(star_line[i].split('#')[1])
				n=i

	for i in range (n+5,len(star_line)):
		if len(star_line[i].split())==0:
			break
		res=star_line[i].split()[res_index-1]
		fsc=star_line[i].split()[nus-1]
		r.write(str(res)+"\t"+str(fsc)+"\n")

	g.close()
	r.close()

	
def parse_command_line():
	usage="%prog <starfile> <SIRM weight filename>"
	parser = OptionParser(usage=usage, version="%1")
	
	if len(sys.argv)<3: 
		print "<starfile> <SIRM weight filename>"
		sys.exit(-1)
	
	(options, args)=parser.parse_args()
	
	starfile = args[0]
	fscfile = args[1]
	return (starfile, fscfile)

if __name__== "__main__":
	main()


			
