#You are given an integer n. Your task is to return the largest digit present in the number.
n= int(input("enter the no:"))
if n==0:
    print(0)
max_digit=0
while n>0:
    digit = n%2 !=0
    if digit >max_digit:
        max_digit=digit
    n //=10
print(max_digit)