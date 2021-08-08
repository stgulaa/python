#map을 이용하여 정수 a와 b를 입력받아 a+b출력
input_num = int(input()) #반복횟수 입력

for i in range(input_num):
    a,b=map(int, input().split())
    print(a+b)