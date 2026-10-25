#  Mini-project: Latency Statistics Calculator

#Purpose: Built a small tool that will later help me analyze neural-network interence measurements.
import statistics

time_ms = list(map(float, input("Enter numbers: ").split()))

count = len(time_ms)
minimum= min(time_ms)
maximum = max(time_ms)
mean =sum(time_ms) / count
median = statistics.median(time_ms)

with open("latency_statistics_calculation.txt","w") as file:
	file.write(f"Number of measurements: {count} \n")
	file.write(f" Minimum Latency: {minimum} \n")
	file.write(f"Maximum Latency: {maximum} \n")
	file.write(f" Mean Latency: {mean} \n")
	file.write(f"Median Latency: {median} \n")
	
with open ("latency_statistics_calculation.txt","r") as file:
	for line in file:
		print(line.strip())
