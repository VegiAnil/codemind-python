n=int(input())
c=0
x=n
sq=n**2
t=10
while n>0:
  r=sq%t
  if r==x:
    c=c+1
  n=n//10
  t=t*10
if c==1:
  print("Automorphic Number")
else:
  print("Not an Automorphic Number")