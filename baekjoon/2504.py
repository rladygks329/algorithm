import sys

s = sys.stdin.readline().strip()
stack = []
nums = []
answer = 0
depth = 0

for braket in s:
    if braket in '([':
        stack.append(braket)
        depth += 1
    else:
        if not stack:
            print(0)
            sys.exit()
        elif braket == ')' and stack.pop() == '(':
            hasChild = True
            for i in range(len(nums)):
                dep, value = nums[i]
                if dep > depth:
                    nums[i] = (nums[i][0]-1, nums[i][1] * 2)
                    hasChild = False
            if hasChild:
                nums.append((depth, 2))
            depth -= 1
            if depth == 0:
                answer += sum(map(lambda x: x[1], nums))
                nums.clear()
        elif braket == ']' and stack.pop() == '[':
            hasChild = True
            for i in range(len(nums)):
                dep, value = nums[i]
                if dep > depth:
                    nums[i] = (nums[i][0]-1, nums[i][1] * 3)
                    hasChild = False
            if hasChild:
                nums.append((depth, 3))
            depth -= 1
            if depth == 0:
                answer += sum(map(lambda x: x[1], nums))
                nums.clear()
        else:
            print(0)
            sys.exit()

print(answer if not stack else 0)