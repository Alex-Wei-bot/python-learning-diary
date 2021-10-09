#英尺厘米换算
i=float(input('input an number'))
j=input('is it inch or centimeter?')
if j == 'inch':
    inch=i
    centimeter=inch*2.54
    print(f'the length in centimeter is {centimeter:.2}')
else:
    centimeter=i
    inch=centimeter/2.54
    print('the length in inch is %.2f' %inch)