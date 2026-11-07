<h3> Latency </h3> <br>
- It is the time taken to process an input completely.<br>
- For eg, if a function takes 4ms to give and output, its latency i 4ms.

<br><h3> Throughput </h3> <br>
-It is the number of operations completed per unit time.<br>
- For example, if a program processes 500 independent inputs per second, its throughput is 500 operation/second.<br>

<br> Throughput = 1/Latency <br>
This is the theoritical relationship. In practical this doesn't happen because batching, parallel processing, scheduling and other affects.<br>

<br>
- A real-time system prioritize low latency, while a server processing prioritze throughput.
<br>

<h3>Why repeated measurements matter?</h3><br>
-> One run might affected by operating-system, background application, CPU scheduling, or other intereferences. So, repeated measuremetns helps us estimate the distribution of execution times. <br>
-> For performance benchmarking, median and upper percentile will be usefule, coz outlier can affect the mean. <br>
<br>

<h3> Warm-up time vs Timed run </h3> <br>
-A Warm-up run is perfomed before recording the timed run. <br>
- Warm-up run is the first run. <br>
- It is because the first execution can behave differently because of initialization, memory alocation, cache, and other effect.<br>
- So, for bringing the uniformity in the timed-runs , warm-up run is done. <br>
- For eg: 12ms, 5ms, 4.8 ms, 4.5 ms, 6m/s.<br>
- Here 12ms should be considered as warm-up run.<br>

<h3> Outliers:</h3><br>
- It is a value unusually far from the rest of the observations.<br>
- Do not automatically delete ourliers: record them, incestigage possible causes, and document any exclusion.

<br>
<br>
- For better experimental conditions: same computer and python version, same input data and input size, and other remaining conditions should be same .. <br>

