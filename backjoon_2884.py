#h = int(input())
#m = int(input())

h,m = map(int,input().split())

if(h>=0 and h<=23):
  if(m>=0 and m<60):
    alert_m = m - 45
    if alert_m < 0:
      if(h==0):
        print("23 " +str(alert_m+60))
      else:
        print (str(h-1) + " " + str(alert_m+60))
    else:
      print(h)
      print(alert_m)

#만약 h와 m 변수를 각각 받는 경우 런타임 에러(Runtime Error)가 발생한다
# "첫째 줄에 두 정수 H와 M이 주어진다."라고 명시되어 있기 때문이다...문제를 읽자