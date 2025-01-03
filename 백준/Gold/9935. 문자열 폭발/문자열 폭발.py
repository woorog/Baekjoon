bo = input()
boom = input()

stack = []
boom_len = len(boom)

for char in bo:
    stack.append(char)
    if ''.join(stack[-boom_len:]) == boom:
        del stack[-boom_len:]

result = ''.join(stack)
if result:
    print(result)
else:
    print("FRULA")
