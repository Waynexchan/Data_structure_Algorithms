

def reverseStringRecursive(str):
    if len(str) == 0:
        return ""
    
    else:
        return reverseStringRecursive(str[1:]) + str[0]
    

print(reverseStringRecursive("yoyo master"))

def reverseString(str):
    return ''.join(reversed(str))

result = reverseString("yoyo master")
print(result)


def reverseString2(str):
    return str[len(str)-1: : -1]

print(reverseString2("yoyo master"))

def reverse_for_loop(str):
    reversed_ans = ''

    for char in str:
        reversed_ans = char +reversed_ans

    return reversed_ans

def reverse_while_loop(str):
    reversed_ans = ""
    index = len(str)-1
    while index >= 0:
        reversed_ans = reversed_ans + str[index]
        index -= 1
    
    return reversed_ans

