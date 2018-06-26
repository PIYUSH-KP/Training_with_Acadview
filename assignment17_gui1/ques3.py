# Q3. Create a frame using tkinter with any label text and two buttons.One to exit and other to change the label to some other text.
from tkinter import *
root1 = Tk()
#place window of 550x350 at (50,50)
root1.geometry("550x350+100+100")

label_1 = Label(root1, text='chnage this text by clicking button below')
label_1.pack()


# METHOD 1
def a():
    label_1.config(text="changed")

label_button = Button(root1, text='change label text', command= a )
label_button.pack()

label_2 = Label(root1, text='\n\ntry changing this text too')
label_2.pack()

#  METHOD 2
def b():
    label_2["text"] = "changed it again"
label_button2 = Button(root1, text='change label text again', command= b )
label_button2.pack()

exit_button1 = Button(root1, text='Exit Program', command=root1.destroy)
exit_button1.pack()


root1.mainloop()