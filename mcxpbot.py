#! /usr/bin/python3

#	Minecraft Cave-Spider XP Bot
#	Coded by Nullbyte (Warren Hood)
#	Created:	11:15PM Fri, 21 December 2018
#	Updated:	12:39PM Sat, 22 December 2018

import pyautogui as pg
import time


#	All intervals/durations below are in seconds

#	INTERVALS AND DURATIONS

WALK_DURATION = 2 #Time to move horizontally across
CLICK_INTERVAL = 0.8 #TIme between clicks (well... hits)
XP_INTERVAL = 60 #Time between XP collection
EAT_INTERVAL = 480 #Time between eating

#	CUSTOM CONTROLS

WEAPON_SLOT_NUM = "1"
FOOD_SLOT_NUM = "3"
HIT_KEY = "k"
USE_KEY = "i"
JUMP_KEY = "space"

#	eat will be called every EAT_DURATION seconds
def eat():
	pg.press(FOOD_SLOT_NUM)
	time.sleep(0.1)
	pg.keyDown(USE_KEY)
	time.sleep(10)
	pg.keyUp(USE_KEY)
	pg.press(WEAPON_SLOT_NUM)
	time.sleep(0.1)

#	collectXP will be called every XP_INTERVAL seconds
def collectXP():
	# Move left
	try:
		pg.keyUp("d")
		pg.keyDown("a")
	except:
		pass

	# Move left for 2 seconds
	for i in range(4):
		pg.press(HIT_KEY)
		time.sleep(0.5)

	# Move to the centre... Takes 0.8 sec approx
	pg.keyUp("a")
	pg.keyDown("d")
	pg.press(HIT_KEY)
	time.sleep(CLICK_INTERVAL)
	pg.press("HIT_KEY")
	time.sleep(max(0,0.8-CLICK_INTERVAL))

	# Stop moving right now... We are in middle(hopefully)
	pg.keyUp("d")

	# Initial direction is left
	cdir = 0

	# Clear spiders out from middle before collecting xp
	for i in range(20):
		
		# If dir is 0 then go left
		if not cdir:
			pg.keyUp("d")
			pg.keyDown("a")	
		
		# Otherwise go right 
		else:
			pg.keyUp("a")
			pg.keyDown("d")
		pg.press(HIT_KEY)
		time.sleep(0.1)
		cdir = not cdir
	# Stop all movement
	pg.keyUp("d")
	pg.keyUp("a")

	# Start moving forwards
	pg.keyDown("w")

	# After .3 seconds jump
	time.sleep(0.3)
	pg.keyDown(JUMP_KEY)
	time.sleep(0.1)
	pg.keyUp(JUMP_KEY)

	# Keep moving forward for .5 seconds
	time.sleep(0.5)

	# Move away!
	pg.keyUp("w")
	pg.keyDown("s")

	# Move back for .5 seconds
	time.sleep(0.5)
	pg.keyUp("s")

	# Move forward fully(1 second should do it)
	pg.keyDown("w")
	time.sleep(1)
	pg.keyUp("w")

	# XP should be collected now

print('''
		11       11 11111111	XXXXXX    XXX   XXXXXXX
		 11     11  11    11	X     X  X   X     X
		  11   11   11    11	X     X X     X    X
		   11 11    11    11	X     X X     X    X
		    11      11111111	XXXXXXX X     X    X
		   11 11    11          X     X X     X    X
		  11   11   11          X     X X     X    X
		 11     11  11          X     X  X   X     X
		11       11 11          XXXXXX    XXX      X

		            PRESS ENTER TO BEGIN


	''')
input()

print("Please give Minecraft focus")
print("Starting Warren's Afk Spider XP Farm Bot in 5 Seconds...")
time.sleep(5)
print("Bot is running (Ctrl-C to quit)")

# Set current walk direction to left (0)
cdir = 0
# Start walking left
pg.keyDown("a")


# Get current time
lasttime = time.time()

# Set up timers (Descriptions on right)
ctime = 0				# Current time elpased (used to determine direction)
clicktimer = 0			# A timer to determine when to hit
xptimer = 0				# A timer to determine when to collect xp
eattimer = 0			# A timer to determine when to eat

# Begin the xp bot loop
try:
	while 1:
		# Get the current time
		thistime = time.time()

		# Add timedelta to all timers
		ctime += thistime-lasttime
		clicktimer += thistime-lasttime
		xptimer += thistime-lasttime
		eattimer += thistime-lasttime

		# Record current time
		lasttime = thistime

		# Check if time to eat
		if eattimer >= EAT_INTERVAL:
			eattimer = 0
			eat()

		# Check if time to collect xp
		if xptimer >= XP_INTERVAL:
			xptimer = 0
			collectXP()

		# Check if time to click (hit)
		if clicktimer >= CLICK_INTERVAL:
			clicktimer = 0
			pg.press(HIT_KEY)

		# Check if time to change walk direction
		if ctime >= WALK_DURATION:
			ctime = 0

			# Alternate direction
			cdir = not cdir

			# If dir is 0 then go left
			if not cdir:
				pg.keyUp("d")
				pg.keyDown("a")

			# Otherwise go right 
			else:
				pg.keyUp("a")
				pg.keyDown("d")

except KeyboardInterrupt:
	print("Bot terminated by user")

