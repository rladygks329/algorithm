import sys

n, m = map(int, sys.stdin.readline().strip().split())
arr = [sys.stdin.readline().strip() for i in range(n)]
length = sum(map(len, arr))

needLonger = (m - length)%(n - 1)
separator = '_' * ((m - length)//(n-1))
separatorL = separator + '_'
index = 0

answer = []
for i in range(n + n - 1):
    if i%2 == 0:
        answer.append(arr[index])
        index += 1
        continue
    else:
        # 소문자인 경우
        if 'a' <= arr[index][0] <= 'z':
            if needLonger:
                answer.append(separatorL)
                needLonger -= 1
            else:
                answer.append(separator)
        # 대문자인 경우
        else:
            if n - index == needLonger:
                answer.append(separatorL)
                needLonger -= 1
            else:
                answer.append(separator)
print(''.join(answer))

