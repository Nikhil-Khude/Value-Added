#Given an array arr of size n, your task is to find the sum of all the elements in the
#array

def sum_of_array_elements(n, arr):
    # Write your code here
    sum=0
    for i in arr:
        sum+=i

    return sum