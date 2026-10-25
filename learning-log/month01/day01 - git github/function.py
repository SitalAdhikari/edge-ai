# Write a function that calculates the average of a list of numbers.

li = [1,2,3,4,5]

def average(li):
	sum = 0
	count = 0
	for i in li:
		sum = sum+i
		count = count +1
	return sum/count

avg = average(li)
print("Average", avg)
