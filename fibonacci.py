n =(int(input("Enter value of n:")))
i=0
a=0
b=1
while i<n:
  c=a+b
  print("Series is ",c) 
  a=b
  b=c
  i=i+1
