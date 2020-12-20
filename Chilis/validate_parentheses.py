'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.'''


def isValid(s):
    # odd char number strings are False
    lista = [c for c in s]
    if len(lista) % 2 != 0:
        return False
    stack = []
    for char in s:
        if char in ["(", "[", "{"]:
            stack.append(char)
        elif len(stack) != 0:
            popped = stack.pop()
            if char == ")" and popped != "(":
                return False
            elif char == "]" and popped != "[":
                return False
            elif char == "}" and popped != "{":
                return False
        else:
            return False
    if len(stack) != 0:
        return False
    else:
        return True


print(isValid(")(){}"))
