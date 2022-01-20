
# for문과 range()함수
# range(): 범위를 생성하는 함수
# 구조: range(초기값, 종료값, 증감값)

# range(5): 0,1,2,3,4
# range(1,11): 1,2,3,4,...,10 -> 종료값-1 까지 증가
# range(1,10,2): 1,3,5,7,9

# 단을 입력받아서 구구단을 출력하시오
dan = input("단: ")
dan = int(dan)
for n in range(1,10):
    print('{} x {} = {}'.format(dan, n, dan*n))
    
# 중첩 반복문: 반복문 안에 또 하나의 반복문을 작성
# i: 2~9
# j: 1~9
print()
for i in range(2,10):
    for j in range(1,10):
        print('{} x {} = {}'.format(i, j, i*j))
    print()
    
