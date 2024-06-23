ls=list(map(int,input().split()))
key=int(input("Enter the key"))
s=0
e=len(ls)-1
last=-1
ans=-1
while s<=e:
    mid=(s+e)//2
    if ls[mid]==key:
        last=mid
        s=mid+1
        print("PRESENT AT First",mid)
    elif ls[mid]==key:    
        ans=mid
        e=mid-1
        print("PRESENT AT Last",mid)
        break
    elif ls[mid]<key:
        s=mid+1
    else:
        e=mid-1
           