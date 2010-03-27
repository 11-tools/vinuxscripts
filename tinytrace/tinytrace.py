#!/usr/bin/python

# This is a tiny debugger which offers trace capability to
# a log file.  Set tinytrace.Enabled to True to start tracing.

import sys
import os

tinytrace_enabled = False
tinytrace_file = open('/tmp/trace.log', 'w')
print >>tinytrace_file, "Starting trace"
tinytrace_file.close()
os.chmod('/tmp/trace.log', 0666)

def Enable():
    global tinytrace_enabled
    tinytrace_enabled = True

def Disable():
    global tinytrace_enabled
    tinytrace_enabled = False

def logTrace(message):
    global tinytrace_file
    tinytrace_file = open('/tmp/trace.log', 'a')
    print >>tinytrace_file, message
    tinytrace_file.close()

def frameLocation(frame):
    prevFrame = frame.f_back
    lineno = frame.f_lineno
    function = frame.f_code.co_name
    location = "%s-%s" % (function, lineno)
    if prevFrame != None:
        return "%s.%s" % (location, frameLocation(prevFrame))
    return location

def fileLocation(frame):
    framePath = frameLocation(frame);
    return "%s: %s" % (frame.f_code.co_filename, framePath)

def traceit(frame, event, arg):
    if not tinytrace_enabled:
	return traceit
    if event == "line":
        logTrace(fileLocation(frame))
    elif event == 'call':
        pass
    elif event == 'exception':
        pass
    elif event == 'c_call':
        pass
    elif event == 'c_return':
        pass
    elif event == 'c_exception':
        pass
    return traceit

sys.settrace(traceit)
