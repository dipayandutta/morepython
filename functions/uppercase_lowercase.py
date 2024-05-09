def string_test(strmsg):
	d = {'UPPER_CASE':0, 'LOWER_CASE':0}

	for char in strmsg:
		if char.isupper():
			d['UPPER_CASE']+=1
		elif char.islower():
			d['LOWER_CASE']+=1

		else:
			pass

	print("Main String{}".format(strmsg))
	print("Number of upper case {}".format(d['UPPER_CASE']))
	print("Number of lower case {}".format(d['LOWER_CASE']))


strmsg = 'The quick BrOwN Fox'

string_test(strmsg)