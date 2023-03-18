def ispalin(d):
    rev=0
    temp=d
    while(d>0):
        rem=d%10
        rev=rev*10+rem
        d//=10
    if(temp==rev):
        return True
    else:
        return False

def fun(n):
    d=n+1
    while(True):
        if(ispalin(d)):
            return d
        d+=1

n=int(input())
print(fun(n))
