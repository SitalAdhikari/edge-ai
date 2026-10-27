# Latency Statistics Calculator

### Overview
  (introduction, what, and why)
  <br>
  This is the beginner Python Project which takes the CSV file and does statisticts calculation.
  This project is my Edge AI System and Optimization learning roadmap.
  
### Features
- Read the latency measurement from the CSV file. <br>
- Calculate count, minimum, maximum, mean and median.<br>
- Check the valid input and handle the invalid inputs. <br>
- Test the calculation function

### Requirements

- Python3 <br>
- Python Standard Libraries 

### Project Structure:

- main.py - program entry point
- statistics_utils.py - calculation
- test_statistics_utils.py - testing 
- data.csv - sample input

### Input Format

- The input CSV contains a header['run_id','latency_ms']
- Latency is measured in millisecond

### How to Run:

-python3 main.py


### Output:

The program give the number of valid measurements, minimum, maximum, mean and median latency.


### Limitation:

This project is using the supplied measurement. It does not contain the real benchmark a neural network or measure real edge-device performance.


### Learning Objectives:

- Practice Python functions and modules.
- Read and write the CSV files.
- Handle the invalid inputs
-Write automated tests.
- Use Git to track project changes.
- Document a workflow.

### Future Improvements:

- Add standard deviation
- Generate a latency distribution plot.
- Benchmark actual machine-learning inference in a future project.
   
