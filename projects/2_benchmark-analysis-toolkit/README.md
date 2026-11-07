# Benchmark Analysis Toolkit - version 1

## Overview

The Benchmark Analysis Toolkit is a Python project that analyzes execution-time measurements and generates statistical summaries and visualizations.

It is designed to develop foundational skills in performance analysis and benchmarking, which are important for future Edge AI systems and inference optimization work.

## Objectives

- Load latency measurements from CSV files.
- Convert raw string values into numerical data using NumPy.
- Calculate descriptive statistics.
- Generate latency visualizations using Matplotlib.
- Export statistical results to a CSV file.
- Handle invalid input and empty datasets.
- Understand basic benchmarking principles through repeated timing experiments.

## Project Structure

```text
benchmark-analysis-toolkit/
│
├── data.csv
├── 4_analyze_benchmarks.py
├── benchmark_experiment.py
├── analyze_benchmark.csv
├── summary.csv
├── benchmarking-notes.md
├── README.md
│
└── plots/
    ├── latency_line.png
    └── latency_distribution.png
```

Some output files are generated when the programs run.

## Requirements

- Python 3
- NumPy
- Matplotlib

Install the required libraries:

```bash
python -m pip install numpy matplotlib
```

## Input Data

The analysis program reads latency measurements from a CSV file.

Expected format:

```csv
latency_ms
12.4
11.8
13.1
12.0
14.2
```

Each row represents one latency measurement in milliseconds.

**Data source:** Document whether the measurements are synthetic sample data or actual measurements collected from a specific experiment. Do not describe synthetic data as real hardware benchmarks.

## Statistical Analysis

The toolkit calculates the following measurements:

| Statistic | Description |
|---|---|
| Count | Total number of measurements |
| Minimum | Smallest latency |
| Maximum | Largest latency |
| Mean | Average latency |
| Median | Middle value of sorted measurements |
| Standard deviation | Measures the spread of latency values |
| P90 | 90th percentile latency |
| P95 | 95th percentile latency |

These statistics help describe both typical performance and variation in execution times.

## Visualizations

The toolkit generates two plots:

### 1. Latency Line Plot

Displays individual latency measurements in their recorded order.

It helps identify fluctuations and unusually high measurements.

### 2. Latency Histogram

Displays the distribution of latency measurements.

It helps show where most measurements are concentrated and how widely they vary.

## Benchmark Experiment

The `benchmark_experiment.py` script measures the execution time of a simple Python operation.

The experiment:

1. Creates a fixed list of integers.
2. Performs warm-up executions.
3. Measures the operation repeatedly.
4. Records execution times in milliseconds.
5. Saves the measurements to `experiment_measurements.csv`.

The experiment uses Python's `time.perf_counter_ns()` for elapsed-time measurement.

These measurements are affected by the Python runtime, operating system, and hardware. They should not be interpreted as universal performance values.

## Running the Project

Run the benchmark experiment:

```bash
python benchmark_experiment.py
```

Analyze the experiment measurements using:

```bash
python 4_analyze_benchmark.py
```

Ensure that the analysis script is configured to read `experiment_measurements.csv` when analyzing the experiment. It may otherwise read `measurements.csv` by default.

## Error Handling

The analysis program should handle:

- Missing input files.
- Empty datasets.
- Missing or incorrect CSV headers.
- Invalid numeric values.
- Negative latency values.
- Non-finite values such as NaN and infinity.

Invalid measurements should be reported rather than silently ignored.

## Learning Outcomes

Through this project, I practiced:

- Python file handling and CSV processing.
- NumPy arrays and statistical calculations.
- Matplotlib data visualization.
- Modular Python programming.
- Input validation and exception handling.
- Repeated performance measurements.
- Warm-up procedures and measurement variability.
- Basic benchmarking methodology.

## Future Improvements

Possible future extensions include:

- Comparing multiple implementations of the same operation.
- Measuring different input sizes.
- Comparing execution time across Python and C++.
- Analyzing CPU and memory usage.
- Benchmarking machine-learning inference.
- Investigating model quantization and inference optimization.

## Current Scope

This is a foundational benchmarking and data-analysis project. It does not yet benchmark neural-network models or evaluate hardware-specific Edge AI optimizations.
