# 125. Valid Palindrome
# A phrase is palindrome if, after converting all uppercase letters into lowercase letters
# and removing all non-alphanumeric characters, it reads the same forwards and backward.
# Alphanumeric characters include letters and numbers

# Given a string s, return true if it is a palindrome. Otherwise, return false.
def isPalindrome(s):
    s = s.lower()
    i = 0
    j = len(s) - 1
    while i < j:
        if not s[i].isalnum():
            i += 1
        elif not s[j].isalnum():
            j -= 1
        elif s[i] != s[j]:
            return False
        else:
            i += 1
            j -= 1
    return True

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
