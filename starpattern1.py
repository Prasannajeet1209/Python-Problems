a =(int(input("Enter value of a"))) 
for i in range(0,a):
    for j in range(0,a-i):
     print(" ",end=" ")
    for k in range(0,a-j ) :
       print("*",end=" ")
    for m in range(1,i+1):
       print("*",end=" ")
    print(" ") 
    