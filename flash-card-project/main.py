from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except:
    data = pandas.read_csv("data/chinese_words.csv")

to_learn = data.to_dict(orient='records')
curr_card = {}

def next_card():
    global curr_card, flip_timer
    window.after_cancel(flip_timer)
    curr_card = random.choice(to_learn)
    canvas.itemconfig(card_bg, image=card_front_img)
    canvas.itemconfig(card_title, text="Chinese", fill="black")
    canvas.itemconfig(card_word, text=curr_card["Chinese"], fill="black")
    flip_timer = window.after(3000,flip_card)

def flip_card():
    canvas.itemconfig(card_bg, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=curr_card["English"], fill="white")

def is_known():
    to_learn.remove(curr_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()
    

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_bg = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 264, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

cross_img = PhotoImage(file="./images/wrong.png")
unknown_btn = Button(image=cross_img, highlightthickness=0, command=next_card)
unknown_btn.grid(row=1, column=0)

check_img = PhotoImage(file="./images/right.png")
know_btn = Button(image=check_img, highlightthickness=0, command = is_known)
know_btn.grid(row=1, column=1)

next_card()

window.mainloop()