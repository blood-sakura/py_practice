#!/usr/bin/env python
class FooClass(object):
	"""my very first class:FooClass"""
	version = 0.1
	def __init__(self, name="Shippo Zhang"):
		"""constructor"""
		self.name=name
		print "Created a class instance for",self.name
	
	def showName(self):
		"""display instances attribute and class name"""
		print "Your name is %s"%self.name
		print "My name is %s"%self.__class__.__name__
	
	def showVersion(self):
		"""display class static attribute"""
		print self.version
	
	def addMe2Me(self, x):
		"""apply + operation to argument"""
		return x+x
