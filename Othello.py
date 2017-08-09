# Nakas Konstantinos-Panagiotis 2501

DIM = 8
A = [[0 for x in range(DIM)] for y in range(DIM)]
reverse_lst = list()
score1 = 0
score2 = 0

def create_board():
	A[3][3] = 1
	A[4][4] = 1
	A[3][4] = 2
	A[4][3] = 2
	
	
def print_board():
	global A
	l=0
	print("     0", "", "1", "", "2" , "" ,"3", "", "4", "", "5" , "", "6" ,"", "7")
	print("----------------------------------------------------------------")
	for i in range(DIM):
		print(l, "|", end='')
		for j in range(DIM):
			print (" ", A[i][j],  end='')
		l = l + 1
		print()	
	print("----------------------------------------------------------------")
	
def reverse_count_up(x,y,player):
	global reverse_lst
	global A
	tmp_reverse_lst = list()
	if (A[x][y] != 0): return
	if (y!=0):
		for j in range(y-1,0,-1):
			if (player != A[x][j] and A[x][j] != 0):
				tmp_reverse_lst.append([x , j])
			elif(A[x][j] != 0):
				if (tmp_reverse_lst != []):
					reverse_lst.append(tmp_reverse_lst)
					break
			else:
				break
	
def reverse_count_down(x,y,player):
	global A
	global reverse_lst
	tmp_reverse_lst = list()
	if (A[x][y] != 0): return
	if (y!=DIM):
		for j in range(y+1,DIM):
			if (j > 7):
				break
			if (player != A[x][j] and A[x][j] != 0):
				tmp_reverse_lst.append([x , j])
			elif(A[x][j] != 0):
				if (tmp_reverse_lst != []):
					reverse_lst.append(tmp_reverse_lst)
					break
			else:
				break
				
def reverse_count_left(x,y,player):
	global A
	global reverse_lst
	tmp_reverse_lst = list()
	if (A[x][y] != 0): return
	if (x!=0):
		for i in range(x-1,0,-1):
			if (player != A[i][y] and A[i][y] != 0):
				tmp_reverse_lst.append([i , y])
			elif(A[i][y] != 0):
				if (tmp_reverse_lst != []):
					reverse_lst.append(tmp_reverse_lst)
					break
			else:
				break
				
def reverse_count_right(x,y,player):
	global A
	global reverse_lst
	tmp_reverse_lst = list()
	if (A[x][y] != 0): return
	if (x!=DIM):
		for i in range(x+1,DIM):
			if (i > 7):
				break
			if (player != A[i][y] and A[i][y] != 0):
				tmp_reverse_lst.append([i,y])
			elif(A[i][y] != 0):
				if (tmp_reverse_lst != []):
					reverse_lst.append(tmp_reverse_lst)
					break
			else:
				break
				
def reverse_count_up_left(x,y,player):	
	global A
	global reverse_lst
	tmp_reverse_lst = list()
	if (A[x][y] != 0): return
	i = x
	if (y!=0):
		if (x!=0):
			for j in range(y-1,0,-1):
				i = i - 1
				if (player != A[i][j] and A[i][j] != 0):
					tmp_reverse_lst.append([i ,  j])
				elif(A[i][j] != 0):
					if (tmp_reverse_lst != []):
						reverse_lst.append(tmp_reverse_lst)
						break
				else:
					break
					
def reverse_count_down_left(x,y,player):	
	global A
	global reverse_lst
	tmp_reverse_lst = list()
	if (A[x][y] != 0): return
	i = x
	if (y!=DIM):
		if (x!=0):
			for j in range(y+1,DIM):
				i = i - 1
				if (j > 7 or i > 7):
					break
				if (player != A[i][j] and A[i][j] != 0):
					tmp_reverse_lst.append([i , j])
				elif(A[i][j] != 0):
					if (tmp_reverse_lst != []):
						reverse_lst.append(tmp_reverse_lst)
						break
				else:
					break	

def reverse_count_up_right(x,y,player):
	global A
	global reverse_lst
	tmp_reverse_lst = list()
	if (A[x][y] != 0): return
	i = x
	if (y!=0):
		if (x!=DIM):
			for j in range(y-1,0,-1):
				i = i + 1
				if (j > 7 or i > 7):
					break
				if (player != A[i][j] and A[i][j] != 0):
					tmp_reverse_lst.append([i , j])
				elif(A[i][j] != 0):
					if (tmp_reverse_lst != []):
						reverse_lst.append(tmp_reverse_lst)
						break
				else:
					break
					
def reverse_count_down_right(x,y,player):
	global A
	global reverse_lst
	tmp_reverse_lst = list()
	if (A[x][y] != 0): return
	i = x
	if (y!=DIM):
		if (x!=DIM):
			for j in range(y+1,DIM):
				i = i + 1
				if (j > 7 or i > 7):
					break
				if (player != A[i][j] and A[i][j] != 0):
					tmp_reverse_lst.append([i , j])
				elif(A[i][j] != 0):
					if (tmp_reverse_lst != []):
						reverse_lst.append(tmp_reverse_lst)
						break
				else:
					break
					
def reverse_count(x,y,player):
	global reverse_lst
	global A
	reverse_count_up(x,y,player)
	reverse_count_down(x,y,player)
	reverse_count_left(x,y,player)
	reverse_count_right(x,y,player)
	reverse_count_up_right(x,y,player)
	reverse_count_up_left(x,y,player)
	reverse_count_down_right(x,y,player)
	reverse_count_down_left(x,y,player)
	return len(reverse_lst)
	
	
def compute_counts(player):
	global reverse_lst
	B = [[0 for x in range(DIM)] for y in range(DIM)]
	for i in range(DIM):
		for j in range(DIM):
			B[i][j] = reverse_count(i,j,player)	
			reverse_lst = list()		
#	l=0
#	print("     0", "", "1", "", "2" , "" ,"3", "", "4", "", "5" , "", "6" ,"", "7")
#	print("----------------------------------------------------------------")
#	for i in range(DIM):
#		print(l, "|", end='')
#		for j in range(DIM):
#			print (" ", B[i][j],  end='')
#		l = l + 1
#		print()	
#	print("----------------------------------------------------------------")
	return B
	
def add_checker(x,y,player):
	global A
	global reverse_lst
	A[x][y] = player
	for element in reverse_lst:
		if element != None:
			A[element[0][0]][element[0][1]] = player
	reverse_lst = list()	
		
def human_play(player):
	global reverse_lst
	B = compute_counts(player)
	Available_flag = False
	Choice_flag = False
	for i in range(DIM):
		for j in range(DIM):
			if (B[i][j] > 0):
				Available_flag = True
	if (Available_flag):
		while (True):
			print("There is at least one available move. Give the coordinates of your choice!")
			var1 = int(input("Please enter x: "))
			var2 = int(input("Please enter y: "))
			if (B[var1][var2] > 0):
				reverse_count(var1,var2,player)
				add_checker(var1,var2,player)
				Choice_flag = True
			if(Choice_flag):
				break
			print("Not a valid choice. Try again!")			
	return Available_flag	
	
	
def computer_play():
	Available_flag = False
	B = compute_counts(1)
	max = 0
	for i in range(DIM):
		for j in range(DIM):
			if (B[i][j] > 0):
				Available_flag = True
	if (Available_flag):
		for i in range(DIM):
			for j in range(DIM):
				if (B[i][j] > max):
					max = B[i][j]
					x_coord = i
					y_coord = j
		print(x_coord,y_coord)			
		reverse_count(x_coord,y_coord,1)
		add_checker(x_coord,y_coord,1)
	return Available_flag		
	
	
def print_score():
	global A
	global score1 
	global score2 
	score1 = 0
	score2 = 0
	for i in range(DIM):
		for j in range(DIM):
			if (A[i][j] == 1):
				score1 = score1 + 10
			if (A[i][j] == 2):
				score2 = score2 + 10
	print("Score for player1 is: ", score1,"Score for player2 is: ", score2)			
	
	
	