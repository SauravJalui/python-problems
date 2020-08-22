class Solution:
    def cycle_check(self, node):

        # Begin both markers at the first node
        marker1 = node
        marker2 = node

        # Go until end of list
        while marker2 != None and marker2.next != None:
            
            # Note
            marker1 = marker1.next
            marker2 = marker2.next.next

            # Check if the markers have matched
            if marker2 == marker1:
                return True

        # Case where marker ahead reaches the end of the list
        return False

# class Solution:
#     def cycle_check(self,node):
# #     Use fast and slow pointer
#         fast, slow = node, node
#         while fast and fast.next:
#             fast = fast.next
#             if fast == slow:
#                 return True
#             fast = fast.next
#             slow = slow.next
#         return False
       