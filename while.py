# 백준 알고리즘 - 0이 들어올 때까지 A+B를 출력하는 문제
while True:
    	a,b = map(int, input().split())
	if(a==0):
		if(b==0):
			break
	print(a+b)