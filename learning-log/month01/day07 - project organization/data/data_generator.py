import csv
import numpy as np
import time

numbers = list(range(10000))
warmup_runs =5
timed_run = 100


def operation():
	return sum(numbers) # sum adds all the elements of the list
	
def main():
	
	for _ in range(warmup_runs): # here _ is used coz loop counter variable isn't used later
		operation()
		
	timing_ms =[]
	
	# collecting the measurements:
	for _ in range(timed_run):
		start = time.perf_counter_ns()
		operation()
		end = time.perf_counter_ns()
		
		time_in_ms =(end - start) / 1000000 # converting nanosecond to milisecond
		timing_ms.append(time_in_ms)
		
	with open('data/data.csv','w') as file:
		writer = csv.writer(file)
		writer.writerow(['run_id','latency_ms'])
		for i, latency in enumerate( timing_ms):
			writer.writerow([i+1 ,latency])
			
	
if __name__ =='__main__':
	main()
