# @author
# Ashutosh.Verma

# Problem: https://leetcode.com/problems/longest-common-subsequence/

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        X = text1
        Y = text2
        m = len(X)
        n = len(Y)
        arr = []
        
        for i in range(m+1):
            arr.append([0]*(n+1))
        
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    arr[i][j] = 0
                elif X[i-1] == Y[j-1]:
                    arr[i][j] = 1 + arr[i-1][j-1]
                else:
                    arr[i][j] = max(arr[i-1][j], arr[i][j-1])
        
        return arr[m][n]
    
