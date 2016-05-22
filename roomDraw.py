import csv
from collections import deque

first = True
upperBound = -99
lowerBound = -99

def get_last_row(csv_filename):
    with open(csv_filename, 'r') as f:
        try:
            lastrow = deque(csv.reader(f), 1)[0]
        except IndexError:  # empty file
            lastrow = None
        return lastrow

with open('2015number.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"')
    for row in reader:
    	if(row[1].find('Soph') != -1 and first):
    		lowerBound = int(row[2])
    		first = False

upperBound = int(get_last_row('2015number.csv')[2])
highestLow = (upperBound-lowerBound)/3 + lowerBound

with open('2015name.csv', 'rb') as f2:
    reader = csv.reader(f2, delimiter=',', quotechar='"')
    for row in reader:
    	try:
    		if(int(row[2]) > highestLow):
        		print row
        except ValueError:
        	pass

