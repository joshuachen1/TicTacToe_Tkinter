from tkinter import Tk, Frame, Canvas

main_window = Tk()

def mark00(event):
    canvas_00.create_line(20, 20, 80, 80)
    canvas_00.create_line(20, 80, 80, 20)

def mark01(event):
    canvas_01.create_line(20, 20, 80, 80)
    canvas_01.create_line(20, 80, 80, 20)

def mark02(event):
    canvas_02.create_line(20, 20, 80, 80)
    canvas_02.create_line(20, 80, 80, 20)

def mark10(event):
    canvas_10.create_line(20, 20, 80, 80)
    canvas_10.create_line(20, 80, 80, 20)

def mark11(event):
    canvas_11.create_line(20, 20, 80, 80)
    canvas_11.create_line(20, 80, 80, 20)

def mark12(event):
    canvas_12.create_line(20, 20, 80, 80)
    canvas_12.create_line(20, 80, 80, 20)

def mark20(event):
    canvas_20.create_line(20, 20, 80, 80)
    canvas_20.create_line(20, 80, 80, 20)

def mark21(event):
    canvas_21.create_line(20, 20, 80, 80)
    canvas_21.create_line(20, 80, 80, 20)

def mark22(event):
    canvas_22.create_line(20, 20, 80, 80)
    canvas_22.create_line(20, 80, 80, 20)

canvas = Canvas(main_window, width=500, height=500)
canvas.pack()

canvas.create_line(100, 0, 100, 300)
canvas.create_line(200, 0, 200, 300)
canvas.create_line(0, 100, 300, 100)
canvas.create_line(0, 200, 300, 200)


canvas_00 = Canvas(canvas, width=100, height=100, bg='red')
canvas_00.bind("<Button-1>", mark00)
canvas_00.grid(row=0, column=0)

canvas_01 = Canvas(canvas, width=100, height=100, bg='blue')
canvas_01.bind("<Button-1>", mark01)
canvas_01.grid(row=0, column=1)

canvas_02 = Canvas(canvas, width=100, height=100, bg='green')
canvas_02.bind("<Button-1>", mark02)
canvas_02.grid(row=0, column=2)

canvas_10 = Canvas(canvas, width=100, height=100, bg='red')
canvas_10.bind("<Button-1>", mark10)
canvas_10.grid(row=1, column=0)

canvas_11 = Canvas(canvas, width=100, height=100, bg='blue')
canvas_11.bind("<Button-1>", mark11)
canvas_11.grid(row=1, column=1)

canvas_12 = Canvas(canvas, width=100, height=100, bg='green')
canvas_12.bind("<Button-1>", mark12)
canvas_12.grid(row=1, column=2)

canvas_20 = Canvas(canvas, width=100, height=100, bg='red')
canvas_20.bind("<Button-1>", mark20)
canvas_20.grid(row=2, column=0)

canvas_21 = Canvas(canvas, width=100, height=100, bg='blue')
canvas_21.bind("<Button-1>", mark21)
canvas_21.grid(row=2, column=1)

canvas_22 = Canvas(canvas, width=100, height=100, bg='green')
canvas_22.bind("<Button-1>", mark22)
canvas_22.grid(row=2, column=2)


main_window.mainloop()