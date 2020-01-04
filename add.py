def add (a, b):
	return a+b
print (add (1, 4))

myList=[1,7,9,3,1,2,8]
seen = []
for number in myList:
    if number in seen:
        print ("Number repeated!")
    else:
       seen.append(number)
print ("Hello World")
