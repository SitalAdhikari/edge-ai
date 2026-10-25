# Write a script that saves benchmark measurements to a file.

latency = 10
throughput = 95
memory = 128

with open("benchmark_logger.txt","w") as file:
	file.write(f"Latency: {latency} \n")
	file.write(f"Throughput: {throughput} \n")
	file.write(f"Memory: {memory}")
	
with open("benchmark_logger.txt",'r') as file:
	for line in file:
		print(line.strip())
		print("\n")
