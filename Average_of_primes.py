def prime(x):
  if x==1:
     return False
  for i in range(2,int(x**0.5)+1):
     if x%i==0:
        return False
  else:
     return True
n=int(input())
l=list(map(int,input().split()))
c=0
k=0
for i in range(n):
 if prime(l[i])==True:
    c=c+l[i]
    k=k+1
res="{:.2f}".format(c/k)
print(res)