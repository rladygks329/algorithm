import sys
import _collections

#sys.stdin = open("../input/1966.txt", "r")

n = int(input())
for i in range(n):
    number_of_document, target = map(int, input().split())

    arr = _collections.deque(map(int, input().split()))
    result = False
    count = 0
    while(not result):
        x = False
        #자신보다 중요한게 있는지 검사
        for i in arr:
            if(i > arr[0]):
                x = True
                break

        tmp = arr.popleft()

        if (x): #중요한게 있으므로 빼서 옆에 넣는다.
            arr.append(tmp)
            if (target == 0):
                target = len(arr)-1
            else:
                target -= 1
        else: # 중요한게 없으므로 빼기만 한다.
            count += 1
            if (target == 0):
                result = True
            else:
                target -= 1
    print(count)



