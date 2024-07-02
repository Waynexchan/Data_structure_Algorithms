
#O(n)
def factorial_recursion(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial_recursion(num-1)
    

print(factorial_recursion(5))


#O(n)
def factorial_interaite(num):
    result = 1
    i = 2
    while i <= num:
        result = result*i
        i += 1
    return result

print(factorial_interaite(5))