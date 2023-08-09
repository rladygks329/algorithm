import sys

len_of_poketmon, num_of_problem = map(int, sys.stdin.readline().split())
data = []
dictionary = {}
for i in range(len_of_poketmon):
    poketmon_name = sys.stdin.readline().strip()
    data.append(poketmon_name)
    dictionary[poketmon_name] = i
for i in range(num_of_problem):
    input = sys.stdin.readline().strip()
    if(input.isnumeric()):
        print(data[int(input)-1])
    else:
        print(int(dictionary[input])+1)
