#for problem 383
from collections import Counter

#for problem 1
def two_sum_recursion(nums, target, point1, point2):
    if (nums[point1] + nums[point2]) > target:
        point2 -= 1
        return two_sum_recursion(nums, target, point1, point2)
    elif (nums[point1] + nums[point2]) < target:
        point1 += 1
        return two_sum_recursion(nums, target, point1, point2)
    else:
        answer = [point1, point2]
        return answer

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
    
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[floor(len(nums) / 2)]

    #WORST PROBLEM YET REVISE REVISE REVISE
    def maxProfit(self, prices: List[int]) -> int:
        # if prices == sorted(prices, reverse = True):
        #     print("reverse")
        #     return 0
        # # print(min(prices))
        # # print(prices)
        # # og_price = prices.copy()
        # # print(prices[prices.index(min(prices)):])
        # # if len(prices[prices.index(min(prices)):]) != 1:
        # #     return (prices[prices.index(max(prices[prices.index(min(prices)):]))] - prices[prices.index(min(prices))])
        # # prices.remove(min(prices))
        # # while len(prices) > 0:
        # #     print(prices)
        # #     minimum = min(prices)
        # #     if len(og_price[og_price.index(minimum):]) != 1:
        # #         return (og_price[og_price.index(max(og_price[og_price.index(minimum):]))] - og_price[og_price.index(minimum)])
        # # return 0
        # biggest_diff = 0
        # for i in range(len(prices)):
        #     for j in range(i, len(prices)):
        #         if (prices[j] - prices[i]) > biggest_diff:
        #             # print(prices[j])
        #             # print(j)
        #             # print(prices[i])
        #             # print(i)
        #             biggest_diff = prices[j] - prices[i]
        # return biggest_diff
        mini = prices[0]
        biggest_diff = 0
        for i in prices:
            if mini > i:
                mini = i
            if (i - mini) > biggest_diff:
                biggest_diff = (i - mini)
        return biggest_diff

    def longestCommonPrefix(self, strs):
        num = min(len(s) for s in strs)
        same = False
        while num > 0 and same == False:
            for s in strs:
                if strs[0][:num] != s[:num]:
                    num -= 1
                    same = False
                    break
                same = True
        return strs[0][:num]

    def rotate(self, nums: list[int], k: int) -> None:
        # if k > len(nums):
        #     for i in range(k):
        #         num = nums.pop()
        #         nums.insert(0, num)
        # else:
        #     new_num = nums[-k:] + nums[:k + 1]
        #     print(new_num)
        #     for i in range(len(nums)):
        #         nums[i] = new_num[i]
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        # counter = k
        # if k > len(nums):
        #     counter = counter % len(nums)
        # old_nums = nums.copy()
        # og = 0
        # for i in range(len(nums)):
        #     if counter > 0:
        #         nums[i] = old_nums[-counter]
        #         counter -= 1
        #     else:
        #         nums[i] = old_nums[og]
        #         og += 1

        #BOTH SOLUTIONS WORK BUT THE ONE BOTTOM IS MORE EFFICIENT AND CLEANER THAN THE ONE ABOVE
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # dict_a = {}
        # dict_b = {}
        # for i in magazine:
        #     dict_b[i] = dict_b.get(i, 0) + 1
        # for i in ransomNote:
        #     dict_a[i] = dict_a.get(i, 0) + 1
        #     if i not in dict_b.keys():
        #         return False
        # for key in dict_a.keys():
        #     if dict_a[key] > dict_b[key]:
        #         return False
        # return True
        dict_a = Counter(ransomNote)
        dict_b = Counter(magazine)
        for key in dict_a.keys():
            if dict_a[key] > dict_b.get(key, 0):
                return False
        return True

    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)):
            return False
        dict_s = {}
        for i in range(len(s)):
            if s[i] in dict_s:
                if dict_s[s[i]] != t[i]:
                    return False
            else:
                dict_s[s[i]] = t[i]
        return True

    def twoSum(self, nums, target):
        og_nums = nums[:]
        nums.sort()
        answer = two_sum_recursion(nums, target, 0, len(nums) - 1)
        if nums[answer[0]] == nums[answer[1]]:
            last_index = og_nums.index(nums[answer[1]], og_nums.index(nums[answer[0]]) + 1)
            return [og_nums.index(nums[answer[0]]), last_index]
        else:
            return [og_nums.index(nums[answer[0]]), og_nums.index(nums[answer[1]])]