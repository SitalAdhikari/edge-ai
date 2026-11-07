import argparse
from pathlib import Path

parser=argparse.ArgumentParser(
		description='Analye the benchmark latency of the measurements'
)
parser.add_argument('--input', required=True, help="Input the CSV file") # requried = True makes it compulsory, we can use default='value' to make it optional instead of required=True
parser.add_argument('--output', default='results', help='Directory where the result will be saved')
args=parser.parse_args()

input_path = Path(args.input)
if not input_path.is_file():
	parser.error(f"Invalid input file:{input_path}")

output_path = Path(args.output)
output_path.mkdir(parents=True, exist_ok=True)




