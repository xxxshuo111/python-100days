score=float(input('请输入分数：'))
if score>=90:
    level='A'
elif score>=80:
    level='B'
elif score>=70:
    level='C'
elif score>=60:
    level='D'
else:
    level='F'
print(level)