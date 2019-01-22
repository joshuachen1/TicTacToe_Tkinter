from tkinter import Tk, Canvas, Label, StringVar, BOTTOM, SUNKEN, W, X, Y, Menu, ALL, messagebox, TOP, LEFT, RIGHT


class TicTacToe:

    def __init__(self, master):
        self.root = master

        # ***** Board *****
        self.board = [[(' ') for i in range(3)] for i in range(3)]

        self.current_turn = 1
        self.current_player = 1

        self.game_log = list()

        # ***** Scoreboard *****
        self.p1_points = 0
        self.player1_score = StringVar()
        self.player1_score.set("Player 1\n--------\n{}".format(self.p1_points))
        self.p1_score_display = Label(self.root, textvariable=self.player1_score, bd=1, relief=SUNKEN)
        self.p1_score_display.pack(side=LEFT, padx=2, fill=X)

        self.p2_points = 0
        self.player2_score = StringVar()
        self.player2_score.set("Player 2\n--------\n{}".format(self.p2_points))
        self.p2_score_display = Label(self.root, textvariable=self.player2_score, bd=1, relief=SUNKEN)
        self.p2_score_display.pack(side=RIGHT, padx=2, fill=X)

        # ***** Bottom Player Message *****
        self.player_turn_message = StringVar()
        self.player_turn_message.set("Player {}'s Turn".format(self.current_player))
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
            if self.current_player == 1:
                self.canvas_00.create_line(20, 20, 80, 80)
                self.canvas_00.create_line(20, 80, 80, 20)
                self.board[0][0] = 'X'
            else:
                self.canvas_00.create_oval(15, 15, 90, 90)
                self.board[0][0] = 'O'

            self.game_log.append("({turn}): P-{player} placed {mark} at top left"
                             .format(turn=self.current_turn, player=self.current_player,
                                     mark=self.board[0][0]))

            self.update_player_turn()

    def mark01(self, event):
        if self.board[0][1] == ' ':
            if self.current_player == 1:
                self.canvas_01.create_line(20, 20, 80, 80)
                self.canvas_01.create_line(20, 80, 80, 20)
                self.board[0][1] = 'X'
            else:
                self.canvas_01.create_oval(15, 15, 90, 90)
                self.board[0][1] = 'O'

            self.game_log.append("({turn}): P-{player} placed {mark} at top middle"
                             .format(turn=self.current_turn, player=self.current_player,
                                     mark=self.board[0][1]))
            self.update_player_turn()

    def mark02(self, event):
        if self.board[0][2] == ' ':
            if self.current_player == 1:
                self.canvas_02.create_line(20, 20, 80, 80)
                self.canvas_02.create_line(20, 80, 80, 20)
                self.board[0][2] = 'X'
            else:
                self.canvas_02.create_oval(15, 15, 90, 90)
                self.board[0][2] = 'O'

            self.game_log.append("({turn}): P-{player} placed {mark} at top right"
                                 .format(turn=self.current_turn, player=self.current_player,
                                         mark=self.board[0][2]))
            self.update_player_turn()

    def mark10(self, event):
        if self.board[1][0] == ' ':
            if self.current_player == 1:
                self.canvas_10.create_line(20, 20, 80, 80)
                self.canvas_10.create_line(20, 80, 80, 20)
                self.board[1][0] = 'X'
            else:
                self.canvas_10.create_oval(15, 15, 90, 90)
                self.board[1][0] = 'O'

            self.game_log.append("({turn}): P-{player} placed {mark} at left middle"
                                 .format(turn=self.current_turn, player=self.current_player,
                                         mark=self.board[1][0]))
            self.update_player_turn()

    def mark11(self, event):
        if self.board[1][1] == ' ':
            if self.current_player == 1:
                self.canvas_11.create_line(20, 20, 80, 80)
                self.canvas_11.create_line(20, 80, 80, 20)
                self.board[1][1] = 'X'
            else:
                self.canvas_11.create_oval(15, 15, 90, 90)
                self.board[1][1] = 'O'

            self.game_log.append("({turn}): P-{player} placed {mark} at the center"
                                 .format(turn=self.current_turn, player=self.current_player,
                                         mark=self.board[1][1]))
            self.update_player_turn()

    def mark12(self, event):
        if self.board[1][2] == ' ':
            if self.current_player == 1:
                self.canvas_12.create_line(20, 20, 80, 80)
                self.canvas_12.create_line(20, 80, 80, 20)
                self.board[1][2] = 'X'
            else:
                self.canvas_12.create_oval(15, 15, 90, 90)
                self.board[1][2] = 'O'

            self.game_log.append("({turn}): P-{player} placed {mark} at right middle"
                                 .format(turn=self.current_turn, player=self.current_player,
                                         mark=self.board[1][2]))
            self.update_player_turn()

    def mark20(self, event):
        if self.board[2][0] == ' ':
            if self.current_player == 1:
                self.canvas_20.create_line(20, 20, 80, 80)
                self.canvas_20.create_line(20, 80, 80, 20)
                self.board[2][0] = 'X'
            else:
                self.canvas_20.create_oval(15, 15, 90, 90)
                self.board[2][0] = 'O'

            self.game_log.append("({turn}): P-{player} placed {mark} at bottom left"
                                 .format(turn=self.current_turn, player=self.current_player,
                                         mark=self.board[2][0]))
            self.update_player_turn()

    def mark21(self, event):
        if self.board[2][1] == ' ':
            if self.current_player == 1:
                self.canvas_21.create_line(20, 20, 80, 80)
                self.canvas_21.create_line(20, 80, 80, 20)
                self.board[2][1] = 'X'
            else:
                self.canvas_21.create_oval(15, 15, 90, 90)
                self.board[2][1] = 'O'

            self.game_log.append("({turn}): P-{player} placed {mark} at bottom middle"
                                 .format(turn=self.current_turn, player=self.current_player,
                                         mark=self.board[2][1]))
            self.update_player_turn()

    def mark22(self, event):
        if self.board[2][2] == ' ':
            if self.current_player == 1:
                self.canvas_22.create_line(20, 20, 80, 80)
                self.canvas_22.create_line(20, 80, 80, 20)
                self.board[2][2] = 'X'
            else:
                self.canvas_22.create_oval(15, 15, 90, 90)
                self.board[2][2] = 'O'

            self.game_log.append("({turn}): P-{player} placed {mark} at bottom right"
                                 .format(turn=self.current_turn, player=self.current_player,
                                         mark=self.board[2][2]))
            self.update_player_turn()

    def update_player_turn(self):

        if self.check_winner() == False:
            self.current_turn += 1

            if self.current_turn % 2 == 1:
                self.current_player = 1
            else:
                self.current_player = 2

            self.player_turn_message.set("Player {player}'s Turn".format(player=self.current_player))


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
                    self.player_turn_message.set("Player {} wins!".format(self.current_player))
                    self.game_log.append("Player {} matched the left column and top row!".format(self.current_player))
                    self.game_log.append("Player {} wins!".format(self.current_player))
                    messagebox.showinfo("", "Player {} matched the left column and top row!\n\nPlayer {} wins!"
                                        .format(self.current_player, self.current_player))
                    winner_declared = True
                    game_over = True

            # Top Row
            elif self.board[0][0] == self.board[0][1] and self.board[0][0] == self.board[0][2]:
                self.player_turn_message.set("Player {} wins!".format(self.current_player))
                self.game_log.append("Player {} matched the top row!".format(self.current_player))
                self.game_log.append("Player {} wins!".format(self.current_player))
                messagebox.showinfo("", "Player {} matched the top row!\n\nPlayer {} wins!"
                                    .format(self.current_player, self.current_player))
                winner_declared = True
                game_over = True

            # Left Column
            elif self.board[0][0] == self.board[1][0] and self.board[0][0] == self.board[2][0]:
                self.player_turn_message.set("Player {} wins!".format(self.current_player))
                self.game_log.append("Player {} matched the left column!".format(self.current_player))
                self.game_log.append("Player {} wins!".format(self.current_player))
                messagebox.showinfo("", "Player {} matched the left column!\n\nPlayer {} wins!"
                                    .format(self.current_player, self.current_player))
                winner_declared = True
                game_over = True


        # Bottom Right
        if self.board[2][2] != ' ':
            if (self.board[2][2] == self.board[2][0] and self.board[2][2] == self.board[2][1] and
                self.board[2][2] == self.board[0][2] and self.board[2][2] == self.board[1][2]):
                    self.player_turn_message.set("Player {} wins!".format(self.current_player))
                    self.game_log.append("Player {} match the bottom row and right column!".format(self.current_player))
                    self.game_log.append("Player {} wins!".format(self.current_player))
                    messagebox.showinfo("", "Player {} match the bottom row and right column!\n\nPlayer {} wins!"
                                        .format(self.current_player, self.current_player))
                    winner_declared = True
                    game_over = True

            # Bottom Row
            elif self.board[2][2] == self.board[2][0] and self.board[2][2] == self.board[2][1]:
                self.player_turn_message.set("Player {} wins!".format(self.current_player))
                self.game_log.append("Player {} match the bottom row!".format(self.current_player))
                self.game_log.append("Player {} wins!".format(self.current_player))
                messagebox.showinfo("", "Player {} match the bottom row!\n\nPlayer {} wins!"
                                    .format(self.current_player, self.current_player))
                winner_declared = True
                game_over = True

            # Right Column
            elif self.board[2][2] == self.board[0][2] and self.board[2][2] == self.board[1][2]:
                self.player_turn_message.set("Player {} wins!".format(self.current_player))
                self.game_log.append("Player {} match the right column!".format(self.current_player))
                self.game_log.append("Player {} wins!".format(self.current_player))
                messagebox.showinfo("", "Player {} match the right column!\n\nPlayer {} wins!"
                                    .format(self.current_player, self.current_player))
                winner_declared = True
                game_over = True


        # Middle
        if self.board[1][1] != ' ':
            # Cross
            if (self.board[1][1] == self.board[0][0] and self.board[1][1] == self.board[2][2] and
                self.board[1][1] == self.board[0][2] and self.board[1][1] == self.board[2][0]):
                    self.player_turn_message.set("Player {} wins!".format(self.current_player))
                    self.game_log.append("Player {} matched a cross!".format(self.current_player))
                    self.game_log.append("Player {} wins!".format(self.current_player))
                    messagebox.showinfo("", "Player {} matched a cross!\n\nPlayer {} wins!"
                                        .format(self.current_player, self.current_player))
                    winner_declared = True
                    game_over = True

            # Left Diagonal
            elif self.board[1][1] == self.board[0][0] and self.board[1][1] == self.board[2][2]:
                self.player_turn_message.set("Player {} wins!".format(self.current_player))
                self.game_log.append("Player {} matched the left diagonal!".format(self.current_player))
                self.game_log.append("Player {} wins!".format(self.current_player))
                messagebox.showinfo("", "Player {} matched the left diagonal!\n\nPlayer {} wins!"
                                    .format(self.current_player, self.current_player))
                winner_declared = True
                game_over = True

            # Right Diagonal
            elif self.board[1][1] == self.board[0][2] and self.board[1][1] == self.board[2][0]:
                self.player_turn_message.set("Player {} wins!".format(self.current_player))
                self.game_log.append("Player {} matched the right diagonal!".format(self.current_player))
                self.game_log.append("Player {} wins!".format(self.current_player))
                messagebox.showinfo("", "Player {} matched the right diagonal!\n\nPlayer {} wins!"
                                    .format(self.current_player, self.current_player))
                winner_declared = True
                game_over = True

            # Plus-Shape
            if (self.board[1][1] == self.board[0][1] and self.board[1][1] == self.board[2][1] and
                self.board[1][1] == self.board[1][0] and self.board[1][1] == self.board[1][2]):
                    self.player_turn_message.set("Player {} wins!".format(self.current_player))
                    self.game_log.append("Player {} matched a plus shape!".format(self.current_player))
                    self.game_log.append("Player {} wins!".format(self.current_player))
                    messagebox.showinfo("", "Player {} matched a plus shape!\n\nPlayer {} wins!"
                                        .format(self.current_player, self.current_player))
                    winner_declared = True
                    game_over = True

            # Middle Column
            elif self.board[1][1] == self.board[0][1] and self.board[1][1] == self.board[2][1]:
                self.player_turn_message.set("Player {} wins!".format(self.current_player))
                self.game_log.append("Player {} matched the middle column!".format(self.current_player))
                self.game_log.append("Player {} wins!".format(self.current_player))
                messagebox.showinfo("", "Player {} matched the middle column!\n\nPlayer {} wins!"
                                    .format(self.current_player, self.current_player))
                winner_declared = True
                game_over = True

            # Middle Row
            elif self.board[1][1] == self.board[1][0] and self.board[1][1] == self.board[1][2]:
                self.player_turn_message.set("Player {} wins!".format(self.current_player))
                self.game_log.append("Player {} matched the middle row!".format(self.current_player))
                self.game_log.append("Player {} wins!".format(self.current_player))
                messagebox.showinfo("", "Player {} matched the middle row!\n\nPlayer {} wins!"
                                    .format(self.current_player, self.current_player))
                winner_declared = True
                game_over = True

        if not winner_declared and self.current_turn > 9:
            self.player_turn_message.set("Cat's Game! Game Over.")
            self.game_log.append("Cat's Game! Game Over.")
            game_over = True

        if winner_declared:
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

    def display_game_log(self):
        game_history = ''
        for i in range(len(self.game_log)):
            game_history += self.game_log[i] + '\n'

        messagebox.showinfo("Game Log", game_history)

    def quit(self):
        self.root.destroy()


main_window = Tk()
game = TicTacToe(main_window)
game.check_winner()
main_window.mainloop()