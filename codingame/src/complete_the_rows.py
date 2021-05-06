'''
STORY:
The satellite that used to remotely control the rover you're in was destroyed by a passing comet.

You manage to turn on a monitor with an aerial view of the place you're in (An ASCII map with: '.'s representing the lunar plains, '>' your position and 'X' the base's position), and after racking your head for a few minutes you can only remember two basic commands:

COMMANDS:
'F' to Move forward one unit
'R' to Rotate 90 degrees clockwise (to the right)

Using only these two commands can you find a way to get back to the lunar base 'X' from your Rover '>'?

IMPORTANT:
The Rover always starts looking EAST (To the right)
Astronaut protocol dictates that you FIRST move on the HORIZONTAL axis and THEN move on the VERTICAL axis

EXAMPLE:
Input:
"4 1"
"X..>"
Solution:
"R R F F F"
Rotate 180 degrees (= Rotating 90 degrees to the right twice) in order for the rover to be facing west.
Move Forward 3 times to reach the base.

'''