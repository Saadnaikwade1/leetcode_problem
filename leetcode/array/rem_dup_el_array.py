
# remove duplicate element from sorted array

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i=0
    r=[]
    for i in set(nums):
        if i not in r:
            r.append(i)
    return r
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

