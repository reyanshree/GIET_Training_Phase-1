ds=[]
def subsetcount(index,list1,sum,target,ds):
    if(target>sum):
        return 
    
    if(index==len(list1)):
        if(sum==target):
            return 1
    ds.append(list1[index])
    target+=list1[index]
    subsetcount(index,list1,sum,target,ds)
    ds.pop()
    target-=list1[index]
    subsetcount(index+1,list1,sum,target,ds)
    





k=int(input())

l=[int(i) for i in input().split()]
subsetcount(0,l,k,0,ds)
print(len(ds))
