n=int(input())
d=[int(i) for i in input().split()]
c=[]
f=0
for i in range(len(d)):
  if i%2==1 and d[i]%2==1:
    f=f+1
for i in d:
  if i%2==1:
    c.append(i)
if f>=len(c):
  print(True)
else:
  print(False)