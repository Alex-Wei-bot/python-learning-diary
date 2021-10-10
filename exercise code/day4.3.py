#打印三角形
#1
n=1
while(n<=5):
    print(n*'*')
    n+=1
#2
m=4
while(m>=0):
    print(m*' '+(5-m)*'*')
    m-=1
#3
for r in range(1,11,2):
    print(int(4-(r-1)/2)*' '+r*'*')

#3 update 添加了end的选项
for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()