#You are given an integer n. Your task is to return the integer formed by placing 
#the digits of n in reverse order. Note that the result should not have leading zeros
n=int(input("enter the number"))
rev=0
while n>0:
    digit= n % 10
    rev=rev*10+digit
    n//=10
print(rev)

