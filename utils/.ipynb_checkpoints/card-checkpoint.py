"""Create a class called `Symbol` with two attributes:
- `color` which is a string.
- `icon` which is a string: `[♥, ♦, ♣, ♠]`
"""
#Parent class
class Symbol():
    def __init__(self, icon: str, color: str=""):
        
        self.icon = icon              #'[♥, ♦, ♣, ♠]' 
        if icon == '♥' or '♦':
            color = 'red'
        else: 
            color = 'black'
        self.color = color            #'[black, red]'
        
"""create a class `Card` that **inherits** from `Symbol` and add an attribute:
- `value` which is a string. *(it can be 'A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K')*
"""

# Child class
class Card(Symbol):
    def __init__(self, value: str, icon, color = ""):
        Symbol.__init__(icon, color)
        self.value = value            #'[A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K]'
        return f"{self.value}"
        