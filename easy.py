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

    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(t) == Counter(s)

    def summaryRanges(self, nums: List[int]) -> List[str]:
        answer = []
        if nums == []:
            return []
        previous = nums[0]
        beginning = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > (previous + 1):
                if beginning == previous:
                    answer.append(f"{previous}")
                else:
                    answer.append(f"{beginning}->{nums[i-1]}")
                beginning = nums[i]
            previous = nums[i]
        if beginning == previous:
            answer.append(f"{previous}")
        else:
            answer.append(f"{beginning}->{nums[-1]}")
        return (answer)

    def isPalindrome(self, x):
        return (str(x) == (str(x)[::-1]))

    def plusOne(self, digits: List[int]) -> List[int]:
        actual_num = 0
        for i in range(len(digits)):
            actual_num = actual_num + (digits[-i - 1] * 10**i)
        actual_num += 1
        answer = []
        while actual_num > 0:
            answer.append((actual_num % 10))
            actual_num = (actual_num // 10)
        return answer[::-1]

    #REVIEW REVIEW REVIEW
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left = 1
        right = x
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1
        return right

    #REVIEW REVIEW REVIEW
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return list1
        elif list1 == None and list2 != None:
            return list2
        elif list1 != None and list2 == None:
            return list1
        if list1.val > list2.val:
            answer = ListNode(list2.val, None)
            list2 = list2.next
        else:
            answer = ListNode(list1.val, None)
            list1 = list1.next
        head = answer
        while list1 != None or list2 != None:
            if list1 != None and list2 != None:
                if list1.val > list2.val:
                    answer.next = list2
                    answer = answer.next
                    list2 = list2.next
                else:
                    answer.next = list1
                    answer = answer.next
                    list1 = list1.next
            elif list1 == None:
                answer.next = list2
                break
            else:
                answer.next = list1
                break
        return head