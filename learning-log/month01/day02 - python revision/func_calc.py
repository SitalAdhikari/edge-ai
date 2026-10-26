def mean(l1):
	""" To calculate the mean"""
	total=0
	count =0
	for  i in l1:
		total = total + i
		count = count+1
	return total/count

# docstring:
print(mean.__doc__)

def min_max(li):
	""" To calculate the minimum and maximum value in the list"""
	for i in li:
		if (i < min):
			min =i
	for i in li:
		if (i > max):
			max =i			
	print(f" Minimum: {min} \n Maximum: {max}")
	
list = [1,2,3,4,5]
min_max(list)


