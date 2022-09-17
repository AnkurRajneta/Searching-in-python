a=[1,5,7,10,15,20,23]
target=20
n=len(a)

ans=-1
start=0
end=n-1
while start<=end:
    mid=(start+end)//2
    if a[mid]==target:
        ans=mid
        break
    elif a[mid]>target:
        end=mid-1
    else:
        start=mid+1
print("The index of the target :", ans)
    