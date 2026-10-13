#You are given an integer n. You need to check if the number is a perfect number or not.
 #Return true if it is a perfect number, otherwise, return false


n=int(input("enter the number"))
sum=0
for i in range(1,n):
    if n % i ==0:
        sum +=i

if sum==n:
    print("number is the perfect")
else:
    print("not perfect no")