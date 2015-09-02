# This sets the original values of the variables
a1, a2, a3 = ["_"], ["_"], ["_"]
b1, b2, b3 = ["_"], ["_"], ["_"]
c1, c2, c3 = [" "], [" "], [" "]
playerX = "X"
playerO = "O"
x_or_o = "Choose X or O"

# This function prints the board
def print_board():
	print "\n   1   2   3 "
	print "a _%s_|_%s_|_%s_" % (a1[0], a2[0], a3[0])
	print "b _%s_|_%s_|_%s_" % (b1[0], b2[0], b3[0])
	print "c  %s | %s | %s " % (c1[0], c2[0], c3[0])

# This lets the users choose where to place their mark
# and verifies if that space is already occupied
	
def player_input(x_or_o):	
	while True:
		player = raw_input("\nPlace your %s:\n> " % x_or_o)
		if player == "a1":
			if a1 == ["X"] or a1 == ["O"]:
				print "\nAlready occupied, choose again.\n"
			else:
				a1.pop()
				a1.append(x_or_o)
				return a1
		elif player == "a2":
			if a2 == ["X"] or a2 == ["O"]:
				print "\nAlready occupied, choose again.\n"
			else:
				a2.pop()
				a2.append(x_or_o)
				return a2
		elif player == "a3":
			if a3 == ["X"] or a3 == ["O"]:
				print "\nAlready occupied, choose again.\n"
			else:
				a3.pop()
				a3.append(x_or_o)
				return a3
		elif player == "b1":
			if b1 == ["X"] or b1 == ["O"]:
				print "\nAlready occupied, choose again.\n"
			else:
				b1.pop()
				b1.append(x_or_o)
				return b1
		elif player == "b2":
			if b2 == ["X"] or b2 == ["O"]:
				print "\nAlready occupied, choose again.\n"
			else:
				b2.pop()
				b2.append(x_or_o)
				return b2
		elif player == "b3":
			if b3 == ["X"] or b3 == ["O"]:
				print "\nAlready occupied, choose again.\n"
			else:
				b3.pop()
				b3.append(x_or_o)
				return b3
		elif player == "c1":
			if c1 == ["X"] or c1 == ["O"]:
				print "\nAlready occupied, choose again.\n"
			else:
				c1.pop()
				c1.append(x_or_o)
				return c1
		elif player == "c2":
			if c2 == ["X"] or c2 == ["O"]:
				print "\nAlready occupied, choose again.\n"
			else:
				c2.pop()
				c2.append(x_or_o)
				return c2
		elif player == "c3":
			if c3 == ["X"] or c3 == ["O"]:
				print "\nAlready occupied, choose again.\n"
			else:
				c3.pop()
				c3.append(x_or_o)
				return c3
		else:
			print "\nUnrecognized input."

# This checks if the winning conditions have been met
def win_check(x_or_o):
	if (a1 == [x_or_o] and a2 == [x_or_o] and a3 == [x_or_o]) or \
(b1 == [x_or_o] and b2 == [x_or_o] and b3 == [x_or_o]) or \
(c1 == [x_or_o] and c2 == [x_or_o] and c3 == [x_or_o]) or \
(a1 == [x_or_o] and b1 == [x_or_o] and c1 == [x_or_o]) or \
(a2 == [x_or_o] and b2 == [x_or_o] and c2 == [x_or_o]) or \
(a3 == [x_or_o] and b3 == [x_or_o] and c3 == [x_or_o]) or \
(a1 == [x_or_o] and b2 == [x_or_o] and c3 == [x_or_o]) or \
(a3 == [x_or_o] and b2 == [x_or_o] and c1 == [x_or_o]):
		print "\n%s wins!\n" % x_or_o
		quit()
		
# The program starts here
print_board()
while True:
	player_input("X")
	print_board()
	win_check("X")
	player_input("O")
	print_board()
	win_check("O")
