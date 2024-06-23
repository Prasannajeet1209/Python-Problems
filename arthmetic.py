def A(a,b):
    add=a+b
    sub=a-b
    mul=a*b
    div=a//b
    return add,sub,mul,div

a=int(input("Enter value 1 :"))
b=int(input("Enter value 2 :"))
add,sub,mul,div=A(a,b)
print("addition is",add)  
print("Subtration is",sub)   
print("Multiplication is",mul) 
print("Division is",div) 