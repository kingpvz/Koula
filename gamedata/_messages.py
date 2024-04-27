from random import randint as rnd

_MESSAGES = """
Much worse than other games!
Try not to die of boredom!
Seriously this game is bad.
Made by that one guy!
Made with SimpleQuery!
You can make your own levels!
Made using python! (Snake, not language)
No balls were harmed while making this game.
Your ball was originally red.

Has up to 5 levels!
Contains whopping 2 game mechanics!
"""

def randomMessage():
    x = _MESSAGES.split("\n")
    x = [i for i in x if i != ""]
    y = rnd(0,len(x)-1)
    return x[y]