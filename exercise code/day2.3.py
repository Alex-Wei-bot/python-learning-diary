#闰年判断
year=int(input('input a year:'))
if year/4==0 and not year/100==0:
    print('是闰年')
elif year/400==0:
    print('是闰年')
else:
    print('非闰年')
#version 2
year=int(input('input a year:'))
if year/4==0 and not year/100==0 or year/400:
    print('true')
else: print('false')