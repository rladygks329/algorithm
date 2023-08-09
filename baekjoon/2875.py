import sys

woman, man, intern = map(int, sys.stdin.readline().split())

while intern:
    if(woman > 2 * man):
        woman -= 1
    else:
        man -= 1
    intern -= 1

print(man if 2 * man < woman else woman //2)