def strStr(haystack, needle):
    if len(needle) > len(haystack):
        return -1
    i = 0
    while i < len(haystack) - len(needle) + 1:
        if haystack[i] == needle[0]:
            j = 1
            flag = 0
            while j < len(needle):
                if haystack[i+j] != needle[j]:
                    flag = 1
                    break
                j += 1
            if flag == 0:
                return i
                
        i += 1
    return -1
    
haystack = "aaaaa"
needle = "bba"
print(strStr(haystack,needle))
