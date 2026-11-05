from benchmark_toolkit.data_loader import load_data
from benchmark_toolkit.statistics import calculate_statistics
from benchmark_toolkit.visualization import plot_latency

def main():
	measurements = load_data('data/data.csv')
	print(measurements)
	statistics= calculate_statistics(measurements)
	for name,value in statistics.items() :
		print(f"{name}:{value}")
	plot_latency(measurements)
	
if __name__ == "__main__":
	main()
