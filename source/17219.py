import sys

stdin = sys.stdin.read().splitlines()
n, m = map(int, stdin[0].split())
dict = {}

for site, password in map(lambda x: (x.split()[0], x.split()[1]), stdin[1:n+1]):
    dict[site] = password

for site in stdin[n+1:]:
    print(dict[site])