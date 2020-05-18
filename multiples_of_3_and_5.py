### Problem 1 ###

n=1
i=0
while n < 1000 :
    if n % 3 == 0 or n % 5 == 0 :
        i+=n
    n+=1
print(i)

