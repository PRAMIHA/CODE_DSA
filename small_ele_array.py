n=5
arr=[]
for i in range(n):
  arr.append(int(input()))
small=arr[0]
for i in range(1,n):
  if small>arr[i]:
    small=arr[i]
print(arr[i])
