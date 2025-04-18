    def findKRotation(self, arr):
      
        low=0
        high=len(arr)-1
        while low<=high:
            if arr[low]<=arr[high]:
                return low
            mid=(low+high)//2
            next_=(mid+1)%len(arr)
            prev=(mid-1+len(arr)%len(arr))
            if arr[mid]<=arr[next_] and arr[mid]<=arr[prev]:
                return mid
            if arr[mid]>=arr[low]:
                low=mid+1
            else:
                high=mid-1
                
