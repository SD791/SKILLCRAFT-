import tkinter as tk
from tkinter import messagebox


def is_valid(board, row, col, num):
    for x in range(9):
        if board[row][x] == num:
            return False

    for x in range(9):
        if board[x][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True


def solve_sudoku(board):
    empty_cell = find_empty(board)
    if not empty_cell:
        return True  

    row, col = empty_cell

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False


def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None


def get_board_from_gui():
    board = []
    for i in range(9):
        row = []
        for j in range(9):
            value = entry_widgets[i][j].get()
            if value == "":
                row.append(0)
            else:
                try:
                    row.append(int(value))
                except ValueError:
                    row.append(0)
        board.append(row)
    return board


def set_board_to_gui(board):
    for i in range(9):
        for j in range(9):
            entry_widgets[i][j].delete(0, tk.END)
            if board[i][j] != 0:
                entry_widgets[i][j].insert(0, str(board[i][j]))


def solve():
    board = get_board_from_gui()
    if solve_sudoku(board):
        set_board_to_gui(board)
    else:
        messagebox.showerror("No Solution", "This puzzle cannot be solved.")


root = tk.Tk()
root.title("Sudoku Solver")
root.geometry("750x450")
root.configure(bg='powder blue')

entry_widgets = []
for i in range(9):
    row = []
    for j in range(9):
        entry = tk.Entry(root, width=5, font=("Arial", 18), borderwidth=2, relief="solid", justify="center",fg="black",bg="white")
        entry.grid(row=i, column=j, padx=3, pady=3)
        row.append(entry)
    entry_widgets.append(row)


solve_button = tk.Button(root, text="Solve", font=("Arial", 18), command=solve,bg="black",fg="white")
solve_button.grid(row=9, column=0, columnspan=9, pady=10)


root.mainloop()
