"""
petGreeting.py
====================================
This program says hello to pets by inputting their name.

| Author: Eein McKinley
| Date: 2026 April 09
"""

class SayHello:
    """
    This is the way to say hello to the pet.
    
    Parameters
    ----------
    name : str
        The pet's name
    
    Attributes
    ----------
    name : str
        The owner's name
        
    Examples
    --------
    >>> hello = SayHello("Bob")
    >>> hello.greet(', welcome!')
    Hello Bob, welcome!
    """
    
    def __init__(self, name):
        """
        Initialize a new SayHello instance.
        
        Parameters
        ----------
        name : str
            The pet's name
        """
        self.name = name
   
    def greet(self, extraText):
        """
        Greets self.name and adds extraText to the output.
        
        Parameters
        ----------
        extraText : str
            Text to add after the hello username
            
        Returns
        -------
        str 
            The string that says hello to the pet.
        """

        return f'Hello {self.name}{extraText}'


if __name__ == '__main__':
    """Runs if file called as script as opposed to being imported as a library
    """
    bob = SayHello('Fido')
    bobLen = bob.greet(', welcome!')
    print(bobLen)
