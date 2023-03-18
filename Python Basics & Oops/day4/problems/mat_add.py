row=int(input())
col=int(input())
mat1=[]
for i in range(row):
    l1=[]
    for j in range(col):
        a=int(input())
        l1.append(a)
    mat1.append(l1)
mat2=[]
for i in range(row):
    l1=[]
    for j in range(col):
        a=int(input())
        l1.append(a)
    mat2.append(l1)
mat3=[[mat1[i][j]+mat2[i][j] for j in range(col)]for i in range(row)]
print(mat3)
