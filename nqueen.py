def solveNQueens(n):
    # To store final solutions
    solutions = []

    # Tracking arrays for Branch & Bound
    col = [False] * n                  # Column check
    diag1 = [False] * (2 * n)          # (row - col + n-1)
    diag2 = [False] * (2 * n)          # (row + col)

    # board[row] = col index of queen placed in that row
    board = [-1] * n

    def solve(row):
        # All queens placed
        if row == n:
            solutions.append(board[:])
            return
        
        for c in range(n):
            if not col[c] and not diag1[row - c + n - 1] and not diag2[row + c]:
                # Place queen
                board[row] = c
                col[c] = diag1[row - c + n - 1] = diag2[row + c] = True

                # Recurse next row
                solve(row + 1)

                # Backtrack (remove)
                col[c] = diag1[row - c + n - 1] = diag2[row + c] = False

    solve(0)
    return solutions


def printBoard(solution):
    n = len(solution)
    for r in range(n):
        row = ["Q" if solution[r] == c else "." for c in range(n)]
        print(" ".join(row))
    print()


# ----------- MAIN ----------
if __name__ == "__main__":
    n = int(input("Enter value of N (e.g., 4 or 8): "))
    sols = solveNQueens(n)

    print("\nTotal solutions found:", len(sols))
    print("\nDisplaying solutions:\n")

    for i, sol in enumerate(sols, 1):
        print(f"Solution {i}:")
        printBoard(sol)
