#判断一个正整数是否为素数
while(True):
    i=int(input('input a positive number'))
    if type(i)!=int:
        continue
    counter=0
    for j in range(1,i+1):
        if i%j==0:
            counter+=1
        if counter>2:
            print('非素数')
            break
    if counter<=2:
        print('是素数')
    if input()=='Esc':
        break