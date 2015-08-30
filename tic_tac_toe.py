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
# and verifies if that space is already occupied
def player_input(player, x_or_o):
	global a1, a2, a3, b1, b2, b3, c1, c2, c3
	verif_loop = True
	while verif_loop == True:
		player = raw_input("\nPlace your %s:\n> " % x_or_o)
		if player == "a1":
			if a1 == "X" or a1 == "O":
				print "\nAlready occupied, choose again.\n"
			else:
				a1 = x_or_o
				print_board()
				verif_loop = False
		elif player == "a2":
			if a2 == "X" or a2 == "O":
				print "\nAlready occupied, choose again.\n"
			else:
				a2 = x_or_o
				print_board()
				verif_loop = False
		elif player == "a3":
			if a3 == "X" or a3 == "O":
				print "\nAlready occupied, choose again.\n"
			else:
				a3 = x_or_o
				print_board()
				verif_loop = False
		elif player == "b1":
			if b1 == "X" or b1 == "O":
				print "\nAlready occupied, choose again.\n"
			else:
				b1 = x_or_o
				print_board()
				verif_loop = False
		elif player == "b2":
			if b2 == "X" or b2 == "O":
				print "\nAlready occupied, choose again.\n"
			else:
				b2 = x_or_o
				print_board()
				verif_loop = False
		elif player == "b3":
			if b3 == "X" or b3 == "O":
				print "\nAlready occupied, choose again.\n"
			else:
				b3 = x_or_o
				print_board()
				verif_loop = False
		elif player == "c1":
			if c1 == "X" or c1 == "O":
				print "\nAlready occupied, choose again.\n"
			else:
				c1 = x_or_o
				print_board()
				verif_loop = False
		elif player == "c2":
			if c2 == "X" or c2 == "O":
				print "\nAlready occupied, choose again.\n"
			else:
				c2 = x_or_o
				print_board()
				verif_loop = False
		elif player == "c3":
			if c3 == "X" or c3 == "O":
				print "\nAlready occupied, choose again.\n"
			else:
				c3 = x_or_o
				print_board()
		else:
			print "\nUnrecognized input."

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
		print "\n%s wins!\n" % x_or_o
		quit()
		
# The program starts here
print_board()
input_loop = True
while input_loop == True:
	player_input(playerX, "X")
	win_check("X")
	player_input(playerO, "O")
	win_check("O")
