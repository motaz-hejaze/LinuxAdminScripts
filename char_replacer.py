#!/usr/bin/python3.6
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
print("here")
for filename in os.listdir(dir_path):
	if filename.endswith(".php"):
		print(filename)
		s = open(filename).read()
		s = s.replace('=&' , '=')
		f = open(filename , 'w')
		f.write(s)
		f.close()
