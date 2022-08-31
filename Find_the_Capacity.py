p,t,r=map(int,input().split())
c=2*p*t*r*512
s=str(c//1024)
print(s+'KB')