def validate_values(value):
	"""Check whether the input is valid or not"""
	if not value:
		raise ValueError("The value is empty")
	
	for v in value:
		if isinstance(v, bool):
			raise ValueError("The input value must be integer or float.")
		
		if not isinstance(v,(int,float)):
			raise ValueError("The input value must be integer or float.")
		if v <= 0:
			raise ValueError("The value must be a positive number.")

def calculate_mean(value):
	"""To calculate the mean of the values."""
	validate_values(value)
	return  sum(value)/len(value)

def calculate_median(value):
	"""To calculate the median of the values."""
	validate_values(value)
	ordered = sorted(value)
	middle = len(ordered) // 2
	
	if (len(ordered) % 2 == 1):
		return ordered[middle]
	else:
		return (ordered[middle-1] + ordered[middle]) / 2
		
def calculate_min(value):
	"""Minimum Value calculation"""
	validate_values(value)
	return min(value)
	
def calculate_max(value):
	"""Maximum value calculation"""
	validate_values(value)
	return max(value)
	

