#/usr/bin/env python
fname = raw_input("Enter file name:")
print

try:
	fobj = file(fname)
except IOError, e:
	print "***File open error:",e
else:
	for eachLine in fobj:
		print eachLine,
	fobj.close()
