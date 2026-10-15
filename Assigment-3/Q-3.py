#Given an array arr of size n, the task is to check if the given array is sorted in 
#ascending (increasing or non-decreasing) order. If the array is sorted, return True; 
#otherwise, return False
    
def isArraySorted(arr):
    # Write your code here
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True