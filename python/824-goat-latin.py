# easy

'''2020-07-21'''
class Solution:
    def toGoatLatin(self, S: str) -> str:
        words = S.split()
        for i in range(len(words)):
            if words[i][0].lower() in 'aeiou':
                words[i] += 'ma'
            else:
                words[i] = words[i][1:] + words[i][0] + 'ma'
            words[i] += (i+1) * 'a'
        return ' '.join(words)
