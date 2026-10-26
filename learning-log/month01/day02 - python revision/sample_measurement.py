measure = [
	{"model":1, "latency_ms":12.4},
	{"model":2, "latency_ms": "11.8"},
	{"model":3, "latency_ms":"-2"},
	{"model":4, "latency_ms":"john cena"},
	{"model":5}
]

valid_latency = []

for i in range(len(measure)):
	if ('latency_ms' not in measure[i]):
		print(f"{measure[i]['model']}: missing the latency value")
		continue
		
			
	try:
		latency = float(measure[i]['latency_ms'])
	except Exception:
		print(f"{measure[i]['model']}: invalid latency value: {measure[i]['latency_ms']}")
		continue
	
	if latency < 0:
		print(f"Negative latency")
		continue
	
	valid_latency.append(measure[i]['latency_ms'])
	
print("The valid latency:", valid_latency)
