a = int(input())
b = int(input())

b_100 = int(b/100)
b_10 = int(b%100/10)
b_1  = int(b%10)

print(a*b_1)
print(a*b_10)
print(a*b_100)
print(a*b)