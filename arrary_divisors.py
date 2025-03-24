def print_divisors(n,i=1):
    if i>n:
        return n
    if n%i==0:
        print(i,end="")
    print_divisors(n,i+1)
num=6
print_divisors(num)
