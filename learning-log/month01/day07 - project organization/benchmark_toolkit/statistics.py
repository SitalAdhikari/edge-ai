import numpy as np

def calculate_statistics(measurement):
	if len(measurement) == 0:
		raise ValueError('The file is empty.')
	latency = np.array(measurement)
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
