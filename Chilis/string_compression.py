"""
    Takes one parameter string and compresses the contents such that any
    duplicate sequential characters are removed and the count replaced
    in the output string. E.g. AABBBCCCC would become A2B3C4
"""


def string_compression(text):
    if type(text) is not str:
        raise ValueError("The input parameter can only be a string")
    retbuff = ""
    if text > "":
        cnt = 1
        for c in range(len(text)-1):
            if text[c] == text[c+1]:
                cnt += 1
            else:
                retbuff += text[c]+str(cnt) if cnt > 1 else text[c]
                cnt = 1
        retbuff += text[c]+str(cnt) if cnt > 1 else text[c+1]
    return retbuff


print(string_compression("abddccbaacccccfddbbbacddd"))
