from tkinter import *
from tkinter import messagebox
import random
import json



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)
    

    random.shuffle(password_list)

    password = "".join(password_list)
    
    password_entry.insert(0,string=password)
    #print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def get_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    data1 = " "
    
    new_data = {website:
    {"email":email,
    "password":password,
    }
    } 

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error",message="Website or Password field is blank ")

    else:
        try:
            with open("C:\\Users\\Elorm\\Desktop\\Code\\100Days of Coding Challenge\\GUI\\Password Manager\\data.json",mode ="r") as file:
                data1 = json.load(file)
        except FileNotFoundError:
            with open("C:\\Users\\Elorm\\Desktop\\Code\\100Days of Coding Challenge\\GUI\\Password Manager\\data.json",mode ="w") as file:
                json.dump(new_data,file,indent=4)
                
        else:
            data1.update(new_data)

            with open("C:\\Users\\Elorm\\Desktop\\Code\\100Days of Coding Challenge\\GUI\\Password Manager\\data.json",mode ="w") as file:
                json.dump(new_data,file,indent=4)

        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)

# ---------------------------- SEARCH PASSWORD------------------------------- #
def find_passowrd():
    name = website_entry.get()
    try:
        with ("C:\\Users\\Elorm\\Desktop\\Code\\100Days of Coding Challenge\\GUI\\Password Manager\\data.json") as a:
            web = json.load(a)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if name in web:
            email = web[name]["email"]
            password = web[name]["password"]
            messagebox.showinfo(title=email,message = f"Email = {email}\n Password = {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {web} exists.")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx= 50,pady= 50)

canva = Canvas(width= 200,height= 200)

logo = PhotoImage(file ="C:\\Users\\Elorm\\Desktop\\Code\\100Days of Coding Challenge\\GUI\\Password Manager\\logo.png")

canva.create_image(100,100,image = logo)
canva.grid(row = 0,column=1)

website_label = Label(text= "Website:")
website_label.grid(row = 1, column=0)

website_entry = Entry(width= 25)
website_entry.focus()
website_entry.grid(row = 1, column= 1)

name_label = Label(text= "Email/Username:")
name_label.grid(row = 2, column=0)


email_entry = Entry(width= 35)
email_entry.insert(0,string="justincomla@gmail.com")
email_entry.grid(row = 2, column= 1, columnspan= 2)

password_label = Label(text= "Password:")
password_label.grid(row = 3, column=0)

password_entry = Entry(width= 21)
password_entry.grid(row = 3, column= 1)

add_button = Button(text="Add",width=35,command=get_data)
add_button.grid(row=4,column=1,columnspan=2)

generate_button = Button(text="Generate Password",command=pass_gen)
generate_button.grid(row =3,column=2)

search_button = Button(text="Search",width= 13,command=find_passowrd)
search_button.grid(row =1,column=2)

window.mainloop()