### Given an array of numbers , move all the non-zero elements to beginning of array and zeroes to the end
### Input array = [1,0,3,0,12]  Output should be = [ 1, 3, 12, 0, 0]

class Solution:
    def moveZeroesToEnd(self,array)->list:
        j=0

        for i in array:
            ## check for non-zero element and set the pointer j to that
            if i:
                array[j]=i
                j+=1
        ## set remaining elements to zero    
        for i in range(j,len(array)):
            array[i]=0
        
        return array
    
s=Solution()

print(s.moveZeroesToEnd([1,0,3,0,4,12]))

print(s.moveZeroesToEnd([0,0,12,0,1,13]))
