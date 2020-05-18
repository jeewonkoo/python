a = 1
b = 2
n_sum = 2
while b < 4000000: 
    b += a
    a = b - a
    if b % 2 ==0 :
        n_sum += b
print (n_sum)
