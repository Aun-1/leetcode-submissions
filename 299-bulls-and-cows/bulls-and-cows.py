class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = 0
        cow = 0
        secret_c=[0]*10
        guess_c=[0]*10
        for s,g in zip(secret, guess):
            if s==g:
                bull+=1
            else:
                secret_c[int(s)]+=1
                guess_c[int(g)]+=1
        for i in range(10):
            cow+=min(secret_c[i],guess_c[i])
        return str(bull)+"A"+str(cow)+"B"