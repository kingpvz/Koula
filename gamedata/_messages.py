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
Do not press A on the first level!
For all the ball lovers!
You'll love these colorful balls!
Deaf people friendly!
Boredom for entire family!
Your friends will love these balls!

Has up to 5 levels!
Contains whopping 2 game mechanics!
"""

def randomMessage():
    x = _MESSAGES.split("\n")
    x = [i for i in x if i != ""]
    y = rnd(0,len(x)-1)
    return x[y]

def getLevelBack(id):
    if id == 1: return "There are no more levels back there."
    elif id == 2: return "Seriously what are you trying?"
    elif id == 3: return "If you continue like this you'll break something."
    elif id == 4: return "This game is too easy to break."
    elif id == 5: return "So you'd like to talk about something?"
    elif id == 6: return "No?"
    elif id == 7: return "That's fine, me neither."
    elif id == 8: return "..."
    elif id == 9: return "So how's life?"
    elif id == 10: return "I doubt you have one anyway."
    elif id == 11: return "Someone with a life wouldn't do this."
    elif id == 12: return "Wasting time on a dialogue with a game."
    elif id == 13: return "This is not even a dialogue at this point."
    elif id == 14: return "Since I'm monologuing you see."
    elif id == 15: return "Umm... You want anything?"
    elif id == 16: return "Oh right more levels."
    elif id == 17: return "There are no more levels."
    elif id == 18: return "I'm not making more levels."
    elif id == 19: return "I'm writing these messages instead."
    elif id == 20: return "If you want more levels this bad go make some."
    elif id == 21: return "Yeah, did you know you could do that?"
    elif id == 22: return "Go on, go make some levels."
    elif id == 23: return "I wish I could use match/case here."
    elif id == 24: return "Whatever old python sucks."
    elif id == 25: return "I'm getting tired."
    elif id == 26: return "You know what, fine, here is something."
    elif id == 27: return "I'll give you a special counter."
    elif id == 28: return "It will count how many times you've tried it."
    elif id == 29: return "How many times you've tried getting into a level."
    elif id == 30: return "A level that doesn't even exist."
    else: return "Fine here it is: "+str(id)