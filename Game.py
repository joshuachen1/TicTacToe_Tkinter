from tkinter import Tk, Frame, Canvas


class TicTacToe:

    def __init__(self, master):
        self.canvas = Canvas(master, width=300, height=300)
        self.canvas.pack()

        self.draw_board()

    def draw_board(self):
        line_1 = self.canvas.create_line(100, 0, 100, 300)
        line_2 = self.canvas.create_line(200, 0, 200, 300)
        line_3 = self.canvas.create_line(0, 100, 300, 100)
        line_4 = self.canvas.create_line(0, 200, 300, 200)





main_window = Tk()
game = TicTacToe(main_window)

main_window.mainloop()