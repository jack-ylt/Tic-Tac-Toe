
import random



def run():
	print "Welcom to Tic_Tac_toe!"
	player, computer = choose_x_or_o() 
	
	while True:
		# initialize the game
		board = create_board()
		turn = who_go_first(['player', 'computer'])
		
		# playing game
		while True:
			# make move
			if turn == 'player':
				show_board(board)
				board = player_move(board, player)
			else:
				board = computer_move(board, player, computer)
			
			# compute and handle game result
			if is_winner(board, player):
				final_msg = "Hooray! You have won the game!"
				break
			elif is_winner(board, computer):
				final_msg = "The computer has beaten you! You lose."
				break
			elif is_tie(board):
				final_msg = "The game is a tie!"
				break
			else:
				turn = change_turn(turn)
			
		show_board(board)
		print final_msg
		
		print "\n"
		if not play_again():
			break
			
def create_board():
	"""
	() -> list of string
	create a new board
	
	>>> create_board()
	[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
	"""
	return [" " for i in range(9)]

def choose_x_or_o():
	"""
	() -> string
	player choose X or O
	"""
	
	def is_x_or_o(s):
		"""
		str -> boolean
		check if s is x or o
		"""
		return s.upper() in ['X', 'O']
		
	msg = "Do you want to be X or O?"
	player = get_user_input(msg, is_x_or_o).upper()
	if player == 'X':
		return ['X', 'O']
	return ['O', 'X']
	
def who_go_first(l):
	"""
	list -> string
	compute who goes first? (computer or player)
	"""
	turn = random.choice(l)
	print "{} will go first".format(turn)
	return turn
	
def show_board(b):
	"""
	(list) -> None
	draw the board
	"""
	for i in range(3):
		print "| {} | {} | {} |".format( *b[i*3: i*3+3] )
		if i in (0, 1):
			print "- - - - - - -"

def player_move(board, player):
	"""
	(list, string) -> list-of str
	player make move, return the updated board
	"""
	
	def is_valid_move(i):
		"""
		(number) -> boolean
		check if the move is valid
		"""
		try:
			i = int(i)
		except:
			return False
		else:
			return i-1 in get_possible_move(board)
	
	msg = "What is your next move? (1-9)"
	move = get_user_input(msg, is_valid_move)
	i = int(move) - 1
	return build_board(board, i, player)

	
def computer_move(board, player, computer):
	"""
	(list, str, str) -> list of str
	computer chose move, return the updated board
	"""
	p_move = get_possible_move(board)
	move = sample_ai(p_move, board, computer, player)
	return build_board(board, move, computer)
	
def is_tie(board):
	return get_possible_move(board) == []
	
def change_turn(turn):
	"""
	(str) -> str
	change the game turn
	"""
	return 'player' if turn == 'computer' else 'computer'
	
def sample_ai(possible_move, board, computer, player):
	"""
	(list, list, str, str) -> int
	compute the computer 
	"""
	b = board[:]
	
	# check if can win
	for i in possible_move:
		b_tmp = build_board(b, i, computer)
		if is_winner(b_tmp, computer):
			return i
	
	# block the player to win
	for i in possible_move:
		b_tmp = build_board(b, i, player)
		if is_winner(b_tmp, player):
			return i
	
	# # choose a center or corner
	# for i in possible_move:
		# if i in [0, 2, 4, 6, 8]:
			# return i
	
	# choose a random place
	return possible_move[0]
	
def play_again():
	"""
	ke -> boolean
	Ask if player want to play game again.
	"""
	print "Do you want to play again? (yes or no)"
	i = raw_input('> ')
	return i.upper().startswith('Y')
	
	
	
###################################################
# help funcs
###################################################
def is_space_free(b, i):
	"""
	(list, int) -> boolean
	check if b[i] == ' '
	"""
	return b[i] == ' '

def get_user_input(msg, is_valid):
	"""
	(str, func) -> str
	get a valid user input
	"""
	while True:
		print msg
		i = raw_input("> ")
		if is_valid(i):
			return i

def get_possible_move(board):
	p = [i for i in range(9) 
		if is_space_free(board, i)]
	random.shuffle(p)
	return p
			
def build_board(board, i, letter):
	"""
	list -> list
	make board[i] = letter
	"""
	b = board[:]
	b[i] = letter
	return b
			
def is_winner(b, s):
	"""
	(list, str) -> boolean
	given the board: b, check if the s win the game
	"""
	return s == b[0] == b[1] == b[2] or \
		s == b[3] == b[4] == b[5] or \
		s == b[6] == b[7] == b[8] or \
		s == b[0] == b[3] == b[6] or \
		s == b[1] == b[4] == b[7] or \
		s == b[2] == b[5] == b[8] or \
		s == b[0] == b[4] == b[8] or \
		s == b[2] == b[4] == b[6]			


		
if __name__ == "__main__":
	import doctest
	doctest.testmod()
	
	run()