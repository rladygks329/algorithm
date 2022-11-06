import sys

# 입력 받기
n = int(sys.stdin.readline())
length = int(sys.stdin.readline())
data = sys.stdin.readline()

# IOIOI 문자를 만듦
s = "I" + "OI" * n

# 순회에 필요한 데이터 선언
size = len(s)
i = 0
j = 0
count = 0

# 반복문을 도는 부분 101->01만찾으면 하나 더 즉 -2
for i in data:
    if(i == s[j]):
        j += 1
        if(j == size):
            count += 1
            j -= 2
    else:
        j = int(i == "I")
print(count)