#!/usr/bin/env python
import time

def function_performance_statistics(trace_this=True):
	if trace_this:
		def performance_statistics_delegate(func):
			def counter(*args, **kwargs):
				start=time.time()
				print '---------Started at %d----------'%start
				func(*args, **kwargs)
				end=time.time()
				print '---------Ended at %d----------'%end
				print 'used time:%d'%(end-start,)
			return counter
	else:
		def performance_statistics_delegate(func):
			return func
	return performance_statistics_delegate

@function_performance_statistics(trace_this=True)
def add(x,y):
	time.sleep(3)
	print 'add result:%d'%(x+y,)

@function_performance_statistics(trace_this=False)
def mul(x, y=1):
	print 'mul result:%d'%(x*y,)


add(1, 1)
mul(10)
