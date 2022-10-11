# 문제
# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.

# 출력
# 각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.
# 만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다. 단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.

word = input()
word = word.upper()

a,b,c,d,e,f,g=-1,-1,-1,-1,-1,-1,-1
h,i,j,k,l,m,n=-1,-1,-1,-1,-1,-1,-1
o,p,q,r,s,t,u = -1,-1,-1,-1,-1,-1,-1
v,w,x,z,y,z = -1,-1,-1,-1,-1,-1

#index 배열 위치
#cnt 글자
for index,cnt in enumerate(word):
    if(cnt == 'A'):
        if(a==-1):
            a = index
    elif (cnt == 'B'):
        if (b == -1):
            b = index
    elif (cnt == 'C'):
        if (c == -1):
            c = index
    elif (cnt == 'D'):
        if (d == -1):
            d = index
    elif (cnt == 'E'):
        if (e == -1):
            e = index
    elif (cnt == 'F'):
        if (f == -1):
            f = index
    elif (cnt == 'G'):
        if (g == -1):
            g = index
    elif (cnt == 'H'):
        if (h == -1):
            h = index
    elif (cnt == 'I'):
        if (i == -1):
            i = index
    elif (cnt == 'J'):
        if (j == -1):
            j = index
    elif (cnt == 'K'):
        if (k == -1):
            k = index
    elif (cnt == 'L'):
        if (l == -1):
            l = index
    elif (cnt == 'M'):
        if (m == -1):
            m = index
    elif (cnt == 'N'):
        if (n == -1):
            n = index
    elif (cnt == 'O'):
        if (o == -1):
            o = index
    elif (cnt == 'P'):
        if (p == -1):
            p = index
    elif (cnt == 'Q'):
        if (q == -1):
            q = index
    elif (cnt == 'R'):
        if (r == -1):
            r = index
    elif (cnt == 'S'):
        if (s == -1):
            s = index
    elif (cnt == 'T'):
        if (t == -1):
            t = index
    elif (cnt == 'U'):
        if (u == -1):
            u = index
    elif (cnt == 'V'):
        if (v == -1):
            v = index
    elif (cnt == 'W'):
        if (w == -1):
            w = index
    elif (cnt == 'X'):
        if (x == -1):
            x = index
    elif (cnt == 'Y'):
        if (y == -1):
            y = index
    elif (cnt == 'Z'):
        if (z == -1):
            z = index
print(a, b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z)
