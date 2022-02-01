class Guesser: 
    
    def __init__(self) -> None:
        pass

    def guess (self,word, guess): 
        word = "hola"
        word_in_progress = ""
        for letter in word:
                if letter in guess:
                 word_in_progress += letter
                 #replace the i element in the line


