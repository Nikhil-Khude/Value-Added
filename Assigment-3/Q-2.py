#Given an array of n elements, the task is to return the count of the number of odd
#numbers in the array

def countOddNumbers(n, array):
    # Write your code here
    sum=0
    for i in array:
       if n % i !=0:
           sum +=1
    return sum
