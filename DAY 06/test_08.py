
# 대한민국의 수도는 서울이다.

# 무한 반복: 무조건 계속 반복하는 반복문
# 반드시, 종료조건을 넣어주어야 한다.
while True:
    city = input('대한민국의 수도는?')
    if city == '서울':
        print('정답입니다.')
        break
    else:
        print('틀렸습니다.')
        