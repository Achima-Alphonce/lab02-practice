def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def is_even(n):
    return n % 2 == 0

def subtract(a,b): 
    return a-b #if a+b then gives assertion error

def max_of_three(a,b,c):
    return max(a,b,c)

def is_palindrome(s):
    s = s.lower().split()
    s = "".join(s)
    return s == s[::-1]

def find_min(numbers):
    return min(numbers)

def remove_duplicates(items):
    dupl = []
    for i in items:
        if i not in dupl:
            dupl.append(i)
    return dupl

