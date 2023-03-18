
def fun(l):
    l1=[]
    for i in range(0,len(l)):
        for j in range(i,len(l)):
            l1.append(l[i:j+1])
    l1=[l[i:j+1] for i in range(0,len(l)) for j in range(i,len(l))]
    print(l1)
    count=0
    for i in l1:
        sum=0
        for j in i:
            sum+=j
        if(sum%2!=0):
            count+=1
    return count
            
        





n1=int(input())
n2=int(input())
l=[]
for i in range(n1,n2+1):
    l.append(i)
print(fun(l))
