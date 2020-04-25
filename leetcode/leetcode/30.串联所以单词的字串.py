from collections import defaultdict
class Solution:
    def findSubstring(self, s, words):
        '''
        滑动窗口 + 两个哈希表
        '''
        #case
        n = len(words)
        if n == 0: return []
        #赋初值
        res = []
        wordLength = len(words[0])
        #存储words当中的哈希
        wordMap = defaultdict(int)
        #存储滑动窗口当中的sub word的哈希
        subWordMap = defaultdict(int)
        #初始化第一个哈希表
        for word in words:
            wordMap[word] += 1
        #开始滑动窗口
        for i in range(len(s) - n * wordLength + 1):
            #计数第几个word
            count = 0
            while count < n:
                word = s[i+count*wordLength: i+(count+1)*wordLength]
                #判断当前word 是否出现再words中
                if word in words:
                    subWordMap[word] += 1
                    if wordMap[word] < subWordMap[word]:
                        break
                else:
                    break
                count += 1
            #判断count是否匹配
            if count == n: res.append(i)
        return res



