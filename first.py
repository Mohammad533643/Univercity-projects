def factorail(x):
    p = 1
    for i in range(1,x+1):
        p *= i
    return p
    
def combination(n,k):
    c_answre = factorial(n)/((n-k)*(factoral(k))
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
        k += 1
        d += final_answre(a,x,n,k)
    print(d)
    
run()
     
