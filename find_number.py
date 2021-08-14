#자연수 a,b,c,가 주어질 때, a*b*c를 계산한 결과에 0부터 9까지 각각 숫자가 몇 번 나온는지 알 수 있는 프로그램
#내가 짠 코드
a,b,c = map(int, input().split())

result = list(str(a * b * c))
for i in range(10):
    print(result.count(str(i)))

#문제발생) 런타임 에러(ValueError)

#최종 코드
a = int(input())
b = int(input())
c = int(input())

result = list(str(a * b * c))
for i in range(10):
    print(result.count(str(i)))