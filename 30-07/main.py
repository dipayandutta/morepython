L = {('a', 'b', 'c', 'd'): 1, ('a', 'b', 'c', 'e'): 2, ('f', 'g', 'h'): 3}

remove='b'
L = {tuple(i for i in k if i != remove) if remove in k else k:v for (k,v) in L.items()}

print (L)


my_tuple = ('bobby', 'hadz', 'com', 'abc')

new_tuple = tuple(
    item for item in my_tuple if item != 'bobby'
)

# 👇️ ('hadz', 'com', 'abc')
print(new_tuple)
