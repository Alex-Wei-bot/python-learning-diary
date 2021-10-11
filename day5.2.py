#perfect number(slow algorithm version)
for i in range(1,10000):
    set1=set()
    sum=0
    for k in range(1,i):
        if i%k==0:
            set1.add(k)
    for j in range(len(set1),0,-1):
        sum+=set1.pop()
    if sum == i:
        print(f'{i}是完美数')