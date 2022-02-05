from game.Word import Words
import random
class Guesser: 
    
    def __init__(self):
        #self.word = Words
        self.list = ['stock', 'over', 'flow']
        self.word = random.choice(self.list)
        self._word_in_progress = "_"

    def guess (self): 
        guess = input('Guess a letter [a-z]: ')
        
        for letter in self.word:
                if letter == guess:
                    self._word_in_progress += letter
                    #replace the i element in the line
                else:
                    self._word_in_progress += '_'
                
        return self._word_in_progress 







