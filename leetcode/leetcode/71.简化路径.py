class Solution:
    def simplifyPath(self, path):
        # 存储路径
        stack = []
        res = ""
        fields = path.split("/")
        for field in fields:
            # 如果等于..，则弹出路径
            if field == "..":
                if stack: stack.pop()
            # 如果当前路径不为空，且不为.，stack加入路径
            elif field and field != ".":
                stack.append(field)
        if not stack: return "/"
        for p in stack:
            res += "/" + p
        return res
