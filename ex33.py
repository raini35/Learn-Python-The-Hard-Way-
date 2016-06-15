i = 0 
numbers = []  #Empty list created 

def while_loop(total, iterator): 
	i = 0
	while i < total: 
		print "At the top of i is %d" % i 
		numbers.append(i)
	
		i = i + iterator
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i 
	
	print "The numbers: " 

	for num in numbers: 
		print num
		
print "How many numbers?: "
numba = int(raw_input("> "))
print "Increments?: " 
increment = int(raw_input("> "))

while_loop(numba, increment)