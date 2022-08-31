n=int(input())
n1=0#1
n2=1#0
sum=0#1,1,2
if n==1 or n==0:
   print(True)
else:
  while sum<n:
    n1=n2#1,0,1
    n2=sum#0,1,1
    sum=n1+n2#1,1
  if sum==n:
     print(True)
  else:
     print(False)