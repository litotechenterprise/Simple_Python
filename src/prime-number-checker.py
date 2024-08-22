def is_prime(num):
    prime = True
    if num == 1 or num == 2:
        return prime
    
    for i in range(2,num):
        result = num % i
        print(f"{num} % {i} = {result}")
        if result == 0:
            prime = False
            break
    return prime

print(is_prime(8))