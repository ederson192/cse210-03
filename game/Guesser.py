from game.Word import Words
import random
class Guesser: 
    
    def __init__(self):
        
        self.list = ['stock', 'over', 'flow']
        self.word = random.choice(self.list)
        self._word_in_progress = []
        self.j = 0
        self.size = len(self.word)
        #self.guesser = False
        for self.j in self.word:
            self._word_in_progress += '_'

    def guess (self): 
        failed = 0
        self.guesser = False
        j = 0

        guess = input('Guess a letter [a-z]: ')

        for idx, character in enumerate(self.word):
            if character == guess:
                self._word_in_progress[idx] = guess
                self.guesser = True
                break

        return self._word_in_progress 

    def is_found (self):
        return (self._word_in_progress == self.word)








