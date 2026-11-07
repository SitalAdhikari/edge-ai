import matplotlib.pyplot as plt
from pathlib import Path

def plot_latency(latency,output_dir):
	"""Create and save Lineplot and a histogram"""
	
	count= range(1,len(latency)+1)
	
	plt.plot(count,latency)
	plt.xlabel("Measurement Number")
	plt.ylabel("Latency(ms)")
	plt.grid()
	plt.tight_layout()
	
	output_path1 = output_dir/"lineplot.png"
	plt.savefig(output_path1)
	plt.close()
	
	
	# histrogram
	plt.hist(latency,bins='auto')
	plt.xlabel('Latency')
	plt.ylabel('Frequency')
	plt.title('Distribution of Latency Measurement')
	plt.grid()
	output_path2 = output_dir/"histogram.png"
	plt.savefig(output_path2)
	plt.close()
