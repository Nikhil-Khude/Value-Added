#You are given two integers n1 and n2. Your task is to find the Lowest Common Multiple (LCM) of the two 
#given numbers. The LCM of two integers is the smallest positive integer that is divisible by both integers.

n1=int(input("enter the number"))
n2=int(input("enter the number"))

num=max(n1,n2)
while True:
    if num % n1==0 and num % n2 ==0:
        print(num)
        break
    num +=1

