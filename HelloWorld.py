#To run code have code runner extension installed and hit CTRL ALT N on Windows or Control Option N on Mac

message = "Hello World"
print (message)

k = 17
list = [1, 4, 10, 56, 78]
listLength = len(list)

def adds_up(listLength, k):
	i = 0
	while i<listLength:
		j = 1
		while j<listLength:
			if (list[i] + list[j] == k):
				return True
			else:
				j = j+1
	i = i+1

print adds_up(listLength, k)
		

print listLength