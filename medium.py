class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current_counter = 0
        counter = 0
        current = nums[0]
        old_nums = nums
        for i in range(len(old_nums)):
            if current != old_nums[i]:
                current_counter = 0
                current = old_nums[i]
            current_counter += 1
            if current_counter <= 2:
                nums[counter] = current
                counter += 1
        return counter