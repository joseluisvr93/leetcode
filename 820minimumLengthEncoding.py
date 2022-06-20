# 820. Short Encoding of Words
# A valid encoding of an array of words is any reference string s and array of indices such that:

# * words.length = indices.length
# * The reference string s ends with the '#' character.
# * For each index indices[i], the substring of s starting form indices:[i] and
#   up to (but not including) the next '#' character is equal to words[i].

# Given an array of words, return the length of the shortest reference string s
# possible of any valid encoding of words
def minimumLengthEncoding(words):
    words_length = {}
    for word in words:
        words_length[word] = len(word)
    print({k: v for k, v in sorted(words_length.items(), reverse=True, key=lambda item: item[1])})

    s = words[0] + "#"
    if len(words) > 1:
        for i in range(1,len(words)):
            if words[i] not in s:
                s += words[i] + "#"

    print(s)
    return len(s)

words = ["t"]
words = ["time", "me", "bell"]
print(minimumLengthEncoding(words))
