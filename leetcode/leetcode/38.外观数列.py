class Solution:
    def countndSay(self, n):
        prePerson = '1'
        for i in range(1, n):
            nextPerson, num, count = '', prePerson[0], 1
            for j in range(1, len(prePerson)):
                if prePerson[j] == num:
                    count += 1
                else:
                    nextPerson += str(count) + num
                    num = prePerson[j]
                    count += 1
            nextPerson += str(count) + num
            prePerson = nextPerson
        return prePerson