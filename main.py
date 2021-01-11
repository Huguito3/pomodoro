from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✓"
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_clicked():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    my_label.config(text="Timer", fg=GREEN)
    my_label_check.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_clicked():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_breack_sec = SHORT_BREAK_MIN * 60
    long_breack_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_breack_sec)
        my_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_breack_sec)
        my_label.config(text="Break", fg=PINK)
    else:
        countdown(work_sec)
        my_label.config(text="Work", fg=GREEN)

        # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_clicked()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += CHECKMARK
        my_label_check.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./img/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, "35", "bold"))
canvas.grid(column=2, row=2)

# Label
my_label = Label(text="Timer", font=(
    FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
my_label.grid(column=2, row=1)

# Button Start
button_start = Button(text="Start", command=start_clicked,
                      highlightthickness=0)
button_start.grid(column=1, row=3)

# Button
button_reset = Button(text="Reset", command=reset_clicked,
                      highlightthickness=0)
button_reset.grid(column=3, row=3)

# Label
my_label_check = Label(font=(
    FONT_NAME, 18, "bold"), bg=YELLOW, fg=GREEN)
my_label_check.grid(column=2, row=4)


window.mainloop()
