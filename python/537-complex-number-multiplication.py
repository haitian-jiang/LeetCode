# medium

'''2020-11-07'''
class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        ar, ai = map(int, a[:-1].split("+"))
        br, bi = map(int, b[:-1].split("+"))
        real = ar * br - ai * bi
        imag = ai * br + ar * bi
        return str(real)+"+"+str(imag)+"i"