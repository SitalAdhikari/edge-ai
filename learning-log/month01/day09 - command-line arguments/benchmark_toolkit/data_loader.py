import csv

def load_data(filename):
	measurements=[]
	
	with open(filename,'r') as file:
		reader = csv.DictReader(file)
		
		if not reader.fieldnames:
			raise ValueError('Empty file')
		if ("latency_ms" not in reader.fieldnames):
			raise ValueError('latency_ms missing')
		
		for row in reader:
			try:
				value = float(row['latency_ms'])
				
				if value <= 0 :
					raise ValueError('Invalid Input')
				measurements.append(value)
			except Exception as e:
				print(f'Invalid Input: {e} ')
			
	return measurements
