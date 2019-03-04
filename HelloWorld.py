#To run code have code runner extension installed and hit CTRL ALT N on Windows or Control Option N on Mac

message = "Hello World"
print (message)

k = 57
list = [1, 4, 10, 56, 78]

def sum_equal_num (arr, num):
	list_length = len(arr)
	i = 0
	j = 1
	while (i < list_length-2):
		while (j < list_length-1):
			if ((arr[i]+arr[j]) == num):
				return True
			j = j+1
		i = i+1
	return False

answer = sum_equal_num (list,k)

print (answer)
