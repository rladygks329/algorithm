import sys

n = int(sys.stdin.readline())
# 고리 끝값 1 7 19 37 61 -> 1 , 1+6 , 1+6+12, 1+6+12+18, ... 1+6+ ... + 6^n-1

current = 1 #현재 보고 있는 위치가 어떻게 되니
count = 1 #몇번째고리니
tmp = 1 #무슨 수를 더해야하니
while( n > current):
    current += 6*tmp
    tmp += 1
    count += 1
print(count)