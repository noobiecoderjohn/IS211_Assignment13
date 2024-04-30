#Part I - Fibonacci Sequence
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))


#Part II - Euclid's GCD Algorithm
def gcd(a, b):
    if a == 0 :
        return b

    return gcd(b%a, a)

a=int(input())
b=int(input())
print("gcd(", a , "," , b, ") = ", gcd(a, b))



#Part III - String Comparison
def compareTo(s1, s2):
    if len(s1) == 0 and len(s2) == 0:
        return 0
    elif len(s1) == 0:
        return -1
    elif len(s2) == 0:
        return 1
    else:
        if s1[0] < s2[0]:
            return -1
        elif s1[0] > s2[0]:
            return 1
        else:
            return compareTo(s1[1:], s2[1:])
a=input()
b=input()
print("string equality= ", compareTo(a, b))
