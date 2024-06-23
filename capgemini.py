a=int(input("Enter Number of Semeter"))
ls=[]
for i in range(0,a):
    s=int(input("Enter Number of Subject"))
    for j in range(0,s):  
        ls1=[]
        sub=int(input("Enter Number marks :"))
        ls1.append(sub)
    ls.append(ls1)
for i in ls:
    print(" Max",max(i))



