#You are given an integer n. Your task is to check if the number is prime or not. A prime
#number is defined as a numbergreater than 1 that has no divisors other than 1 and itself

n=int(input("enter the number :"))
if n<=1:
    print("false not prime no. ")
for i in range(2,n):
    if n % i ==0:
        print("not prime")
    break
else:
    print("prime")


    