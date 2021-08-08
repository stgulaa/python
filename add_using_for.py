#n이 주어젔을 때, n까지의 합을 구한다.
num = int(input())
result = 0
for i in range(num):
	result = i+1 + result
print(result)