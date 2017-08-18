#!/usr/bin/env python
filename=raw_input("Enter the file name you hope to display:")
try:
	logfile=file(filename,"r")
	for eachLine in logfile:
		print eachLine
	logfile.close()
except IOError, e:
	print "File open error:", e
