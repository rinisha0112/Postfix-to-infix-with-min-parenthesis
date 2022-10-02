# POSTFIX TO INFIX WITH MINIMUM PARENTHESIS
from collections import deque

#expression = "KL+MN*-OP^W*U/V/T*+Q+"
expression = "ab+cd+-ef+*"
exp_stack = deque()
op_stack = deque()

precedence = {
    '^': 3,
    '*': 2,
    '/': 2,
    '-': 1,
    '+': 1
}

for c in expression:
    if c in precedence.keys():
        right_operand = exp_stack.pop()
        left_operand = exp_stack.pop()
        right_operator = op_stack.pop()
        left_operator = op_stack.pop()

        if left_operator and precedence[left_operator] < precedence[c]:
            left_operand = '({})'.format(left_operand)

        if right_operator and precedence[right_operator] <= precedence[c]:
            if precedence[right_operator] == precedence[c]:
                if c=='/' or c=='-':
                    right_operand = '({})'.format(right_operand)
            else:
                right_operand = '({})'.format(right_operand)

        exp_stack.append(left_operand+c+right_operand)
        op_stack.append(c)
            

    else:
        exp_stack.append(c)
        op_stack.append(None)

print(exp_stack.pop())
