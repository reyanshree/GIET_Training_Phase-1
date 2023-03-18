def fun(dict,st):
    l=st.split()
    str=""
    count=0
    for i in l:
        if i in dict:
            str+=dict[i]+" "
        else:
            str+='-1 '
    #if(count==1):
       # return -1 
    return str



dict={"merry":"god","christmas":"jul","and":"och","happy":"gott","new":"nytt","year":"ar"}
st=input()
print(fun(dict,st))

