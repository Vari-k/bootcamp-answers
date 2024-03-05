#Contains Duplicate

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i]==nums[j]:
                        return True
        return False



#Video Stitching

class Solution(object):
    def videoStitching(self, clips, time):
        """
        :type clips: List[List[int]]
        :type time: int
        :rtype: int
        """
        
        clips.sort()
        n = len(clips)
        count = 0
        i, j = 0, 0
    
        while j < time:
            max_end = j
            while i < n and clips[i][0] <= j:
                max_end = max(max_end, clips[i][1])
                i += 1
        
            if max_end == j:
                return -1
        
            j = max_end
            count += 1
    
        return count



# Container With Most Water

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        left = 0
        right = len(height) - 1
    
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)
        
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
    
        return max_area
