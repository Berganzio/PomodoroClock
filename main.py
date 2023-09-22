import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Terminal"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmarks = ''

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global checkmarks
    global reps
    canvas.itemconfig(timer_text, text='00:00')
    canvas.itemconfig(title_text, text='Timer')
    canvas.itemconfig(checkmark, text='')

    screen.after_cancel(timer)
    reps = 0
    checkmarks = ''
    start_button.config(text='START', command=start_timer)

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global work_sec
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_brake_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        count_down(work_sec)
        canvas.itemconfig(title_text, text='Work', fill=GREEN)
    elif reps == 8:
        count_down(long_brake_sec)
        canvas.itemconfig(title_text, text='Brake', fill=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        canvas.itemconfig(title_text, text='Brake', fill=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')

    if count > 0:
        global timer
        start_button.config(text='RESET', command=reset_timer)
        timer = screen.after(1000, count_down, count - 1)
    else:
        global checkmarks
        start_timer()
        if reps % 2 == 0:
            checkmarks += '✓'
            canvas.itemconfig(checkmark, text=checkmarks)

# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title('Productivity Clock')
screen.config(bg=YELLOW)

canvas = Canvas(width=400, height=300, bg=YELLOW, highlightthickness=0)
timer_img = PhotoImage(file='timer.png')

canvas.create_image(200, 230, image=timer_img)
title_text = canvas.create_text(300, 210, text='Timer', fill=GREEN, font=(FONT_NAME, 20, 'normal'))
timer_text = canvas.create_text(300, 255, text='00:00', fill='beige', font=(FONT_NAME, 45, 'normal'))
checkmark = canvas.create_text(140, 50, fill=GREEN, font=(FONT_NAME, 20, 'normal'))
canvas.grid()
start_button = Button(justify='center', bg=PINK, text='START', font=(FONT_NAME, 15, 'bold'),
                      borderwidth=5, command=start_timer)
start_button.grid(column=0, row=0)


screen.mainloop()