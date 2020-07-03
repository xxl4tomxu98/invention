""" A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].

Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the left of a closing bracket (i.e., ), ], or }) of the exact same type. There are three types of matched pairs of brackets: [], {}, and ().

A matching pair of brackets is not balanced if the set of brackets it encloses are not matched. For example, {[(])} is not balanced because the contents in between { and } are not balanced. The pair of square brackets encloses a single, unbalanced opening bracket, (, and the pair of parentheses encloses a single, unbalanced closing square bracket, ].

By this logic, we say a sequence of brackets is balanced if the following conditions are met:

It contains no unmatched brackets. i.e. the opening and closing brackets are of same number.
The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets.
Given  strings of brackets, determine whether each sequence of brackets is balanced. If a string is balanced, return YES. Otherwise, return NO.

Function Description

Complete the function isBalanced in the editor below. It must return a string: YES if the sequence is balanced or NO if it is not.

isBalanced has the following parameter(s):

s: a string of brackets """


def matches(a, b):
    if (a == "{" and b == "}") or (a == "(" and b == ")") or (a == "[" and b == "]"):
        return True
    else:
        return False


def isBalanced(s):
    mystack = []
    p = "NO"
    for i in s:
        if i in ["[", "{", "("]:
            mystack.append(i)
        else:
            # situation that closing brackets appear first
            if len(mystack) == 0:
                return "NO"
            else:
                b = mystack.pop()
            if matches(b, i):
                p = "YES"
            else:
                return "NO"
    # balanced in numbers but maynot match
    if len(mystack) == 0:
        return p
    # unbalanced in numbers
    else:
        return "NO"


print(isBalanced("{[()]}"))
print(isBalanced("{[(])}}"))
print(isBalanced("{{[[(())]]}}"))
