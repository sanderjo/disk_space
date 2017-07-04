#!/usr/bin/env python
import os
import sys
import subprocess
import time

print "python version:", sys.version

try:
	_dir = sys.argv[1]
except:
	print "Please specify directory ... exiting."
	sys.exit(-1)

print "Directory", _dir
s = os.statvfs(_dir)
print "statvfs" , s

GB = float(1024**3)
disk_size = float(s.f_blocks) * float(s.f_frsize) / GB
available = float(s.f_bavail) * float(s.f_frsize) / GB

print "disk_size [GB]", disk_size
print "available [GB]", available

command = ("df -m " + _dir).split()

millis1 = int(round(time.time() * 1000))
p = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
result = p.stdout.readlines()
millis2 = int(round(time.time() * 1000))

print "The df took [ms]:", millis2-millis1

for line in result: 
	if line.find("/") >= 0 :
		print line.rstrip()
		print "Available [MB]:",  line.split()[3]

