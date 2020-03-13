class Sulotion:
    def reverse_sentence(self, s):
        if not s:
            return ""
        s = s.split(" ")
        # res = []
        # for i in range(len(s)):
        #     res.append(s.pop())
        res = s.reverse()
        return " ".join(res)