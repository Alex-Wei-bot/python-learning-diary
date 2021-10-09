#输入三条边，若能构成三角形则计算周长和面积
import math
a,b,c=input("input three number as a triangle's edges")
a=int(a)
b=int(b)
c=int(c)
if a+b>c and a+c>b and b+c>a:
    q=(a+b+c)/2
    square=math.sqrt(q*(q-a)(q-b)(q-c))
    circumference=2*q
else: print('invalid edge number')