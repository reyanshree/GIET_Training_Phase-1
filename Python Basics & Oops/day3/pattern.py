2

l=[]
for i in range(8):
    l1=[]
    for j in range(8):
        if(i==0 or j==0 or i==7 or j==7):
            l1.append('...')
        else:
            tup=tuple((j,i))
            l1.append(tup)
    l.append(l1)
for i in l:
    print(i)
