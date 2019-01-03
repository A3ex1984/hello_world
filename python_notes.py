#This is the overview of my python notes
#Python Documentation: https://docs.python.org/3/contents.html
#Overview of different Python commands and syntax for me

#Mixed stuff
"/n" #Adds a new line 
Data structures are containers that can include different data types.
A list is an example of a data structure
All data structures are data types
A list is mutable an ordered
Lists are mutable, tuples are not - both are ordered

#Strings
dimensions = 50, 40, 100 # This is a tuple
length, width, height = dimensions #Tuple unpacking; this assigns tuple values to three variables
print ("The dimensions are {}x{}x{}".format(length, width, height) # .format() transforms data to strings to print them

#Variables

print("scores: " + str(scores)) #Converts into a String so that it can get concatenated

#Mutable and non Mutable
Lists are mutable
Tuples are non-mutable
       
#Common methods
len()
max() #In a list of numbers it returns the highest number, in list of strings in returns the one that would appear last in the alphabet
min()
sorted() #creates a copy of a list e.g. print (sorted(sizes, reverse=True)) --> this would give a highest to lowest list
join() # Join is a string method that takes a list of strings as an argument, and returns a string consisting of the list elements joined by a separator string. 
names = ["Carol", "Albert", "Ben", "Donna"]
print(" & ".join(sorted(names)))
# new_str = "\n".join(["fore", "aft", "starboard", "port"]) print(new_str)
append() #A helpful method that adds an element to the end of the list
letters = ['a', 'b', 'c', 'd']
letters.append('z')
print(letters)

# Definition of a function

points = 12

def which_prize(points):
	wooden_rabbit = 50
	no_prize = 150
	wafer_thin = 180
	penguin = 200
	if points <= wooden_rabbit:
		prize = "wooden rabit"
	elif points <= no_prize:
		prize = "No prize"
	elif points <= wafer_thin:
		prize = "wafer-thin mint"
	elif points <= penguin:
		prize = "penguin"
	else:
		prize = "No prize"
	if 51 <= points <= 150:
		return "Oh dear, no prize this time."
	else:
		return "Congratulations! You have won a " + prize + "!"
	
print (which_prize(points))

def welcome_message(name):
#Prints out a personalised welcome message
    return "Welcome to this Python script, " + name + "!"

#Call the welcome message function with the input "Udacity Student" 
#and print the output
print(welcome_message("Udacity Student"))

# Definition of an Array/List (Data Structure)
list_of_random_things = [1, 3.4, 'a string', True]
list_of_random_things[0] # this will return the first item in the list which is 1
list_of_random_things[0:2] #Subset of a list. Lower bound is inclusive and the upper is exclusive. This would return [1, 3.4]
list_of_random_things[-3:] #Subset of a list. Starts with the third to last item and goes to end of array
arr[len(arr) - 1] #Last element of a list
arr[-2] #Second to last element of the list arr

#In or not in 
>>> 'this' in 'this is a string'
True
>>> 'in' in 'this is a string'
True
>>> 'isa' in 'this is a string'
False
>>> 5 not in [1, 2, 3, 4, 6]
True
>>> 5 in [1, 2, 3, 4, 6]
False

#Tuples (Data Structure) - A data type for immutable ordered sequences of elements
location = (13.4125, 103.866667)
print("Latitude:", location[0])
print("Longitude:", location[1])

#Set (Data Structure) - A data type for mutable unordered collections of unique elements
numbers = [1, 2, 6, 3, 1, 1, 6] #This is a list with duplicate items
unique_nums = set(numbers) 
print(unique_nums) # This would remove all the duplicate entries form the list
{1, 2, 3, 6} #This is the result - SINCE SETS ARE UNORDERED YOU CANNOT ADDRESS THEM BY INDEX

fruit = {"apple", "banana", "orange", "grapefruit"}  # define a set
print("watermelon" in fruit)  # check for element
fruit.add("watermelon")  # add an element
print(fruit)
print(fruit.pop())  # remove a random element
print(fruit)
#This is the output
False
{'grapefruit', 'orange', 'watermelon', 'banana', 'apple'}
grapefruit
{'orange', 'watermelon', 'banana', 'apple'}

#Dictionaries and Identity Operators (Data Structures) - Dictionaries store sets of elements
elements = {"hydrogen": 1, "helium": 2, "carbon": 6} #hydrogen is key and 1 is value
print(elements["helium"])  # print the value mapped to "helium"
elements["lithium"] = 3  # insert "lithium" with a value of 3 into the dictionary
print("carbon" in elements)
print(elements.get("dilithium")) #Get looks up things in the dictionary - They will not crash the program though
#Dictionary keys must be immutable


Data Structure 	Ordered 	Mutable 	Constructor 	Example
List 			Yes 		Yes 		[ ] or list() 	[5.7, 4, 'yes', 5.7]
Tuple 			Yes 		No 			( ) or tuple() 	(5.7, 4, 'yes', 5.7)
Set 			No 			Yes 		{}* or set() 	{5.7, 4, 'yes'}
Dictionary 		No 			No** 		{ } or dict() 	{'Jun': 75, 'Jul': 89}

cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }
for key, value in cast.items():
    print("Actor: {}    Role: {}".format(key, value))

#Control Flow 
#conditional statements (if, else, elif) for and while loops, break and continue
#Usally code runs top to bootom every line; control flows allow for selective execution

if phone_balance < 5:
    phone_balance += 10
    bank_balance -= 10

if season == 'spring':
    print('plant the garden!')
elif season == 'summer':
    print('water the garden!')
elif season == 'fall':
    print('harvest the garden!')
elif season == 'winter':
    print('stay indoors!')
else:
    print('unrecognized season')

#First Example - try changing the value of phone_balance
phone_balance = 10
bank_balance = 50

if phone_balance < 10:
    phone_balance += 10
    bank_balance -= 10

print(phone_balance)
print(bank_balance)

#Second Example - try changing the value of number

number = 145
if number % 2 == 0:
    print("Number " + str(number) + " is even.")
else:
    print("Number " + str(number) + " is odd.")

#Third Example - try to change the value of age
age = 35

# Here are the age limits for bus fares
free_up_to_age = 4
child_up_to_age = 18
senior_from_age = 65

# These lines determine the bus fare prices
concession_ticket = 1.25
adult_ticket = 2.50

# Here is the logic for bus fare prices
if age <= free_up_to_age:
    ticket_price = 0
elif age <= child_up_to_age:
    ticket_price = concession_ticket
elif age >= senior_from_age:
    ticket_price = concession_ticket
else:
    ticket_price = adult_ticket

message = "Somebody who is {} years old will pay ${} to ride the bus.".format(age, ticket_price)
print(message)

#Multiple conditions in an if statement; all must be true to execute the code
if is_raining and is_sunny:
    print("Is there a rainbow?")

if (not unsubscribed) and (location == "USA" or location == "CAN"):
    print("send email")
	
	
#Loops - There are for and while loops - They are both control loops
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
for city in cities:
    print(city)
print("Done!")

#Range
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

for index in range(len(cities)): #range(start, stop, step)
    cities[index] = cities[index].title()
	
for i in range(5, 35, 5):
    print(i)
	
	
#While loops
start_num = 5
end_num = 100
count_by = 2
break_num = start_num
while break_num < end_num:
    break_num += count_by
print(break_num)

#Break and continue
break terminates a loop (for or while)
continue skips one iteration of a loop

#Zip
letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))

#Enumerate
letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)

#Try Statement

We can use try statements to handle exceptions. There are four clauses you can use (one more in addition to those shown in the video).

    try: This is the only mandatory clause in a try statement. The code in this block is the first thing that Python runs in a try statement.
    except: If Python runs into an exception while running the try block, it will jump to the except block that handles that exception.
    else: If Python runs into no exceptions while running the try block, it will run the code in this block after running the try block.
    finally: Before Python leaves this try statement, it will run the code in this finally block under any conditions, even if it's ending the program. E.g., if Python ran into an error while running code in the except or else block, this finally block will still be executed before stopping the program.

def party_planner(cookies, people):
    leftovers = None
    num_each = None

    try:
        num_each = cookies // people
        leftovers = cookies % people
    except ZeroDivisionError:
        print("Oops, you entered 0 people will be attending.")
        print("Please enter a good number of people for a party.")

    return(num_each, leftovers)

#Reading a file in Python
f = open('my_path/my_file.txt', 'r') # r indicates that the file is in read-only (which is the default) - you can also use w in order to write to it
file_data = f.read()
f.close()
       
 with open('my_path/my_file.txt', 'r') as f: #Python provides a special syntax that auto-closes a file for you once you're finished using it.
    file_data = f.read()

    #If you pass the read method an integer argument, it will read up to that number of characters, output all of them, and keep the 
    # 'window' at that position ready to read on. 

    Need to learn more VSCode
    Need to sync and not refresh    
    