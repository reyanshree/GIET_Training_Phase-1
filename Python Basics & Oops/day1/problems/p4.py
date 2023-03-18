def fun(coin1,coin5,total):
    num=total//5
    count=0
    if(coin5<=num):
        total-=5*num
        count=1
    count1=0
    if(coin1>=total):
        count1=1
    if(count==1 and count1==1):
        print(num," ",total)
    else:
        print('-1')
    
        

coin1=int(input())
coin5=int(input())
total=int(input())
fun(coin1,coin5,total)
