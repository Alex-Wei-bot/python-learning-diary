#华氏温度摄氏温度转换器
f=float(input())
c=(f-32)/1.8
print(c)
#version 2
print('%.1ff=%.1fc' %(f,c))
#version 3
print(f'{f:.1f}f={c:.1f}c')