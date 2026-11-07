import argparse
from pathlib import Path
import csv

from benchmark_toolkit.data_loader import load_data
from benchmark_toolkit.statistics import calculate_statistics
from benchmark_toolkit.visualization import plot_latency

def main():
	
	parser= argparse.ArgumentParser(
		prog='Benchmark Analysis Toolkit - v2',
		description='To analyze the benchmark of the measured latencies of the performance.'
	)
	parser.add_argument("--inputfile", required=True, help='Give the path of the data')
	parser.add_argument("--output",default='results', help='Path of the output directory')
	args=parser.parse_args()
	input_path,output_path = args.inputfile, args.output
	
	measurements = load_data(input_path)
	print(measurements)
	
	
	statistics= calculate_statistics(measurements)
	output_path= Path(output_path)
	output_path.mkdir(parents=True, exist_ok=True)
	summary= output_path/"summary.csv"
	with open(summary,'w') as file:
		writer=csv.writer(file)
		writer.writerow(['Metric','Value'])
		for metric,value in statistics.items():
			writer.writerow([metric,value])
	
	plot_latency(measurements,output_path)
			
if __name__ == "__main__":
	main()
