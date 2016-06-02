from random import randrange

def calculate(np):
	count = [0 for i in xrange(365)]
	for i in xrange(np):
		count[randrange(365)] += 1
	for x in count:
		if x > 1:
			return 1
	return 0

def paradox():
	num_trials = 1000
	np = int(raw_input('Enter the number of people in set '))
	found_dupe = 0
	for i in xrange(num_trials):
		if calculate(np):
			found_dupe += 1

	print "Probability is: " + str(float(found_dupe)/(num_trials))

paradox()
