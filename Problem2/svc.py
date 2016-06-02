#!/usr/bin/env python

import filecmp
import sys,string

alphabets=list(string.ascii_lowercase)+list(string.ascii_uppercase)
numbers=['0','1','2','3','4','5','6','7','8','9']

# Enter the directory Name where the files such as test.txt, test_copy.txt and final.txt are stored
# e.g.:- '/home/yash/' ; don't forget to put the last forward slash
directory='********************'

def version_control(arg):
	if len(arg)>1:
		comp=filecmp.cmp(arg,directory+'test_copy.txt')
		s=[]
		if comp==False:
			f=open(directory+arg,'r')
			copy=open(directory+'test_copy.txt','w')

			for i in f:
				s.append(i)
				copy.write(i)

			f.close()
			copy.close()

			final_file=open(directory+'final.txt','a')
			final_file.write(str(s)+"\n")
			final_file.close()

	elif len(arg)==1 and arg.isdigit():
		final_file=open(directory+'final.txt','r')
		for index,line in enumerate(final_file):
			if index==int(arg):
				print line[:-1]

	
version_control(sys.argv[1])