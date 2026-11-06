import matplotlib.pyplot as plt

def plot_latency(latency):
	"""Create and save Lineplot and a histogram"""
	
	count= range(1,len(latency)+1)
	
	plt.plot(count,latency)
	plt.xlabel("Measurement Number")
	plt.ylabel("Latency(ms)")
	plt.grid()
	plt.tight_layout()
	plt.savefig('results/lineplot.png')
	plt.close()
	
	
	# histrogram
	plt.hist(latency,bins='auto')
	plt.xlabel('Latency')
	plt.ylabel('Frequency')
	plt.title('Distribution of Latency Measurement')
	plt.grid()
	plt.savefig('results/histogram.png')
	plt.close()
