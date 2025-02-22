# Check if a string is substring of another
# Given two strings txt and pat,
# the task is to find if pat is a substring of txt. If yes, return the index of the first occurrence, else return -1.

def isSubstring(txt, pat):
    pat_ind = 0
    txt_ind = 0
    while(txt_ind < len(txt)):
        while(txt_ind < len(txt) and pat_ind < len(pat) and txt[txt_ind] == pat[pat_ind]):
            pat_ind+=1
            txt_ind+=1
            if pat_ind == len(pat):
                return True, txt_ind-pat_ind
        pat_ind = 0
        if txt[txt_ind] != pat[pat_ind]:
            txt_ind+=1
    return False, -1

# Follow-up: if a circle is allowed
# TODO: implement it. idea: concetanate the txt with itself till it is bigger than substring, and check
def isSubstringCircular(txt, pat):
    pass


if __name__ == "__main__":
    print(isSubstring("Hello", "lo"))
    print(isSubstring("Hello", "la"))
    