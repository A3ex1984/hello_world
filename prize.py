points = 12

def which_prize(points):
	wooden_rabbit = 50
	no_prize = 150
	wafer_thin = 180
	penguin = 200
	if points <= wooden_rabbit:
		prize = "wooden rabit"
	elif points <= no_prize:
		prize = "No prize"
	elif points <= wafer_thin:
		prize = "wafer-thin mint"
	elif points <= penguin:
		prize = "penguin"
	else:
		prize = "No prize"
	if 51 <= points <= 150:
		return "Oh dear, no prize this time."
	else:
		return "Congratulations! You have won a " + prize + "!"
	
print (which_prize(points))