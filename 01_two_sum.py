class Solution(object):

	def twoSum(self, nums, target):
		"""
		:type num: List[int] 
		:type target: int 
		:rtype: List[int]
		"""
		map = {}
		for i, num in enumerate(nums):
			complement = target - num 
			if complement in map: 
				return [i, map.get(complement)]
			map[num] = i
		

sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))