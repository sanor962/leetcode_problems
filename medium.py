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