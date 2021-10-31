#设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
import random
def identify(len):
    list1=[]
    tuple1=('abcdefghijklmnopqrstuvwxyz')
    tuple2=('ABCDEFJHIJKLMNOPQRSTUVWXYZ')
    num=random.randint(1,len-2)
    for i in range(num):
        j=str(random.randint(0,9))
        list1.append(j)
    num2=random.randint(1,len-num-1)
    for j in range(num2):
        i=random.randint(0,9)
        list1.append(tuple1[i])
    for j in range(len-num-num2):
        i=random.randint(0,9)
        list1.append(tuple2[i])
    random.shuffle(list1)
    return list1

len=input()
len=int(len)
print(identify(len))