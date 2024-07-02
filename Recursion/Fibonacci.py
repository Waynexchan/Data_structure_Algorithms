def fibonacci_recursive(n):
    f0 = 0
    f1 = 1
    if n == 1:
        return 1
    elif n ==2:
        return 1
    else:
        return fibonacci_recursive(n-1) +fibonacci_recursive(n-2)

# print(fibonacci_recursive(6))


def fibonacci_iterative(n):
    result = 0
    i =3
    temp1 = 1
    temp2 = 1
    if n == 1 :
        result =1
    elif n == 2:
        result =1
    else:
        while i <= n:
            result = temp1 + temp2
            temp1 =temp2 
            temp2 = result
            i+= 1

    return result
    
print(fibonacci_iterative(7))