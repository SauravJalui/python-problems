class Solution:
    def anagram(self, s1,s2):
        s1 = s1.replace(' ', '').lower()
        s2 = s2.replace(' ', '').lower()
        
        #edge cases check
        if len(s1) != len(s2):
            return False
        
        count = {}
        
        for letter in s1:
            if letter in count:
                count[letter] += 1
            else:
                count[letter] = 1
        
        for letter in s2:
            if letter in count:
                count[letter] -= 1
            else:
                count[letter] = 1
                
        for letter in count:
            if count[letter] != 0:
                return False
        return True
