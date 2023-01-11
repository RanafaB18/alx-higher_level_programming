#!/usr/bin/python3

def pascal_triangle(n, stack=[]):
    for i in range(1, n + 1):
        if i == 1:
            stack.append([1])
        elif i == 2:
            stack.append([1, 1])
        else:
            index = 0
            layer = []
            TOS = stack[-1]
            while index < len(TOS) + 1:
                if index == 0:
                    layer.append(1)
                elif index == len(TOS):
                    layer.append(1)
                else:
                    sum = TOS[index] + TOS[index - 1]
                    layer.append(sum)
                index += 1
            stack.append(layer)
    return stack
