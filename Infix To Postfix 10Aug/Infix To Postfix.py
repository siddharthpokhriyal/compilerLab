INFIX TO POSTFIX CONVERSION:-

Operator = {'+', '-', '*', '/', '(', ')', '^'}
Priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}


def post(value):
    stack = [ ]
    output = ' '

    for ch in value:
        if ch not in Operator:
            output += ch
        elif ch == '(':
            stack.append('(')
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()

        else:

            while stack and stack[-1] != '(' and Priority[ch] <= Priority[stack[-1]]:
                output += stack.pop()

            stack.append(ch)

    while stack:
        output += stack.pop()
    return output


expression = input('Enter infix expression')

print('infix expression: ', expression)
print('postfix expression: ', post(expression))
