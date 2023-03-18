str=input()
l=[]
for i in str:
    l.append(int(i))

cursum=0
d={}
l2=[]
for i in range(len(l)):
    l1=[]
    cursum+=l[i]
    if cursum==10:
        l1=(l[:i+1])
    if cursum-10 in d:
        l1=l[d[cursum-10]+1:i+1]
    if cursum not in d:
        d[cursum]=i
    if(len(l1)!=0):
        l2.append(l1)
print(l2)
        
