def stringReverse(str1):
	rstr = ''
	index = len(str1)

	while index>0:
		rstr += str1[index -1]
		index -= 1

	return rstr

print(stringReverse('1234abcd'))