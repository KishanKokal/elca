import re

precedence = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3
}

def infix_to_postfix(expression):
    postfix = []
    stack = []
    for token in re.findall('\d+|\w+|\+|\-|\*|\/|\^|\(|\)', expression):
        if token.isdigit() or token.isalpha():
            postfix.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence[token] <= precedence[stack[-1]]:
                postfix.append(stack.pop())
            stack.append(token)
    while stack:
        postfix.append(stack.pop())
    return postfix

def generate_tac(postfix):
    stack = []
    count = 0
    for token in postfix:
        if token.isdigit() or token.isalpha():
            stack.append(token)
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            count += 1
            result = 't' + str(count)
            print(result + ' = ' + op1 + ' ' + token + ' ' + op2)
            stack.append(result)

expression = input('Enter a mathematical expression: ')
postfix = infix_to_postfix(expression)
print('Postfix expression:', ' '.join(postfix))
generate_tac(postfix)