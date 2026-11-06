import numpy as np

def calculate_statistics(value):
	if len(value) == 0:
		raise ValueError('The file is empty.')
	
	try:
		latency = np.array(value , dtype= np.float64)
	except Exception:
		raise ValueError('All input must be numerical value.')
	
	if not np.all(np.isfinite(latency)):
		raise ValueError('Input cannot be NaN or infinity.')
	
	if np.any(latency < 0):
		raise ValueError("Latency cannot contain negative values.")
		
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
