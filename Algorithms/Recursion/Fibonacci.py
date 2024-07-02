def fibonacci_recursive(n): #O(2^n) use a lot of time
    
    if n < 2:
        return n
    else:
        return fibonacci_recursive(n-1) +fibonacci_recursive(n-2)

# print(fibonacci_recursive(6))


def fibonacci_iterative(n): #O(n)
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