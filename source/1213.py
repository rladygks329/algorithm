import sys

s = sys.stdin.readline().rstrip()
arr = [0] * 26

for alpha in s:
    arr[ord(alpha) - 65] += 1

answer, center = "", ""
for i in range(0, 26):
    if arr[i]%2 == 1:
        if not center == "":
            print("I'm Sorry Hansoo")
            sys.exit()
        else:
            center = chr(i + 65)
    answer += chr(i + 65) * (arr[i]//2)

print(f'{answer}{center}{answer[::-1]}')
