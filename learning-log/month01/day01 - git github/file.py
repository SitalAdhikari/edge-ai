file = open("data.txt","w")
file.write("Hello,Python")
file.close()

file = open("data.txt","r")
print(file.read())
file.close()

with open("data.txt","r") as file:
	print(file.readline())
