a=[4,2,5,6,12,7,1,-1]
key=7
ans=-1
for i in range(len(a)):
    if a[i] == key:
        ans=i
        break
    
if ans==-1:
    print("not found")
else:
    print("found at index",ans)