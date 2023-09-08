import sys

n, m = map(int, sys.stdin.readline().strip().split())
arr = sys.stdin.read().splitlines()
answer = ""
distance = m * n

for i in range(m):
    d = {
        "T" : 0,
        "A" : 0,
        "G" : 0,
        "C": 0
    }
    for j in range(n):
        letter = arr[j][i]
        d[letter] = d[letter] + 1

    count = 0
    letter = "T"
    for key, value in d.items():
        if value > count:
            count = value
            letter = key
        elif value == count and key < letter:
            letter = key
    answer += letter
    distance -= count

print(answer)
print(distance)