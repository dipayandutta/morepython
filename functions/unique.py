def unique_list(lst):
	x = []

	for nums in lst:
		if nums not in x:
			x.append(nums)
	return x


print(unique_list([1,2,3,3,3,3,4,5]))