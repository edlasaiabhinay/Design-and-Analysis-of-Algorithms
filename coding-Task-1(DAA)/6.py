def computeLPS(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1] #fall back
            else:
                lps[i] = 0
                i += 1
    return lps

#kmp search 
def KMP_search(text, pattern):
    lps = computeLPS(pattern)
    i = j = 0
    positions = []

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == len(pattern): 
            positions.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return positions

text = "CATSABCBCAABCDOGSABCBCAABC"
pattern = "ABCBCA"
print("Pattern found at indices:", KMP_search(text, pattern))
