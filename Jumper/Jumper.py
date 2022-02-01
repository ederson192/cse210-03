class Jumper:
    """Updates the status of Jumper, showing the guesser how many guess they have left. 
    
    The responsibility of a Jumper is to keep track of many many guesses are left.
    
    Attributes:
        jumper (List['']): Image of jumper
        trys (int): Number of guesses the user has
    """
    

    def __init__(self):
        """Constructs a new Jumper.

        Args:
            self (Jumper): An instance of Jumper.
        """
        self._jumper = ['  ___ \n',
        ' /___\ \n',
        ' \   / \n',
        '  \ / \n',
        '   O  \n',
        '  /|\ \n',
        '  / \ \n',
        '      \n',
        '^^^^^^^\n']
        self.trys = 5

        
    def update_jumper(self):
        """Updates the Jumpers image
        
        Returns:
           self._jumper
        """
        if self._guesser is False: 
            self._jumper.pop(0)
            self.trys -= 1
        if self.trys == 0:
            self._jumper.insert(0,'x')
        
        return self._jumper