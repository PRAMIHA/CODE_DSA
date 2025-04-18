def ZerosToEnd(arr):
  n=len(arr)
  j=0
  for i in range(n):
    if arr[i]!=0:
      arr[j]=arr[i]
      j+=1
  for i in range(j,n):
    arr[i]=0
    return arr 
arr=[1,0,6,9,7,0]
print(ZerosToEnd(arr))
