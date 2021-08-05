from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
my_timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(my_timer)
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00:00")
    check_marks.config(text="")
    global reps
    reps -= 1
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps

    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60


    if reps % 8 == 0:
        title_label.config(text='Rest')
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title_label.config(text='Break')
        count_down(short_break_sec)
    else:
        title_label.config(text='Focus')
        count_down(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"


    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global my_timer
        my_timer = window.after(1000, count_down,  count - 1)
    else:
        start_timer()

        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✓"
        check_marks.config(text=mark)

def open_settings():
    settings_window = Tk()
    new_Window = Toplevel(settings_window)

    new_Window.title("New Window")

    # sets the geometry of toplevel
    new_Window.geometry("200x200")

    # A Label widget to show in toplevel
    new_Window.mainloop()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=200, pady=200, bg=YELLOW)



title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 55, 'bold'))
title_label.grid(column=1, row=0)

start_buttton = Button(text='Start',font=(FONT_NAME, 15, 'bold'), fg=RED, command=start_timer)
reset_button = Button(text='Reset', font=(FONT_NAME, 15, 'bold'), fg=RED, command=reset_timer)
settings_button = Button(text='Settings', font=(FONT_NAME, 15, 'bold'), fg=RED, command=open_settings)

check_marks= Label(text="", font=(FONT_NAME, 30, 'bold'), fg=GREEN, bg=YELLOW)

canvas = Canvas(width=400, height=448, bg=YELLOW, highlightthickness=0)
tomato_photo = PhotoImage(file="tomato.png")
canvas.create_image(200, 224, image=tomato_photo)
timer_text = canvas.create_text(200, 224, text="00:00:00", fill='white', font=(FONT_NAME, 25, 'bold'))
canvas.grid(column=1, row=1)

start_buttton.grid(column=0, row=2)
reset_button.grid(column=2, row=2)
settings_button.grid(column=2, row=0)

check_marks.grid(column=1, row=2)


window.mainloop()
