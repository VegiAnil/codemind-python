def revese(num):
    sum=0
    D=1
    if num<0:
        D=-1
        num=num*-1
    while num>0:
        r=num%10
        sum=sum*10+r
        num=num//10
    if not-2147483648<sum<2147483647:
        return 0
    return D*sum 
n=int(input())
print(revese(n))
 