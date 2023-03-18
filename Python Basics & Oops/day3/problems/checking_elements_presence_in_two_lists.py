

mylist=[9,3,6,1,5,0,8,2,4,7]
listb=[6,4,9,1,2,3]
l=[(i,mylist.index(i))  for i in listb]
print(l)

d={}
for i in listb:
    d[i]=mylist.index(i)
print(d)

# Dictionary Comprhension
l={i:mylist.index(i)  for i in listb}
print(l)
