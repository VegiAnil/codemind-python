n=int(input())
n1=0#1
n2=1#0
sum=0#1,1,2
for i in range(n):
   print(sum,end=' ')#0,1,1,2
   n1=n2#1,0,1
   n2=sum#0,1,1
   sum=n1+n2#1,1,2
  