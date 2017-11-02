

import json

def readfile():
	with open('./data.json', 'r') as file:
		#print(file)
		b = file.read()
		#print(b)
		a = json.loads(b)
		print(type(a))
		for line in a:
		 	print(line)
		 	print('*' * 10)

if __name__ == '__main__':
	readfile()