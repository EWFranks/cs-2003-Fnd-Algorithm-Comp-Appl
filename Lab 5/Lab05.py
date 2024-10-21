# Eliga Franks
# Lab 05 – Spring 21
#First function see if the parentheses matach and the second function evaluates Postfix Expressions.
import obj as obj
from pythonds.basic.stack import Stack


def ParenMatch(equation):
    s = []
    sym = '( { ['
    for functionSym in equation:
        if functionSym in sym:
            s.append(functionSym)
        elif functionSym in sym:
            if len(s) == 0:
                return False
            s.pop()
            if functionSym == ')':
                return False
            elif functionSym == '}':
                return False
            elif functionSym == ']':
                return False
        return len(s) == 0


def PostfixExpression(expression):
    stack = []
    expression = expression.split()
    num = len(expression)

    for i in range(num):
        if expression[i].isdigit():
            stack.append(int(expression[i]))
        if expression[i] == "+":
            a = stack.pop()
            b = stack.pop()
            stack.append(int(a) + int(b))
        if expression[i] == "-":
            a = stack.pop()
            b = stack.pop()
            stack.append(int(b) - int(a))
        if expression[i] == "*":
            a = stack.pop()
            b = stack.pop()
            stack.append(int(a) * int(b))
        if expression[i] == "/":
            a = stack.pop()
            b = stack.pop()
            stack.append(int(b) / int(a))

    return stack.pop()


print("A*B+C*D")
print(ParenMatch("A*B+C*D"))
print("(A+B)*(C-(D-E))*(F+G)")
print(ParenMatch("(A+B)*(C-(D-E))*(F+G)"))
print("((A+{B+C}-[D-E])+[F]-[G]")
print(ParenMatch("((A+{B+C}-[D-E])+[F]-[G]"))
print("(A+B)*(C+D)")
print(ParenMatch("(A+B)*(C+D)"))
print("A/B-C+D*E-A*C")
print(ParenMatch("A/B-C+D*E-A*C"))
print("(((A/B)-C)+(D*E))-A*C)")
print(ParenMatch("(((A/B)-C)+(D*E))-A*C)"))
print("A/(B-C+D))*(E-A)*C")
print(ParenMatch("A/(B-C+D))*(E-A)*C"))

print()

print("9 7 2 - *")
print(PostfixExpression("9 7 2 - *"))
print("10 2 8 * + 3 -")
print(PostfixExpression("10 2 8 * + 3 -"))
print("5 2 + 8 3 - * 4 -")
print(PostfixExpression("5 2 + 8 3 - * 4 -"))
print("20 3 1 * + 90 -")
print(PostfixExpression("20 3 1 * + 90 -"))
