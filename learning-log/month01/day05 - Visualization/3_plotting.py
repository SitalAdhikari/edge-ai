import numpy as np
import matplotlib.pyplot as plt
import csv


def load_latencies(filename):
	"""Load the latency file"""
	
	latency = []
	
	with open(filename,'r') as file:
		reader = csv.DictReader(file)
		
		if not reader.fieldnames:
			raise ValueError("The file is empty.")
		if ("latency_ms" not in reader.fieldnames):
			raise ValueError("latency_ms is missing in the file.")
		
		for row in reader:
			try:
				value = float( row['latency_ms'])
				if value < 0:
					raise ValueError("The latency cannot be negative value.")
				latency.append(value)
			except Exception as e:
				raise (f"It accepts only int and float values.: {e}")
				
		return latency

def plot_latency(latency):
	"""Create and save Lineplot and a histogram"""
	
	count= range(1,len(latency)+1)
	
	plt.plot(count,latency)
	plt.xlabel("Measurement Number")
	plt.ylabel("Latency(ms)")
	plt.grid()
	plt.tight_layout()
	plt.savefig('output_plot/latency_line.png')
	plt.show()
	plt.close()
	
	
	# histrogram
	plt.hist(latency,bins='auto')
	plt.xlabel('Latency')
	plt.ylabel('Frequency')
	plt.title('Distribution of Latency Measurement')
	plt.grid()
	plt.savefig('output_plot/latency_distribution.png')
	plt.show()

def main():
	latency = load_latencies('data.csv')
	plot_latency(latency)
	print('Plots are saved')
	
if __name__=='__main__':
	main()
