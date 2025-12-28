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
LONG_BREAK_MIN = 2
reps=0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    if reps==0 or reps==2 or reps==4 or reps==6:
        count_down(work_sec)
    elif reps==7:
        count_down(long_break_sec)
    elif reps==1 or reps==3 or reps==5:
        count_down(short_break_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min=math.floor(count/60)
    count_sec= count%60


    if(count_sec==0):
        count_sec="00"
        global  reps
        reps+=1

    
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")




    window.after(1000, count_down, count-1)

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("pomadoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas = Canvas(height=224, width=220,bg=PINK,highlightthickness=0, )
tom= PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tom)
timer_text=canvas.create_text(100,112,text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1, row=1)


lab=Label(text="timer", font=(FONT_NAME,20,"bold"), padx=15, pady=15, fg=GREEN)
lab.grid(row=0,column=1)

but= Button(text="start", font=(FONT_NAME,20,"bold"), padx=15, pady=15, command=start_timer)
but.grid(row=2, column=0)

but1= Button(text="reset", font=(FONT_NAME,20,"bold"), padx=15, pady=15)
but1.grid(row=2, column=2)

lab=Label(text="✔", font=(FONT_NAME,20,"bold"), padx=15, pady=15)
lab.grid(row=3,column=1)























window.mainloop()
