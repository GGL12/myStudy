class Solution:
    def findContentChildren(self, children, cookies):
        #贪心算法
        children.sort()
        cookies.sort()

        idxChild = idxCookie = 0
        while idxChild < len(children) and idxCookie < len(cookies):
            if children[idxChild] <= cookies[idxCookie]:
                idxCookie += 1
            idxChild += 1

        return idxChild
