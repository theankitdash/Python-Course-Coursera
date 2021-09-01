import re

fname = input('Enter File name :')

handle = open(fname)

sum = 0

count = 0

for line in handle:
    temp = line.strip()
    temp = re.findall('[0-9]+', temp)

    if len(temp) > 0:
        for w in temp:
            count = count + 1
            sum = sum + int(w)

print ('There are', count, 'values with a sum =', sum)
