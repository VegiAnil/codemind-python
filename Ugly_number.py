def ugly(n,div):
  while(n%div==0):
    n=n//div
  return n
n=int(input())
n=ugly(n,2)
n=ugly(n,3)
n=ugly(n,5)
if n==1:
  print("Ugly Number")
else:
  print("Not Ugly Number")