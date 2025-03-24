def sum_array(a,n,i):
    if i >=n:
        return 0
    return a[i]+sum_array(a,n,i+1)
def check_sort(a,n,i):
    if i >= n-1:
        return True
    if a[i]>a[i+1]:
        return False
a=[89,0,2,5,4]
print(check_sort(a,5,0))
