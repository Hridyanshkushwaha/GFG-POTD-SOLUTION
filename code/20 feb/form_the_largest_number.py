class Solution:
    def findLargest(self, arr):
       
        arr = [str(x) for x in arr]
        def compare(a, b):
            if a + b > b + a:
                return -1  # 'a' comes first
            else:
                return 1   # 'b' comes first
        
       
        arr.sort(key=cmp_to_key(compare))
        
       
        result = "".join(arr)
        
       
        return "0" if result[0] == "0" else result
