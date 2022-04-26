sample_list = [10,20,60,30,20,40,30,60,70,80]
new = [] # defining output list

for a in sample_list:

	# checking the occurrence of elements
	n = sample_list.count(a)
	
	# if the occurrence is more than one we add it to the output list
	if n > 1:		

		if new.count(a) == 0: # condition to check

			new.append(a)
print(new)


