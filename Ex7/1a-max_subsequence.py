def lcs(X, Y):
	table = [[None for i in range(len(X))] for j in range(len(Y))]
	lcs_helper(X, Y, len(X) - 1, len(Y) - 1, table)
	return get_seq(X, Y, table, len(X) - 1, len(Y) - 1)

def get_seq(X, Y, table, x, y):
	if x < 0 or y < 0:
		return ""
	e = table[y][x]
	return get_seq(X, Y, table, e.x, e.y) + (X[x] if X[x] == Y[y] else "")

def lcs_helper(X, Y, x, y, table):
	if x < 0 or y < 0:
		return 0
	
	if table[y][x] is not None:
		return table[y][x].len
	
	if X[x] == Y[y]:
		table[y][x] = Entry(x-1, y-1, lcs_helper(X, Y, x - 1, y-1, table) + 1)
		return table[y][x].len
	
	left_len = lcs_helper(X, Y, x-1, y, table)
	top_len = lcs_helper(X, Y, x, y-1, table)
	if left_len > top_len:
		table[y][x] = Entry(x-1, y, left_len)
		return left_len
	table[y][x] = Entry(x, y-1, top_len)
	return top_len

class Entry:
	def __init__(self, x, y, length):
		self.x = x
		self.y = y
		self.len = length
		
if __name__ == "__main__":
	X = input("Enter X: ")
	Y = input("Enter Y: ")
	seq = lcs(X, Y)
	print(f"Longest Common Subsequence: {seq}")

