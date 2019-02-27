def add (a, b):
	return a+b
print add (1, 2)


k = 17
list = [1, 4, 10, 56, 78]
listLength = len(list)

#for i in list:

print listLength


myList=[1,7,9,3,1,2,8]
seen = []
for number in myList:
    if number in seen:
        print "Number repeated!"
    else:
        seen.append(number)
	
