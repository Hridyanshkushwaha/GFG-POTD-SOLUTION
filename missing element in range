class Solution:
    def missingRange(self, arr, low, high):
        # Convert list to a set for O(1) lookups
        present_elements = set(arr)
        missing_elements = []
        
        # Iterate through the required range
        for i in range(low, high + 1):
            if i not in present_elements:
                missing_elements.append(i)
        
        return missing_elements
