def add (a, b):
	return a+b
print add (1, 2)


k = 17
list = [1, 4, 10, 56, 78]
listLength = len(list)

def adds_up:
	i = 0
	while i<listLength:
		j = 1
		while j<=listLength:
			if (list[i] + list[j] == k):
				return True
			else:
				j++
	i++
		

print listLength


myList=[1,7,9,3,1,2,8]
seen = []
for number in myList:
    if number in seen:
        print "Number repeated!"
    else:
        seen.append(number)
	
