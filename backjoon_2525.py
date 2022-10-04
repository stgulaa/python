h, m = map(int, input().split())
c = int(input())
c_final = m + c

if (h >= 0 and h <= 23):
    if (m >= 0 and m <= 59):
        if (c >= 0 and c <= 1000):
            if (c_final >= 60):  # 분의 결과가 60분 이상이면
                h = h + int(c_final / 60)
                c_final = c_final - 60 * int(c_final / 60)
                if(h>=24):
                    h = h-24
            if (c_final == 60):
                c_final = 0
                if (h >= 24):
                    h = h - 24
print(str(h) + " " + str(c_final))