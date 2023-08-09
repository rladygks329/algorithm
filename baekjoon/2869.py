import sys
import math

def sol(day, night, height):
    if(height <= day):
        return 1
    return math.ceil((height - day)/(day-night))+1

if __name__ == '__main__':
    day, night, height = map(int, sys.stdin.readline().split())
    print(sol(day, night, height))