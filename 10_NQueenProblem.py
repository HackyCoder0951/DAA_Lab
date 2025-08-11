import time
import tracemalloc
import os
import psutil

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
					line = ['Q' if solution[row] == col else '_' for col in range(n)]
					print(' '.join(line))
			else:
				print(f"No solution exists for {n} queens.")
	except ValueError:
		print(f"No solution exists for {n} queens.")
	except ValueError:
		print("Invalid input. Please enter an integer.")
		
		# Time and Space Complexity Analysis:
		# Time Complexity:
		# The N-Queens problem is solved using backtracking. In the worst case, for each row, we try all columns.
		# So, the time complexity is O(N!), where N is the number of queens (and the size of the board).
		# This is because for the first row, there are N choices, for the second row N-1, and so on.
		# However, due to pruning (noConflicts), the actual number of recursive calls is less, but the worst-case is still O(N!).

		# Space Complexity:
		# The space complexity is O(N), as we use a list of size N to store the column positions of the queens.
		# Start measuring time and memory
		start_time = time.perf_counter()
		tracemalloc.start()
		process = psutil.Process(os.getpid())
		mem_before = process.memory_info().rss

		# Run the computation again for measurement
		_ = calcQueens(n)

		# Stop measuring time and memory
		end_time = time.perf_counter()
		current, peak = tracemalloc.get_traced_memory()
		mem_after = process.memory_info().rss
		tracemalloc.stop()
		print(f"CPU Execution Time: {end_time - start_time:.6f} seconds")
		print(f"Peak Memory Used by Variables: {peak * 8:.2f} b")
		print(f"Process Memory Before: {mem_before * 8:.2f} b")
		print(f"Process Memory After: {mem_after * 8:.2f} b")
		# Print the range of memory addresses used by the 'solution' variable
		addresses = [id(x) for x in solution]
		if addresses:
			print(f"Memory address range for 'solution': {hex(min(addresses))} - {hex(max(addresses))}")
		else:
			print("No memory addresses to display for 'solution'.")