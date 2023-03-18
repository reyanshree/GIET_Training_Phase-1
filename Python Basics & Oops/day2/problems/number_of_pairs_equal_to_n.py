


# to find the sum of a pair of nummber t0 obtain sum equal to number


def fun(l,n):
    count=0
    for i in range(0,len(l)-1):
        for j in range(i+1,len(l)):
            if(l[i]+l[j]==n):
                count+=1
                print((l[i],l[j]))
    return count




list1=[int(i) for i in input().split()]
n=int(input())
print(fun(list1,n))