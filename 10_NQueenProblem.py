def calcQueens(size):
	board = [-1] * size
	if queens(board, 0, size):
		return board
	else:
		return None

def queens(board, current, size):
	if current == size:
		return True
	else:
		for i in range(size):
			board[current] = i
			if noConflicts(board, current):
				if queens(board, current + 1, size):
					return True
def noConflicts(board, current):
	for i in range(current):
		if board[i] == board[current]:
			return False
		if abs(board[current] - board[i]) == current - i:
			return False
	return True
if __name__ == "__main__":
	try:
		n = int(input("Enter the number of queens: "))
		if n <= 0:
			print("Number of queens must be positive.")
		else:
			solution = calcQueens(n)
			if solution:
				print(f"A solution exists for {n} queens:")
				for row in range(n):
					line = ['Q' if solution[row] == col else '.' for col in range(n)]
					print(' '.join(line))
			else:
				print(f"No solution exists for {n} queens.")
	except ValueError:
		print("Invalid input. Please enter an integer.")
		print(f"No solution exists for {n} queens.")
	except ValueError:
		print("Invalid input. Please enter an integer.")
