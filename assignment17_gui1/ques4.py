from tkinter import *

root4 = Tk()
root4.title("Ques 4")
root4.geometry('550x350')
lbl = Label(root4, text="Enter something:")
lbl.grid(column=0, row=0)
txt = Entry(root4,width=15)
txt.grid(column=1, row=0)
def show():
    data = txt.get()
    lbl = Label(root4, text="Your entered :"+data)
    lbl.grid(column=2, row=6)
btn = Button(root4, text="show", command=show)
btn.grid(column=2, row=1)

exit_button = Button(root4, text='Exit Program', command=root4.destroy)
exit_button.grid(column=1, row=2)
root4.mainloop()
