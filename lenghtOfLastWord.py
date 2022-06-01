def lenghtOfLastWord(s):
    s = s.strip()
    if len(s) == 0:
        return 0
    else:
        return len(s.split()[-1])


s = "Hello World"
print(lenghtOfLastWord(s))
