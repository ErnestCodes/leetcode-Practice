# visualize the recursive tree, cache solution for O(n) time/mem complexity, iterative is O(1) mem, 
# just iterate backwards to see if element can reach goal node, if yes, then set it equal to goal node, continue;
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) -1
        
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False
