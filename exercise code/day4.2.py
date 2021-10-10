#判断两个正整数的最小公倍数与最小公约数
i=int(input())
j=int(input())
minimum=min(i,j)
m=0
n=max(i,j)
for k in range(1,minimum+1):
    if i%minimum==0 and j%minimum==0 and k>=m:
        m=k
while(n%i!=0 or n%j!=0):
    n+=1
print('最小公倍数是%d' %(n))
print('最小公约数是%d' %m)