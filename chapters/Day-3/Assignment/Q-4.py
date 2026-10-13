#You are given two integers n1 and n2. Your task is to find the Greatest Common Divisor
#(GCD) of the two given numbers. The GCD of two integers is the largest positive 
#integer that divides both of the integers without leaving a remainder

def gcdOfTwoNumbers(n1, n2):
    gcd=1
    for i in range(1,min(n1,n2)+1):
        if n1 % i==0 and n2 % i==0:
            gcd=i
    return gcd
