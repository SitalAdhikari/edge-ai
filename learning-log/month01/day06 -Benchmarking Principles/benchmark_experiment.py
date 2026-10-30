import csv
import numpy as np
import time

numbers = list(range(10000))

warmup_runs =5
timed_run = 100
output_file = 'summary.csv'
analyze_bm = 'analyze_benchmark.csv'


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
		
	with open(output_file,'w') as file:
		writer = csv.writer(file)
		writer.writerow(['latency_ms'])
		for latency in timing_ms:
			writer.writerow([latency])
			
	print(f"Operation:{len(numbers)}")
	print(f"Warmup Runs: {warmup_runs}")
	print(f"Timed runs: {timed_run}")
	print(f"minimum:{min(timing_ms): .5f} ms")
	print(f"Median:{sorted(timing_ms)[len(timing_ms) // 2]: .6f} ms")
	
	
	# analyzing the benchmark
	timing_ms = np.array(timing_ms, dtype = float)
	result = {
		"count": int(timing_ms.size),
		"min": float(np.min(timing_ms)),
		"max": float(np.max(timing_ms)),
		"median": float(np.median(timing_ms)),
		"mean": float(np.mean(timing_ms)),
		"std": float(np.std(timing_ms)),
		"p90": float(np.percentile(timing_ms,90)),
		"p95": float(np.percentile(timing_ms,95)),
		
	}
	
	with open(analyze_bm,'w') as file:
		writer = csv.writer(file)
		writer.writerow(['Metric','Value'])
		for metric, value in result.items():
			writer.writerow([metric,value])
	
	
	
	
if __name__ =='__main__':
	main()
