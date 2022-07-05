import sys
num_of_test = int(sys.stdin.readline())
for i in range(num_of_test):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    data = [[0 for width in range(n)] for height in range(k+1)]
    for height in range(k+1):
        for width in range(n):
            if(height == 0):
                data[height][width] = width+1
            elif(width == 0):
                data[height][width] = 1
            else:
                data[height][width] = data[height-1][width] + data[height][width-1]
    print(data[height][width])
'''
0층 1호:1명, 2호:2명, 3명:3명
1층:1호:1명, 2호:3명, 3호:6명
2층:1호:1명, 2층:4명, 3층:10명
'''