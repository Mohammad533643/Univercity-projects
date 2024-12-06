# We need under code for calculating factorial of numbers(for combinaton)
def factorial(x):
    p = 1
    for i in range(1,x+1):
        p *= i
    return p
# We calculate the combinations of numbers
def combination(n,k):
    c_answre = int(factorial(n)/((n-k)*(factorial(k)))
    return c_answre

def final_answre(a,x,n,k):
    y = (x**k)*(a**(n-k))
    f_answre = combination(n,k) * y
    return f_answre

def run():
    a,x,n = map(int,input().split())
    k = 0
    d = 0
    while k<= n:
        d += final_answre(a,x,n,k)
        k += 1
    print(d)
    
run()
     
