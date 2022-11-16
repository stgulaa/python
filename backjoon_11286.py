# 문제
# 절댓값 힙은 다음과 같은 연산을 지원하는 자료구조이다.
import getpass
# 배열에 정수 x (x ≠ 0)를 넣는다.
# 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. 절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.
# 프로그램은 처음에 비어있는 배열에서 시작하게 된다.

# 입력
# 첫째 줄에 연산의 개수 N(1≤N≤100,000)이 주어진다. 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다.
# 만약 x가 0이 아니라면 배열에 x라는 값을 넣는(추가하는) 연산이고, x가 0이라면 배열에서 절댓값이 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우이다.
# 입력되는 정수는 -231보다 크고, 231보다 작다.

# 출력
# 입력에서 0이 주어진 회수만큼 답을 출력한다. 만약 배열이 비어 있는 경우인데 절댓값이 가장 작은 값을 출력하라고 한 경우에는 0을 출력하면 된다.

from queue import PriorityQueue
import sys

q = PriorityQueue()
q_abs = PriorityQueue() # 절댓값을 담는 큐
n = int(input())

for i in range(n):
    x = int(sys.stdin.readline())
    if(x != 0):
        q.put(x)
        q_abs.put(abs(x))

    else: #입력이 0일 경우 절대값이 작은 것 출력
        if(q_abs.empty()): #큐가 빈 경우
            print("0")
        else:
            min = q_abs.get() #절대값이 가장 작은 값 min에 저장
            for i in range(q.qsize()): #원 값을 담은 큐를 순회하면서 min과 같은 -값이 있는지 확인
                turn = q.get() #q의 최솟값 저장
                if (turn == -min): #만약 -절댓값이 turn과 같다면 min 값 변경
                    min = turn
                    break
                else:
                    q.put(turn) #아닐 경우 q의 삭제된 값 다시 넣기

            print(min)



# 동일한 - 값이 들어오면 양수로 출력함 ex. -1 -1 -> 1, 1
