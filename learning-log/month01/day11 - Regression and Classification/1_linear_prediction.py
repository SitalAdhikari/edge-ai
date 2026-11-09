# understanding y= mx +c
# predicting executing time based on cpu_utilization

def linear_prediction(slope,x,c):
	y = slope * x +c
	return y

cpu_utilization= [10,20,30,40,50]
slope =0.5
c= 3
print("CPU Utilization  |  Execution time")
print(" ----------------------------------")

for cpu in cpu_utilization:
	y = linear_prediction(slope,cpu,c)
	print(f"{cpu}% \t \t | \t {y} ms")

# when slope =0, y became independent of x.
