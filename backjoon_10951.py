# 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다.

# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

# 출력
# 각 테스트 케이스마다 A+B를 출력한다.

while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break

#아래와 같은 경우 종결 조건이 명확하지 않아 eof 오류 발생
#파이썬은 정보를 입력받을 때 어디가 끝인지 확인이 불가하므로 예외처리가 없으면 계속적으로 입력을 받기 때문
#try-catch문을 이용할 경우 몇 개의 테스트 케이스가 주어졌는지 몰라도 입력을 EOF까지만 받도록 함
while True:
    a, b = map(int, input().split())
    if(a>0 & b<10):
        print(a+b)
    else: break