#You are given an integer n. Your task is to find all the divisors of n and return them in a 
#sorted array

n=int(input("enter the number :"))
arr=[]
for i in range(1,n+1):
    if n% i ==0:
        arr.append(i)
print(arr)