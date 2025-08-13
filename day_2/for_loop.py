for i in range(1000):
    if i == 0:
        continue
    is_prime = True
    for j in range(i):
        if j == 0 or j == 1:
            continue
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print (i)
