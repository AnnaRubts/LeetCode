# Given two strings text1 and text2,
# return the length of their longest common subsequence. If there is no common subsequence, return 0.

def longestCommonSubsequence(text1, text2):
    memo = [[0]*len(text2) for _ in text1]
    # for c in range(len(text2)):
    #     memo[0][c] = int(text1[0] == text2[c])
    
    # for r in range(len(text1)):
    #     memo[r][0] = int(text1[r] == text2[0])

    memo[0][0] = int(text1[0] == text2[0])

    for r in range(0, len(text1)):
        for c in range(0, len(text2)):
            if r==0 and c==0:
                continue
            if r==0:
                memo[r][c] = max(memo[r][c-1], int(text1[r] == text2[c]))
            if c==0:
                memo[r][c] = max(memo[r-1][c], int(text1[r] == text2[c]))
            if text1[r] == text2[c]:
                memo[r][c] = memo[r-1][c-1]+1
            else:
                memo[r][c] = max(memo[r-1][c], memo[r][c-1])
    
    return memo[len(text1)-1][len(text2)-1]
            

if __name__ == "__main__":
    print(longestCommonSubsequence("ace", "abcde"))
    print(longestCommonSubsequence("abc", "abc"))
    print(longestCommonSubsequence("abc", "def"))
    print(longestCommonSubsequence("abcd", "def"))