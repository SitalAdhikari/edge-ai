import csv
import statistics

latencies=[]
with open("data.csv","r") as file:
	reader = csv.reader(file)
	for row in reader:
		print(row)
	
	file. seek(0)  # return to the beginning
	print(next(reader)) # to know the titles , row[1] below can create the problem so
	reader = csv.reader(file) # 2 times coz here we cannot use the item in the loop here multiple times.. all the rows are taken by above loop, so here if this is not done then the empty list will come.
	for row in reader:
		latency = float(row[1])
		latencies.append(latency)
	
print(latencies)
	
	
#calculation:
print("-----------Analysis----------------")
count = len(latencies)
minimum = min(latencies)
maximum = max(latencies)
mean = sum(latencies)/ count 
median = statistics.median(latencies)
print(f"Count = {count} \n Minimum = {minimum: .2f} \n Maximum = {maximum} \n Mean={mean} \n Median = {median}")
	
	
#Note:
# it stores the data in the string and need to be converted in the float before the calculation
