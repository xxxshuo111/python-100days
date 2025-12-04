1.注释的用法：
    """1111"""
    #1111
2.常见数据类型：
    整型（int），浮点型（float），字符串型（str），布尔型（bool）：只有True，False两个值
3.type函数：
a=100
print(type(a))
b=123.45
print(type(b))
4.类型强制转换：
a=100
b=123.45
c='100'
print(float(a))
print(int(b))
print(int(c,base=2)) #按照二进制（base=2）的方式转换为十进制整数4，只有str类型转int类型时可以通过base参数来指定进制
5.比较重要的运算符（按照优先级排序）：
**：幂
%：模（取余）
//：整除
*=：a*=a+2相当于a=a*（a+2）
+=：a+=b相当于a=a+b
示例
a = 10
b = 3
a += b        # 相当于：a = a + b
a *= a + 2    # 相当于：a = a * (a + 2)
print(a) 
6.
and：与 → 两边都为 True，结果才是 True
or：或 → 只要有一边是  True，结果就是 True
not：非 → 取反（not True 是 False，not False 是 True）
优先级：not>and>or
7.math-case构造分支结构
status_code = int(input('响应状态码: '))
match status_code:
    case 400: description = 'Bad Request'
    case 401: description = 'Unauthorized'
    case 403: description = 'Forbidden'
    case 404: description = 'Not Found'
    case 405: description = 'Method Not Allowed'
    case 418: description = 'I am a teapot'
    case 429: description = 'Too many requests'
    case _: description = 'Unknown Status Code'
print('状态码描述:', description)
如果有case是相同的 还可以这么写
    case 400 | 405: description = 'Invalid Request'
    case 401 | 403 | 404: description = 'Not Allowed'