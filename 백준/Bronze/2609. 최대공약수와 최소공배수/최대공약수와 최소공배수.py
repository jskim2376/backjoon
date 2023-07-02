def gcd(a,b):
    if a%b == 0:
        return b
    return gcd(b,a%b)
a, b = map(int,input().split())
if a<b:
    a,b = b,a
myGcd = gcd(a,b)
print(myGcd)
print(a*b//myGcd)