#!/usr/bin/python3

__author__ = "Patrick Powell"
__copyright__ = "Copyright 2017, Patrick Powell"
__email__ = "patrickopowell@gmail.com"

import urllib
import httplib
from urlparse import urlparse
import threading
import logging
import sys

class Counter(object):
    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start
    def increment(self):
        logging.debug('Waiting for lock')
        self.lock.acquire()
        try:
            logging.debug('Acquired lock')
            self.value = self.value + 1
        finally:
            self.lock.release()

class Writer(object):
	def __init__(self, start):
		self.lock = threading.Lock()
		self.file = start

	def writefile(self, url):
		logging.debug('Waiting for lock')
		self.lock.acquire()
		try:
			logging.debug('Acquired lock')
			self.file.write(url + "\n")
		finally:
			self.lock.release()
			
def worker(num, w, total, writer):	
	count = 0
	isCollege = 0
	new = 0
	
	print("Worker[" + str(w) + "]: range[" + str(num) + ", " + str(num + perThread) + "]\n")

	for k in range (num, num + perThread):
		isCollege = 0
		for i in range(1, 3):
			dir = str(i)
			for j in range(1, 1000):
				img = str(j).zfill(4)
				group = str(k)
					
				p = urlparse('https://www.photospecialties.com/Images/Graduation/2017/' + group + '/0000' + dir + '/' + img + '.jpg')
				conn = httplib.HTTPConnection(p.netloc)
				conn.request('HEAD', p.path)
				response = conn.getresponse()

				if response.status == 404:
					break
					
				total.increment()
				isCollege = 1
			
				writer.writefile('https://www.photospecialties.com/Images/Graduation/2017/' + group + '/0000' + dir + '/' + img + '.jpg\n')

			if not isCollege:
				break

		if not isCollege:
			continue
		else:
			print("Worker[" + str(w) + "]\nCollege Code: " + str(k) + " " + str(total.value))
			writer.writefile("\nCollege Code: " + str(k) + ", Total = " + str(total.value) + "\n\n")
	
	writer.writefile("\n\n----- RUNNING TOTAL: " + str(total.value) + " -----\n\n")		
	print("running total: " + str(total.value))

min = 26990000
max = 30000000
numThreads = 25
perThread = (max - min) / numThreads
filename = "filenames.txt"

file = open(filename, "a")

threads = []
writer = Writer(file)
counter = Counter()

for i in range(numThreads):
	t = threading.Thread(target=worker, args=(min + i*perThread, i, counter, writer,))
	threads.append(t)
	t.start()

	
