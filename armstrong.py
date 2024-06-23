a =(int(input("Enter Number")))
num1=a 
num=0

while num!=0:
 rev=num%10
 num1=num1*10+rev*rev*rev
 num=num/10
if a==num1:
  print("Yes")
else: 
  print("No")   
 
