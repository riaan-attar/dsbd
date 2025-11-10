# n-queens: find all solutions with simple backtracking

def solve_n_queens(n=8):
    cols = set()          # columns used
    diag1 = set()         # r - c used (main diagonals)
    diag2 = set()         # r + c used (anti-diagonals)
    board = [-1] * n      # board[r] = c where the queen is in row r
    solutions = []

    def place(row=0):
        if row == n:
            solutions.append(board[:])  # store a copy
            return
        for c in range(n):
            if c in cols or (row - c) in diag1 or (row + c) in diag2:
                continue
            board[row] = c
            cols.add(c); diag1.add(row - c); diag2.add(row + c)
            place(row + 1)
            cols.remove(c); diag1.remove(row - c); diag2.remove(row + c)
            board[row] = -1

    place()
    return solutions

def pretty_print(solution):
    n = len(solution)
    line = "+" + "---+" * n
    for r in range(n):
        print(line)
        row = [" Q " if solution[r] == c else "   " for c in range(n)]
        print("|" + "|".join(row) + "|")
    print(line)

# run it
if __name__ == "__main__":
    N = 4  # change N to what you need
    sols = solve_n_queens(N)
    print(f"total solutions for N={N}: {len(sols)}")
    if sols:
        print("\none solution:\n")
        pretty_print(sols[0])
