#수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다.
#그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램

#내가 쓴 코드
for i in range(10):
	a = int(input())
	num = list(str(a%42))
for i in range(10):
	print(num.count(str(i)))

#해결
num =[]
for i in range(10):
    n = int(input())
    num.append(n%42)
num = set(num)
print(len(num))