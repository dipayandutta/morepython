print("This will always run!")

def main():
	print(__name__)

def functionFromFirstModule():
	print("This is function ")
	a = 10
	b = 'abc'
	c = str(a)+b 

	print(c)

if __name__ == '__main__':
	main()