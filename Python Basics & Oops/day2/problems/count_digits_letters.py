

# output returns a list [no of characters, no of digits]

# used string.isdigit() and string.isalpha()


def fun(st):
    l=[]
    l_count=0
    d_count=0
    for i in st:
        if(i.isdigit()):
            d_count+=1
        if(i.isalpha()):
            l_count+=1
        
    l.append(l_count)
    l.append(d_count)
    return l


#main
st=input()
print(fun(st))
