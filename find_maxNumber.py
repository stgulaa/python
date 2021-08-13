#내가 짠 코드
number = list(map(int, input().split()))
print(max(number))

for i in number:
  if(max(number)==number[i]):
    print(i+1)
    break

#남의 코드
import sys
number =[]
max = 0

for i in range(0,10):
  number.append(int(sys.stdin.readline()))
  if number[i]>max:
    max = number[i]
    count = i+1
  
print(max)
print(count) 

#런타임 에러(indexError)를 없애기 위해 import sys를 추가

#최종 해결 코드
num_list = []
for i in range(9):
    num_list.append(int(input()))
    
print(max(num_list))
print(num_list.index(max(num_list))+1)
#런타임 에러(ERROR VALUE)를 위해 for문의 범위 이용