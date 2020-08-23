# #can use the code below if we have to show the numbers as well.
# class Solution():
#     def pair_sum(self, arr,k):
        
#         if len(arr)<2:
#             return
        
#         # Sets for tracking
#         seen = set()
#         output = set()
        
#         # For every number in array
#         for num in arr:
            
#             # Set target difference
#             target = k-num
            
#             # Add it to set if target hasn't been seen
#             if target not in seen:
#                 seen.add(num)
            
#             else:
#                 # Add a tuple with the corresponding pair
#                 output.add( (min(num,target),  max(num,target)) )
        
        
#         # FOR TESTING
#         return len(output)
#         # Nice one-liner for printing output
#         #return '\n'.join(map(str,list(output)))

# since we only need the number of pairs, we can use the below function
class Solution():
    def pair_sum(self,arr, k):
        
        counter = 0
        lookup = set()
        for num in arr:
            if k - num in lookup:
                counter += 1
            else:
                lookup.add(num)
        return counter