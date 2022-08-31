n=int(input())
lst=list(map(int,input().split()))
l1=[]
l2=[]
for i in range(n):
  if lst[i]%2==1:
     l1.append(lst[i])
for j in range(n):
  if lst[j]%2==0:
     l2.append(lst[j])
l=l1+l2
print(*l)
     