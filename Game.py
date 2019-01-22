from tkinter import Tk, Frame, Canvas


class TicTacToe:

    def __init__(self, master):
        self.canvas = Canvas(master, width=300, height=300)
        self.canvas.pack()

        self.current_turn = 1

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
        else:
            self.canvas_00.create_oval(15, 15, 90, 90)

        self.current_turn += 1

    def mark01(self, event):
        if self.current_turn % 2 == 1:
            self.canvas_01.create_line(20, 20, 80, 80)
            self.canvas_01.create_line(20, 80, 80, 20)
        else:
            self.canvas_01.create_oval(15, 15, 90, 90)

        self.current_turn += 1

    def mark02(self, event):
        if self.current_turn % 2 == 1:
            self.canvas_02.create_line(20, 20, 80, 80)
            self.canvas_02.create_line(20, 80, 80, 20)
        else:
            self.canvas_02.create_oval(15, 15, 90, 90)

        self.current_turn += 1

    def mark10(self, event):
        if self.current_turn % 2 == 1:
            self.canvas_10.create_line(20, 20, 80, 80)
            self.canvas_10.create_line(20, 80, 80, 20)
        else:
            self.canvas_10.create_oval(15, 15, 90, 90)

        self.current_turn += 1

    def mark11(self, event):
        if self.current_turn % 2 == 1:
            self.canvas_11.create_line(20, 20, 80, 80)
            self.canvas_11.create_line(20, 80, 80, 20)
        else:
            self.canvas_11.create_oval(15, 15, 90, 90)

        self.current_turn += 1

    def mark12(self, event):
        if self.current_turn % 2 == 1:
            self.canvas_12.create_line(20, 20, 80, 80)
            self.canvas_12.create_line(20, 80, 80, 20)
        else:
            self.canvas_12.create_oval(15, 15, 90, 90)

        self.current_turn += 1

    def mark20(self, event):
        if self.current_turn % 2 == 1:
            self.canvas_20.create_line(20, 20, 80, 80)
            self.canvas_20.create_line(20, 80, 80, 20)
        else:
            self.canvas_20.create_oval(15, 15, 90, 90)

        self.current_turn += 1

    def mark21(self, event):
        if self.current_turn % 2 == 1:
            self.canvas_21.create_line(20, 20, 80, 80)
            self.canvas_21.create_line(20, 80, 80, 20)
        else:
            self.canvas_21.create_oval(15, 15, 90, 90)

        self.current_turn += 1

    def mark22(self, event):
        if self.current_turn % 2 == 1:
            self.canvas_22.create_line(20, 20, 80, 80)
            self.canvas_22.create_line(20, 80, 80, 20)
        else:
            self.canvas_22.create_oval(15, 15, 90, 90)

        self.current_turn += 1


main_window = Tk()
game = TicTacToe(main_window)
main_window.mainloop()