print("x + y + z =", x + y + z,"Nice")
print("Is it less or equal?", 5 <= -2) #prints true or false
print("There are", cars,"cars available.") #using variable in between, the variable is defined earlier
Using f"" and {}
round(2.3897) #rounding off a number

w = "This is the left side of..."
e = "a string with a right side."
print(w + e)
#using strings as variables

print("." * 10) # prints "." 10 times

#using formatter
formatter = "{},{},{},{}"
print(formatter.format(1,2,3,4))

#using \n for next line
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print("Here are the months:", months)

# \t = tab
# \n = next line

input() #using input to take value

# taking input from argv
from sys import argv
script, first, second, third = argv

#using symbol before the input
prompt = "> "
likes = input(prompt) #shows > symbol before the input

txt.read #read a file
open(filename) # open filename
#take filename as input from the user

#Erase something in a file and write from another file

target = open(filename, 'w')
target.truncate() #deletes everything in the target file
truncate - deletes
'W' - opening the file in write mode
'r' - opening the file in read mode
target = open(filename, 'w')
line1 = input("line1: ") #takes input from user
target.write(line1) #writes line1 in the target file

#copy from one file to another
CAN'T UNDERSTAND - from os.path import exists
in_file = open(from_file) #opens the from file
indata = in_file.read()   # assigns the data in the "from file" to in data
out_file = open(to_file, 'w') # opens the "to file" in 'W'- write mode
out_file.write(indata) # writes "in data" in the "to file"
