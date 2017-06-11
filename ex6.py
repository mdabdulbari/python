x = f"There are {10} types of people." # using %d for variable
binary = "binary" # string
do_not = "don't" # string
y = f"Those who know {binary} and those who {do_not}" # using two strings in a variable

print(x) # printing
print(y) # printing

print(f"I said: {x}.") #printing using %r
print(f"I also said: '{y}'.") #printing using string

hilarious = False #variable
joke_evaluation = "Isn't that joke so funny?! {}" #using %r in a variable

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."
print(w + e)
