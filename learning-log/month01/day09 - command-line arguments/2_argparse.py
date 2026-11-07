import argparse

parser= argparse.ArgumentParser(
	prog = 'Calculator',
	description='To perform simple calculation',
)

parser.add_argument('num1', help='First Number', type=int)
parser.add_argument('num2', help = 'Second Number', type=int)
parser.add_argument('operation', help = 'add, sub, multiply, divide')
parser.add_argument('--message', help='You can write any message here') # --message is a flag

args= parser.parse_args()

print(f"Message from user:{args.message}")

num1, num2, operation =  args.num1, args.num2, args.operation

if operation == 'add':
	print(num1+num2)
elif operation=='sub':
	print(num1-num2)
elif operation == 'multiply':
	print(num1*num2)
elif operation=='divide':
	print(num1/num2)
else:
	print('Invalid Inputs')


# python 2_argparse.py 2 3 add
# python 2_argparse.py 2 3 add --message 'I am doing addition'

