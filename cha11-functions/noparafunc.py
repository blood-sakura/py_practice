#/usr/bin/env python
def testfunc(**profile):
	print 'profile type=%s'%type(profile)
	print 'profile = %s'%str(profile)

testfunc(name='lin zhang', age=34,gender='male')
testfunc(name='shippo', company="Kohler")
args={'arg1':'arg value1', 'arg2':'arg value2', 'arg3':'arg value3'}
testfunc(**args)
	
