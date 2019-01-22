from tkinter import Tk, Toplevel, Button,Checkbutton, Entry, Canvas, Label, StringVar, BOTTOM, SUNKEN, E, W, X, Y, Menu, ALL, messagebox, TOP, LEFT, RIGHT


def player1_get_name():
    global p1_name
    p1_name = p1_name.get()

def player2_get_name():
    global p2_name
    p2_name = p2_name.get()

class TicTacToe:

    def __init__(self, master, name1, name2):
        self.root = master

        if name1 == '':
            self.p1_ID = "Player 1"
        else:
            self.p1_ID = name1
        if name2 == '':
            self.p2_ID = "Player 2"
        else:
            self.p2_ID = name2

        # ***** Board *****
        self.board = [[(' ') for i in range(3)] for i in range(3)]

        self.current_turn = 1
        self.current_player = self.p1_ID
        
        self.current_game = 1
        self.game_log = list()
        self.win_history = list()

        # ***** Scoreboard *****
        self.p1_points = 0
        self.player1_score = StringVar()
        self.player1_score.set("{}\n--------\n{}".format(self.p1_ID, self.p1_points))
        self.p1_score_display = Label(self.root, textvariable=self.player1_score, bd=1, relief=SUNKEN)
        self.p1_score_display.pack(side=LEFT, padx=2, fill=X)

        self.p2_points = 0
        self.player2_score = StringVar()
        self.player2_score.set("{}\n--------\n{}".format(self.p2_ID, self.p2_points))
        self.p2_score_display = Label(self.root, textvariable=self.player2_score, bd=1, relief=SUNKEN)
        self.p2_score_display.pack(side=RIGHT, padx=2, fill=X)

        # ***** Bottom Player Message *****
        self.player_turn_message = StringVar()
        self.player_turn_message.set("{}'s Turn".format(self.p1_ID))
        self.player_turn = Label(self.root, textvariable=self.player_turn_message, bd=1, relief=SUNKEN)
        self.player_turn.pack(side=BOTTOM, padx=2, fill=X)

        # ***** Game Canvas *****
        self.canvas = Canvas(master, width=500, height=500)
        self.canvas.pack()

        # ***** Menu *****
        main_menu = Menu(master)
        master.config(menu=main_menu)

        game_menu = Menu(main_menu)
        main_menu.add_cascade(label="Game", menu=game_menu)
        game_menu.add_command(label="New Game", command=self.new_game)
        game_menu.add_separator()
        game_menu.add_command(label="Exit", command=self.quit)

        moves_menu = Menu(main_menu)
        main_menu.add_cascade(label="Moves", menu=moves_menu)
        moves_menu.add_command(label="Game Log", command=self.display_game_log)
        moves_menu.add_command(label="Win History Log", command=self.display_win_history)

        # ***** Colorized Board *****
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
        if self.board[0][0] == ' ':
            if self.current_player == self.p1_ID:
                self.canvas_00.create_line(20, 20, 80, 80)
                self.canvas_00.create_line(20, 80, 80, 20)
                self.board[0][0] = 'X'
            else:
                self.canvas_00.create_oval(15, 15, 90, 90)
                self.board[0][0] = 'O'

            self.game_log.append("({turn}): {player} placed {mark} at top left"
                                 .format(turn=self.current_turn, player=self.current_player,
                                         mark=self.board[0][0]))

            self.update_player_turn()

    def mark01(self, event):
        if self.board[0][1] == ' ':
            if self.current_player== self.p1_ID:
                self.canvas_01.create_line(20, 20, 80, 80)
                self.canvas_01.create_line(20, 80, 80, 20)
                self.board[0][1] = 'X'
            else:
                self.canvas_01.create_oval(15, 15, 90, 90)
                self.board[0][1] = 'O'

            self.game_log.append("({turn}): {player} placed {mark} at top middle"
                                 .format(turn=self.current_turn, player=self.current_player,
                                         mark=self.board[0][1]))
            self.update_player_turn()

    def mark02(self, event):
        if self.board[0][2] == ' ':
            if self.current_player == self.p1_ID:
                self.canvas_02.create_line(20, 20, 80, 80)
                self.canvas_02.create_line(20, 80, 80, 20)
                self.board[0][2] = 'X'
            else:
                self.canvas_02.create_oval(15, 15, 90, 90)
                self.board[0][2] = 'O'

            self.game_log.append("({turn}): {player} placed {mark} at top right"
                                 .format(turn=self.current_turn, player=self.current_player,
                                         mark=self.board[0][2]))
            self.update_player_turn()

    def mark10(self, event):
        if self.board[1][0] == ' ':
            if self.current_player == self.p1_ID:
                self.canvas_10.create_line(20, 20, 80, 80)
                self.canvas_10.create_line(20, 80, 80, 20)
                self.board[1][0] = 'X'
            else:
                self.canvas_10.create_oval(15, 15, 90, 90)
                self.board[1][0] = 'O'

            self.game_log.append("({turn}): {player} placed {mark} at left middle"
                                 .format(turn=self.current_turn, player=self.current_player,
                                         mark=self.board[1][0]))
            self.update_player_turn()

    def mark11(self, event):
        if self.board[1][1] == ' ':
            if self.current_player == self.p1_ID:
                self.canvas_11.create_line(20, 20, 80, 80)
                self.canvas_11.create_line(20, 80, 80, 20)
                self.board[1][1] = 'X'
            else:
                self.canvas_11.create_oval(15, 15, 90, 90)
                self.board[1][1] = 'O'

            self.game_log.append("({turn}): {player} placed {mark} at the center"
                                 .format(turn=self.current_turn, player=self.current_player,
                                         mark=self.board[1][1]))
            self.update_player_turn()

    def mark12(self, event):
        if self.board[1][2] == ' ':
            if self.current_player == self.p1_ID:
                self.canvas_12.create_line(20, 20, 80, 80)
                self.canvas_12.create_line(20, 80, 80, 20)
                self.board[1][2] = 'X'
            else:
                self.canvas_12.create_oval(15, 15, 90, 90)
                self.board[1][2] = 'O'

            self.game_log.append("({turn}): {player} placed {mark} at right middle"
                                 .format(turn=self.current_turn, player=self.current_player,
                                         mark=self.board[1][2]))
            self.update_player_turn()

    def mark20(self, event):
        if self.board[2][0] == ' ':
            if self.current_player == self.p1_ID:
                self.canvas_20.create_line(20, 20, 80, 80)
                self.canvas_20.create_line(20, 80, 80, 20)
                self.board[2][0] = 'X'
            else:
                self.canvas_20.create_oval(15, 15, 90, 90)
                self.board[2][0] = 'O'

            self.game_log.append("({turn}): {player} placed {mark} at bottom left"
                                 .format(turn=self.current_turn, player=self.current_player,
                                         mark=self.board[2][0]))
            self.update_player_turn()

    def mark21(self, event):
        if self.board[2][1] == ' ':
            if self.current_player == self.p1_ID:
                self.canvas_21.create_line(20, 20, 80, 80)
                self.canvas_21.create_line(20, 80, 80, 20)
                self.board[2][1] = 'X'
            else:
                self.canvas_21.create_oval(15, 15, 90, 90)
                self.board[2][1] = 'O'

            self.game_log.append("({turn}): {player} placed {mark} at bottom middle"
                                 .format(turn=self.current_turn, player=self.current_player,
                                         mark=self.board[2][1]))
            self.update_player_turn()

    def mark22(self, event):
        if self.board[2][2] == ' ':
            if self.current_player == self.p1_ID:
                self.canvas_22.create_line(20, 20, 80, 80)
                self.canvas_22.create_line(20, 80, 80, 20)
                self.board[2][2] = 'X'
            else:
                self.canvas_22.create_oval(15, 15, 90, 90)
                self.board[2][2] = 'O'

            self.game_log.append("({turn}): {player} placed {mark} at bottom right"
                                 .format(turn=self.current_turn, player=self.current_player,
                                         mark=self.board[2][2]))
            self.update_player_turn()

    def update_player_turn(self):

        if self.check_winner() == False:
            self.current_turn += 1

            if self.current_turn % 2 == 1:
                self.current_player = self.p1_ID
            else:
                self.current_player = self.p2_ID

            self.player_turn_message.set("{player}'s Turn".format(player=self.current_player))


    def check_winner(self):
        winner_declared = False
        game_over = False

        for i in range(3):
            print("|", self.board[i][0], self.board[i][1], self.board[i][2], "|")
        print()

        # Top Left
        if self.board[0][0] != ' ':
            if (self.board[0][0] == self.board[0][1] and self.board[0][0] == self.board[0][2] and
                    self.board[0][0] == self.board[1][0] and self.board[0][0] == self.board[2][0]):
                self.game_log.append("{} matched the left column and top row!".format(self.current_player))
                self.game_log.append("{} wins!".format(self.current_player))

                self.win_history.append("Game {}: {}"
                                        .format(self.current_game, self.current_player))

                messagebox.showinfo("", "{} matched the left column and top row!\n\nPlayer {} wins!"
                                    .format(self.current_player, self.current_player))
                winner_declared = True
                game_over = True

            # Top Row
            elif self.board[0][0] == self.board[0][1] and self.board[0][0] == self.board[0][2]:
                self.game_log.append("{} matched the top row!".format(self.current_player))
                self.game_log.append("{} wins!".format(self.current_player))

                self.win_history.append("Game {}: {}"
                                        .format(self.current_game, self.current_player))

                messagebox.showinfo("", "{} matched the top row!\n\n{} wins!"
                                    .format(self.current_player, self.current_player))
                winner_declared = True
                game_over = True

            # Left Column
            elif self.board[0][0] == self.board[1][0] and self.board[0][0] == self.board[2][0]:
                self.game_log.append("{} matched the left column!".format(self.current_player))
                self.game_log.append("{} wins!".format(self.current_player))

                self.win_history.append("Game {}: {}"
                                        .format(self.current_game, self.current_player))

                messagebox.showinfo("", "{} matched the left column!\n\n{} wins!"
                                    .format(self.current_player, self.current_player))
                winner_declared = True
                game_over = True


        # Bottom Right
        if self.board[2][2] != ' ':
            if (self.board[2][2] == self.board[2][0] and self.board[2][2] == self.board[2][1] and
                    self.board[2][2] == self.board[0][2] and self.board[2][2] == self.board[1][2]):
                self.game_log.append("{} match the bottom row and right column!".format(self.current_player))
                self.game_log.append("{} wins!".format(self.current_player))

                self.win_history.append("Game {}: {}"
                                        .format(self.current_game, self.current_player))

                messagebox.showinfo("", "{} match the bottom row and right column!\n\n{} wins!"
                                    .format(self.current_player, self.current_player))
                winner_declared = True
                game_over = True

            # Bottom Row
            elif self.board[2][2] == self.board[2][0] and self.board[2][2] == self.board[2][1]:
                self.game_log.append("{} match the bottom row!".format(self.current_player))
                self.game_log.append("{} wins!".format(self.current_player))

                self.win_history.append("Game {}: {}"
                                        .format(self.current_game, self.current_player))

                messagebox.showinfo("", "{} match the bottom row!\n\n{} wins!"
                                    .format(self.current_player, self.current_player))
                winner_declared = True
                game_over = True

            # Right Column
            elif self.board[2][2] == self.board[0][2] and self.board[2][2] == self.board[1][2]:
                self.game_log.append("Player {} match the right column!".format(self.current_player))
                self.game_log.append("Player {} wins!".format(self.current_player))

                self.win_history.append("Game {}: Player {}"
                                        .format(self.current_game, self.current_player))

                messagebox.showinfo("", "Player {} match the right column!\n\nPlayer {} wins!"
                                    .format(self.current_player, self.current_player))
                winner_declared = True
                game_over = True


        # Middle
        if self.board[1][1] != ' ':
            # Cross
            if (self.board[1][1] == self.board[0][0] and self.board[1][1] == self.board[2][2] and
                    self.board[1][1] == self.board[0][2] and self.board[1][1] == self.board[2][0]):
                self.game_log.append("{} matched a cross!".format(self.current_player))
                self.game_log.append("{} wins!".format(self.current_player))

                self.win_history.append("Game {}: {}"
                                        .format(self.current_game, self.current_player))

                messagebox.showinfo("", "{} matched a cross!\n\n{} wins!"
                                    .format(self.current_player, self.current_player))
                winner_declared = True
                game_over = True

            # Left Diagonal
            elif self.board[1][1] == self.board[0][0] and self.board[1][1] == self.board[2][2]:
                self.game_log.append("{} matched the left diagonal!".format(self.current_player))
                self.game_log.append("{} wins!".format(self.current_player))

                self.win_history.append("Game {}: {}"
                                        .format(self.current_game, self.current_player))

                messagebox.showinfo("", "{} matched the left diagonal!\n\n{} wins!"
                                    .format(self.current_player, self.current_player))
                winner_declared = True
                game_over = True

            # Right Diagonal
            elif self.board[1][1] == self.board[0][2] and self.board[1][1] == self.board[2][0]:
                self.game_log.append("{} matched the right diagonal!".format(self.current_player))
                self.game_log.append("{} wins!".format(self.current_player))

                self.win_history.append("Game {}: {}"
                                        .format(self.current_game, self.current_player))

                messagebox.showinfo("", "{} matched the right diagonal!\n\n{} wins!"
                                    .format(self.current_player, self.current_player))
                winner_declared = True
                game_over = True

            # Plus-Shape
            if (self.board[1][1] == self.board[0][1] and self.board[1][1] == self.board[2][1] and
                    self.board[1][1] == self.board[1][0] and self.board[1][1] == self.board[1][2]):
                self.game_log.append("{} matched a plus shape!".format(self.current_player))
                self.game_log.append("{} wins!".format(self.current_player))

                self.win_history.append("Game {}: {}"
                                        .format(self.current_game, self.current_player))

                messagebox.showinfo("", "{} matched a plus shape!\n\n{} wins!"
                                    .format(self.current_player, self.current_player))
                winner_declared = True
                game_over = True

            # Middle Column
            elif self.board[1][1] == self.board[0][1] and self.board[1][1] == self.board[2][1]:
                self.game_log.append("{} matched the middle column!".format(self.current_player))
                self.game_log.append("{} wins!".format(self.current_player))

                self.win_history.append("Game {}: {}"
                                        .format(self.current_game, self.current_player))

                messagebox.showinfo("", "{} matched the middle column!\n\n{} wins!"
                                    .format(self.current_player, self.current_player))
                winner_declared = True
                game_over = True

            # Middle Row
            elif self.board[1][1] == self.board[1][0] and self.board[1][1] == self.board[1][2]:
                self.game_log.append("{} matched the middle row!".format(self.current_player))
                self.game_log.append("{} wins!".format(self.current_player))

                self.win_history.append("Game {}: {}"
                                        .format(self.current_game, self.current_player))

                messagebox.showinfo("", "{} matched the middle row!\n\n{} wins!"
                                    .format(self.current_player, self.current_player))

                winner_declared = True
                game_over = True

        if not winner_declared and self.current_turn >= 9:
            self.game_log.append("Cat's Game! Game Over.")
            self.win_history.append("Game {}: Cat's Game! Game Over.".format(self.current_game))
            messagebox.showinfo("Cat's Game! Game Over.")
            game_over = True

        if winner_declared:
            self.current_game += 1

            if self.current_player == 1:
                self.p1_points += 1
                self.player1_score.set("Player 1\n--------\n{}".format(self.p1_points))
            else:
                self.p2_points += 1
                self.player2_score.set("Player 2\n--------\n{}".format(self.p2_points))

        if game_over:
            replay = messagebox.askquestion("Rematch", "Play again?")

            if replay == 'yes':
                self.new_game()
            else:
                messagebox.showinfo("", "Thanks for playing.")
                self.quit()

        return game_over

    def new_game(self):
        self.board = [[(' ') for i in range(3)] for i in range(3)]
        self.current_turn = 1
        self.current_player = self.p1_ID
        self.player_turn_message.set("Player 1's Turn")
        self.canvas_00.delete(ALL)
        self.canvas_01.delete(ALL)
        self.canvas_02.delete(ALL)
        self.canvas_10.delete(ALL)
        self.canvas_11.delete(ALL)
        self.canvas_12.delete(ALL)
        self.canvas_20.delete(ALL)
        self.canvas_21.delete(ALL)
        self.canvas_22.delete(ALL)

        self.game_log = list()

    def display_game_log(self):
        move_log = ''

        if len(self.game_log) == 0:
            move_log = "No moves played yet."

        else:
            for i in range(len(self.game_log)):
                move_log += self.game_log[i] + '\n'

        messagebox.showinfo("Game Log", move_log)

    def display_win_history(self):
        game_history = ''

        if len(self.win_history) == 0:
            game_history = "No wins yet."

        else:
            for i in range(len(self.win_history)):
                game_history += self.win_history[i] + '\n'

        messagebox.showinfo("Win History", game_history)

    def quit(self):
        self.root.destroy()




root = Tk()
root.withdraw()

def game_start():
    login_window.destroy()
    root.deiconify()
    print (p1_name)
    game = TicTacToe(root, p1_name, p2_name)
    game.check_winner()

# ***** Login Window *****
login_window = Toplevel(root)
login_window.title("Player Login")

player1_label = Label(login_window, text="Player 1: ")
player1_label.grid(row=0, column=0, sticky=E)
p1_name = Entry(login_window)
p1_name.grid(row=0, column=1)
p1_ready = Label(login_window, text="Ready?")
p1_ready.grid(row=0, column=2)
p1_check = Checkbutton(login_window, text="", command=player1_get_name)
p1_check.grid(row=0, column=3)

player2_label = Label(login_window, text="Player 2: ")
player2_label.grid(row=1, column=0, sticky=E)
p2_name = Entry(login_window)
p2_name.grid(row=1, column=1)
p2_ready = Label(login_window, text="Ready?")
p2_ready.grid(row=1, column=2)
p2_check = Checkbutton(login_window, text="", command=player2_get_name)
p2_check.grid(row=1, column=3)

play_button = Button(login_window, text="Play", command=game_start)
play_button.grid(row=2, column=1)

root.mainloop()