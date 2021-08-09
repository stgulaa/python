#내가 짠 코드 - 문제 코드를 잘못인식함
#내가 이해한 것) 모든 입력이 끝났을 때 각각 더한 값을 한번에 출력
#출제의도) 입력이 들어오면 바로 더한 값 출력
result =[]

while True:
	a,b = map(int, input().split())
	adding = a+b
	result.extend([adding])
	if(a>0 & b<10):
		break

for i in result:
	print(i)


#타 코드
while True:
    try:
        a,b = map(int, input().split())
    except:
        break
    print(a+b)