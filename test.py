#!/usr/bin/env python
from TestModule import FooClass

foo=FooClass()
foo.showName()
foo.showVersion()
print foo.addMe2Me(1)
print foo.addMe2Me("xyz")

foo=FooClass("Lin Zhang")
foo.showName()
foo.showVersion()
print foo.addMe2Me(2.23)
print foo.addMe2Me("abc")
print __name__
