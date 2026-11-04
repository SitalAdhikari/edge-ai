import csv
import matplotlib.pyplot as plt
import numpy as np

def load_latency(file_load):
	latency=[]
	with open(file_load,'r') as file:
		reader = csv.DictReader(file)
		
		if not reader.fieldnames:
			raise ValueError("File is empty")
		if 'latency_ms' not in reader.fieldnames: 
			raise ValueError("latency_ms is missing")
		
		for row in reader:
			try:
				value = float(row['latency_ms'])
				latency.append(value)
			except Exception as e:
				raise ValueError(f"Invalid Input:{e}")
	return np.array(latency, dtype = float)
	
def calculate_statistics(latency):
	
	result = {
		"count": int(latency.size),
		"min": float(np.min(latency)),
		"max": float(np.max(latency)),
		"median": float(np.median(latency)),
		"mean": float(np.mean(latency)),
		"std": float(np.std(latency)),
		"p90": float(np.percentile(latency,90)),
		"p95": float(np.percentile(latency,95)),
		
	}
	return result
	
def summary(stat,sum_file):
	with open(sum_file,'w') as file:
		writer = csv.writer(file)
		writer.writerow(['metric','value'])		
		
		for metric,value in stat.items():
			writer.writerow([metric,value])

if __name__=='__main__':
	latency = load_latency('data.csv')
	stat= calculate_statistics(latency)
	summary(stat,'summary.csv')

		
	
