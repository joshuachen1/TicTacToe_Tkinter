from tkinter import Tk, Canvas, Label, StringVar, BOTTOM, SUNKEN, W, X, Y


class TicTacToe:

    def __init__(self, master):
        self.canvas = Canvas(master, width=300, height=300)
        self.canvas.pack()

        self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]

        self.current_turn = 1

        self.player_turn_message = StringVar()
        self.player_turn_message.set("Player 1's Turn")
        self.player_turn = Label(main_window, textvariable=self.player_turn_message, bd=1, relief=SUNKEN, anchor=W)
        self.player_turn.pack(side=BOTTOM, padx=2, fill=X)

        self.canvas.create_line(100, 0, 100, 300)
        self.canvas.create_line(200, 0, 200, 300)
        self.canvas.create_line(0, 100, 300, 100)
        self.canvas.create_line(0, 200, 300, 200)

        self.canvas_00 = Canvas(self.canvas, width=100, height=100, bg='red')
        self.canvas_00.bind("<Button-1>", self.mark00)
        self.canvas_00.grid(row=0, column=0)

        self.canvas_01 = Canvas(self.canvas, width=100, height=100, bg='blue')
        self.canvas_01.bind("<Button-1>", self.mark01)
        self.canvas_01.grid(row=0, column=1)

        self.canvas_02 = Canvas(self.canvas, width=100, height=100, bg='green')
        self.canvas_02.bind("<Button-1>", self.mark02)
        self.canvas_02.grid(row=0, column=2)

        self.canvas_10 = Canvas(self.canvas, width=100, height=100, bg='red')
        self.canvas_10.bind("<Button-1>", self.mark10)
        self.canvas_10.grid(row=1, column=0)

        self.canvas_11 = Canvas(self.canvas, width=100, height=100, bg='blue')
        self.canvas_11.bind("<Button-1>", self.mark11)
        self.canvas_11.grid(row=1, column=1)

        self.canvas_12 = Canvas(self.canvas, width=100, height=100, bg='green')
        self.canvas_12.bind("<Button-1>", self.mark12)
        self.canvas_12.grid(row=1, column=2)

        self.canvas_20 = Canvas(self.canvas, width=100, height=100, bg='red')
        self.canvas_20.bind("<Button-1>", self.mark20)
        self.canvas_20.grid(row=2, column=0)

        self.canvas_21 = Canvas(self.canvas, width=100, height=100, bg='blue')
        self.canvas_21.bind("<Button-1>", self.mark21)
        self.canvas_21.grid(row=2, column=1)

        self.canvas_22 = Canvas(self.canvas, width=100, height=100, bg='green')
        self.canvas_22.bind("<Button-1>", self.mark22)
        self.canvas_22.grid(row=2, column=2)

    def mark00(self, event):
        if self.current_turn % 2 == 1:
            self.canvas_00.create_line(20, 20, 80, 80)
            self.canvas_00.create_line(20, 80, 80, 20)
            self.board[0][0] = 'X'
        else:
            self.canvas_00.create_oval(15, 15, 90, 90)
            self.board[0][0] = 'O'

        self.update_player_turn()

    def mark01(self, event):
        if self.current_turn % 2 == 1:
            self.canvas_01.create_line(20, 20, 80, 80)
            self.canvas_01.create_line(20, 80, 80, 20)
            self.board[0][1] = 'X'
        else:
            self.canvas_01.create_oval(15, 15, 90, 90)
            self.board[0][1] = 'O'

        self.update_player_turn()

    def mark02(self, event):
        if self.current_turn % 2 == 1:
            self.canvas_02.create_line(20, 20, 80, 80)
            self.canvas_02.create_line(20, 80, 80, 20)
            self.board[0][2] = 'X'
        else:
            self.canvas_02.create_oval(15, 15, 90, 90)
            self.board[0][2] = 'O'

        self.update_player_turn()

    def mark10(self, event):
        if self.current_turn % 2 == 1:
            self.canvas_10.create_line(20, 20, 80, 80)
            self.canvas_10.create_line(20, 80, 80, 20)
            self.board[1][0] = 'X'
        else:
            self.canvas_10.create_oval(15, 15, 90, 90)
            self.board[1][0] = 'O'

        self.update_player_turn()

    def mark11(self, event):
        if self.current_turn % 2 == 1:
            self.canvas_11.create_line(20, 20, 80, 80)
            self.canvas_11.create_line(20, 80, 80, 20)
            self.board[1][1] = 'X'
        else:
            self.canvas_11.create_oval(15, 15, 90, 90)
            self.board[1][1] = 'O'

        self.update_player_turn()

    def mark12(self, event):
        if self.current_turn % 2 == 1:
            self.canvas_12.create_line(20, 20, 80, 80)
            self.canvas_12.create_line(20, 80, 80, 20)
            self.board[1][2] = 'X'
        else:
            self.canvas_12.create_oval(15, 15, 90, 90)
            self.board[1][2] = 'O'

        self.update_player_turn()

    def mark20(self, event):
        if self.current_turn % 2 == 1:
            self.canvas_20.create_line(20, 20, 80, 80)
            self.canvas_20.create_line(20, 80, 80, 20)
            self.board[2][0] = 'X'
        else:
            self.canvas_20.create_oval(15, 15, 90, 90)
            self.board[2][0] = 'O'

        self.update_player_turn()

    def mark21(self, event):
        if self.current_turn % 2 == 1:
            self.canvas_21.create_line(20, 20, 80, 80)
            self.canvas_21.create_line(20, 80, 80, 20)
            self.board[2][1] = 'X'
        else:
            self.canvas_21.create_oval(15, 15, 90, 90)
            self.board[2][1] = 'O'

        self.update_player_turn()

    def mark22(self, event):
        if self.current_turn % 2 == 1:
            self.canvas_22.create_line(20, 20, 80, 80)
            self.canvas_22.create_line(20, 80, 80, 20)
            self.board[2][2] = 'X'
        else:
            self.canvas_22.create_oval(15, 15, 90, 90)
            self.board[2][2] = 'O'

        self.update_player_turn()

    def update_player_turn(self):

        self.current_turn += 1

        if self.current_turn % 2 == 1:
            self.player_turn_message.set("Player 1's Turn")
        else:
            self.player_turn_message.set("Player 2's Turn")
            
        self.check_winner()

    def check_winner(self):
        current_player = self.current_turn % 2 + 1
        winner_declared = False

        for i in range(3):
            print ("|", self.board[i][0], self.board[i][1], self.board[i][2], "|")
        print()

        # Top Left
        if self.board[0][0] != ' ':
            if (self.board[0][0] == self.board[0][1] and self.board[0][0] == self.board[0][2] or
                self.board[0][0] == self.board[1][0] and self.board[0][0] == self.board[2][0]):
                    self.player_turn_message.set("Player {} wins!".format(current_player))
                    winner_declared = True

        # Bottom Right
        if self.board[2][2] != ' ':
            if (self.board[2][2] == self.board[2][0] and self.board[2][2] == self.board[2][1] or
                self.board[2][2] == self.board[0][2] and self.board[2][2] == self.board[1][2]):
                    self.player_turn_message.set("Player {} wins!".format(current_player))
                    winner_declared = True

        # Middle
        if self.board[1][1] != ' ':
            # Diagonal
            if (self.board[1][1] == self.board[0][0] and self.board[1][1] == self.board[2][2] or
                self.board[1][1] == self.board[0][2] and self.board[1][1] == self.board[2][0]):
                    self.player_turn_message.set("Player {} wins!".format(current_player))
                    winner_declared = True

            # T-Shape
            if (self.board[1][1] == self.board[0][1] and self.board[1][1] == self.board[2][1] or
                self.board[1][1] == self.board[1][0] and self.board[1][1] == self.board[1][2]):
                    self.player_turn_message.set("Player {} wins!".format(current_player))
                    winner_declared = True

        if not winner_declared and self.current_turn == 10:
            self.player_turn_message.set("Cat's Game! Game Over.")


main_window = Tk()
game = TicTacToe(main_window)
game.check_winner()
main_window.mainloop()