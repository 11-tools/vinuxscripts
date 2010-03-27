#!/usr/bin/python
import tinytrace

def foo():
   print "In foo"

def bar():
   print "In bar"
   foo()

tinytrace.Enable()
foo()
bar()
