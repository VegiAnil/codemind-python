n=int(input())
s=list(str(n))
for i in range(len(s)):
    if s[i]=='6':
       s[i]='9'
       break
st=" "
for i in s:
    st+=i
print(int(st))    