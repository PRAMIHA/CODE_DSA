def cum_of_dig(n):
    if n==0:
        return 0
    if n<10:
        return n
    return n%10+cd(n//10)
print(sum_of_dig(256))
