def printrec(a, n, i, target):
    if i >= n:  
        return -1
    if a[i] == target: 
        return i
    return printrec(a, n, i + 1, target)  
a = [1, 2, 389, 4, 5]
result = printrec(a, 5, 0, 4)
print(result)  
