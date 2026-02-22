class Solution:
    def subarrayXor(self, arr, k):
        current_xor = 0
        count = 0
        freq = {0: 1}
        for num in arr:
            current_xor ^= num
            target = current_xor ^ k
            if target in freq:
                count += freq[target]
            freq[current_xor] = freq.get(current_xor, 0) + 1
        
        return count
