class Solution:
    def longestSubarray(self, arr, k):
        n = len(arr)
       
        prefix_map = {}
        curr_sum = 0
        max_len = 0
        
        for i in range(n):
          
            if arr[i] > k:
                curr_sum += 1
            else:
                curr_sum -= 1
            
            if curr_sum > 0:
                max_len = i + 1
            
          
            else:
                if (curr_sum - 1) in prefix_map:
                    max_len = max(max_len, i - prefix_map[curr_sum - 1])
            
            if curr_sum not in prefix_map:
                prefix_map[curr_sum] = i
                
        return max_len


