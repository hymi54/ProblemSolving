class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        start_position : int = -1
        end_position : int = -1
        for i in range(len(nums)):
            # if target is found first
            if nums[i] == target and start_position == -1 :
                start_position = end_position = i
            elif nums[i] == target:
                end_position = i
        return [start_position,end_position]