#To run code have code runner extension installed and hit CTRL ALT N on Windows or Control Option N on Mac

message = "Hello World"
print (message)

k = 60
list = [1, 4, 10, 56, 78]
listLength = len(list)
print (listLength)

i = 0
while i<=(listLength-2):
	j = 1
	while j<=(listLength-1):
		#print (i, j)
		if (list[i]+list[j]==k):
			print ("True")
		j = j+1
	
	i = i+1
	print ("False")

