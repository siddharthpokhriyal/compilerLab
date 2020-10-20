s = input("Enter Prefix Expression:")
stack = []
Operators = {'+', '-', '*', '/', '^'}
s = s[::-1]
for i in s:
    if i in Operators:
        a = stack.pop()
        b = stack.pop()
        temp = a + b + i
        stack.append(temp)
    else:
        stack.append(i)

print("Postfix Expression:", *stack)
