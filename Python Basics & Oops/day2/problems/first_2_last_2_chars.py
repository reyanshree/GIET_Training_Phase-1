# s = input()

def fun1(st):
    if(len(st)<2):
        print("-1")
    else:
        print(st[0:2]+st[-2:])


st=input()
fun1(st)
