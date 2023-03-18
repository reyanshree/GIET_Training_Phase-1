def almost(i,k):
    count=0
    if(len(i)!= len(k)):
       return False
    for j in range(0,len(i)):
        if(i[j]!=k[j]):
            count+=1
        if(count>2):
            return False
    return True
def fun(d):
    l1=[]
    count_crct=0
    count_alm=0
    count_wrong=0
    for i in d:
        if(i==d[i]):
            count_crct+=1
        elif(almost(i,d[i])):
             count_alm+=1
        else:
            count_wrong+=1
    l1.append(count_crct)
    l1.append(count_alm)
    l1.append(count_wrong)
    print(l1)

d={"their":"their","business":"bisiness","windows":"windmil","were":"wear","sample":"sample"}
fun(d)
