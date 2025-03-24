def sum_array(a,n,i):
    if i >=n:
        return 0
    return a[i]+sum_array(a,n,i+1)
a=[1,3,2,4,5]
print(sum_array(a,5,0))
