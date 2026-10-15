#Given an array arr of n elements, the task is to reverse the given array in-place. 
#The reversal should not create a new array; instead, it should modify the original array

def reversearray(arr):
    rev=[]
    for i in range(len(arr)-1):
        rev.append(arr[i])
    return rev