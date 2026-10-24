a=int(input("give:"))
b=int(input("give:"))
c=int(input("give:"))
def qua(a,b,c):
    qua=(-b+(b**2-4*a*c)**0.5)/(2*a)
    qua1=(-b-(b**2-4*a*c)**0.5)/(2*a)
    return qua,qua1
add = qua(a,b,c)
print(add)
