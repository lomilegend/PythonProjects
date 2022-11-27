import tkinter
#window
window = tkinter.Tk()

window.title("Miles to Km Converter")
window.minsize(width= 300, height= 200)
window.config(padx=50,pady=50)


#label
my_label3 = tkinter.Label(text=" ",font=("Calibri",16))
my_label3.grid(row = 0,column = 0)

my_label = tkinter.Label(text="is equal to",font=("Calibri",16))
my_label.grid(row = 1,column = 0)

result_label =tkinter.Label(text="0",font=("Calibri",16))
result_label.grid(row = 1,column = 1)

my_label1 = tkinter.Label(text="Miles",font=("Calibri",16))
my_label1.grid(row = 0,column = 2)

my_label2 = tkinter.Label(text="Km",font=("Calibri",16))
my_label2.grid(row = 1,column = 2)


#button

# def button_clicked():
#     print("i got clicked")
#     my_label.config(text= input.get())


def answer():
    n = float(input.get()) * 1.60934
    result_label.config(text=f"{n}")



button = tkinter.Button(text = "Calculate",command= answer)
button.grid(row = 2,column = 1)


#Input

input = tkinter.Entry(width= 10)
input.insert(index = 0 ,string= 0)
input.grid(row = 0,column = 1)




window.mainloop()
