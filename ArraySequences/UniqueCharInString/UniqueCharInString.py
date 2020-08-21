#can use the set keyword for this
# class Solution:
#     def uniq_char(self, s):
#         return len(set(s)) == len(s)
    
#more manual approach of the above program
class Solution:
    def uniq_char(self, s):
        char = set()

        for string in s:
            if string in char:
                return False
            else:
                char.add(string)
        return True