# Nakas Konstantinos-Panagiotis 2501

import Othello

print("OTHELLO GAME...")
Othello.create_board()
Othello.print_board()

print("DO YOU WANT TO PLAY WITH COMPUTER OR ANOTHER PLAYER? ")
a = int(input("FOR COMPUTER PRESS: 1   FOR ANOTHER PLAYER PRESS: 2"))
if (a == 1):
	while(True):
		move = Othello.human_play(2)
		if (move == False):
			break
		Othello.print_board()	
		Othello.print_score()
		move = Othello.computer_play()
		if (move == False):
			break
		Othello.print_board()	
		Othello.print_score()
	
else:	
	while(True):
		move = Othello.human_play(1)
		if (move == False):
			break
		Othello.print_board()	
		Othello.print_score()
		move = Othello.human_play(2)
		if (move == False):
			break
		Othello.print_board()	
		Othello.print_score()
		
if(Othello.score1 > Othello.score2):	
	print("The winner is: Player1!!!")	
else:
	print("The winner is: Player2!!!")			
		
		
		