#A text-based Ultimate tic-tac-toe game coded in python. Features a nested tic-tac-toe board. It also features a save and load so players can quit the game whenever they want. It keeps track of whose turn is it and also the scores.
#Slightly different than a traditional ultimate tic-tac-toe because the winner decides which cell to play at the main board

import random
import os
import datetime

file_game = ""

folder_name = "saves"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

def winnerdisplaymessage():

	message = r"""  
  ░██████    ░██████  
 ░██   ░██  ░██   ░██ 
░██        ░██        
░██  █████ ░██  █████ 
░██     ██ ░██     ██ 
 ░██  ░███  ░██  ░███ 
  ░█████░█   ░█████░█ 
     
               """

	print(message)

def titlesign():
	message = r"""
 _   _ _   _____ ___ __  __    _  _____ _____   _____ ___ ____    _____  _    ____    _____ ___  _____ 
| | | | | |_   _|_ _|  \/  |  / \|_   _| ____| |_   _|_ _/ ___|  |_   _|/ \  / ___|  |_   _/ _ \| ____|
| | | | |   | |  | || |\/| | / _ \ | | |  _|     | |  | | |   _____| | / _ \| |   _____| || | | |  _|  
| |_| | |___| |  | || |  | |/ ___ \| | | |___    | |  | | |__|_____| |/ ___ \ |__|_____| || |_| | |___ 
 \___/|_____|_| |___|_|  |_/_/   \_\_| |_____|   |_| |___\____|    |_/_/   \_\____|    |_| \___/|_____|

	"""
	print(message)

def printboard(board):
    print("\n---+---+---")
    for r in range(3):
        print("", board[r][0], "|", board[r][1], "|", board[r][2])
        print("---+---+---")

def instructions():
	print()
	print("Welcome to an ultimate game of tic tac toe! Here are the instructions:")
	print("(1) Both players must enter their names and their symbols will be randomly assigned")
	print("(2) At the start of the game, the game randomly chooses a cell to play in")
	print("(3) Once the game chooses a cell, players will then play in that small board")
	print("(4) The game will keep checking to see if that small board has a winner or a draw")
	print("(5) Once the small board is done, that cell will be marked by the symbol of the winner, otherwise D for draw")
	print("(6) The game will keep checking if the main board has a winner or not")
	print("(7) Once the game has declared a winner, players wins/losses/ties will be updated and they may choose to repeat the match again")
	print()
	print("Note: While playing, players can save their match at any time. They can choose to: \n (S) to save the game and exit \n (E) exit the game without saving \n They may play the saved matched by going to the load game")

	go_back = input("\n Press any key to return to the menu: ")

def parse_value(text):
	if text == "None":
		return None
	if text == "True":
		return True
	if text == "False":
		return False
	return text

def get_player_name(player_number):
	invalid_characters = '\\/:*?"<>|~#%&()[{]}^.+-'

	while True:
		name = input("Enter name for player " + str(player_number) + ": ")

		sanitized_name = ""

		for ch in name:
			if ch in invalid_characters:
				sanitized_name += "_"

			else:
				sanitized_name += ch 

		if sanitized_name == "":
			print("Name cannot be empty. Try again!")
			continue

		break

	return sanitized_name

def num_to_row_column(n):
	n = int(n)
	n -= 1  
	row = n // 3
	column = n % 3
	return row, column

def check_winner(board):
	for r in range(3):
		if board[r][0] == board[r][1] == board[r][2] and board[r][0] != " ":
			return board[r][0]
	for c in range(3):
		if board[0][c] == board[1][c] == board[2][c] and board[0][c] != " ":
			return board[0][c]

	if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
		return board[0][0]

	if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
		return board[0][2]

	for r in range(3):
		for c in range(3):
			if board[r][c] == " " or board[r][c] == "•":
				return " "   # game still ongoing
	return "D"   # board full and no winner = Draw

def assign_symbol(player1, player2):
    rng = random.randint(1, 2)
    if rng == 1:
        print("Player 1 ", player1, " will be X!")
        print("Player 2 ", player2, " will be O!")
        return {player1: "X", player2: "O"}, player1
    else:
        print("Player 1 ", player1, " will be O!")
        print("Player 2 ", player2, " will be X!")
        return {player1: "O", player2: "X"}, player2

def save_game(a):
	global file_game
	if file_game != "":
		os.remove(file_game)
		file_game = ""


	saved_progress = a

	timestamp = str(datetime.datetime.now().strftime("%Y%m%d_%H%M%S"))

	filename = "saves/" + saved_progress["saved_player1"]["name"] + "__" + saved_progress["saved_player2"]["name"] + "__" + timestamp + ".txt"

	f = open(filename, "w")

	f.write("PLAYER 1 INFO:" + "\n")
	f.write("Name: " + saved_progress["saved_player1"]["name"] + "\n")
	f.write("Symbol: " + saved_progress["saved_player1"]["symbol"] + "\n")
	f.write("Wins: " + str(saved_progress["saved_player1"]["wins"]) + "\n")
	f.write("Losses: " + str(saved_progress["saved_player1"]["losses"]) + "\n")
	f.write("Draws: " + str(saved_progress["saved_player1"]["ties"]) + "\n" + "\n")

	f.write("PLAYER 2 INFO:" + "\n")
	f.write("Name: " + saved_progress["saved_player2"]["name"] + "\n")
	f.write("Symbol: " + saved_progress["saved_player2"]["symbol"] + "\n")
	f.write("Wins: " + str(saved_progress["saved_player2"]["wins"]) + "\n")
	f.write("Losses: " + str(saved_progress["saved_player2"]["losses"]) + "\n")
	f.write("Draws: " + str(saved_progress["saved_player2"]["ties"]) + "\n" + "\n")

	f.write("Status of active small board: " + saved_progress["saved_minor_board"] + "\n")
	f.write("Status of the main board: " + saved_progress["saved_main_board"] + "\n")
	f.write("Current main board row: " + str(saved_progress["saved_row_main_board"]) + "\n")
	f.write("Current main board column: " + str(saved_progress["saved_column_main_board"]) + "\n" + "\n")

	f.write("CURRENT ACTIVE PLAYER INFO:" + "\n")
	f.write("Name: " + saved_progress["saved_current_player"]["name"] + "\n")
	f.write("Symbol: " + saved_progress["saved_current_player"]["symbol"] + "\n")
	f.write("Wins: " + str(saved_progress["saved_current_player"]["wins"]) + "\n")
	f.write("Losses: " + str(saved_progress["saved_current_player"]["losses"]) + "\n")
	f.write("Draws: " + str(saved_progress["saved_current_player"]["ties"]) + "\n" + "\n")

	f.write("ADDITIONAL INFO: " + "\n")

	if saved_progress["saved_small_board_winner"] is None:
		f.write("Current small board winner: " + str(saved_progress["saved_small_board_winner"]) + "\n")
	else:
		f.write("Current small board winner: " + str(saved_progress["saved_small_board_winner"]["name"]) + "\n")

	f.write("Time stamp: " + timestamp)

	f.close()

	print("DONE! Saved as: ", filename)

def check_if_finished_match(file):

	f = open(file, "r")
	content = f.read()
	f.close()

	if "FINISHED MATCH" in content:
		return True
	else:
		return False

def save_finished_game(a):
	global file_game

	if file_game != "":
		os.remove(file_game)
		file_game = ""

	saved_progress = a
	timestamp = str(datetime.datetime.now().strftime("%Y%m%d_%H%M%S"))
	filename = "saves/" + saved_progress["saved_player1"]["name"] + "__" + saved_progress["saved_player2"]["name"] + "__" + timestamp + ".txt"
	f = open(filename, "w")

	f.write("FINISHED MATCH" + "\n" + "\n")
	f.write("PLAYER 1 INFO:" + "\n")
	f.write("Name: " + saved_progress["saved_player1"]["name"] + "\n")
	f.write("Previous Symbol: " + saved_progress["saved_player1"]["symbol"] + "\n")
	f.write("Wins: " + str(saved_progress["saved_player1"]["wins"]) + "\n")
	f.write("Losses: " + str(saved_progress["saved_player1"]["losses"]) + "\n")
	f.write("Draws: " + str(saved_progress["saved_player1"]["ties"]) + "\n" + "\n")

	f.write("PLAYER 2 INFO:" + "\n")
	f.write("Name: " + saved_progress["saved_player2"]["name"] + "\n")
	f.write("Previous Symbol: " + saved_progress["saved_player2"]["symbol"] + "\n")
	f.write("Wins: " + str(saved_progress["saved_player2"]["wins"]) + "\n")
	f.write("Losses: " + str(saved_progress["saved_player2"]["losses"]) + "\n")
	f.write("Draws: " + str(saved_progress["saved_player2"]["ties"]) + "\n" + "\n")

	f.close()

	return

def load_finished_game(file_name):
	saved_player1 = {"name": "", "symbol": None, "wins": 0, "losses": 0, "ties": 0} 
	saved_player2 = {"name": "", "symbol": None, "wins": 0, "losses": 0, "ties": 0}

	f = open(file_name, "r")
	lines = f.readlines()
	f.close()

	if len(lines) < 15:
		print("file is corrupted.")
		return None


	saved_player1["name"] = lines[3].split(": ")[1].strip()
	saved_player1["wins"] = int(lines[5].split(": ")[1].strip())
	saved_player1["losses"] = int(lines[6].split(": ")[1].strip())
	saved_player1["ties"] = int(lines[7].split(": ")[1].strip())

	saved_player2["name"] = lines[10].split(": ")[1].strip()
	saved_player2["wins"] = int(lines[12].split(": ")[1].strip())
	saved_player2["losses"] = int(lines[13].split(": ")[1].strip())
	saved_player2["ties"] = int(lines[14].split(": ")[1].strip())

	saved_information = {"saved_player1": saved_player1, "saved_player2": saved_player2}

	return saved_information

def load_game(file_name):

	saved_player1 = {"name": "", "symbol": None, "wins": 0, "losses": 0, "ties": 0} 
	saved_player2 = {"name": "", "symbol": None, "wins": 0, "losses": 0, "ties": 0}

	f = open(file_name, "r")
	lines = f.readlines()
	f.close()

	if len(lines) < 29:
		print("file is corrupted.")
		return None

	saved_player1["name"] = lines[1].split(": ")[1].strip()
	saved_player1["symbol"] = lines[2].split(": ")[1].strip()
	saved_player1["wins"] = int(lines[3].split(": ")[1].strip())
	saved_player1["losses"] = int(lines[4].split(": ")[1].strip())
	saved_player1["ties"] = int(lines[5].split(": ")[1].strip())

	saved_player2["name"] = lines[8].split(": ")[1].strip()
	saved_player2["symbol"] = lines[9].split(": ")[1].strip()
	saved_player2["wins"] = int(lines[10].split(": ")[1].strip())
	saved_player2["losses"] = int(lines[11].split(": ")[1].strip())
	saved_player2["ties"] = int(lines[12].split(": ")[1].strip())

	minor_board_string = lines[14].split(": ")[1].rstrip("\n")

	saved_minor_board = [
	[minor_board_string[0], minor_board_string[1], minor_board_string[2]],
	[minor_board_string[3], minor_board_string[4], minor_board_string[5]],
	[minor_board_string[6], minor_board_string[7], minor_board_string[8]]
	]

	main_board_string = lines[15].split(": ")[1].rstrip("\n")

	saved_main_board = [
	[main_board_string[0], main_board_string[1], main_board_string[2]],
	[main_board_string[3], main_board_string[4], main_board_string[5]],
	[main_board_string[6], main_board_string[7], main_board_string[8]]
	]

	saved_row_main_board = int(lines[16].split(": ")[1].strip())
	saved_column_main_board = int(lines[17].split(": ")[1].strip())

	saved_current_player = lines[20].split(": ")[1].strip()

	if saved_current_player == saved_player1["name"]:
		current_player = saved_player1
	else:
		current_player = saved_player2

	saved_small_board_winner = parse_value(lines[27].split(": ")[1].strip())

	saved_progress = {
			"saved_player1": saved_player1, 
			"saved_player2": saved_player2, 
			"saved_main_board": saved_main_board,
			"saved_minor_board": saved_minor_board,
			"saved_row_main_board": saved_row_main_board,
			"saved_column_main_board": saved_column_main_board,
			"saved_current_player": current_player,
			"saved_small_board_winner": saved_small_board_winner,
			}

	print("Succesfully loaded match!")

	return saved_progress

def small_board(player1, player2, current_player, minor_board_progress = None):
	global file_game

	if minor_board_progress is not None:
		minor_board = minor_board_progress
	else:
		minor_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

	while True:
		print()
		print("========== SMALL BOARD ==========")
		printboard(minor_board)
		print("Input reference: \n 1 2 3 \n 4 5 6 \n 7 8 9")
		print("---> It is", current_player["name"], "(", current_player['symbol'], ")", "turn to pick a cell")

		while True: #validates the input of row and column
			try:
				choice = int(input("Enter a cell (1-9): "))
			except ValueError:
				print("Make sure to enter a number. Thank you!")
				continue

			if not (1 <= choice <= 9):
				print("Make sure choice is within 1-9")
				print()
				continue

			row, column	= num_to_row_column(choice)

			if minor_board[row][column] != " ":
				print("That cell is occupied! Select another one.")
				print()
				continue

			break

		while True:
				keep = input("(S) for save and exit | (E) for exit without saving | Enter (or type any) to continue: ")

				if keep == "S" or keep == "s":
					minor_board_progress = {"minor_board": minor_board, "current_player": current_player}
					return minor_board_progress

				elif keep == "E" or keep == "e":
					print("Closing game without saving...")
					file_game = ""
					minor_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
					current_player = None
					return

				else:
					break

		minor_board[row][column] = current_player["symbol"]	
		result = check_winner(minor_board)

		if result == "X" or result == "O":
			print()
			print("========== SMALL BOARD ==========")
			printboard(minor_board)
			print("--->", current_player["name"], "(", current_player['symbol'], ")", "wins this main board cell!")
			print()
			minor_board_progress = None
			return result

		elif result == "D":
			print()
			print("========== SMALL BOARD ==========")
			printboard(minor_board)
			print()
			print("---> Current board ended in a draw!")
			minor_board_progress = None
			return result

		if current_player is player1:
			current_player = player2
		else:
			current_player = player1

def main_tic_tac_toe(small_board_winner = None, first_turn = True, Draw_match = False, saved_progress = None, saved_player_infos = None): 
	global file_game

	main_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

	player1 = {"name": "", "symbol": None, "wins": 0, "losses": 0, "ties": 0} 
	player2 = {"name": "", "symbol": None, "wins": 0, "losses": 0, "ties": 0}

	if saved_progress is None:
		if saved_player_infos:

			player1 = saved_player_infos["saved_player1"]
			player2 = saved_player_infos["saved_player2"]
		else:
			player1["name"] = get_player_name(1)
			player2["name"] = get_player_name(2)

		rng = random.randint(1, 2)

		if rng == 1:
			player1["symbol"] = "X"
			player2["symbol"] = "O"
		else:
			player1["symbol"] = "O"
			player2["symbol"] = "X"

		print()
		print(player1["name"], "will be", player1["symbol"])
		print(player2["name"], "will be", player2["symbol"])
		print()

		if player1["symbol"] == "X":
			current_player = player1
		else:
			current_player = player2

	else:
		first_turn = False
		player1 = saved_progress["saved_player1"]
		player2 = saved_progress["saved_player2"]
		main_board = saved_progress["saved_main_board"]
		current_player = saved_progress["saved_current_player"]

		if saved_progress["saved_small_board_winner"] == player1:
			small_board_winner = player1
		else:
			small_board_winner = player2

	while True:

		if first_turn:
			while True:
				row = random.randint(0, 2)
				column = random.randint(0, 2)
				if main_board[row][column] == " ":
					break

			main_board[row][column] = "•"

			print("========== SCOREBOARD ==========")
			print()
			print(player1["name"], " | ", "Wins:", player1["wins"], "Losses:", player1["losses"], "Draws:", player1["ties"])
			print(player2["name"], " | ", "Wins:", player2["wins"], "Losses:", player2["losses"], "Draws:", player2["ties"])
			print()
			print("================================")
			print()
			print("========== MAIN BOARD ==========")
			printboard(main_board)
			print()

			print("Start of game! The first main board cell to play is at", "[", row, ",", column, "]")
			first_turn = False

		elif Draw_match:

			for r in range(3):
				for c in range(3):
					if main_board[r][c] == "•":
						main_board[r][c] = " "

			while True:
				row = random.randint(0, 2)
				column = random.randint(0, 2)
				if main_board[row][column] == " ":
					break
	
			main_board[row][column] = "•"

			print("========== SCOREBOARD ==========")
			print()
			print(player1["name"], " | ", "Wins:", player1["wins"], "Losses:", player1["losses"], "Draws:", player1["ties"])
			print(player2["name"], " | ", "Wins:", player2["wins"], "Losses:", player2["losses"], "Draws:", player2["ties"])
			print()
			print("================================")
			print()
			print("========== MAIN BOARD ==========")
			printboard(main_board)
			print()
			print("Since the previous small board ended in a draw. We're now playing at", "[", row, ",", column, "]")
			print("RANDOM PICK:", current_player["name"], "(", current_player["symbol"], ")", "will be the first one to go!")
			Draw_match = False

		else:
			print("========== SCOREBOARD ==========")
			print()
			print(player1["name"], " | ", "Wins:", player1["wins"], "Losses:", player1["losses"], "Draws:", player1["ties"])
			print(player2["name"], " | ", "Wins:", player2["wins"], "Losses:", player2["losses"], "Draws:", player2["ties"])
			print()
			print("================================")
			print()
			print("========== MAIN BOARD ==========")
			printboard(main_board)
			print()
			print(small_board_winner["name"], "(", small_board_winner["symbol"], ")", "is choosing a cell")

			if saved_progress is not None:
				row = saved_progress["saved_row_main_board"]
				column = saved_progress["saved_column_main_board"]

			else:
				while True:
					try:
						row = int(input("Enter a row (0-2): "))
						column = int(input("Enter a column (0-2): "))
					except ValueError:
						print("Make sure to enter a number. Thank you!")
						continue

					if not (0 <= row <= 2 and 0 <= column <= 2):
						print("Make sure choice is within 0-2")
						print()
						continue

					if main_board[row][column] != " ":
						print("That cell is occupied! Select another one.")
						print()
						continue

					break

				while True:
					keep = input("(S) for save and exit | (E) for exit without saving | Enter (or type any) to continue: ")

					if keep == "S" or keep == "s":
						saved_player1 = player1 
						saved_player2 = player2

						saved_main_board = ""
						
						saved_row_main_board = row
						saved_column_main_board = column
						saved_current_player = small_board_winner
						saved_small_board_winner = small_board_winner
						saved_first_turn = first_turn 

						for row in main_board:
							for cell in row:
								saved_main_board += cell

						saved_progress = {
						"saved_player1": saved_player1, 
						"saved_player2": saved_player2, 
						"saved_main_board": saved_main_board,
						"saved_minor_board": "         ",
						"saved_row_main_board": saved_row_main_board,
						"saved_column_main_board": saved_column_main_board,
						"saved_current_player": saved_current_player,
						"saved_small_board_winner": saved_small_board_winner,
						}

						result = None
						main_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
						small_board_winner = None
						first_turn = True
						Draw_match = False
						player1 = {"name": "", "symbol": None, "wins": 0, "losses": 0, "ties": 0}
						player2 = {"name": "", "symbol": None, "wins": 0, "losses": 0, "ties": 0}

						save_game(saved_progress)
						print("Game saved! Returning to menu...")
						print()
						titlesign()
						print("Welcome to a game of ultimate tic-tac-toe! Select from the menu \n [1] New game \n [2] Load game \n [3] Instructions \n [4] Exit")
						return

					elif keep == "E" or keep == "e":
						file_game = ""
						print("Closing game without saving...")
						titlesign()
						print("\n Welcome to a game of ultimate tic-tac-toe! Select from the menu \n [1] New game \n [2] Load game \n [3] Instructions \n [4] Exit")
						return

					else:
						break

			main_board[row][column] = "•"
			print()
			print("========== MAIN BOARD ==========")
			printboard(main_board)
			print()
			print("Now playing at", "[", row, ",", column, "]")

		if saved_progress is not None:
			result = small_board(player1, player2, current_player, minor_board_progress = saved_progress["saved_minor_board"])
			saved_progress = None
		else:	
			result = small_board(player1, player2, current_player)

		if isinstance(result, dict):
			for r in range(3):
				for c in range(3):
					if main_board[r][c] == "•":
						main_board[r][c] = " "

			saved_player1 = player1 

			saved_player2 = player2

			saved_main_board = ""
			saved_minor_board = "" 
			saved_row_main_board = row
			saved_column_main_board = column
			saved_current_player = result["current_player"]
			saved_small_board_winner = small_board_winner
			saved_first_turn = first_turn 

			for row in main_board:
				for cell in row:
					saved_main_board += cell

			quick_minor_board = result["minor_board"]

			for row in quick_minor_board:
				for cell in row:
					saved_minor_board += cell

			quick_minor_board = None

			saved_progress = {
			"saved_player1": saved_player1, 
			"saved_player2": saved_player2, 
			"saved_main_board": saved_main_board,
			"saved_minor_board": saved_minor_board,
			"saved_row_main_board": saved_row_main_board,
			"saved_column_main_board": saved_column_main_board,
			"saved_current_player": saved_current_player,
			"saved_small_board_winner": saved_small_board_winner,
			}

			result = None
			main_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
			small_board_winner = None
			first_turn = True
			Draw_match = False
			player1 = {"name": "", "symbol": None, "wins": 0, "losses": 0, "ties": 0}
			player2 = {"name": "", "symbol": None, "wins": 0, "losses": 0, "ties": 0}

			save_game(saved_progress)

			print()
			titlesign()
			print("Welcome to a game of ultimate tic-tac-toe! Select from the menu \n [1] New game \n [2] Load game \n [3] Instructions \n [4] Exit")
			break

		elif result == None:
			titlesign()
			print("Welcome to a game of ultimate tic-tac-toe! Select from the menu \n [1] New game \n [2] Load game \n [3] Instructions \n [4] Exit")
			break

		main_board[row][column] = result

		if result == player1["symbol"]:
			small_board_winner = player1

		elif result == player2["symbol"]:
			small_board_winner = player2

		if result == "D":
			small_board_winner = random.choice([player1, player2])
			print("Small board resulted in a draw, therefore I'll randomly choose a player to be the first one to play in the next main cell")
			print()
			Draw_match = True

		else:
			Draw_match = False

		current_player = small_board_winner

		winner_symbol = check_winner(main_board)

		if winner_symbol == " ":
			continue

		if winner_symbol == player1["symbol"]:
			player1["wins"] += 1
			player2["losses"] += 1
			print()
			print("========== MAIN BOARD ==========")
			printboard(main_board)
			print()
			print(player1["name"], "wins the game!")

		elif winner_symbol == player2["symbol"]:
			player2["wins"] += 1
			player1["losses"] += 1
			print()
			print("========== MAIN BOARD ==========")
			printboard(main_board)
			print()
			print(player2["name"], "wins the game!")

		elif winner_symbol == "D":
			player1["ties"] += 1
			player2["ties"] += 1
			print()
			print("========== MAIN BOARD ==========")
			printboard(main_board)
			print()
			print("Overall game resulted in a draw")

		for r in range(3):
				for c in range(3):
					if main_board[r][c] == "•":
						main_board[r][c] = " "

		winnerdisplaymessage()
		print("========== SCOREBOARD ==========")
		print()
		print(player1["name"], " | ", "Wins:", player1["wins"], "Losses:", player1["losses"], "Draws:", player1["ties"])
		print(player2["name"], " | ", "Wins:", player2["wins"], "Losses:", player2["losses"], "Draws:", player2["ties"])
		print()
		print("================================")
		print()

		while True:
			replay = input("Want to play again (Y/N)?: ")

			if replay == "Y" or replay == "y":
				break
			elif replay == "N" or replay == "n":
				break
			else:
				print("Enter a valid option (Y/N)")
				print()

		while True:
				keep = input("Save player scores (Y/N)?: ")

				if keep == "Y" or keep == "y":
					saved_player1 = player1 
					saved_player2 = player2

					saved_finished_match = {
					"saved_player1": saved_player1, 
					"saved_player2": saved_player2, 
					}

					save_finished_game(saved_finished_match)
					print("saving scores...")
					break

				elif keep == "N" or keep == "n":
					file_game = ""
					break

				else:
					print("Please enter Y/N.")
					print()

		if replay == "Y" or replay == "y":
			main_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
			small_board_winner = None
			first_turn = True
			Draw_match = False
			player1["symbol"] = None
			player2["symbol"] = None


			rng = random.randint(1, 2)
			if rng == 1:
				player1["symbol"] = "X"
				player2["symbol"] = "O"
			else:
				player1["symbol"] = "O"
				player2["symbol"] = "X"

			if player1["symbol"] == "X":
				current_player = player1
			else:
				current_player = player2

			print("Alright! Another round. Randomizing on who is X and O")
			print()
			print(player1["name"], "will be", player1["symbol"])
			print(player2["name"], "will be", player2["symbol"])
			print()

			continue

		else:
			main_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
			small_board_winner = None
			first_turn = True
			Draw_match = False
			player1 = {"name": "", "symbol": None, "wins": 0, "losses": 0, "ties": 0}
			player2 = {"name": "", "symbol": None, "wins": 0, "losses": 0, "ties": 0}
			file_game = ""
			print("Thank you for playing! Returning to menu...")
			print()
			titlesign()
			print("\n Welcome to a game of ultimate tic-tac-toe! Select from the menu \n [1] New game \n [2] Load game \n [3] Instructions \n [4] Exit")
			break


titlesign()
print("Welcome to a game of ultimate tic-tac-toe! Select from the menu \n [1] New game \n [2] Load game \n [3] Instructions \n [4] Exit")
while True:
	try:
		choice = int(input("Enter an option: "))
	except ValueError:
		print("Please ensure you've typed a number. Thanks!")
		continue

	if choice == 1:
		print("Starting a new game of tic-tac-toe!")
		print()
		main_tic_tac_toe()
		continue

	elif choice == 2:
		saves = []

		for file in os.listdir("saves"):
			if file.endswith(".txt"):
				saves.append(file)

		if saves == []:
			print("========== SAVED GAMES ==========")
			print()
			print("No saved games yet. Start playing!")

		else:
			print("========== SAVED GAMES ==========")
			print()

			for i in range(len(saves)):
				print("(", str(i+1), ")", saves[i])

		print()
		print("=================================")

		while True:
			choose = input("Pick a number to load | D to delete | B to go back: ")

			if choose == "D" or choose == "d":
				delete_str = input("Enter the file number to delete: ")

				try:
					delete_index = int(delete_str) - 1

				except ValueError:
					print("Invalid input. Must be a number.")
					print()
					continue

				if delete_index < 0 or delete_index >= len(saves):
					print("Invalid file number.")
					print()
					continue

				deleted_file = "saves/" + saves[delete_index]
				os.remove(deleted_file)
				print("Successfully deleted", deleted_file)
				titlesign()
				print("Welcome to a game of ultimate tic-tac-toe! Select from the menu \n [1] New game \n [2] Load game \n [3] Instructions \n [4] Exit")
				break

			if choose == "B" or choose == "b":
				print("Returning to menu\n")
				titlesign()
				print("Welcome to a game of ultimate tic-tac-toe! Select from the menu \n [1] New game \n [2] Load game \n [3] Instructions \n [4] Exit")
				break

			try:
				num = int(choose)
			except ValueError:
				print("Invalid choice. Try again.\n")
				continue

			if num < 1 or num > len(saves):
				print("Choice is out of bounds. Try again.\n")
				continue

			filename = "saves/" + saves[num - 1]

			is_finished_match = check_if_finished_match(filename)

			if is_finished_match:
				file_game = filename
				saved_infos = load_finished_game(filename)

				if saved_infos is None:
					continue
				else:
					main_tic_tac_toe(saved_player_infos = saved_infos)
					break

			else:
				file_game = filename
				progress = load_game(filename)

				if progress is None:
					continue

				else:
					main_tic_tac_toe(saved_progress = progress)
					break

		continue

	elif choice == 3:
		instructions()
		titlesign()
		print("Welcome to a game of ultimate tic-tac-toe! Select from the menu \n [1] New game \n [2] Load game \n [3] Instructions \n [4] Exit")
		continue

	elif choice == 4:
		print('Thank you for playing! Goodbye!!')
		print()
		break

	else:
		print("Uh oh, please enter the right option (1 - 4), thank you!")

