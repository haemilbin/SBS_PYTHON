'''
    내장함수
    : 외부에 따로 정의한 모듈에 있는 함수가 아니라
      파이썬에 내장 되어있는 함수
      바로 사용할 수 있는 함수
'''
# 문자열 내장 함수
'''
    (참조) 모든 문자는 각각 문자 코드를 가지고 있다.
        (아스키 코드, 유니코드)
    
    1. chr() 함수
    : 특정 문자의 유니코드 값을 입력하면,
      해당 문자를 변환하는 함수
    
    2. ord() 함수
    : 특정 문자를 입력하면,
      해당 문자의 유니코드를 반환하는 함수
      
    3. eval() 함수
    : 표현식을 문자로 입력하면 표현식의 결과를 변환하는 함수
    ex) ecal('100 + 200') --> 300
        a = 10
        eval('a * 5') --> 50
    
    4. format() 함수
    : 전달받은 값과 포맷코드에 따른 형식 문자열을 변환하는 함수
    1,000,000
    format(1000000,',')     # 천 단위 구분 기호로 쉼표(,)를 사용
    
    5. str() 함수
    : 전달받은 함수를 문자열로 변환하는 함수
    ex) str(10) --> '10'
'''

# chr
from ast import expr


print(chr(97))
print(chr(98))
print(chr(99))
print(chr(100))

# ord
print(ord('a'))
print(ord('b'))
print(ord('c'))
print(ord('d'))

# eval
expr = input('수식을 입력: ')
result = eval(expr)
print('계산 결과: ' + str(result))

# format
print( format(1000000, ',') )

# str
print( str(1,5) )
