# Benchmark Analysis Toolkit v2

A Python-based benchmarking and performance analysis tool that reads latency measurements from CSV files, calculates statistical metrics, and generates visualizations.

Version 2 focuses on **software engineering practices**, including modular project organization, reusable functions, code quality, documentation, and command-line argument handling.

## 1. Project Overview

Benchmarking is an important part of Edge AI systems engineering. Before optimizing a machine learning model for edge hardware, we need to understand how to collect, analyze, and interpret performance measurements.

This project provides a foundation for that process by analyzing execution latency measurements.

The toolkit can:

- Read latency measurements from CSV files.
- Validate input data.
- Calculate statistical metrics.
- Generate latency visualizations.
- Save analysis results to an output directory.
- Run through a command-line interface (CLI).

## 2. What's New in Version 2?

Version 2 improves the original Benchmark Analysis Toolkit through better software organization and usability.

| Feature | Improvement |
|---|---|
| Project organization | Separated code into independent Python modules |
| Reusability | Created reusable functions |
| Separation of concerns | Separated data loading, statistics, visualization, and execution |
| Code quality | Improved naming, readability, and documentation |
| Type hints | Added type annotations where appropriate |
| Testing | Added automated tests |
| CLI | Added command-line arguments using `argparse` |
| Dependencies | Added dependency management with `requirements.txt` |

## 3. Project Structure

```text
3_Benchmark-Analysis-Toolkit-v2/
│
├── main.py
├── requirements.txt
├── README.md
│
├── data/
│   └── data.csv
│
├── results/
│   ├── summary.csv
│   └── plots/
│       ├── latency_line.png
│       └── latency_histogram.png
│
├── benchmark_toolkit/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── statistics.py
│   └── visualization.py
│
└── tests/
    ├── __init__.py
    └── test_statistics.py
```

### Module responsibilities

- `main.py`: Handles command-line arguments and coordinates program execution.
- `data_loader.py`: Loads and validates CSV measurements.
- `statistics.py`: Calculates statistical metrics.
- `visualization.py`: Generates plots using Matplotlib.
- `tests/`: Contains automated tests.
- `requirements.txt`: Lists external Python dependencies.

## 4. Technologies Used

- **Python 3:** Main programming language.
- **NumPy:** Numerical calculations and statistical analysis.
- **Matplotlib:** Data visualization.
- **argparse:** Command-line argument parsing.
- **unittest:** Automated testing.
- **CSV:** Measurement data storage.
- **Git and GitHub:** Version control and project management.

## 5. Installation and Setup

### Step 1: Clone the repository

```bash
git clone https://github.com/SitalAdhikari/edge-ai.git
```

Navigate to the project directory:

```bash
cd edge-ai/3_Benchmark-Analysis-Toolkit-v2
```

### Step 2: Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it.

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux/macOS:**

```bash
source .venv/bin/activate
```

### Step 3: Install dependencies

```bash
python -m pip install -r requirements.txt
```

## 6. Usage

The application uses command-line arguments to specify the input CSV file and output directory.

### Run the program

```bash
python main.py --inputfile data/data.csv
```

### Command-line arguments

| Argument | Description |
|---|---|
| `--inputfile` | Path to the input CSV file |
| `--output` | Directory where analysis results are saved |

The application should display a helpful usage message when incorrect arguments are supplied.

For example:

```bash
python main.py --help
```

## 7. Input Data Format

The input CSV file contains latency measurements. There are 100 measurements of the add operation just for reference.

Each row represents one latency measurement in milliseconds.

## 8. Statistical Analysis

The toolkit calculates the following metrics:

| Metric | Description |
|---|---|
| Count | Total number of valid measurements |
| Minimum | Lowest recorded latency |
| Maximum | Highest recorded latency |
| Mean | Average latency |
| Median | Middle value of sorted measurements |
| Standard deviation | Measures variation in latency |
| P90 | 90th percentile latency |
| P95 | 95th percentile latency |

These metrics help characterize the performance and variability of a system.

## 9. Output

After successful execution, the application generates:

- `summary.csv`: Contains calculated statistical metrics.
- `latency_line.png`: Displays latency measurements across observations.
- `latency_histogram.png`: Shows the distribution of latency measurements.

Example output structure:

```text
results/
├── summary.csv
└── plots/
    ├── latency_line.png
    └── latency_histogram.png
```

## 10. Running Tests

The project uses Python's built-in `unittest` framework.

Run all tests using:

```bash
python -m unittest discover -s tests -v
```

Tests cover data loading, input validation, and statistical calculations.

## 11. Engineering Concepts Practiced

Through this project, I practiced:

1. Organizing Python applications into modules and packages.
2. Applying separation of concerns.
3. Writing reusable and documented functions.
4. Using type hints.
5. Managing dependencies through virtual environments.
6. Handling command-line arguments with `argparse`.
7. Writing automated tests.
8. Processing numerical measurements using NumPy.
9. Generating visualizations using Matplotlib.
10. Maintaining and documenting a GitHub project.

## 12. Limitations and Future Improvements

Current limitations:

- Analysis is focused on latency measurements.
- Measurements are assumed to come from a consistent experimental setup.
- The toolkit does not yet collect hardware performance data directly.
- It does not yet benchmark machine learning inference workloads.

Potential future improvements:

- Add throughput and memory usage analysis.
- Support multiple benchmark runs and experimental configurations.
- Add comparison between different hardware platforms.
- Introduce ML model inference benchmarking.
- Add hardware-aware performance analysis.

## 13. Project Context

This project is part of my learning journey toward becoming an **Edge AI Systems and Optimization Engineer**.

The objective is to develop the programming, data analysis, software engineering, and benchmarking foundations required for future work in efficient machine learning and hardware-aware AI optimization.

**Author:** Sital Adhikari

**GitHub:** [SitalAdhikari](https://github.com/SitalAdhikari)

**Repository:** [edge-ai](https://github.com/SitalAdhikari/edge-ai)
