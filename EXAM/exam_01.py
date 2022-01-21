'''
    제어문(조건문, 반복문) 을 이용하여,
    아래와 같이 * 문자로 이루어진 도형을 출력하는
    프로그램을 완성하시오
    1단계)
    숫자 N을 입력받아 N행의 줄에 다음과 같이
    삼각형 모양을 출력하는 프로그램
    (입력 예시)
    N: 5 
    *
    **
    ***
    ****
    *****
    2단계)
    (입력 예시)
    N: 5 
        *
       ***
      *****
     *******
    *********
'''

# 1단계
# 1. 입력 받은 수 N만큼 줄이 반복
# 2. N번째 줄의 크기만큼 별의 개수가 반복

N = input('N: ')
N = int(N)

# i: 0,1,2,3,4
for i in range (0,N):
    for j in range(0,i+1):
        print('*',end="")
    print()

# 2단계
# N: 5
# i: 1,2,3,4,..N
for i in range(1, N+1):
    for j in range(N-i):
        print(' ', end='')
    for j in range(1, i*2):
        print('*', end='')
    print()
            
        
        