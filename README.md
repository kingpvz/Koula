# HOW TO PLAY?
### Step 1: Download
Basically download the entire repository.
### Step 2: Open `run.py`
Simply double click `run.py` to open it.
### Step 3: Play
Ignore the console window popping up and wait for the tkinter window to open.<br>
Enjoy playing! You can get more insights on how to play in-game by pressing `H` to open help, or by simply reading the key binds at the bottom of the screen.
<br><br>
# HOW TO CREATE CUSTOM LEVELS?
### Step 1: Open `_levels.py` in edit mode
Ignore all the code besides the `DATA` list.
### Step 2: Add a new level to the `DATA` list
Simply add a comma and add a new entry. The entry needs to follow this syntax: `{"m": M, "c": C, "b": B}`<br>
In the entry, replace `M`, `C` and `B` with your level settings.<br>
`M` is the amount of blue balls.<br>
`C` is the amount of black balls.<br>
`B` is the amount of points required to win the level.<br>
Example: `{"m": 10, "c": 3, "b": 8}` creates a level with 10 blue balls and 3 black balls. You need to get 8 points to win this level.<br>
Note: The example is actually level 3 from the game.
### Step 3: Save and Play
Save `_levels.py` and launch the game. In game, press `S` to skip the levels until you reach yours.
<br><br>
# WHAT IS THE PURPOSE OF THIS?
School.
