name = 'Abdul Bari'
age = 21 # not a lie
height = 65 # inches
weight = 154 # lbs
eyes = 'Black'
teeth = 'White'
hair = 'Black'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "It's %r in Kgs" % (weight * 0.45)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
print "%r" % False
print "%s" % "This is a string."
print round(2.434543)
