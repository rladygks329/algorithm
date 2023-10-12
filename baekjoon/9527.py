import sys

s, e = map(int, sys.stdin.readline().strip().split())
dp = [0] * 66

for i in range(60):
    dp[i] = (i * 2**(i-1)) + 1
dp[0] = 1

#
# for i in range(1, 65):
#     dp[i] = dp[i-1] + i.bit_count()
# print(dp)


def helper(n):
    n = list(str(bin(n).replace('0b', '')))
    size = len(n)
    result = 0
    print(n)
    for i in range(size):
        if n[i] == '1':
            result += dp[size - i - 1]

    return result

answer = []
for i in range(1, 20):
    answer.append(helper(i))
print(dp)
print(answer)
'''
[0, 1, 2, 4, 5, 7, 9, 12, 13, 15, 17, 20, 22, 25, 28, 32, 33]

[0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1]



10000
->
0000 1111 1이 4개네?
0001 1110 1이 4개네?
4비트로 만들수 있는 수 
-> 1111 까지 1의 합 : (4 * 16)/2
-> 16 까지의 합 : (4 * 16)/2+ 1 (10000)
-> 2^n 까지의합 : n*(2^n)/2 + 1

12 = 1100
1000
+ 100

15까지의 합 => 4 * 16 / 2 =? 32?
0000 1111
0001 1110
0010 1101
0011 1100
0100 1011
.
.
.

'''