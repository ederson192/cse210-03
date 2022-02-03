from Word import words
class Guesser: 
    
    def __init__(self):
        self.word = words
        

    def guess (self, word, guess): 
        word_in_progress = ""
        for letter in word:
            if letter in guess:
                word_in_progress += letter
                 #replace the i element in the line
            else:
                word_in_progress = '*'
                
        return word_in_progress 







