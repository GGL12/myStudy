class Sulotion:
    # def left_rotate_string(self, s, n):
    #     if len(s) < n or not s:
    #         return []
    #     s_list = list(s)
    #     for i in range(n):
    #         s_list.append(s_list.pop(0))
    #     return "".join(s_list)

    #YX = (XTYT)T
    def reverse(self,str, s, e):
        e -= 1
        while s < e:
            str[s], str[e] = str[e], str[s]
            s += 1
            e -= 1
    def left_rotate_string(self, s, n):
        if len(s) == 0 or n == 0:
            return s
        s = list(s)
        self.reverse(s, 0, n)
        self.reverse(s, n, len(s))
        self.reverse(s, 0, len(s))
        return "".join(s)
