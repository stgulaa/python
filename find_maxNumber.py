#내가 짠 코드
number = list(map(int, input().split()))
print(max(number))

for i in number:
  if(max(number)==number[i]):
    print(i+1)
    break