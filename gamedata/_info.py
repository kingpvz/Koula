VERSION = "beta2.2"

HELP = """Welcome to KOULA!
(the best game ever for real)

This is a quick tutorial to help you get started.
Every level consists of many small balls on the screen. And the goal is simple: Get the amount of points you need to win the level.
Every ball has a different purpose and acts differently too.

Here is an overview:
YELLOW - Your player ball. You can move it around. Always spawns in the middle of the playarea.
BLUE (white outline) - Goal ball. Collect it to get 1 point.
BLACK (red outline) - Doom ball. Collect it to lose 1 point.

Levels will always give you at least the amount of points you need. Basically try not to lose any. Simple as that!
"""

CHANGELOG = """\
BETA 2.2
Moved some things around
Made series into functions

BETA 2.1
Added messages with progression to levelback
- This basically means that when you wil attempt to go back to a level that doesn't exist (level 0, level -1, etc.) you'll get a series of messages to stop you.
- It doesn't do much but I don't care
- Yes I do that instead of coding in new features
- No I do not care, I am not procrastinating either
- Ok maybe I am procrastinating but I don't care
New game load messages

BETA 2.0
Cleaned up folders and files
Fixed previous level getting you into negative levels
Added message bar
Remade error catching in custom level data
Added alternative syntax for at/put command
- Now you can write a put/at command too!
Added a random message to welcome you
- Every time you begin the game there is a random message to greet you!
"""