a,b,c=map(int,input().split())
sum=0
for i in range(1,c+1):
    sum+=a*i
if sum>=b:
  print(sum-b)
else:
    print(0)  