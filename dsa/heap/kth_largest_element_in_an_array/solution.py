class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        return self._quickselect(nums, 0, len(nums) - 1, len(nums) - k)

    def _quickselect(self, nums: list[int], lo: int, hi: int, k: int) -> int:
        if lo == hi:
            return nums[lo]
        pivot = nums[hi]
        i = lo
        for j in range(lo, hi):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[hi] = nums[hi], nums[i]
        if i == k:
            return nums[i]
        if i < k:
            return self._quickselect(nums, i + 1, hi, k)
        return self._quickselect(nums, lo, i - 1, k)

