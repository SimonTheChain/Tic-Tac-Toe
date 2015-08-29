# This sets the original values of the variables
a1, a2, a3 = "_", "_", "_"
b1, b2, b3 = "_", "_", "_"
c1, c2, c3 = " ", " ", " "
playerX = "X"
playerO = "O"
x_or_o = "Choose X or O"

# This function prints the board
def print_board():
	print "\n   1   2   3 "
	print "a _%s_|_%s_|_%s_" % (a1, a2, a3)
	print "b _%s_|_%s_|_%s_" % (b1, b2, b3)
	print "c  %s | %s | %s " % (c1, c2, c3)

# This lets the users choose where to place their mark
def player_input(player, x_or_o):
	player_loop = True
	while player_loop == True:
		player = raw_input("\nPlace your %s:\n> " % x_or_o)
		if player == "a1":
			global a1
			a1 = x_or_o
			print_board()
		elif player == "a2":
			global a2
			a2 = x_or_o
			print_board()
		elif player == "a3":
			global a3
			a3 = x_or_o
			print_board()
		elif player == "b1":
			global b1
			b1 = x_or_o
			print_board()
		elif player == "b2":
			global b2
			b2 = x_or_o
			print_board()
		elif player == "b3":
			global b3
			b3 = x_or_o
			print_board()
		elif player == "c1":
			global c1
			c1 = x_or_o
			print_board()
		elif player == "c2":
			global c2
			c2 = x_or_o
			print_board()
		elif player == "c3":
			global c3
			c3 = x_or_o
			print_board()
		else:
			print "\nUnrecognized input."
			quit()
		win_check("X")

# This checks if the winning conditions have been met
def win_check(x_or_o):
	if (a1 == x_or_o and a2 == x_or_o and a3 == x_or_o) or \
(b1 == x_or_o and b2 == x_or_o and b3 == x_or_o) or \
(c1 == x_or_o and c2 == x_or_o and c3 == x_or_o) or \
(a1 == x_or_o and b1 == x_or_o and c1 == x_or_o) or \
(a2 == x_or_o and b2 == x_or_o and c2 == x_or_o) or \
(a3 == x_or_o and b3 == x_or_o and c3 == x_or_o) or \
(a1 == x_or_o and b2 == x_or_o and c3 == x_or_o) or \
(a3 == x_or_o and b2 == x_or_o and c1 == x_or_o):
		global player_loop
		player_loop = False
		print "%s wins!" % x_or_o
	
# The program starts here
print_board()
player_input(playerX, "X")
