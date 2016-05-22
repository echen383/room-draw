import csv
from collections import deque

list2015 = list()
list2016 = list()

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

# 2015 lists
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
        		list2015.append(row[0])
        except ValueError:
        	pass

# 2016 lists
first = True
firstSoph = True
with open('2016number.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"')
    for row in reader:
    	if(row[1].find('Jun') != -1 and first):
    		lowerBound = int(row[2])
    		first = False
    	if(row[1].find('Soph') != -1 and firstSoph):
    		upperBound = int(row[2]) - 1
    		firstSoph = False

highestLow = (upperBound-lowerBound)/3 + lowerBound

with open('2016name.csv', 'rb') as f2:
    reader = csv.reader(f2)
    for row in reader:
    	try:
    		if(row[1].find('Jun') != -1 and int(row[2]) > highestLow):
        		list2016.append(row[0])
        except ValueError:
        	pass

highList = list(set(list2016).intersection(set(list2015)))
highList.sort()

print len(list2015)
print len(list2016)
print len(highList)

# for element in highList:
# 	print(element)

with open('high.csv', 'wb') as f:
    writer = csv.writer(f)
    for element in highList:
    	f.write("%s\n" % element)

