from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("BMI calculator")
root.geometry('400x300')
root.config(bg="light green")

#functions
def reset():
    height_e.delete(0, 'end')
    weight_e.delete(0, 'end')

def calculate_bmi():
    kg = int(weight_e.get())
    m = int(height_e.get()) / 100
    bmi = kg / (m * m)
    bmi = round(bmi, 1)
    bmi_index(bmi)

def bmi_index(bmi):
    if bmi < 18.5:
        messagebox.showinfo('BMI Report!', f'BMI = {bmi} is Underweight')
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo('BMI Report!', f'BMI = {bmi} is Normal')
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo('BMI Report!', f'BMI = {bmi} is Overweight')
    elif (bmi > 29.9):
        messagebox.showinfo('BMI Report!', f'BMI = {bmi} is Obesity')
    else:
        messagebox.showerror('BMI Report!', 'something went wrong!')


#layout
can_wid= Canvas(root,height=300,width=400,bg="light green")
can_wid.pack()
can_wid.create_rectangle(50,250,350,45,outline="beige",fill="beige")
can_wid.create_oval(100,250,2,45,outline="beige",fill="beige")
can_wid.create_oval(397,250,300,45,outline="beige",fill="beige")

#title
tit = Label(can_wid,text="BODY MASS INDEX",font="Century 18 bold",bg="light green").place(x=75,y=10)


#labels
height_l= Label(root,text=" Height(in cm) :",font="times 15 bold",bg="beige").place(x=46,y=85)
weight_l= Label(root,text=" Weight(in kg) :",font="times 15 bold",bg="beige").place(x=46,y=125)

#entry_widgets
height_e= Entry(root,font="times 12 bold")
height_e.place(x=190,y=92)
weight_e= Entry(root,font="times 12 bold")
weight_e.place(x=190,y=130)

#buttons
calculate_btn = Button(root,text="Calculate",font="times 12 bold",bg="light green",command=calculate_bmi).place(x=120,y=170)
Reset_btn = Button(root,text="Reset",font="times 12 bold",padx=15,bg="light green",command=reset).place(x=220,y=170)

root.mainloop()