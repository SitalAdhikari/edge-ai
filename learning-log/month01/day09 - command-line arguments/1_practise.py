import sys


print(sys.argv)


arguments = sys.argv
if (int(arguments[1]) >= 18):
	print("You can vote")
else:
	print('You are underaged, so you cannot vote.')

# python main.py 19
# the input value will be in string:
