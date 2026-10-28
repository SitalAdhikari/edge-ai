import numpy as np
import statistics

#convert ms into second
latency_ms = np.array([10,12,11,5,54])
latency_s = latency_ms / 1000
print(latency_s)

#few statistics calculation
print(np.mean(latency_ms))
print(np.median(latency_ms))
print(np.min(latency_ms))
print(np.max(latency_ms))
print(np.std(latency_ms))
print(np.percentile(latency_ms,90))


#compare the median between statistics and the nmppy
print(np.mean(latency_ms))
print(statistics.mean([10,12,11,5,54]))
