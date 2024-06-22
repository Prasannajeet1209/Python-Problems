def calu(l,b):
    area=l*b
    perimeter=2*(l+b)
    return area,perimeter

l=int(input("Enter value 1 :"))
b=int(input("Enter value 2 :"))
area,perimeter=calu(l,b)
print("Area and Perimeter is :",area,perimeter)  