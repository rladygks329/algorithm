import sys

n, T  = map(int, sys.stdin.readline().split())
data = [[0 for i in range(n)] for j in range(n)]
valid = [1 for i in range(n)]
count = 0

for _ in range(T):
    i, j = map(lambda x: int(x)-1, sys.stdin.readline().split())
    data[i][j] = 1
    data[j][i] = 1

for i in range(n):
    if(valid[i] == 1):
        s = [i]
        while(s):
            a = s.pop()
            for b in range(n):
                if(data[a][b] == 1 and valid[b] == 1):
                    valid[b] = 0
                    s.append(b)
        count += 1
        
print(count)
    
     