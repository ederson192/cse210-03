import random
class Guesser: 
    
    def __init__(self):
        
        self.list = ['stock', 'over', 'flow', 'random', 'hello', 'computer', 'happy', 'python', 'health', 'funny']
        self.word = random.choice(self.list)
        self._word_in_progress = []
        self.j = 0
        self.size = len(self.word)

        for self.j in self.word:
            self._word_in_progress += '_'

    def guess (self): 
        self.guesser = False

        guess = input('Guess a letter [a-z]: ')

        for idx, character in enumerate(self.word):
            if character == guess:
                self._word_in_progress[idx] = guess
                self.guesser = True
                break

        return self._word_in_progress 

    def is_found (self):
        return (self._word_in_progress == self.word)








