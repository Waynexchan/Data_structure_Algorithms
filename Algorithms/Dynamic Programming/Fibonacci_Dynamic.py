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

def fibonacci_dynamic_bottom_up(n):
    answer = [0,1]
    for i in range (3, len(n)):
        answer.push(answer[i-1] + answer[i-2])

    return answer[-1]

fasterFib , get_calculation_count= fibonacci_dynamic()
print(fasterFib(10))
print(f'We did {get_calculation_count()} calculations')

# O (n) Time vs O(2^n)
# Drawback Increase Space Complexity.