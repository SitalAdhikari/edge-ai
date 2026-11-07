import csv

from statistics_utils import *

def load_data(file_path):
	"""TO read the latency value from the file"""
	latency =[]
	with open(file_path) as file:
		reader= csv.DictReader(file)
		for row in reader:
			try:
				value = float(row['latency_ms'])
			except Exception:
				raise ValueError("Invalid Latency")
			latency.append(value)
	return latency
	
def main():
	try:
		latency = load_data('data.csv')
		results = {
			"Count": len(latency),
			"Minimum": calculate_min(latency),
			"Maximum": calculate_max(latency),
			"Mean": calculate_mean(latency),
			"Median": calculate_median(latency)
		}
	
		for name, result in results.items():
			print(f"{name}:{result}")
		
		with open('summary.txt','w') as file:
			for name, result in results.items():
				file.write(f"{name}:{result} \n")
	
	except Exception as e:
		print(f"Error:{e}")
		
if __name__== "__main__":
	main()
		
