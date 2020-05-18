def prime_factor(n):
    result = []
    for i in range (1,10000):
        if n % i == 0:
            result.append(i)
    print(max(result))
    
prime_factor(600851475143)
