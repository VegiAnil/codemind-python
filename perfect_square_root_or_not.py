num=int(input())
c=0
for i in range(1,num):
   if i*i==num:
      c=1
      break
if c==1:
   print(True)
else:
   print(False)