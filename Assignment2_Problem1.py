# Tyson Spoelma
# MTH 325
# Assignment 2
# Problem 1
# The program asks the user about his age in years
# and converts it into seconds and prints it out.
print "Problem 1:"
print "How old are you in years? \n",
years = raw_input()
years = int(years)
ageInSeconds = years*365*60*60*24
print "You are %i seconds old." % (ageInSeconds)


print "\nProblem 2 is about to appear"
# Problem 2
p = (3 < 4)  # should be true
q = (3 == 4) # should be false
r = (5 > 2)  # should be true

print '\nProblem 2a: (p and q) or r'
print 'Evaluation: ',(p and q) or r # should be true

print '\nProblem 2b: (p and q) -> r'
# (p -> q) = (-p or q)
print 'Evaluation: ', not (p and q) or r # should be true
