#can use the code below if we have to show the numbers as well.
# class Solution():
#     def pair_sum(self,arr, k):

#         #edge case check
#         if len(arr) < 2:
#             return

#         #sets for tracking
#         seen = set()
#         output = set()

#         for num in arr:
#             target = k - num
#             if target not in seen:
#                 seen.add(num)
#             else:
#                 output.add( ((min(num, target)), max(num, target)) )

#         print (len(output))

#since we only need the number of pairs, we can use the below function
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