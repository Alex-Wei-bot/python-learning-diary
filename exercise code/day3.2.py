#百分制成绩转换为等级制
score=int(input('type down ur score plz'))
if score >=90 and score <=100:
    print('your ranking is A')
elif score >=80:
    print('your ranking is B')
elif score >=70:
    print('your ranking is C')
elif score >=60:
    print('your ranking is D')
elif score >=0:
    print('your ranking is E')
else: print('score invalid')