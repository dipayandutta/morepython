'''
    Example of -> Two pointer technique
    we have a sorted array 
    we have to find two numbers whose sum is zero
'''
arr = [-10,-8,-3,3,4,5]

left = 0
right = len(arr)-1

while(left<right):
    sum = arr[left]+arr[right]
        
    if(sum == 0):
        print(arr[left])
        print(arr[right])
        break

    elif(sum<0):
        left+=1
    else:
        right-=1
    