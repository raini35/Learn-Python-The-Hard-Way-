#sys is a module. module. module. module 
#from sys import argv 

#Take whatever is in argv, unpack it, and assign it to the variables
#script, first, second, third = argv

#print "The script is called: ", script 
#print "Your first variable is: ", first
#print "Your second variable is: ", second 
#print "Your third variable is: ", third


#Study Drill for Exercise 13
from sys import argv
 
script, name = argv

print ("Hellow %r, how's your day going?" % name) 
x = raw_input('>>>')

print('Did you say "%r"?' %x)

