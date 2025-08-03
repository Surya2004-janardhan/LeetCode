class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}

        # o(n)


        for i in range(len(nums)):

            #i odu n times tirugutunnadu 


            num = target - nums[i] 
            
             #2 7 11 15
            # 2 in hashmap(2,3,4) o(1) 
            if num in hashmap:

                # {2:0,7:1}
            
                return [ hashmap[num] , i]
            else:
                hashmap[nums[i]] = i #2 = 0 hashmap pettuko

            

        
                
        
        
  
        