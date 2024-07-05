def fibonacci(n):
    if (n < 2):
        return n 
    
    return fibonacci(n-1) + fibonacci(n-2)


def fibonacci_dynamic():
    cache = {}
    calculation = 0

    def fib(n):
        nonlocal calculation
        calculation +=1
        if (n in cache):
            return cache[n]
        else:
            if (n < 2):
                return n
            else:
                cache[n] = fib(n-1) + fib(n-2)
                return cache[n]
            
    def get_calculation_count():
        return calculation
            
    return fib, get_calculation_count

fasterFib , get_calculation_count= fibonacci_dynamic()
print(fasterFib(10))
print(f'We did {get_calculation_count()} calculations')