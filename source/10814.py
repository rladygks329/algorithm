import sys

class Member:
    def __init__(self, age, name):
        self.age = int(age)
        self.name = name
    def __str__(self):
        return str(self.age) + " " + self.name
    def __repr__(self):
        return  str(self.age) + " " + self.name

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    data = []
    for i in range(n):
        age, name = sys.stdin.readline().split()
        data.append(Member(int(age), name))
    data.sort(key=lambda mem: mem.age)
    for i in range(n):
        print(data[i])