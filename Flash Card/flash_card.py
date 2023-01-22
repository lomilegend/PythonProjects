from tkinter import *
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
to_learn = {}

# ---------------------------- SELECTOR ------------------------------- #





try:
    remaining_words = pd.read_csv("C:\\Users\\Elorm\\Desktop\\Code\\100Days of Coding Challenge\\GUI\\flash-card\\data\\words_to_learn.csv")
except FileNotFoundError:
    csv_data = pd.read_csv("C:\\Users\\Elorm\\Desktop\\Code\\100Days of Coding Challenge\\GUI\\flash-card\\data\\french_words.csv")
    print(csv_data)
    to_learn  = csv_data.to_dict(orient='records')
else:
    to_learn = remaining_words.to_dict(orient="records")

def selector():
    global current_card,timer
    window.after_cancel(timer)
    current_card = random.choice(to_learn)
    canva.itemconfig(title,text = "French",fill ="black")
    canva.itemconfig(word,text = current_card["French"],fill ="black")
    canva.itemconfig(canvas_image,image = card_front)
    timer = window.after(3000,func=change_card)

def change_card():
    canva.itemconfig(title,text="English",fill ="white")
    canva.itemconfig(word,text = current_card["English"],fill ="white")
    canva.itemconfig(canvas_image,image = card_back)

def known_card():
    to_learn.remove(current_card)
    
    data = pd.DataFrame(to_learn)
    data.to_csv("C:\\Users\\Elorm\\Desktop\\Code\\100Days of Coding Challenge\\GUI\\flash-card\\data\\words_to_learn.csv",index = False)

    selector()




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Cards")

timer = window.after(3000,func=change_card)

window.config(padx= 50,pady= 50,bg= BACKGROUND_COLOR)
window.config(padx= 50,pady= 50)
 
canva = Canvas(width= 800,height= 526)


card_front = PhotoImage(file ="C:\\Users\\Elorm\\Desktop\\Code\\100Days of Coding Challenge\\GUI\\flash-card\\images\\card_front.png")
card_back = PhotoImage(file ="C:\\Users\\Elorm\\Desktop\\Code\\100Days of Coding Challenge\\GUI\\flash-card\\images\\card_back.png")

canvas_image = canva.create_image(400,263,image = card_front)
canva.config(bg = BACKGROUND_COLOR,highlightthickness=0)
canva.grid(row =0,column =0,columnspan =2)
title = canva.create_text(400,150,text=" ",font= ("Ariel", 40, "italic"))
word = canva.create_text(400,263,text=" ",font= ("Ariel", 60, "bold"))

# canva.create_image(400,263,image = card_back)
# canva.config(bg = BACKGROUND_COLOR,highlightthickness=0)
# canva.grid(row =0,column =0,columnspan =2)

right = PhotoImage(file ="C:\\Users\\Elorm\\Desktop\\Code\\100Days of Coding Challenge\\GUI\\flash-card\\images\\right.png")

right_button = Button(image=right,highlightthickness=0,command =known_card)

right_button.grid(row = 1,column=1)

wrong= PhotoImage(file ="C:\\Users\\Elorm\\Desktop\\Code\\100Days of Coding Challenge\\GUI\\flash-card\\images\\wrong.png")

wrong_button =Button(image=wrong,highlightthickness=0,command=selector)

wrong_button.grid(row = 1,column=0)



selector()


window.mainloop()