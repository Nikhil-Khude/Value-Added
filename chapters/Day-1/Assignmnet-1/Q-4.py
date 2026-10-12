#You are given an integer n. Your task is to determine if n is a palindrome number.A 
#palindrome number is one that reads the same when reversed.

n=int(input("enter the number"))
original=n
rev=0
while n>0:
    digit = n% 10
    rev=rev*10+digit
    n //= 10
print (original==rev)