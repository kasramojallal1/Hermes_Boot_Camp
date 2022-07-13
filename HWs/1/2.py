def if_prime(num):
    
    if num == 1:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        
    return True

n = int(input("1: "))
m = int(input("2: "))

if n > m:
    print('num_2 must be bigger than num_1')
    exit()


count = 0
for i in range(n, m + 1):
    if if_prime(i):
        count += 1
        
print(count)