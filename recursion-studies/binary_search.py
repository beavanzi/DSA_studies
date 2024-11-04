# Tip: Do NOT Overthink!

def BS(arr, target, start, end):
    
    if start > end:
        return -1
    
    mid = (start + end + 1)//2;
    
    if arr[mid] == target:
        return mid
    
    # if target is greater than the middle element, then target is in the left half
    if target < arr[mid]:
        return BS(arr, target, start, mid-1)
    
    # if target is less than the middle element, then target is in the right half
    if target > arr[mid]:
        return BS(arr, target, mid+1, end)
    

assert BS([1,2,3,4,5,6,7,8,9,10], 7, 0, 9) == 6
assert BS([1,2,3,4,5,6,7,8,9,10], 1, 0, 9) == 0
assert BS([1,2,3,4,5,6,7,8,9,10], 10, 0, 9) == 9
assert BS([1,2,3,4,5,6,7,8,9,10], 50, 0, 9) == -1