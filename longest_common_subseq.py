"""
longest common subsequence
given 2 strings, return their longest common subsequence
subseq is not a substring.
so 'ace' is a subseq of 'abcde'
 input: 2 string
 output: int length
 edge: no subseq, return 0
 assumption: all lowercase
"""
class Solution():
    def longest_common_subseq(self,text1,text2):
        len1,len2 = len(text1), len(text2)
        #len2 is for the no. of col and len1 is for the no. of row
        dp = [[0] * (len2 + 1) for _ in range(len1+1)]
        for i in range(len1):
            for j in range(len2):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return dp[-1][-1]

"""
analysis:
time complexity: n for text 1 and m for text 2, so O(n*m)
space complexity also O((n+1)*(m+1)), since is a (n+1)*(m+1) matrix
"""
