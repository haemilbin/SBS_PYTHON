# 형식을 갖춘 문자열
# %
# %d 정수(10진수)
# %o 정수(8진수)
# %x 정수(16진수)
# %f 실수
# %s 문자열

a = 10
b = 20
print('%d' % 10)
print('%o' % 10)
print('%x' % 10)
print('%f' % 3.14)
print('%s' % 'python')
print('%d %d' % (a,b))

# 문자열 형식 문자 %s는 정수, 실수 모두 처리할 수 있다.
print('%s' % 100)
print('%s' % 3.14)

