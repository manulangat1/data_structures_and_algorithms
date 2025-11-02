"""

    * Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
    * Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
    * Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
    Return k.
"""

class Solution: 
    def removeElement(self, arr,val):

        # start at 0, this will be used to re order the elements 
        k = 0 

        for i in range(len(arr)): 
            if ( arr[i] != val): 
                arr[k] = arr[i]

                k += 1
        return k

mySolution = Solution()
#  arr of custom test  arrs. 
for arr in [ [3,2,2,3]] : 
    print(mySolution.removeElement([arr], 3))