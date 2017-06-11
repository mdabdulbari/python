x = "There are %d types of people." % 10 # using %d for variable
binary = "binary" # string
do_not = "don't" # string
y = "Those who know %s and those who %s" % (binary, do_not) # using two strings in a variable

print x # printing
print y # printing

print "I said: %r." % x #printing using %r
print "I also said: '%s'." % y #printing using string

hilarious = False #variable
joke_evaluation = "Isn't that joke so funny?! %r" #using %r in a variable

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."
print w + e
