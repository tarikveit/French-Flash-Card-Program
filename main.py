import random
from tkinter import *
import pandas
from random import choice
import math
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel",40,"italic")
WORD_FONT = ("Ariel",60,"bold")
timer_secs = 3
timer = None
random_word = None

def count_down(count):
    global random_word
    global timer
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        canvas.itemconfig(card_img,image=card_back_img)
        translated_word = french_word_dict[random_word]
        canvas.itemconfig(word_text,text=translated_word,fill="white")
        canvas.itemconfig(language_text,text="English", fill="white")

def right_button_command():
    global random_word
    global timer
    try:
        window.after_cancel(timer)
    except ValueError:
        pass
    try:
        del french_word_dict[random_word]
    except KeyError:
        pass
    data = {"French":list(french_word_dict.keys()),"English":list(french_word_dict.values())}
    new_french_data_frame = pandas.DataFrame.from_dict(data)
    new_french_data_frame.to_csv("data/words_to_learn.csv",index=False)

    french_list = []
    for key in french_word_dict:
        french_list.append(key)
    random_word = choice(french_list)
    canvas.itemconfig(card_img, image=card_front_img)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=random_word,fill="black")
    count_down(timer_secs)


def wrong_button_command():
    global random_word
    global timer
    try:
        window.after_cancel(timer)
    except ValueError:
        pass
    french_list = []
    for key in french_word_dict:
        french_list.append(key)
    random_word = random.choice(french_list)
    canvas.itemconfig(card_img, image=card_front_img)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=random_word,fill="black")
    count_down(timer_secs)

#french words
french_word_dict = {}
try:
    french_data_frame = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    french_data_frame = pandas.read_csv("data/french_words.csv")
for (index,row) in french_data_frame.iterrows():
    french_word_dict.update({row.French: row.English})

#window
window = Tk()
window.config(width=300,height=300,padx=50,pady=50,bg=BACKGROUND_COLOR)

#canvas
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_img = canvas.create_image(400,263,image=card_front_img)
language_text = canvas.create_text(400,150,text="French",font=LANGUAGE_FONT,fill="black")
word_text = canvas.create_text(400,263,text="Word in french",font=WORD_FONT,fill="black")
canvas.grid(column=0,row=0,columnspan=2)

#buttons
right_button = Button()
right_button_img = PhotoImage(file="images/right.png")
right_button.config(image=right_button_img,relief="flat",borderwidth=0,highlightthickness=0,command=right_button_command)
right_button.grid(column=1,row=1)

wrong_button = Button()
wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button.config(image=wrong_button_img,relief="flat",borderwidth=0,highlightthickness=0,command=wrong_button_command)
wrong_button.grid(column=0,row=1)

window.mainloop()