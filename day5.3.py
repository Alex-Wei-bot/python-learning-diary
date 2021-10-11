#100以内的素数
n=[]
for i in range(1,100):
    sum=0
    for k in range(1,i+1):
        if i%k==0:
            sum+=1
    if sum==2:
        n.append(i)
print(n)