#You are given an integer n. Return the value of n! (n factorial). The factorial of a number is the product of all positive 
# integers less than or equal to that number.

n=int(input("enter the No:"))
if n==1:
    print(1)
result=1
for i in range (1,n+1):
    result*=1
print(result)