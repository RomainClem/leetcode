class Solution:
    res = 0
    def countSubstrings(self, s: str) -> int:
        
        def find_palindrome(left, right, inputStr):
            while left >= 0 and right < len(inputStr) and  inputStr[left] == inputStr[right]:
                self.res+=1
                # Increasing the size of the palindrome by 1 on each side
                left -=1  
                right +=1
        
        
        
        # Going from left to right in the palindrome
        for i in range(len(s)):
            # Odd Palindrome
            # Same concept but starting from the same char index 
            # As an odd palindrome will have a single char in the middle
            find_palindrome(i, i, s)
            # Even Palindrome
            # Checking if the pointers are at valid position (still inside the string)
            # And checking that the left and right char are the same chars
            find_palindrome(i, i+1, s)
            
            
            
        return self.res
        
        