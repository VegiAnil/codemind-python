n=int(input())
l=list(map(int,input().split()))
s=[]
for i in range(n):
  if l[i] not in s:
    s.append(l[i])
print(*s)    
    