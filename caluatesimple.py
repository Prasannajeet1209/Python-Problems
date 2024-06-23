def SI(p,r,n):
    I=(p*r*n)/100
    return I
p=int(input("Enter value 1 :"))
r=float(input("Enter value 2 :"))
n=int(input("Enter value 3 :"))
I=SI(p,r,n)
print("Simple Interest is :",I)