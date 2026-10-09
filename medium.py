#helper function for myPow or problem 50
def pow_help(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    half = pow_help(x, n//2)
    if n % 2 == 1:
        return half * half * x
    return half * half

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

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        sort = {}
        for i in range(len(strs)):
            key = tuple(sorted(strs[i]))
            if key not in sort:
                sort[key] = [strs[i]]
            else:
                sort[key].append(strs[i])
        for key in sort.keys():
            answer.append(sort[key])
        return answer

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

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return (1/pow_help(x, abs(n)))
        return pow_help(x, n)

    #REVIEW REVIEW REVIEW
    def trailingZeroes(self, n: int) -> int:
        #num = (factorial(n))
        # counter = 0
        # while num > 0 and num % 10 == 0:
        #     counter += 1
        #     num = num // 10
        # return counter
        # if n > 25:
        #     return n // 5 + 1
        # else: 
        #     return n // 5
        # # return if n > 25: n // 5 + 1 else: n // 5
        counter = 0
        while n >= 5:
            n = n // 5
            counter += n
        return counter

    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [(left + 1), (right + 1)]
            if current_sum > target:
                right = right - 1
            else:
                left = left + 1
        return []

    def longestConsecutive(self, nums: list[int]) -> int:
            # if nums == []:
            #     return 0
            # sort = list(sorted(set(nums)))
            # current = 0
            # biggest = 0
            # for i in range(len(sort) - 1):
            #     if sort[i] + 1 == sort[i + 1]:
            #         current += 1
            #     else:
            #         if biggest < current:
            #             biggest = current
            #         current = 0
            # if biggest < current:
            #     biggest = current
            # return (biggest + 1)
            longest = 0
            nums = set(nums)
            for i in nums:
                if (i - 1) not in nums:
                    length = 0
                    k = i
                    while k in nums:
                        length+=1
                        k+=1
                    longest = max(longest, length)
            return longest

    #solution 1
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        counter = 0
        num1 = 0
        num2 = 0
        while l1 != None or l2 != None:
            if l1 != None:
                num1 = num1 + (l1.val * pow(10, counter))
                l1 = l1.next
            if l2 != None:
                num2 = num2 + (l2.val * pow(10, counter))
                l2 = l2.next
            counter+=1
        answer = num1 + num2
        head = ListNode(0, None)
        current_node = head
        while answer >= 10:
            last = answer % 10
            answer = int(answer // 10)
            current_node.val = last
            current_node.next = ListNode(0, None)
            current_node = current_node.next
        current_node.val = answer % 10
        return head

    #solution 2 (better time complexity)
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        counter = 0
        num1 = 0
        num2 = 0
        carry = 0
        head = ListNode(0, None)
        current_node = head
        while l1 != None or l2 != None:
            num1 = 0
            num2 = 0
            if l1 != None:
                num1 = (l1.val)
                l1 = l1.next
            if l2 != None:
                num2 = (l2.val)
                l2 = l2.next
            counter+=1
            answer = num1 + num2 + carry
            last = answer % 10
            carry = int(answer // 10)
            current_node.next = ListNode(0)
            current_node = current_node.next
            current_node.val = last
        if carry != 0:
            current_node.next = ListNode(carry)
        return head.next

    #solution 1
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        count = 0
        while left != right:
            left >>= 1
            right >>= 1
            count+=1
        return (left << count)
    
    #solution 2 (better time complexity)
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while right > left:
            right &= (right - 1)
        return right

    #solution 1 (need to improve time complexity)
    def singleNumber(self, nums: list[int]) -> int:
        sums = [0] * 32
        for n in nums:
            for i in range(32):
                if n & 1 == 1:
                    sums[i] = sums[i] + 1
                n >>= 1
        answer = ""
        for i in range(32):
            sums[i] = sums[i] % 3
            answer = str(sums[i]) + answer
        if sums[31] != 0:
            return int(answer, 2) - pow(2, 32)
        return (int(answer, 2))

    #solution 2 (better time complexity)
    def singleNumber(self, nums: list[int]) -> int:
        ones = 0
        twos = 0
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        return ones