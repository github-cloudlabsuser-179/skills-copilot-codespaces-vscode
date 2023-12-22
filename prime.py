def prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i is 0:
            return False
    return True

