class Solution:
    def minSubsequence(self, list):
        list.sort(reverse=True)
        res = []
        tmp, Sum = 0, sum(list)
        for i in list:
            tmp += i
            res.append(i)
            if tmp > Sum - tmp:
                return res
