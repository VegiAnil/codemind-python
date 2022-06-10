def lcm(n1,n2):
    if n1>n2:
        high=n1
    else:
        high=n2
        value=high
        while True:
            if high%n1==0 and high%n2==0:
                return high
                break
            else:
                high=high+value
a,b=map(int,input().split())
print(lcm(a,b))