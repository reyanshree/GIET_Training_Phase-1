def fun1(n):
    dou=n*2
    str1=str(n)
    str2=str(dou)

    l1=[]
    l2=[]
    for i in str1:
        l1.append(i)
    for i in str2:
        l2.append(i)
    print(l1)
    print(l2)
    
    if(len(l1)==len(l2) and l1!=l2) :
        for i in l1:
            if i not in l2:
                return False

        return True
   
    return False


n=int(input())
print(fun1(n))

