import sys

temp = int(sys.argv[1])
count = ' '

def printer(n):
	if n > 0:
		printer(n-1)
		print(str(n)),
	return

printer(temp)
print(count)