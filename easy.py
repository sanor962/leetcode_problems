class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        answer = len(set(nums))
        new = sorted(list(set(nums)))
        num = len(set(nums))
        for i in range(len(nums)):
            if i < num:
                nums[i] = new[i]
            else:
                nums[i] = 0
        return answer

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        sorted_array = sorted(nums1[:m] + nums2[:n])
        for i in range(len(sorted_array)):
            nums1[i]= sorted_array[i]

    def removeElement(self, nums: List[int], val: int) -> int:
        good_list = []
        for i in range(len(nums)):
            if nums[i] != val:
                good_list.append(nums[i])
        for i in range(len(nums)):
            if i < len(good_list):
                nums[i] = good_list[i]
            else:
                nums[i] = None
        return (len(good_list))

    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        while s.find(" ") != -1:
            s = s[s.find(" ") + 1:]
        return len(s)

    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)